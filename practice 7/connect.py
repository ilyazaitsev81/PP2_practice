import psycopg2
import csv
from config import *

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
def add_contact(name,phone):
    conn= get_connection()
    cur= conn.cursor()
    cur.execute(
        "INSERT INTO phbook (name,phnum) VALUES (%s,%s);",
        (name,phone)
    )
    conn.commit()
    print("New contact in your phonebook")
    cur.close()
    conn.close()
def update_phone(new_phone,phnum):
    conn= get_connection()
    cur= conn.cursor()
    cur.execute(
        "UPDATE phbook SET phnum=%s WHERE phnum=%s;",
        (new_phone,phnum)
    )
    conn.commit()
    print("contact number changed")
    cur.close()
    conn.close()
def update_name(new_name,phone):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(
        "UPDATE phbook SET name=%s WHERE phnum=%s;",
        (new_name,phone)
    )
    conn.commit()
    print("contact name changed")
    cur.close()
    conn.close()
def import_csv(filename):
    conn=get_connection()
    cur=conn.cursor()
    with open(filename, newline='') as file:
        reader= csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phbook (name,phnum) VALUES (%s,%s);",
                (row["name"],row["phone"])
            )
    conn.commit()
    print("New contact in your phone book")
    conn.close()
    cur.close()
def searching(queri):
    conn=get_connection()
    cur= conn.cursor()
    cur.execute("""
        SELECT * FROM phbook
        WHERE name ILIKE %s OR phnum ILIKE %s;
    """,(f"%{queri}%",f"%{queri}%"))
    result = cur.fetchall()
    if result:
        print(result)
    else:
        print("Not found")
    cur.close()
    conn.close()
def delete_concact(queri):
    con= get_connection()
    cur= con.cursor()
    cur.execute(
        "DELETE FROM phbook WHERE name=%s OR phnum=%s;",
        (queri,queri)
    )
    print("deleted contact")
    con.commit()
    cur.close()
    con.close()
def search_pattern(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_pattern(%s);", (pattern,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)
def insert_or_update(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
def insert_many(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CALL insert_many_users(%s, %s);",
        (names, phones)
    )
    conn.commit()
    cur.close()
    conn.close()
def get_paginated(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s);",
        (limit, offset)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)
def delete_contact(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CALL delete_by_name_or_phone(%s);",
        (query,)
    )
    conn.commit()
    cur.close()
    conn.close()