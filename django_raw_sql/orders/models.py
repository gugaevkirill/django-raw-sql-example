from django.db import models


class Email(models.Model):
    email_id = models.BigAutoField('Email ID', primary_key=True)
    email_address = models.EmailField('Email Address')

    class Meta:
        db_table = 'emails'
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class Customer(models.Model):
    customer_id = models.BigAutoField('Customer ID', primary_key=True)
    first_name = models.TextField('First Name')
    last_name = models.TextField('Last Name')
    email = models.ForeignKey(Email, verbose_name='Email', on_delete=models.CASCADE)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class OrderStatus(models.Model):
    status_id = models.BigAutoField('Status ID', primary_key=True)
    paid = models.BooleanField('Paid', default=False)

    class Meta:
        db_table = 'order_status'
        verbose_name = 'OrderStatus'
        verbose_name_plural = 'OrderStatuses'


class CustomProduct(models.Model):
    product_id = models.BigAutoField('Product ID', primary_key=True)
    product_name = models.TextField('Product Name')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'custom_products'
        verbose_name = 'CustomProduct'
        verbose_name_plural = 'CustomProducts'


class NonCustomProduct(models.Model):
    p_id = models.BigAutoField('P ID', primary_key=True)
    product_name = models.TextField('Product Name')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'non_custom_products'
        verbose_name = 'NonCustomProduct'
        verbose_name_plural = 'NonCustomProducts'


class Order(models.Model):
    order_id = models.BigAutoField('Order ID', primary_key=True)
    order_number = models.TextField('Order Number')
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, verbose_name='OrderStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order_item_id = models.BigAutoField('OrderItem ID', primary_key=True)
    order = models.ForeignKey(Order, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(
        CustomProduct,
        verbose_name='CustomProduct',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    p = models.ForeignKey(
        NonCustomProduct,
        verbose_name='NonCustomProduct',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'order_items'
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
