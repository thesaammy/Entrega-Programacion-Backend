from flask import Flask, render_template
from routes.productos import productos_bp
from utils.db import db
from config import Config

app = Flask(__name__)

## Configuración
app.config.from_object(Config)

#Conexión a la instancia db
db.init_app(app)

#registro de blueprint
app.register_blueprint(productos_bp)

@app.route('/')
def login():
    return render_template('login.html')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)