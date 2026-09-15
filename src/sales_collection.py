class SalesCollection:
    def __init__(self, sales=None):
        self.sales = sales or []

    def add(self, sale):
        self.sales.append(sale)

    def total_amount(self):
        return sum(sale.amount for sale in self.sales)

    def count(self):
        return len(self.sales)

    def sales_by_client(self, client_id):
        result = []

        for sale in self.sales:
            if sale.client_id == client_id:
                result.append(sale)

        return result

    def total_amount_by_client(self, client_id):
        total = 0

        for sale in self.sales:
            if sale.client_id == client_id:
                total += sale.amount

        return total

    def to_list(self):
        return [sale.to_dict() for sale in self.sales]