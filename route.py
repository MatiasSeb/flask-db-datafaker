from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from forms import PickDBPrefixForm, CreateConnForm, CreateSQLiteConnForm, TableSelectFromDB
from flask_dataemulator_api.functions import UriBuilder, FetchTableNames, FetchColumnData

routes = Blueprint('routes', __name__)

@routes.route('/home', methods=['GET', 'POST'])
def home():
    prefixform = PickDBPrefixForm()

    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        if prefixform.validate_on_submit():
            if prefixform.db_prefix.data:
                return redirect(url_for('routes.connect_with_prefix', option=prefixform.db_prefix.data))

@routes.route('/connect_with_prefix', methods=['GET', 'POST'])
def connect_with_prefix(option):
    form = CreateConnForm()
    form2 = CreateSQLiteConnForm()
    
    if request.method == 'GET':
        if option == '1' or option == '2' or option == '3' or option == '4':
            return render_template('connect.html', form=form)
        elif option == '5':
            return render_template('sqlite.html', form2=form2)
    
    if request.method == 'POST':
        # si es un prefix externo (ip)
        if form.validate_on_submit():
            cred_list = {
                'username': form.conn_username.data,
                'password': form.conn_password.data,
                'ip': form.conn_ip.data,
                'port': form.conn_port.data,
                'dbname': form.conn_dbname.data
            }
            if all(cred_list.values()):
                # Generar uri y muestra de tablas de la bdd a conectar
                built_url = UriBuilder(option, cred_list)
                tables_result = FetchTableNames(built_url)
                if tables_result:
                    return redirect(url_for('routes.select_and_create', tables_result, built_url))
            else:
                return redirect(url_for('routes.connect_with_prefix', option))    
            
        # si el prefix es de sqlite (interno, direccion en explorador)
        elif form2.validate_on_submit():
            if form2.db_address.data:
                built_url = UriBuilder(form2.db_address.data)
                tables_result = FetchTableNames(built_url)
                if tables_result:
                    return redirect(url_for('routes.select_and_detect', tables_result, built_url))
            else:
                return redirect(url_for('routes.connect_with_prefix', form=form))


# Ruta para seleccionar una tabla a llenar con data falsa, dependiendo de los valores que admite la columna
@routes.route('/select_and_detect', methods=['GET', 'POST'])
def select_and_detect(tables, engine):
    tables_form = TableSelectFromDB()
    tables_form.table_name.choices = [(table, table) for table in tables]
    
    if request.method == 'GET':
        return render_template('select.html', tables_form=tables_form)
    
    if request.method == 'POST':
        if tables_form.validate_on_submit() and tables_form.table_name.data:
            selected_table = tables_form.table_name.data
            column_data = FetchColumnData(engine, selected_table)
            if column_data:
                return redirect(url_for('routes.create_fake_data', table=selected_table, data=column_data))
        else:
            return redirect(url_for('routes.select_and_detect', tables_form=tables_form))

# Ruta para finalmente llenar con la data necesaria la tabla
@routes.route('/create_fake_data', methods=['GET', 'POST'])
def create_fake_data(table, data):
    
    if request.method == 'GET':
        return render_template('create.html', table=table, data=data)
    
    if request.method == 'POST':
        pass