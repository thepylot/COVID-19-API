from django.db import models

class Coronavirus(models.Model):
    country = models.CharField(max_length=255)
    cases = models.IntegerField()
    death = models.IntegerField()
    recovers = models.IntegerField()

    def __str__(self):
        return self.country