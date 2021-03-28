from django.db import models
from django.contrib.auth.models import User


class UserQualifications(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalizedName = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profiles(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    qualification = models.ManyToManyField(UserQualifications, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    isHighSchoolGraduate = models.BooleanField(default=False)
    isUndergraduate = models.BooleanField(default=False)
    isCollegeGraduate = models.BooleanField(default=False)
    isDoctor = models.BooleanField(default=False)
    isExpert = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profiles'