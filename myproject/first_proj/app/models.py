from django.db import models

# Create your models here.

class Table(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.TextField(db_column='date & time', blank=True, null=True)
    use = models.FloatField(db_column='use [kw]', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'better'

