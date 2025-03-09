from config.database import db
from models.payment import Payment


class PaymentRepository:
    @staticmethod
    def save(payment):
        db.session.add(payment)
        db.session.commit()

    @staticmethod
    def find_by_id(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def find_by_bank_id(bank_payment_id):
        return Payment.query.filter_by(bank_payment_id=bank_payment_id).first()
