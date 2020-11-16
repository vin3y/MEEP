from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship

#when a new user is creted it get updated in the profile field or added so we use signlas.py for that
@receiver(post_save, sender = User)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    if created:
        Profile.objects.create(user =instance)

#the insatnce is relationship model and it can access every coloumn in it, and basically if the status is accepete both receiver and sender must be added as friennd each othrt
@receiver(post_save, sender = Relationship)
def post_save_add_to_friends(sender, instance, created,**kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()
