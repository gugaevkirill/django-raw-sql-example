from django.http import HttpRequest, HttpResponse

from orders.models import Order
from django.template import loader

def test_view(request: HttpRequest) -> HttpResponse:
    orders = Order.objects.raw('''SELECT c.first_name,
    c.last_name,
    e.email_address,
    o.order_number,
    o.order_id
FROM orders o
INNER JOIN order_status os ON os.status_id = o.status_id
INNER JOIN customers c ON c.customer_id = o.customer_id
INNER JOIN emails e ON e.email_id = c.email_id
WHERE os.paid IS TRUE
    ''')

    template = loader.get_template('test_view.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))
