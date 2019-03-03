from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField, get_thumbnail


# Game = a game that can be played.
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ImageField(upload_to='./games/')

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

# Platform = a game system/platform the game is played on.
class Platform(models.Model):
    name = models.CharField(max_length=100)
    image = ImageField(upload_to='./games/')
    games = models.ManyToManyField(Game)
    description = models.TextField()

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    description = models.TextField()
    users_needed = models.BooleanField()
    users_sign_up = models.BooleanField()
    user_quota = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


# Post = a post by a user.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now= True, blank=True, null=True)
    body = models.TextField()
    due = models.DateTimeField(auto_now=False)
    user = models.ForeignKey(User, related_name='user_posting', on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    users_going = models.ManyToManyField(User, related_name='users_going', blank=True)
    users_needed = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = ImageField(upload_to='./profiles/', null=True)
    platforms = models.ManyToManyField(Platform, related_name="user")
    games = models.ManyToManyField(Game, related_name="user")

    #def save(self, *args, **kwargs):
     #   if self.profile_image:
      #      self.profile_image=get_thumbnail(self.profile_image, '64x64', quality=99, format='JPEG').url
       # super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Comment = Comment on a post
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text

class Message(models.Model):
    text = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    to_user = models.ForeignKey(User, related_name='touser',on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='fromuser',on_delete=models.CASCADE)
    message = models.ManyToManyField(Message)