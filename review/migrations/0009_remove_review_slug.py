# Generated by Django 3.2 on 2022-04-29 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_alter_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]
