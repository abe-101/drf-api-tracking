# Generated by Django 4.2.1 on 2023-05-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_tracking', '0012_auto_20210930_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='apirequestlog',
            name='user_agent',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]