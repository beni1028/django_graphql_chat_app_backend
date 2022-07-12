# import asyncio
import graphene
from .decorators import login_required_sub
from graphene_django import DjangoListField
# from graphene_django.types import DjangoObjectType

from django.core import serializers
from .types import MessageType
from .models import Message
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


# import json
# from django.core import serializers



class Subscription(graphene.ObjectType):
    new_message = graphene.Field(MessageType,team_id = graphene.Int())

    @login_required_sub
    async def resolve_new_message(self, info,team_id):
        # print(info.context['user'])
        user = info.context['user']
        channel_name = await channel_layer.new_channel()
        await channel_layer.group_add(str(team_id), channel_name)
        try:
            while True:
                message = await channel_layer.receive(channel_name)
                x = database_sync_to_async(lambda: Message.objects.get(id=message['id']))()
                print(dir(x))

                yield database_sync_to_async(lambda: Message.objects.get(id=message['id']))()
        except Exception as e:
            print(e)
        finally:
            await channel_layer.group_discard(str(user.team_name), channel_name)
