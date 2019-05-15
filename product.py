
class Product(object):
    def __init__ (self, price, item, weight, brand):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        print self.status
        return self  # chained methods
        

    def add_tax(self, tax):
        self.price = (self.price * tax) + self.price
        

    def return_reason(self, return_reason):
        self.return_reason = return_reason

        if return_reason == 'defective': 
            self.status = "defective"
            self.price = 0
            return self  # chained methods

        elif return_reason == 'like new':
            self.status = 'for sale'
            return self  # chained methods

        elif return_reason == 'opened box':
            self.status = 'used'
            self.price *= .20   
            return self #chained methods    

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Item Name: ' + str(self.item)
        print 'Weight: ' + str(self.weight) + 'lbs'
        print 'Brand: ' + str(self.brand)
        print 'Status: ' + str(self.status)
        

product1 = Product(100, 'iPhone', 2, 'Apple')
product1.add_tax(.09)
product1.return_reason('like new').sell()
product1.display_all()
