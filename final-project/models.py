'''
Classes for defining the structure of the database tables
'''

from django.contrib.auth.models import User # username max characters limited to 20 at this location
from django.db import models


class Reports(models.Model):

    class Meta:
        verbose_name_plural = "Reports"

    user_id_report = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    demo_id_report = models.ForeignKey(Demos, on_delete=models.SET_NULL, null=True)
    report = models.CharField(max_length = 512)
    # Admin to change to true manually when report read
    read = models.BooleanField(default=False)
    # Admin to input action taken manually when report read
    action = models.CharField(max_length = 512, blank=True, null=True)
    timedate = models.DateField(auto_now=True)
    user_pk = models.IntegerField(null = True, blank = True)
    demo_pk = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return f"{self.demo_id_report} {self.timedate}"


