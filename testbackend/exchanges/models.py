from django.conf import settings
from django.db import models


class Exchange(models.Model):
    valute1 = models.CharField(max_length=3, null=False, verbose_name="Валюта1")
    valute2 = models.CharField(max_length=3, null=False, verbose_name="Валюта2")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, verbose_name="Пользователь",
                             on_delete=models.CASCADE)
