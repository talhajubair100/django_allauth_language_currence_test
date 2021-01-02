from django.db import models
from django.contrib.auth.models import User
from currencies.models import Currency

class EmployeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    text = models.CharField(max_length=100)
    discription = models.TextField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    def __str__(self):
        return self.text
    