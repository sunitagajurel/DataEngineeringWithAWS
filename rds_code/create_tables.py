import psycopg2
import boto3

password = 'password'

conn = None
try:
    conn = psycopg2.connect(
        host='database-1.cbsmwc22ek66.us-east-2.rds.amazonaws.com',
        port=5432,
        database='postgres',
        user='postgres',
        password=password,
        sslmode='verify-full',
    sslrootcert='./global-bundle.pem'
    )
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS zones (
        location_id INTEGER PRIMARY KEY,
        borough VARCHAR(100),
        zone VARCHAR(100),
        service_zone VARCHAR(100)
    );
    """)

    cur.execute("""
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id INTEGER PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
    
    cur.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
""")

    tables = cur.fetchall()
    print(tables)
    cur.close()
except Exception as e:
    print(f"Database error: {e}")
    raise
finally:
    if conn:
        conn.close()