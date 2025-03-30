import psycopg2
conn = psycopg2.connect("dbname=logs user=postgres password=postgres host=localhost")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()
cur.close()
conn.close()

