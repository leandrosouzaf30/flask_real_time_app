from datetime import datetime, timedelta

from ..app_factory import socketio
from src.models.payment import Payment
from src.repositories.payment_repository import PaymentRepository

from .pix_service import PixService


class PaymentService:
    @staticmethod
    def create_payment(value):
        expiration_date = datetime.now() + timedelta(minutes=30)
        pix_service = PixService()
        data_payment_pix = pix_service.create_payment()

        new_payment = Payment(
            value=value,
            expiration_date=expiration_date,
            bank_payment_id=data_payment_pix['bank_payment_id'],
            qr_code=data_payment_pix['qr_code_path'],
            paid=False,
        )
        PaymentRepository.save(new_payment)
        return new_payment

    @staticmethod
    def confirm_payment(bank_payment_id, value):
        payment = PaymentRepository.find_by_bank_id(bank_payment_id)

        if not payment or payment.paid or payment.value != value:
            return None

        payment.paid = True
        PaymentRepository.save(payment)
        socketio.emit(f'payment-confirmed-{payment.id}')
        return payment
