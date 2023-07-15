from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Aluno(Base):
    __tablename__ = 'tbl_alunos'

    id = Column("pk_aluno", Integer, primary_key = True)
    num_matricula = Column(String(6), unique = True)
    nome_aluno = Column(String(100))
    turma_aluno = Column(String(3))
    nome_responsavel = Column(String(100))
    cpf_responsavel = Column(String(11))
    tel_responsavel = Column(String(11))
    data_insercao = Column(DateTime, default = datetime.now())

    def __init__(self, num_matricula: str, nome_aluno: str, turma_aluno: str, nome_responsavel: str, cpf_responsavel: str,
                 tel_responsavel: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um registro para um aluno com os seguintes argumentos:
            num_matricula: número da matrícula do aluno.
            nome_aluno: nome do aluno.
            turma_aluno: nome da turma do aluno.
            nome_responsavel: nome do responsável do aluno.
            cpf_responsavel: cpf do responsável do aluno.
            tel_responsavel: telefone do responsável do aluno.
            data_insercao: data na qual o aluno foi cadastrado.
        """
        self.num_matricula = num_matricula
        self.nome_aluno = nome_aluno
        self.turma_aluno = turma_aluno
        self.nome_responsavel = nome_responsavel
        self.cpf_responsavel = cpf_responsavel
        self.tel_responsavel = tel_responsavel

        # se não for informada, será a data do cadastro do aluno
        if data_insercao:
            self.data_insercao = data_insercao