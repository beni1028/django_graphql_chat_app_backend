from typing_extensions import Required
from graphql_auth import mutations
import graphene
from graphql_jwt.decorators import login_required
from .types import MessageType
from .models import Message


class AuthMutation(graphene.ObjectType):
    # register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    # password_set = mutations.PasswordSet.Field() # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    # delete_account = mutations.DeleteAccount.Field()
    # send_secondary_email_activation =  mutations.SendSecondaryEmailActivation.Field()
    # verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    # swap_emails = mutations.SwapEmails.Field()
    # remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()




class SendMessage(graphene.Mutation):
    class Arguments:
        message = graphene.String(required= True)
        team_id = graphene.Int(required = True)

    Message_status = graphene.Boolean()

    # @login_required
    def mutate(parent, info, message,team_id ):
        Message.objects.create(user=info.context.user,message=message,team_name=info.context.user.current_user.get(id=team_id).team_name,team=info.context.user.current_user.get(id=team_id))
        Message_status =True
        return Message_status 

class Mutation(AuthMutation, graphene.ObjectType):
    send_message = SendMessage.Field()