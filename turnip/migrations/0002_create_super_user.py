from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import migrations


def create_superuser(apps, schema_editor):
    User.objects.create_superuser('ivan', 'ivanort97@gmail.com', '1234')


class Migration(migrations.Migration):
    dependencies = [
        ('turnip', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
