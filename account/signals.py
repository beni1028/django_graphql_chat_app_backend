from django.db.models.signals import post_save
from .models import User, Team,Message
from django.dispatch import receiver
from channels.layers import get_channel_layer
import asyncio
from graphql_auth.models import UserStatus

# @receiver(post_save, sender=User)

@receiver(post_save, sender=Message) 
def send_notifications(sender, instance, created, **kwargs):
    if created:
        group_name = str(instance.team.id)
        # print(group_name)
        # print(instance.message,'signals')
        channel_layer = get_channel_layer()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # serialized_qs = serializers.serialize('json', instance)

        # print(serialized_qs)
        loop.run_until_complete(channel_layer.group_send(group_name,
        {
            'type':'sent_message',
            'id': instance.id,
        }))
    else:
        return False



# @receiver(post_save, sender=UserStatus) 
# def send_notifications(sender, instance, created, **kwargs):
#         if instance.verified:
#             group_name = instance.user.team_name 
#             print(group_name)
#             # print(instance.message,'signals')
#             channel_layer = get_channel_layer()
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             # serialized_qs = serializers.serialize('json', instance)

#             # print(serialized_qs)
#             loop.run_until_complete(channel_layer.group_send(group_name,
#             {
#                 'type':'send_notification',
#                 'id': instance.id,
#             }))
#         else:
#             return False