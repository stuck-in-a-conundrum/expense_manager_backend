from django.db import models
from django.contrib.auth.models import User
class Expenses(models.Model):
    created = models.DateField()
    title = models.CharField(max_length=255, blank=True, default="")
    amount=models.FloatField()
    owner = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

class Savings(models.Model):
    created = models.DateField()
    title = models.CharField(max_length=255, blank=True, default="")
    amount=models.FloatField()
    owner = models.ForeignKey(User, related_name='savings', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title