from db import get_connection


def get_user(login, password):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    u.last_name,
                    u.first_name,
                    u.patronymic,
                    r.name AS role
                FROM user u
                JOIN role r ON u.id_role = r.id
                WHERE u.login=%s AND u.password=%s
            """, (login, password))

            return cursor.fetchone()
    finally:
        connection.close()


def get_products():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    g.article,
                    g.name,
                    g.description,
                    g.price,
                    g.quantity_in_stock,
                    g.discount,
                    g.photo,
                    p.name AS producer,
                    s.name AS supplier,
                    c.name AS category
                FROM goods g
                JOIN producer p ON g.id_producer = p.id
                JOIN supplier s ON g.id_supplier = s.id
                JOIN category c ON g.id_category = c.id
            """)
            return cursor.fetchall()
    finally:
        connection.close()

def get_categories():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM category")
            return cursor.fetchall()
    finally:
        connection.close()


def get_producers():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM producer")
            return cursor.fetchall()
    finally:
        connection.close()


def get_suppliers():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM supplier")
            return cursor.fetchall()
    finally:
        connection.close()


def get_product_by_article(article):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM goods WHERE article=%s", (article,))
            return cursor.fetchone()
    finally:
        connection.close()


def add_product(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO goods
                (article, name, description, price, unit_of_measurement,
                 quantity_in_stock, discount, photo,
                 id_producer, id_supplier, id_category)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, data)
        connection.commit()
    finally:
        connection.close()


def update_product(article, data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE goods SET
                name=%s,
                description=%s,
                price=%s,
                unit_of_measurement=%s,
                quantity_in_stock=%s,
                discount=%s,
                photo=%s,
                id_producer=%s,
                id_supplier=%s,
                id_category=%s
                WHERE article=%s
            """, data + (article,))
        connection.commit()
    finally:
        connection.close()


def product_in_order(article):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) as cnt FROM result WHERE id_article=%s",
                (article,))
            result = cursor.fetchone()
            return result["cnt"] > 0
    finally:
        connection.close()


def delete_product(article):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM goods WHERE article=%s", (article,))
        connection.commit()
    finally:
        connection.close()


def get_next_article():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(CAST(article AS UNSIGNED)) as max_id FROM goods")
            result = cursor.fetchone()
            next_id = 1 if result["max_id"] is None else int(result["max_id"]) + 1
            return str(next_id)
    finally:
        connection.close()


def get_orders():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT o.code, o.status, p.address AS address,
                       o.date_z AS order_date, o.date_d AS delivery_date
                FROM `order` o
                JOIN point_of_issue p ON o.id_point_of_issue = p.id
            """)
            return cursor.fetchall()
    finally:
        connection.close()

def get_order_by_code(code):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT o.number, o.code, o.status, p.id AS id_point_of_issue,
                       p.address AS address, o.date_z AS order_date,
                       o.date_d AS delivery_date, o.id_user
                FROM `order` o
                JOIN point_of_issue p ON o.id_point_of_issue = p.id
                WHERE o.code=%s
            """, (code,))
            return cursor.fetchone()
    finally:
        connection.close()

def add_order(data):
    """data = (code, status, id_point_of_issue, date_z, date_d, id_user)"""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO `order` (code, status, id_point_of_issue, date_z, date_d, id_user)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, data)
        connection.commit()
    finally:
        connection.close()

def update_order(code, data):
    """data = (status, id_point_of_issue, date_z, date_d)"""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE `order` SET status=%s, id_point_of_issue=%s,
                    date_z=%s, date_d=%s
                WHERE code=%s
            """, data + (code,))
        connection.commit()
    finally:
        connection.close()

def delete_order(code):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Сначала удаляем все товары из заказа
            cursor.execute("SELECT number FROM `order` WHERE code=%s", (code,))
            order = cursor.fetchone()
            if order:
                cursor.execute("DELETE FROM result WHERE id_order=%s", (order["number"],))
            # Удаляем сам заказ
            cursor.execute("DELETE FROM `order` WHERE code=%s", (code,))
        connection.commit()
    finally:
        connection.close()

def get_points_of_issue():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, address FROM point_of_issue")
            return cursor.fetchall()
    finally:
        connection.close()
