from django.core.exceptions import ValidationError

def validate_cpf(value: str):
    cpf = ''.join([char for char in value if char.isdigit()]) 
    
    if len(cpf) != 11:
        raise ValidationError('CPF deve ter 11 dígitos')
    
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF não pode ser composto por um único dígito')
    
    
def calcular_digito(cpf: str) -> str:
    if not cpf or len(cpf) != 9:
        return ''
    
    soma = 0
    for i, char in enumerate(cpf):
        soma += int(char) * (10 - i)
    
    resto = soma % 11
    digito = 0 if resto < 2 else 11 - resto
    
    return str(digito)