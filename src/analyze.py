import json
import csv
import pandas as pd

try:
    from .client import Client
    from .sale import Sale
    from .client_collection import ClientCollection
    from .sales_collection import SalesCollection
except ImportError:
    from client import Client
    from sale import Sale
    from client_collection import ClientCollection
    from sales_collection import SalesCollection

def generate_report():
    # ==============================
    # 1. CARGAR CLIENTES
    # ==============================

    with open("data/clients.json", "r", encoding="utf-8") as file:
        clients_data = json.load(file)

    clients = ClientCollection()

    for client_data in clients_data:
        client = Client(
            client_data["client_id"],
            client_data["name"],
            client_data["country"],
            client_data["signup_date"]
        )
        clients.add(client)

    # ==============================
    # 2. CARGAR VENTAS
    # ==============================

    with open("data/sales.csv", "r", encoding="utf-8") as file:
        sales_data = csv.DictReader(file)

        sales = SalesCollection()

        for sale_data in sales_data:
            sale = Sale(
                sale_data["sale_id"],
                int(sale_data["client_id"]),
                sale_data["product"],
                sale_data["category"],
                float(sale_data["amount"]),
                sale_data["date"]
            )
            sales.add(sale)

    # ==============================
    # 3. TOTAL CLIENTES
    # ==============================

    total_clients = len(clients.clients)

    # ==============================
    # 4. TOTAL VENTAS
    # ==============================

    total_sales = sales.count()

    # ==============================
    # 5. INGRESOS TOTALES
    # ==============================

    total_revenue = sales.total_amount()

    # ==============================
    # 6. INGRESOS POR CLIENTE
    # ==============================

    income_per_client = {}

    for client in clients.clients:
        total = 0

        for sale in sales.sales:
            if sale.client_id == client.client_id:
                total += sale.amount

        income_per_client[client.name] = total

    # ==============================
    # 7. NÚMERO DE VENTAS POR CLIENTE
    # ==============================

    sales_count_per_client = {}

    for client in clients.clients:
        count = 0

        for sale in sales.sales:
            if sale.client_id == client.client_id:
                count += 1

        sales_count_per_client[client.name] = count

    # ==============================
    # 8. PROMEDIO DE VENTA POR CLIENTE
    # ==============================

    average_sale_per_client = {}

    for client in clients.clients:
        total = 0
        count = 0

        for sale in sales.sales:
            if sale.client_id == client.client_id:
                total += sale.amount
                count += 1

        if count > 0:
            average_sale_per_client[client.name] = round(total / count, 2)
        else:
            average_sale_per_client[client.name] = 0

    # ==============================
    # 9. CLIENTE CON MAYOR GASTO POR PAÍS
    # ==============================

    top_client_by_country = {}

    for client in clients.clients:
        total = income_per_client[client.name]

        if client.country not in top_client_by_country:
            top_client_by_country[client.country] = client.name

        else:
            current_client = top_client_by_country[client.country]

            if total > income_per_client[current_client]:
                top_client_by_country[client.country] = client.name

    # ==============================
    # 10. VENTAS POR CATEGORÍA
    # ==============================

    sales_by_category = {}

    for sale in sales.sales:
        if sale.category not in sales_by_category:
            sales_by_category[sale.category] = 0

        sales_by_category[sale.category] += sale.amount

    # ==============================
    # 11. CLIENTES DE ALTO GASTO
    # ==============================

    threshold = 500

    high_spending_clients = {}

    for client in clients.clients:
        total = income_per_client[client.name]

        if total > threshold:
            high_spending_clients[client.name] = total

    # ==============================
    # 12. VENTAS MENSUALES CON PANDAS
    # ==============================

    sales_df = pd.read_csv("data/sales.csv")

    sales_df["date"] = pd.to_datetime(sales_df["date"])

    sales_df["month"] = sales_df["date"].dt.to_period("M").astype(str)

    monthly_sales = sales_df.groupby("month")["amount"].sum().to_dict()

    # ==============================
    # 13. INFORMACIÓN DE CLIENTES
    # ==============================

    clients_report = []

    for client in clients.clients:
        clients_report.append({
            "client_id": client.client_id,
            "name": client.name,
            "country": client.country,
            "total_spent": income_per_client[client.name],
            "sale_count": sales_count_per_client[client.name],
            "average_sale": average_sale_per_client[client.name]
        })

    # ==============================
    # 14. REPORTE FINAL
    # ==============================

    final_report = {
        "summary": {
            "total_clients": total_clients,
            "total_sales": total_sales,
            "total_revenue": round(total_revenue, 2)
        },
        "clients": clients_report,
        "top_client_by_country": top_client_by_country,
        "sales_by_category": {
            category: round(total, 2)
            for category, total in sales_by_category.items()
        },
        "high_spending_clients": high_spending_clients,
        "monthly_sales": {
            month: round(total, 2)
            for month, total in monthly_sales.items()
        }
    }

    # ==============================
    # 15. GUARDAR JSON
    # ==============================

    with open("final_report.json", "w", encoding="utf-8") as file:
        json.dump(final_report, file, indent=4, ensure_ascii=False)

    return final_report


if __name__ == "__main__":
    report = generate_report()

    print("Clientes cargados:", report["summary"]["total_clients"])
    print("Ventas cargadas:", report["summary"]["total_sales"])
    print("Ingresos totales:", report["summary"]["total_revenue"])
    print("Reporte final generado: final_report.json")