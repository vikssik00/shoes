import csv
import pymysql
import os

BASE_PATH = r"C:\Users\lulun\OneDrive\Рабочий стол\import"

def csv_path(name):
    return os.path.join(BASE_PATH, name)

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="shoes"
)

cursor = conn.cursor()

with open(csv_path("point_of_issue.csv")) as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO point_of_issue (address) VALUES (%s)",
            (row["address"],)
        )
conn.commit()
print("point_of_issue импортировано")

with open(csv_path("role.csv")) as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO role (name) VALUES (%s)",
            (row["name"],)
        )
conn.commit()
print("role импортировано")

with open(csv_path("user.csv")) as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        cursor.execute("""
            INSERT INTO `user`
            (last_name, first_name, patronymic, login, password, id_role)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["last_name"].strip(),
            row["first_name"].strip(),
            row["patronymic"].strip(),
            row["login"].strip(),
            row["password"].strip(),
            row["id_role"].strip()
        ))
conn.commit()
print("user импортировано")

with open(csv_path("supplier.csv")) as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO supplier (name) VALUES (%s)",
            (row["name"],)
        )
conn.commit()
print("supplier импортировано")


with open(csv_path("producer.csv")) as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO producer (name) VALUES (%s)",
            (row["name"],)
        )
conn.commit()
print("producer импортировано")

with open(csv_path("category.csv")) as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO category (name) VALUES (%s)",
            (row["name"],)
        )
conn.commit()
print("category импортировано")

with open(csv_path("goods.csv")) as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        cursor.execute("""
            INSERT INTO goods (
                article, name, description, price,
                unit_of_measurement, quantity_in_stock,
                discount, photo,
                id_producer, id_supplier, id_category
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["article"].strip(),
            row["name"].strip(),
            row["description"].strip(),
            row["price"].strip(),
            row["unit_of_measurement"].strip(),
            row["quantity_in_stock"].strip(),
            row["discount"].strip(),
            row["photo"].strip(),
            row["id_producer"].strip(),
            row["id_supplier"].strip(),
            row["id_category"].strip()
        ))
conn.commit()
print("goods импортировано")

with open(csv_path("order.csv")) as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        cursor.execute("""
            INSERT INTO `order`
            (number, date_z, date_d, code, status, id_point_of_issue, id_user)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row["number"].strip(),
            row["date_z"].strip(),
            row["date_d"].strip(),
            row["code"].strip(),
            row["status"].strip(),
            row["id_point_of_issue"].strip(),
            row["id_user"].strip()
        ))
conn.commit()
print("order импортировано")

with open(csv_path("result.csv")) as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        cursor.execute("""
            INSERT INTO result (id_article, count, id_order)
            VALUES (%s, %s, %s)
        """, (
            row["id_article"].strip(),
            row["count"].strip(),
            row["id_order"].strip()
        ))
conn.commit()
print("result импортировано")

cursor.close()
conn.close()

