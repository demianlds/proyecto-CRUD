from flask import jsonify, request
from app import app, db, ma
from modelos.empleado_modelo import Empleado

class EmpleadoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'email', 'telefono', 'direccion')

empleado_schema = EmpleadoSchema()
empleados_schema = EmpleadoSchema(many=True)

@app.route('/empleados', methods=['GET'])
def get_empleados():
    all_empleados = Empleado.query.all()
    result = empleados_schema.dump(all_empleados)
    return jsonify(result)

@app.route('/empleados/<id>', methods=['GET'])
def get_empleado(id):
    empleado = Empleado.query.get(id)
    return empleado_schema.jsonify(empleado)

@app.route('/empleados/<id>', methods=['DELETE'])
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return empleado_schema.jsonify(empleado)

@app.route('/empleados', methods=['POST'])
def create_empleado():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    telefono = request.json['telefono']
    direccion = request.json['direccion']
    new_empleado = Empleado(nombre, apellido, email, telefono, direccion)
    db.session.add(new_empleado)
    db.session.commit()
    return empleado_schema.jsonify(new_empleado)

@app.route('/empleados/<id>', methods=['PUT'])
def update_empleado(id):
    empleado = Empleado.query.get(id)
    empleado.nombre = request.json['nombre']
    empleado.apellido = request.json['apellido']
    empleado.email = request.json['email']
    empleado.telefono = request.json['telefono']
    empleado.direccion = request.json['direccion']
    db.session.commit()
    return empleado_schema.jsonify(empleado)

@app.route('/')
def bienvenida():
    return "Bienvenidos al backend de empleados"