from django.core.urlresolvers import reverse
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from user.models import UserTicketModel


class UserMiddle(MiddlewareMixin):
    def process_request(self, request):
        need_login =['/axf/mine/','/axf/addcart/', '/axf/subcart/',
                     '/axf/cart/','/axf/generateorder/', '/axf/waitpay/', '/axf/orderpay/']
        if request.path in need_login:
            ticket = request.COOKIES.get('ticket')
            if not ticket:
                return HttpResponseRedirect(reverse('user:login'))
            user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
            if user_ticket:
                if datetime.utcnow() > user_ticket.out_time.replace(tzinfo=None):
                    UserTicketModel.objects.filter(ticket=user_ticket).delete()
                    return HttpResponseRedirect(reverse('user:login'))
                else:
                    request.user = user_ticket.user
                    UserTicketModel.objects.filter(Q(user=user_ticket.user) & ~Q(ticket=ticket)).delete()
                    return None

            else:
                return HttpResponseRedirect(reverse('user:login'))

        else:
            return None