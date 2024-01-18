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
    elif option == '5':
        conn_str = f"sqlite:///{dbname}"
    return conn_str

# Conecta el string al engine del ORM y
# genera una conexion a partir de la URI construida 
# para obtener los nombres de las tablas
def FetchTableNames(conn_str):
    engine = create_engine(conn_str)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    tables_names = [table['name'] for table in tables]
    return tables_names

def FetchColumnData(engine, table_name):
    inspector = inspect(engine)
    # Obtener los nombres y tipos de datos de las columnas de la tabla seleccionada
    columns = inspector.get_columns(table_name)
    column_data = {column['name']: column['type'] for column in columns}
    return column_data