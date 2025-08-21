import os

class Config:
    # Conexión a MySQL
    SQLALCHEMY_DATABASE_URI = "mysql://root:Pruebas123.@localhost:3307/inventarioBackend"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #Config de JWT_Manager
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_CSRF_PROTECT = False 
    JWT_IDENTITY_CLAIM = "uid" 

