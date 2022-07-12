from graphene_django import DjangoObjectType
from .models import User, Message, Team
from graphql_jwt.decorators import login_required
import graphene
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from .decorators import login_required_sub


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('__all__')



class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = ('__all__')
    
    extra_fileds = graphene.Field(UserType)

    async def resolve_extra_fileds(self, info):
        print(dir(self))
        print("here")
        x = database_sync_to_async(lambda: User.objects.get(id=self.user_id))()
        print(dir(x))
        # yield x
    # @login_required
    # async def resolve_extra_fileds(self, info):
    #     print(info.context['user'])
    #     # print("hereher")
    #     x = database_sync_to_async(lambda: Message.objects.get(id=info.context['user']))()
    #     print(x)
    #     yield database_sync_to_async(lambda: Message.objects.get(id=self.user.id))()


class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = ('__all__')
