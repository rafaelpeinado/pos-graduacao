from pydantic import BaseModel, EmailStr, validator
from enum import Enum
import re

class Periodo(Enum):
    MANHA = "manha"
    TARDE = "tarde"
    NOITE = "noite"

class StatusMatricula(Enum):
    ATIVO = "ativo"
    CONCLUIDO = "concluido"

class Email(BaseModel):
    email: EmailStr

class Telefone(BaseModel):
    numero: str

    @validator('numero')
    def validar_telefone(cls, value):
        if not re.match(r"^\d{2}-\d{4,5}-\d{4}$", value):
            raise ValueError("\nFormato de telefone inválido!\nO formato deve ser DDD-99999-9999")
        return value

class CodigoTreinamento(BaseModel):
    codigo: str

    @validator('codigo')
    def validar_codigo(cls, value):
        if not re.match(r"^[A-Z]{2}[0-9]{2}$", value):
            raise ValueError(f"\nO Código do treinamento {value} é inválido!")
        return value


