from django.db import models
import os
from twilio.rest import Client
# Create your models here.

class Detail(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = '****************'
        auth_token = '******************'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=f'Hi {self.name}! {self.details}',
                                    from_='******',
                                    to='+8801735700187'
                                )

        print('your sms id',message.sid)
        return super().save(*args, **kwargs)

