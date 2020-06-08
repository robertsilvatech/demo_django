import psycopg2
import sys
from datetime import datetime
from random import randint

address = '10.0.0.31'
user = 'django'
password = 'django'
database = 'django'

## Conection
conn = psycopg2.connect(host=address, database=database, user=user, password=password)
## Cursor
cursor = conn.cursor()

## Get all payment_method
def get_all_payment_method():
    query = 'select * from stores_paymentmethod'
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def get_all_products():
    query = 'select * from stores_product'
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def get_lastid_stores_sale():
    query = 'select * from stores_sale order by id desc'
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def make_a_sale(store_id=1, payment_method_id=1):
    insert = 'INSERT INTO "stores_sale" ("store_id", "payment_method_id", "created_at", "updated_at") values (%s, %s, %s, %s)'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(type(timestamp))
    row_to_insert = (store_id,payment_method_id, timestamp, timestamp)
    cursor.execute(insert, row_to_insert)
    conn.commit()

def make_a_saledatil(product_id, sale_id):
    insert = 'INSERT INTO "stores_saledetail" ("quantity", "product_id", "sale_id") values (%s, %s, %s)'
    row_to_insert = ('1', product_id, sale_id)
    cursor.execute(insert, row_to_insert)   
    conn.commit()


## Make a sale

arg = sys.argv
store_id = arg[1]
payment_method_id = randint(1,4)
number_of_products = randint(1,3)
make_a_sale(store_id=store_id, payment_method_id=payment_method_id)
last_sale_id = get_lastid_stores_sale()[0]
for sale_detail in range(1, number_of_products+1):
    product_id = randint(1,7)
    make_a_saledatil(product_id,last_sale_id)
    print(f'Venda {last_sale_id} para o produto {product_id} na loja {store_id}')    
cursor.close()
    
