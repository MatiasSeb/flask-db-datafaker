from flask import Flask
from config import Config
from extensions import db
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    csrf.init_app(app)
    # Register blueprints here
    with app.app_context():
        from route import routes
        app.register_blueprint(routes)
    

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)