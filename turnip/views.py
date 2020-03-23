import json

from django.http import HttpResponse
from django.shortcuts import render

from turnip.models import TurnipWeek, TurnipDailyCost


def turnip_statistics_view(request):
    if request.is_ajax():
        week_id = request.GET.get('week_id')

        response_data = {
            'buy_price': TurnipWeek.objects.get(id=week_id).buy_price
        }

        turnip_daily_costs = []
        turnip_daily_costs_items = TurnipDailyCost.objects.filter(turnip_week_id=week_id)
        for day_choice in TurnipDailyCost.DAY_CHOICES:
            for day_time_choice in TurnipDailyCost.DAY_TIME_CHOICES:
                try:
                    turnip_daily_cost = turnip_daily_costs_items.get(day=day_choice[0], day_time=day_time_choice[0])
                    turnip_daily_costs.append(turnip_daily_cost.sell_price)
                except TurnipDailyCost.DoesNotExist:
                    turnip_daily_costs.append(None)

        response_data.update({
            'sell_prices': turnip_daily_costs
        })

        return HttpResponse(json.dumps(response_data), content_type='application/json')

    context = {
        'weeks': TurnipWeek.objects.order_by('week')
    }

    return render(request, template_name='turnip.html', context=context)
