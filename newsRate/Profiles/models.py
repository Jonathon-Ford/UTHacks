from django.db import models
from django.contrib.auth.models import User


class UserQualifications(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalizedName = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)


class Profiles(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    name = models.CharField(max_length=50, blank=True, null=True)
    isHighSchoolGraduate = models.BooleanField()
    isUndergraduate = models.BooleanField()
    isCollegeGraduate = models.BooleanField()
    isDoctor = models.BooleanField()
    isExpert = models.BooleanField()
