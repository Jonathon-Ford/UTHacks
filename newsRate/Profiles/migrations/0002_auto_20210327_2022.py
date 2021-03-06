# Generated by Django 3.1.7 on 2021-03-28 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('normalizedName', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='areaOfExpertise',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='level',
        ),
        migrations.AddField(
            model_name='profiles',
            name='isCollegeGraduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profiles',
            name='isDoctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profiles',
            name='isExpert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profiles',
            name='isHighSchoolGraduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profiles',
            name='isUndergraduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='qualification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profiles.userqualifications'),
        ),
    ]
