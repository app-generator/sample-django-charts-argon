var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
var modal = $('#modal-system');

$(document).ready(function () {
    // Get Order Form to Create or Edit
    $('#orderItems').on('click', '.get-order-form', function (event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.attr('href');
        var params = [];
        params['url'] = url;
        AjaxGETOrderForm(params);
    });

    // Save order after click save-order class
    modal.on('click', '.save-order', function (event) {
        event.preventDefault();
        var btn = $(this);
        var form = btn.closest('form');
        var url = form.attr('action');
        var params = [];
        params['url'] = url;
        params['method'] = form.attr('method');
        params['query'] = form.serialize();
        AjaxPOSTOrderForm(params);
    });
});


// Functions

function AjaxGETOrderForm(params) {
    $.ajax({
        url: params['url'],
        type: 'GET',
        success: function (data) {
            modal.find('.modal-content').html(data.template);
            modal.modal();
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}


function AjaxPOSTOrderForm(params) {
    $.ajax({
        url: params['url'],
        type: params['method'],
        data: params['query'],
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
        },
        success: function (data) {
            notification[data.valid](data.message);

            if (data.valid === 'success') {
                if (params['method'] === 'PUT')
                    $('.order-list').find(".get-order-form[href='" + params['url'] + "']").closest('tr').replaceWith(data.item);
                else
                    $('.order-list tbody').prepend(data.item);
                modal.modal('hide');

                setTimeout(function () {
                    location.reload();
                }, 2000);
            }
        },
        error: function () {
            notification.error('Error occurred');
        }
    });
}


// charts function

function SalesChart(data, labels = months) {
    // Variables
    var sales_chart_data = [];
    $.each(data, function (index, obj) {
        sales_chart_data.push(obj.total_price);
    });

    var $chart = $('#chartSales');

    var salesChart = new Chart($chart, {
        type: 'line',
        options: {
            scales: {
                yAxes: [{
                    gridLines: {
                        lineWidth: 1,
                        color: Charts.colors.gray[900],
                        zeroLineColor: Charts.colors.gray[900]
                    },
                    ticks: {
                        callback: function (value) {
                            if (!(value % 10)) {
                                return '$' + value;
                            }
                        }
                    }
                }]
            },
            tooltips: {
                callbacks: {
                    label: function (item, data) {
                        var label = data.datasets[item.datasetIndex].label || '';
                        var yLabel = item.yLabel;
                        var content = '';

                        if (data.datasets.length > 1) {
                            content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                        }

                        content += '$' + yLabel;
                        return content;
                    }
                }
            }
        },
        data: {
            labels: labels,
            datasets: [{
                label: 'Performance',
                data: sales_chart_data
            }]
        }
    });

    // Save to jQuery object
    $chart.data('chart', salesChart);
}

function OrderChart(data, labels = months) {
    var orders_chart_data = [];
    $.each(data, function (index, obj) {
        orders_chart_data.push(obj.total_order);
    });

    var $chart = $('#chartOrders');

    var ordersChart = new Chart($chart, {
        type: 'bar',
        options: {
            scales: {
                yAxes: [{
                    gridLines: {
                        lineWidth: 1,
                        color: '#dfe2e6',
                        zeroLineColor: '#dfe2e6'
                    },
                    ticks: {
                        callback: function (value) {
                            if (!(value % 10)) {
                                //return '$' + value + 'k'
                                return value
                            }
                        }
                    }
                }]
            },
            tooltips: {
                callbacks: {
                    label: function (item, data) {
                        var label = data.datasets[item.datasetIndex].label || '';
                        var yLabel = item.yLabel;
                        var content = '';

                        if (data.datasets.length > 1) {
                            content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                        }

                        content += yLabel;

                        return content;
                    }
                }
            }
        },
        data: {
            labels: labels,
            datasets: [{
                label: 'Sales',
                data: orders_chart_data
            }]
        }
    });

    // Save to jQuery object
    $chart.data('chart', ordersChart);
}