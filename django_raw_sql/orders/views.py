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


def test_view_full(request: HttpRequest) -> HttpResponse:
    """
    This version is not working due to incorrect SQL-request:

    syntax error at or near ":"
    LINE 9:                     'product_name': cp.product_name,
    """
    with connection.cursor() as cursor:
        cursor.execute('''SELECT c.first_name,
    c.last_name,
    e.email_address,
    o.order_number,
    ARRAY_AGG(
        CASE
            WHEN cp.product_id IS NOT NULL THEN
                JSONB_BUILD_OBJECT(
                    'product_name': cp.product_name,
                    'price': cp.price
                )
            ELSE
                JSONB_BUILD_OBJECT(
                    'product_name': ncp.product_name,
                    'price': ncp.price
                )
        END
    ) products
FROM orders o
INNER JOIN order_status os ON os.status_id = o.status_id
INNER JOIN customers c ON c.customer_id = o.customer_id
INNER JOIN emails e ON e.email_id = c.email_id
INNER JOIN order_items oi ON oi.order_id = o.order_id
LEFT JOIN custom_products cp ON cp.product_id = oi.product_id
LEFT JOIN non_custom_products ncp ON ncp.p_id = oi.p_id
WHERE os.paid IS TRUE
    ''')
        orders = dictfetchall(cursor)

    template = loader.get_template('test_view.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))
