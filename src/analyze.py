import json
import csv
import pandas as pd

from client import Client
from sale import Sale
from client_collection import ClientCollection
from sales_collection import SalesCollection

#1.
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

#2.
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

print("Clientes cargados:", len(clients.clients))
print("Ventas cargadas:", len(sales.sales))

total_clients = len(clients.clients)

print("Total de clientes:", total_clients)

total_sales = sales.count()

print("Total de ventas:", total_sales)

total_revenue = sales.total_amount()

print("Ingresos totales:", total_revenue)

income_per_client = {}

for client in clients.clients:
    total = 0

    for sale in sales.sales:
        if sale.client_id == client.client_id:
            total += sale.amount

    income_per_client[client.name] = total

print("Ingresos por cliente:", income_per_client)

sales_count_per_client = {}

for client in clients.clients:
    count = 0

    for sale in sales.sales:
        if sale.client_id == client.client_id:
            count += 1

    sales_count_per_client[client.name] = count

print("Número de ventas por cliente:", sales_count_per_client)

average_sale_per_client = {}

for client in clients.clients:
    total = 0
    count = 0

    for sale in sales.sales:
        if sale.client_id == client.client_id:
            total += sale.amount
            count += 1

    if count > 0:
        average_sale_per_client[client.name] = total / count
    else:
        average_sale_per_client[client.name] = 0

print("Promedio de venta por cliente:", average_sale_per_client)

#7.
top_client_by_country = {}

for client in clients.clients:
    total = income_per_client[client.name]

    if client.country not in top_client_by_country:
        top_client_by_country[client.country] = {
            "client": client.name,
            "total": total
        }
    elif total > top_client_by_country[client.country]["total"]:
        top_client_by_country[client.country] = {
            "client": client.name,
            "total": total
        }

print("Cliente con mayor gasto por país:", top_client_by_country)

#8.
sales_by_category = {}

for sale in sales.sales:
    if sale.category not in sales_by_category:
        sales_by_category[sale.category] = 0

    sales_by_category[sale.category] += sale.amount

print("Ventas por categoría:", sales_by_category)

#9.
most_sales_by_category = {}

for category in sales_by_category:
    sales_in_category = []

    for sale in sales.sales:
        if sale.category == category:
            sales_in_category.append(sale)

    client_counts = {}

    for sale in sales_in_category:
        if sale.client_id not in client_counts:
            client_counts[sale.client_id] = 0

        client_counts[sale.client_id] += 1

    top_client_id = max(client_counts, key=client_counts.get)

    top_client = clients.get_by_id(top_client_id)

    most_sales_by_category[category] = {
        "client": top_client.name,
        "sales_count": client_counts[top_client_id]
    }

print("Cliente con más ventas por categoría:", most_sales_by_category)

#10.
sales_df = pd.read_csv("data/sales.csv")

sales_df["date"] = pd.to_datetime(sales_df["date"])

sales_df["month"] = sales_df["date"].dt.to_period("M").astype(str)

monthly_sales = sales_df.groupby("month")["amount"].sum().to_dict()

print("Ventas mensuales:", monthly_sales)