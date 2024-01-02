from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from forms import PickDBPrefixForm, CreateConnForm, CreateSQLiteConnForm
from helpers import UriBuilder

routes = Blueprint('routes', __name__)

@routes.route('/home')
def home():
    return 'Hello, World!'

@routes.route('/home', methods=['GET', 'POST'])
def home():
    prefixform = PickDBPrefixForm()

    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST' & prefixform.validate_on_submit():
        db_prefix = prefixform.db_prefix.data
        if db_prefix:
            return redirect(url_for('routes.connect_with_prefix', option=db_prefix))

@routes.route('/connect', methods=['GET', 'POST'])
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
            # Generar uri y muestra de tablas de la bdd a conectar
            if option == '1':
                built_url = UriBuilder(option, cred_list)
                if gene
                
            if option == '2':
                built_url = UriBuilder(option, cred_list)
                pass
            if option == '3':
                built_url = UriBuilder(option, cred_list)
                pass
            if option == '4':
                built_url = UriBuilder(option, cred_list)
                
        
        
        
        # si el prefix es de sqlite (interno, direccion en explorador)
        elif form2.validate_on_submit():
            form2.db_address