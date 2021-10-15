from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JkuVGE7NDMlPazXqZC3PS2TGCC2J5c0bQh2kYgv3MyclycHDlggEl57bjXdzw80OZa5pdtNR02qp1c6N4Y4RPa400Nfittzl0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
