from flask import Blueprint, request, jsonify
from app.services import PagosService
from app.models import Pago
from app.mapping import PagoSchema

pagos = Blueprint('pagos', __name__)
pagos_service = PagosService()
pago_schema = PagoSchema()

@pagos.route('/registrar_pago', methods=['POST'])
def registrar_pago():
    data_pago = request.get_json()
    try:
        pago = pagos_service.registrar_pago(pago_schema.load(data_pago))
        return pago_schema.dump(pago), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Error'}), 500
    
@pagos.route('/eliminar_pago/<int:pago_id>', methods=['DELETE'])
def eliminar_pago(pago_id):
    try:
        observaciones = request.get_json()['observaciones']
        pagos_service.eliminar_pago(pago_id, observaciones)
        return jsonify({'msg': f'Pago con id={pago_id} eliminado'}), 200
    except:
        return jsonify({'msg': 'Error'}), 500

