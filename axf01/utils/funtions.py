import random


def get_ticket():
    ticket = ''
    s = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(30):
        ticket += random.choice(s)
    ticket = 'TK_' + ticket
    return ticket

def get_order_random_id():
    order_num = ''
    s = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(30):
        order_num += random.choice(s)

    return order_num