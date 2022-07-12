from celery import shared_task
# from celery.contrib.abortable import AbortableTask
# from backend.models import OTP, Wallet, AllTransactionHistory, DigitalWallet
# from web3 import Web3

import time
# import requests

# from pycoingecko import CoinGeckoAPI

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags




@shared_task
def emails(to_email, email_type):
    from_email = 'dev.metatest@gmail.com'
    if email_type=="welcome_mail":
        # if OTP.objects.filter(user_id=user_id, verified=False, expired = False).exists():
        #     otp= OTP.objects.filter(user_id=user_id, verified=False, expired = False).latest("created_at")
        # else:
        #     otp = OTP.objects.create(user_id=user_id)
        # print(183)
        # otp.create_slug()
        # # for obj in serializers.deserialize("json", user_instance):
        # #     user  = obj.object
        # # otp = OTP.objects.get(user_id=user_id)
        # to_email = otp.user.email
        subject = 'XXXXX Password Reset'
        # plain_message = strip_tags(html_message)
        context = {
           

        }        
        html_message = render_to_string('emails/welcome_mail.html', context=context)
    
        plain_message = strip_tags(html_message)
        result = send_mail(subject, plain_message, from_email,[to_email], html_message=html_message)
