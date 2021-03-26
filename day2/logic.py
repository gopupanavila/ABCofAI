"""Class for defining the business logic"""
from recommend import recommendations


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


class MLLogic:
    """
    ML based logic
    """
    title = "ABC of AI"

    appliance_choices = ('office', 'home', 'none')
    unit_prices = {
        'SECURITY LOCK': 8000, 'CAMERA': 10000, 'COMPUTER': 35000,
        'COFFEE MACHINE': 12000, 'WAITING LOUNGE': 23000,
        'KITCHEN SET': 2000, 'TELEVISION': 20000, 'SHOW CASE': 12000,
        'DRESSING TABLE': 15000, 'DOUBLE COT': 50000,
        'DISH WASHER': 35000, 'OVEN': 8000, 'TOASTER': 2000,
        'REFRIGERATOR': 25000, 'WASHING MACHINE': 25000, 'BLENDER': 2500,
        'VACCUM CLEANER': 10000, 'SHREDDER': 5000, 'LAZER PRINTER': 10000,
        'PAPER CLIP': 300, 'MARKER': 50, 'CALCULATOR': 200
    }

    items = {
        'office': ['SECURITY LOCK', 'CAMERA', 'COMPUTER', 'COFFEE MACHINE', 'WAITING LOUNGE',
                   'SHREDDER', 'LAZER PRINTER', 'PAPER CLIP', 'MARKER', 'CALCULATOR'],
        'home': ['KITCHEN SET', 'TELEVISION', 'SHOW CASE', 'DRESSING TABLE',
                 'DOUBLE COT', 'DISH WASHER', 'OVEN', 'TOASTER', 'REFRIGERATOR',
                 'WASHING MACHINE', 'BLENDER', 'VACCUM CLEANER']
    }

    def __init__(self):
        self.recommendations = []
        self.selected_choice = None
        self.user_preferences = None

    def set_choice(self, app_type):
        self.selected_choice = self.appliance_choices[app_type]
        self.recommendations.clear()

    def set_preferences(self, preferences):
        self.user_preferences = preferences

    def _set_recommendations(self):
        result = recommendations('appliances_rating.csv',
                                 self.selected_choice,
                                 self.user_preferences)
        cleaned_result = list(set(result))[:5]
        for _items in cleaned_result:
            proposed_item = {}
            for item, quantity in _items:
                proposed_item[item] = (quantity, self.unit_prices[item])
            self.recommendations.append(proposed_item)

    def get_recommendations(self):
        self._set_recommendations()
        return self.recommendations