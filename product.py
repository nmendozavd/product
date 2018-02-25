class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "Sold"
        print self.status

    def add_tax(self, tax):
        return self.price * .08

    def return_item(self, reason, condition):
        self.return_reason = return_reason
        self.condition = condition

        if return_reason == "defective"
            self.status = "defective"
            self.price = 0

        elif condition == "opened box"
            self.status = "used"
            self.price = self.price * .20

    def display_all(self):
        print 'Price', str(self.price)
        print 'Item Name', str(self.item_name)
        print 'Weight', str(self.weight)
        print 'Brand', str(self.brand)
        print 'Cost', str(self.cost)
        return self
