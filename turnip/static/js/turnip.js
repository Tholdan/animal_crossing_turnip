function createChart(buyPrice, data) {
    new Chart($('#myChart'), {
        type: 'line',
        data: {
            labels: ['Monday morning', 'Monday noon', 'Tuesday morning', 'Tuesday moon', 'Wednesday morning',
                'Wednesday noon', 'Thursday morning', 'Thursday noon', 'Friday morning', 'Friday noon',
                'Saturday morning', 'Saturday noon'],
            datasets: [{
                label: "Buy price",
                data: Array(12).fill(buyPrice),
                borderColor: "#BF3F3F",
                backgroundColor: "rgba(191, 63, 63, 0.1)"
            },
            {
                label: "Sell price",
                data: data,
                borderColor: "#59A559",
                backgroundColor: "rgba(0, 0, 0, 0)"
            }]
        },
        options: {
            spanGaps: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

function reloadChart() {
    const weekId = $('#week-selector').val();
    $.ajax({
        url: '',
        data: {
            'week_id': weekId
        },
        success: function (data) {
            createChart(data['buy_price'], data['sell_prices'])
        }
    })
}

$(document).ready(function() {
   reloadChart();

   $('#week-selector').niceSelect();
   $('#week-selector').on('change', function() {
       reloadChart()
   });
});
