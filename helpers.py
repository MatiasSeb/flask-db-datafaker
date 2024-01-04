import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect

# Construir la cadena de conexión dependiendo del prefijo para BDD externas.
def UriBuilder(option, cred_list):
    username = cred_list['username']
    password = cred_list['password']
    ip = cred_list['ip']
    port = cred_list['port']
    dbname = cred_list['dbname']

    # Construir la cadena de conexión dependiendo del prefijo
    if option == '1':
        conn_str = f"mysql+pymysql://{username}:{password}@{ip}:{port}/{dbname}"
    elif option == '2':
        conn_str = f"postgresql+psycopg2://{username}:{password}@{ip}:{port}/{dbname}"
    elif option == '3':
        conn_str = f"mssql+pyodbc://{username}:{password}@{ip}:{port}/{dbname}?driver=ODBC+Driver+17+for+SQL+Server"
    elif option == '4':
        conn_str = f"oracle+oracledb://{username}:{password}@{ip}:{port}/{dbname}"
    
    return conn_str

# Construir la cadena de conexión exclusivamente para SQLite
def SqliteUriBuilder(db_name):
    conn_str = f"sqlite:///{db_name}"
    return conn_str

# Genera una conexion a partir de la URI construida
def GenerateSimpleConn(conn_str):
    engine = create_engine(conn_str)
    inspector = inspect(engine)
    # Obtener los nombres de las tablas
    tables_names = inspector.get_table_names()
    return tables_names

def get_column_names(conn_str, table_name):
    engine = create_engine(conn_str)
    inspector = inspect(engine)
    # Obtener los nombres de las columnas de la tabla seleccionada
    columns = inspector.get_columns(table_name)
    column_names = [column['name'] for column in columns]
    return column_names