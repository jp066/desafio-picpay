from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404
from users.models import User
from rolepermissions.checkers import has_permission

payments_router = Router()

@payments_router.post('/', response={200: dict, 400: dict, 403: dict})
def transaction(request, transaction: TransactionSchema):
    payer = get_object_or_404(User, id=transaction.payer)
    payee = get_object_or_404(User, id=transaction.payee)
    
    if payer.amount < transaction.amount:
        return 400, {"error": "Saldo insuficiente"}
    
    if not has_permission(payer, 'make_transfer'):
        return 403, {'error': "Você não possui permissão para realizar tranferencias"}
    
    return 200, {'transaction_id': 1}