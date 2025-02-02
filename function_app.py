import azure.functions as func
import logging
import re
from typing import Dict
from fastapi import FastAPI, HTTPException

app = FastAPI()

def validate_cpf(cpf: str) -> bool:
    """
    Valida um CPF aplicando todas as regras de validação necessárias.
    """
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        return False
        
    # Validação do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cpf[9]) != digito1:
        return False
        
    # Validação do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cpf[10]) != digito2:
        return False
        
    return True

@app.post("/api/validate-cpf")
async def validate_cpf_endpoint(request: Dict[str, str]) -> Dict[str, bool]:
    """
    Endpoint para validação de CPF.
    Espera receber um JSON no formato: {"cpf": "123.456.789-00"}
    """
    cpf = request.get('cpf')
    if not cpf:
        raise HTTPException(status_code=400, detail="CPF não fornecido")
    
    is_valid = validate_cpf(cpf)
    return {"is_valid": is_valid}

# Configuração para Azure Functions
main = func.AsgiFunctionApp(app=app, http_auth_level=func.AuthLevel.ANONYMOUS)
