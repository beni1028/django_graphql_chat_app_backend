import graphene

from graphql_auth.schema import UserQuery, MeQuery
from graphql_jwt.decorators import login_required
from graphene_django import DjangoListField
from .types import TeamType, MessageType
from .models import Message, Team


class Query(UserQuery, MeQuery, graphene.ObjectType):
    get_all_teams =DjangoListField(TeamType)
    get_sent_message_details = DjangoListField(MessageType,messgae_id=graphene.Int())


    @login_required
    def resolve_get_all_teams(parent, info):
        return Team.objects.filter(user=info.context.user)

    @login_required
    def resolve_sent_message_details(parent, info,message_id):
        return Message.objects.get(id=message_id)