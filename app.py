from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.productos import productos_bp
from routes.usuarios import usuarios_bp
from routes.auth import auth_bp
from utils.db import db
from config import Config
import os

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

## Configuración
app.config.from_object(Config)

#Conexión a la instancia db
db.init_app(app)

#registro de blueprint
app.register_blueprint(productos_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/aplicacion')
def inventario():
    return render_template('app.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)