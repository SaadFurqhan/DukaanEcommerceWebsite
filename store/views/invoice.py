from django.http import HttpResponse
from django.views.generic import View
from store.utils import render_to_pdf 
from django.template.loader import get_template
from store.models.orders import Order

class GeneratePDF(View):
    def post(self, request, *args, **kwargs):
        orderId = request.POST.get("orderId")
        orders = Order.get_allorders_by_orderid(orderId)
        get_Single_Order = Order.get_allorders_by_order_id(orderId)
        template = get_template('invoice.html')
        context = {
            "orderId": orderId,
            "orders": orders,
            "singleOrder" : get_Single_Order
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s" %(orderId)
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")