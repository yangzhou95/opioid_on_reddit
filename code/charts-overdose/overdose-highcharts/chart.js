$.getJSON('./convertcsv.json', function (data) {
    Highcharts.chart('container', {


        title: {
            text: 'Drug Overdose Death Rates By Age'
        },

        subtitle: {
            text: 'Source: kff.org'
        },

        yAxis: {
            title: {
                text: 'Number of Deaths'
            },
            max: 16000,
            tickInterval: 2000
        },
        xAxis: {
            title: {
                text: 'Years'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },

        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 1999
            }
        },

        series: [{
            name: '15-24',
            data: data['15-24']
        }, {
            name: '25-34',
            data: data['25-34']
        }, {
            name: '35-44',
            data: data['35-44']
        }, {
            name: '45-54',
            data: data['45-54']
        }, {
            name: '55-64',
            data: data['55-64']
        }, {
            name: "65 and Over",
            data: data['65 and Over']
        }],

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }

    });
});