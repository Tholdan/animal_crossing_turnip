from django.core.validators import MinValueValidator
from django.db import models


class TurnipWeek(models.Model):
    week = models.IntegerField(verbose_name='week', unique=True, validators=[MinValueValidator(0)])
    buy_price = models.IntegerField(verbose_name='buy price')

    class Meta:
        ordering = ['week']

    def __str__(self):
        return 'Week ' + str(self.week)


class TurnipDailyCost(models.Model):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    DAY_CHOICES = (
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday')
    )

    MORNING = 0
    NOON = 1
    DAY_TIME_CHOICES = (
        (MORNING, 'morning'),
        (NOON, 'noon')
    )

    turnip_week = models.ForeignKey(to=TurnipWeek, on_delete=models.CASCADE)
    day = models.IntegerField(verbose_name='day', choices=DAY_CHOICES)
    day_time = models.IntegerField(verbose_name='day time', choices=DAY_TIME_CHOICES)
    sell_price = models.IntegerField(verbose_name='sell price')

    class Meta:
        ordering = ['turnip_week', 'day', 'day_time']

    def __str__(self):
        return str(self.turnip_week) + ' ' + self.get_day_display() + ' ' + self.get_day_time_display()
