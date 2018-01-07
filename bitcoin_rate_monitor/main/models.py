import requests
import json
import operator
from collections import namedtuple

from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=255)
    api = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def latest_rate(self):
        if self.rate_set.last():
            return self.rate_set.last().rate
        return 0.0

    @property
    def latest_rate_updated_on(self):
        if self.rate_set.last():
            return self.rate_set.last().updated_on
        return 0.0

    def get_latest_rate(self):
        respond = requests.get(self.api).text
        data = json.loads(respond, object_hook=lambda d: namedtuple('_', d.keys())(*d.values()))
        return operator.attrgetter(self.key)(data)

    def do_update_rate(self):
        rate = Rate(rate=self.get_latest_rate(), provider_id=self.id)
        rate.save()

    def __str__(self):
        return self.name


class Rate(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    rate = models.DecimalField(max_digits=12, decimal_places=2)

    # RELATIONAL FIELDS
    # ---------------------------------------------------------------
    provider = models.ForeignKey(Provider, null=True)

    def __str__(self):
        return str(self.rate)
