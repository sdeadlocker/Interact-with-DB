import psycopg2
import environ
env = environ.Env()
environ.Env.read_env()

# Establish a connection to the PostgreSQL database

conn = psycopg2.connect(
    host='db_host',
    port=5432,
    user='postgres',
    password=env('dbpass'),
    database='db_name'
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the product table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        product_id text,
        name text NOT NULL,
        description text NOT NULL,
        icon_path text,
        modifier text NOT NULL,
        status boolean DEFAULT false,
        video_url text,
        video_brief text,
        theme text,
        learning_type text NOT NULL,
        session_count integer DEFAULT 16,
        external_service text,
        category text NOT NULL,
        content_type text DEFAULT 'TOPIC',
        content_list text DEFAULT '[]',
        last_modified timestamp NOT NULL,
        CONSTRAINT product_pkey PRIMARY KEY (product_id)
    )
''')


# Insert sample products into the product table
cursor.execute("""
    INSERT INTO product (
        product_id, name, description, icon_path, modifier, status, video_url,
        video_brief, theme, learning_type, session_count, external_service,
        category, content_type, content_list, last_modified
    ) VALUES (
        'product1', 'HOTS', 'description1',
        '/path/to/icon1', 'Modifier 1', True, 'https://example.com/video1', 'Brief 1', 'cognitive skills', 'Learning Type 1',
        16, 'External Service 1', 'Category 1', 'TOPIC', '[]', '2023-05-01'
    )
""")
cursor.execute("""
    INSERT INTO product (
        product_id, name, description, icon_path, modifier, status, video_url,
        video_brief, theme, learning_type, session_count, external_service,
        category, content_type, content_list, last_modified
    ) VALUES (
        'product2', 'YPDP', 'description2',
        '/path/to/icon2', 'Modifier 2', False, 'https://example.com/video2', 'Brief 2', 'coding', 'Learning Type 2',
        16, 'External Service 2', 'Category 2', 'TOPIC', '[]', '2023-05-02'
    )
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
