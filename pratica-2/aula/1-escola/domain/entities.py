from .value_objects import Email, Telefone, CodigoTreinamento, Periodo, StatusMatricula
from datetime import date
from pydantic import BaseModel, Field


class Aluno(BaseModel):
    """Args: ID, Nome, Email, Telefone"""
    id: int = Field(..., gt=0)
    nome: str
    email: Email
    telefone: Telefone

class Treinamento(BaseModel):
    """Args: ID, Codigo, Descrição, Carga Horária, Capacidade"""
    id: int = Field(..., gt=0)
    codigo: CodigoTreinamento
    descricao: str
    carga_horaria: int = Field(..., gt=0) 
    capacidade: int = Field(..., gt=0) 

class Matricula(BaseModel):
    """Args: ID, Aluno, Treinamento, Periodo, Status, Data de Início"""
    id: int = Field(..., gt=0)
    aluno: Aluno
    treinamento: Treinamento
    periodo: Periodo
    status: StatusMatricula = StatusMatricula.ATIVO
    data_inicio: date

