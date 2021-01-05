from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    
    def __init__(self, request):
        """
            Init cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, product, quantity=1, overrride_quantity=False):
        """
            Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id  not in self.card:
            self.cart[product_id] = {'quantity':0,
                                     'price':str(product.price)}
            
        if overrride_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        # Mark the session as "modified" to make sure it gets save
        self.session.modified = True
    
    def remove(self, product):
        """
            Remove a product from cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        