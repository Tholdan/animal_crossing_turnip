# Generated by Django 3.0.4 on 2020-03-21 21:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TurnipWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='week')),
                ('buy_price', models.IntegerField(verbose_name='buy price')),
            ],
            options={
                'ordering': ['week'],
            },
        ),
        migrations.CreateModel(
            name='TurnipDailyCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'monday'), (1, 'tuesday'), (2, 'wednesday'), (3, 'thursday'), (4, 'friday'), (5, 'saturday'), (6, 'sunday')], verbose_name='day')),
                ('day_time', models.IntegerField(choices=[(0, 'morning'), (1, 'noon')], verbose_name='day time')),
                ('sell_price', models.IntegerField(verbose_name='sell price')),
                ('turnip_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnip.TurnipWeek')),
            ],
            options={
                'ordering': ['turnip_week', 'day', 'day_time'],
            },
        ),
    ]
