class Order:
    def __init__(self, products):
        # products are list of products name, price and qty
        self.products = products
        self.status = "unpaid"

    def calculate_total(self):
        # calculate the total price of all products
        total = 0
        for name, price, qty in self.products:
            total += price * qty
        return total

    def make_payment(self, payment_gateway):
        # total amount to pay
        total = self.calculate_total()

        # external payment service
        total_amt = payment_gateway.execute_payment(total)

        if total_amt:
            self.status = "paid"
        else:
            self.status = "Unpaid"

        return total_amt
