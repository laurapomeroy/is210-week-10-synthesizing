#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Return a combined dictionary"""


def sum_orders(customers, orders):
    """Takes two parameters then combined two datasets into a single dictionary

    Args:
        customers(dict): A dictionary of customers keyed by customer_id
        orers(dict): A dictionary of orders keyed by order id

    Return:
        Returns a new, combined dictionary

    Examples:
    >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
        3: {'customer_id': 2, 'total': 10},
        4: {'customer_id': 3, 'total': 15}}
    >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
        3: {'name': 'Person Two', 'email': 'email@two.com'}}
    >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'orders': 2, 'total': 20, 'name': 'Person One', 'email':
        'email@one.com'}, 3: {'orders': 1, 'total': 15, 'name': 'Person Two',
        'email': 'email@two.com'}}
    """
    customers = {}
    for key, value in customers.iteritems():
        total_orders = 0
        number_orders = 0
        for request in orders.values():
            if key == request['customer_id']:
                total_orders += request['total']
                number_orders += 1
                customers[key] = {'name': value['name'],
                                  'email': value['email'],
                                  'orders': number_orders,
                                  'total': total_orders}
    return customers
