from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponse

from .models import Payment
from .models import Product
from paymentwrapper.payment_wrapper import PaymentWrapper

def index(request):
    pass

def product(request, id):
    product = get_object_or_404(Product, id)
    return render_to_response('market/product.html', {'product':id}, RequestContext(request))

def callback(request):
    input_address = request.GET.get("input_address")
    payment = Payment.objects.get(input_address=input_address)
    payment.state = "CH"
    payment.save()
    return HttpResponse("ok")

def pay(request):
    product_id = request.GET.get("product_id")
    product = Product.objects.get(product_id=product_id)
    p = PaymentWrapper(product.price, product.Account.address)
    input_address = p.generate()
    payment = Payment.object.create(product=product, input_address=input_address)
    payment.save()
