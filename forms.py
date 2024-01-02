from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, HiddenField, widgets
from wtforms.validators import InputRequired, DataRequired, Length, EqualTo, ValidationError, Regexp, Optional

class PickDBPrefixForm(FlaskForm):
    supported_databases = [
        ('1', '. MySQL'),
        ('2', '. PostgreSQL'),
        ('3', '. Oracle'),
        ('4', '. MS SQL Server'),
        ('5', '. SQLite')
    ]
    db_prefix = SelectField('Database Engine', choices=supported_databases, validators=[InputRequired()])
    submit = SubmitField('Select Prefix')

class CreateConnForm(FlaskForm):
    conn_username = StringField('Username', validators=[DataRequired(Length(min=4, max=15)), Regexp('^[a-zA-Z0-9_]+$', message='Solo se permiten letras, números y guiones bajos.')])
    conn_password = PasswordField('Password', validators=[DataRequired()])
    conn_ip = StringField('IP Address', validators=[DataRequired(), Regexp('^((25[0-5]|2[0-4][0-9]|[-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[-1]?[0-9][0-9]?)$', message='Por favor ingrese una dirección IP válida.')])
    conn_port = StringField('Port', validators=[DataRequired(), Regexp('^[0-9]+$', message='Por favor ingrese un número de puerto válido.')])
    conn_dbname = StringField('Database Name', validators=[DataRequired(), Regexp('^[a-zA-Z0-9_]+$', message='Solo se permiten letras, números y guiones bajos.')])
    submit = SubmitField('Crear conexión')
class CreateSQLiteConnForm(FlaskForm):
    db_address = StringField('Dirección de la base de datos SQLite')
    submit = SubmitField('Guardar')