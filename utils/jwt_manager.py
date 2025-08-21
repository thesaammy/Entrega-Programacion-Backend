from flask_jwt_extended import JWTManager
from flask import redirect, url_for, flash

#Instancia de JWTManager
jwt = JWTManager()

def configurar_jwt(app):
    jwt.init_app(app)

    @jwt.unauthorized_loader
    def unauthorized_callback(reason):
        flash("Debes iniciar sesión.", "warning")
        return redirect(url_for('login'))

    @jwt.invalid_token_loader
    def invalid_token_callback(reason):
        flash("Token inválido. Inicia sesión nuevamente.", "danger")
        return redirect(url_for('login'))

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        flash("Tu sesión expiró. Vuelve a iniciar sesión.", "warning")
        return redirect(url_for('login'))

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        flash("Sesión revocada. Inicia sesión nuevamente.", "warning")
        return redirect(url_for('login'))