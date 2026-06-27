class Cart():
    def __init__(self,request):
        self.session = request.session
        cart =  request.session.get('cart')
        if 'cart' not in self.session:
            cart = self.session['cart'] = {}
        self.cart = cart