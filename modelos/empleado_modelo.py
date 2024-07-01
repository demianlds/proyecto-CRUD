from sqlalchemy import Column, Integer, String
from app import app, db

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(200))

    def __init__(self, nombre, apellido, email, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

with app.app_context():
    db.create_all()