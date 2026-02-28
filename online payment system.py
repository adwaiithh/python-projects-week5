class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
        print("Credit Card transaction successful.\n")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")
        print("UPI transaction successful.\n")


class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Digital Wallet.")
        print("Wallet transaction successful.\n")


def process_payment(payment_method, amount):
    payment_method.pay(amount)


credit = CreditCardPayment()
upi = UPIPayment()
wallet = WalletPayment()

process_payment(credit, 2000)
process_payment(upi, 1500)
process_payment(wallet, 500)