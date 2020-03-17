from django.db import models


class inbound(models.Model):
    general_source = models.CharField(max_length=20)
    general_innum = models.CharField(max_length=20, null = True)

