from django.db import models

class Experience(models.Model):
    field_exp = models.CharField(max_length=200)
    exp = models.CharField(max_length=600)


class Skill(models.Model):
    field_skill = models.CharField(max_length=200)
    skill = models.CharField(max_length=600)

class Rate(models.Model):
    rating=models.CharField(max_length=200)
    rating_val=models.IntegerField()
    comment=models.CharField(max_length=1000)
