from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForms
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForms(request.POST)
        if form.is_valid():
            order =  form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # clear the cart
                cart.clear()
                return render(request,
                              'orders/order/created.html',
                              {'order':order})
    else:
        form = OrderCreateForms()
    
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
