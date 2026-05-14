from .dummy_data import ORDERS


def get_order_status(order_id: str):

    order = ORDERS.get(order_id)

    if order:
        return order["status"]

    return "Order not found"
