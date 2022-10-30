from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s: %s: %s" % (self.name, self.state_code, self.country_code)
