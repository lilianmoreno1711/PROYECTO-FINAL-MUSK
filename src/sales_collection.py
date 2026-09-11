class SalesCollection:
    def __init__(self, sales=None):
        self.sales = sales or []

    def add(self, sale):
        self.sales.append(sale)

    def total_amount(self):
        return sum(sale.amount for sale in self.sales)

    def count(self):
        return len(self.sales)

    def to_list(self):
        return [sale.to_dict() for sale in self.sales]