import pandas as pd
import mysql.connector
import os

# MySQL Connection
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ecommerce2'
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully.")
except mysql.connector.Error as err:
    print(f"❌ Error connecting to MySQL: {err}")
    exit()

# Folder Path
folder_path = 'C:/Users/himan/OneDrive/Desktop/Data-Analytics/Ecom'

# List of CSV Files
csv_files = [
    ('customers.csv', 'customers'),
    ('orders.csv', 'orders'),
    ('sallers.csv', 'sallers'),
    ('products.csv', 'products'),
    ('order_items.csv', 'order_items'),
    ('geolocation.csv', 'geolocation'),
    ('payments.csv', 'payments')
]

# Function to get SQL Data Type
def get_sql_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'INT'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    else:
        return 'TEXT'

# Process CSV Files
for csv_file, table_name in csv_files:
    file_path = os.path.join(folder_path, csv_file)

    print(f"\n📂 Processing file: {csv_file}")

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        continue

    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')

    # Debug: Show first few rows
    print(f"🔍 Preview of {csv_file}:")
    print(df.head())

    df = df.where(pd.notnull(df), None)  # Replace NaN with None

    df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]

    # CREATE TABLE Statement
    columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])
    primary_key = df.columns[0]  # Assuming first column is the primary key
    create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns}, PRIMARY KEY (`{primary_key}`))'

    try:
        cursor.execute(create_table_query)
        print(f"✅ Table `{table_name}` created or already exists.")
    except mysql.connector.Error as err:
        print(f"❌ Error creating table `{table_name}`: {err}")
        continue

    # INSERT Data
    inserted_rows = 0
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(x) else x for x in row)
        sql = f"INSERT IGNORE INTO `{table_name}` ({', '.join(['`' + col + '`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(row))})"

        try:
            cursor.execute(sql, values)
            inserted_rows += 1
        except mysql.connector.Error as err:
            print(f"❌ Error inserting into `{table_name}`: {err}")
            break

    conn.commit()
    print(f"✅ Inserted {inserted_rows} rows into `{table_name}`.")

# Close MySQL Connection Properly
try:
    cursor.close()
    conn.close()
    print("\n✅ Database connection closed successfully.")
except Exception as e:
    print(f"❌ Error closing connection: {e}")
