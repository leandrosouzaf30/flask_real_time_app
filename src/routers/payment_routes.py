from flask import Blueprint, jsonify, render_template, request, send_file

from src.models.payment import Payment
from src.services.payment_service import PaymentService

payment_bp = Blueprint('payment_bp', __name__)

@payment_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@payment_bp.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()
    if 'value' not in data:
        return jsonify({'message': 'Invalid value'}), 400

    payment = PaymentService.create_payment(data['value'])
    return jsonify({
        'message': 'The payment has been created',
        'payment': payment.to_dict(),
    }), 201


@payment_bp.route('/payments/pix/qr_code/<file_name>')
def get_image(file_name):
    return send_file(f'static/img/{file_name}.png', mimetype='image/png')


@payment_bp.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    data = request.get_json()
    if 'bank_payment_id' not in data or 'value' not in data:
        return jsonify({'message': 'Invalid payment data'}), 400

    payment = PaymentService.confirm_payment(
        data['bank_payment_id'], data['value']
    )
    if not payment:
        return jsonify({'message': 'Payment not found or invalid'}), 404

    return jsonify({'message': 'The payment has been confirmed'})


@payment_bp.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return render_template('404.html')
    if payment.paid:
        return render_template(
            'confirmed_payment.html',
            payment_id=payment.id,
            value=payment.value,
        )
    return render_template(
        'payment.html',
        payment_id=payment.id,
        value=payment.value,
        host='http://127.0.0.1:5000',
        qr_code=payment.qr_code,
    )
