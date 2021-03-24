"""Class for defining the business logic"""


class BusinessLogic:
    """
    Business logic of the application
    """
    title = "ABC of AI"
    header = ("Order", "Items", "Unit Price", "Quantity")
    items = {
        "Kitchen Set": 10000,
        "Television": 20000,
        "Show Case": 100000,
        "Dressing Table": 15000,
        "Double Cot": 30000
    }
    appliance_choices = ('office', 'home')

    def __init__(self):
        self.selected_items = {}
        self._grant_total = 0

    def total(self, commodity, quantity):
        if quantity:
            try:
                quantity = int(quantity)
            except ValueError as err:
                quantity = 0
            unit_price = self.items.get(commodity)
            _total = quantity * unit_price
            return _total

    def set(self, commodity, quantity):
        self.selected_items[commodity] = quantity

    def grant_total(self):
        if self._grant_total == 0:
            for item, qty in self.selected_items.items():
                result = self.total(item, qty)
                if result:
                    self._grant_total += result
        return self._grant_total

    def tax(self):
        return (self.grant_total() * 10) / 100.0

    def final_amount(self):
        return self.grant_total() + self.tax()
