from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stampled Model Definition """

    created = models.DateTimeField()
    updated = models.datetimeField()

    class Meta:
        abstract = True
