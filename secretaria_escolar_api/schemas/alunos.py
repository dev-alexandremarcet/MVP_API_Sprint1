from pydantic import BaseModel
from typing import Optional, List
from model.alunos import Aluno



class AlunoSchema(BaseModel):
    """ Define como deve ser representado um aluno que será cadastrado.
    """
    num_matricula: str = "123456"
    nome_aluno: str = "João Pedro"
    turma_aluno: str = "901"
    nome_responsavel: str = "Adriana"
    cpf_responsavel: str = "12345678900"
    tel_responsavel: str = "21999999999"


class BuscaAlunoSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca, que será
        feita apenas com base no número de matrícula do aluno.
    """
    num_matricula: str = "123456"


class ListagemAlunosSchema(BaseModel):
    """ Define como uma listagem de alunos cadastrados será retornada.
    """
    list_alunos:List[AlunoSchema]


def exibe_alunos(alunos: List[Aluno]):
    """ Retorna uma representação da listagem de alunos cadastrados seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "num_matricula": aluno.num_matricula,
            "nome_aluno": aluno.nome_aluno,
            "turma_aluno": aluno.turma_aluno,
            "nome_responsavel": aluno.nome_responsavel,
            "cpf_responsavel": aluno.cpf_responsavel,
            "tel_responsavel": aluno.tel_responsavel,
        })

    return {"alunos": result}


class AlunoViewSchema(BaseModel):
    """ Define como um aluno cadastrado será retornado.
    """
    id: int = 1
    num_matricula: str = "123456"
    nome_aluno: str = "João Pedro"
    turma_aluno: str = "901"
    nome_responsavel: str = "Adriana"
    cpf_responsavel: str = "12345678900"
    tel_responsavel: str = "21999999999"


class RemoveAlunoSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção de um aluno.
    """
    mensagem_remove_aluno: str
    nome_remove_aluno: str


def exibe_aluno(aluno: Aluno):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
        "num_matricula": aluno.num_matricula,
        "nome_aluno": aluno.nome_aluno,
        "turma_aluno": aluno.turma_aluno,
        "nome_responsavel": aluno.nome_responsavel,
        "cpf_responsavel": aluno.cpf_responsavel,
        "tel_responsavel": aluno.tel_responsavel
    }
