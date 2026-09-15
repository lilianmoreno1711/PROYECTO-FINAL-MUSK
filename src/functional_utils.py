def get_top_client_by_category(sales, clients, category):
    category_sales = list(
        filter(lambda sale: sale.category == category, sales)
    )

    best_client = None
    max_sales = 0

    for client in clients:
        client_sales = list(
            filter(lambda sale: sale.client_id == client.client_id, category_sales)
        )

        if len(client_sales) > max_sales:
            max_sales = len(client_sales)
            best_client = client.name

    return best_client