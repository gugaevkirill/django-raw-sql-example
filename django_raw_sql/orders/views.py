from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.template import loader

from .utils import dictfetchall


def test_view(request: HttpRequest) -> HttpResponse:
    with connection.cursor() as cursor:
        cursor.execute('''SELECT c.first_name,
    c.last_name,
    e.email_address,
    o.order_number
FROM orders o
INNER JOIN order_status os ON os.status_id = o.status_id
INNER JOIN customers c ON c.customer_id = o.customer_id
INNER JOIN emails e ON e.email_id = c.email_id
WHERE os.paid IS TRUE
    ''')
        orders = dictfetchall(cursor)

    template = loader.get_template('test_view.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))
