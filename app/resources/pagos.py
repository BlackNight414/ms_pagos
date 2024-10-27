from flask import Blueprint, request, jsonify
from app.services import PagosService
from app.models import Pago

pagos = Blueprint('pagos', __name__)
pagos_service = PagosService()

@pagos.route('/registrar_pago', methods=['POST'])
def registrar_pago():
    data_pago = request.get_json()
    try:
        pago = pagos_service.registrar_pago(Pago(**data_pago))
        resp = jsonify({
            'id': pago.id,
            'producto_id': pago.producto_id,
            'precio': pago.precio,
            'medio_pago': pago.medio_pago
        })
        return resp, 200
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

