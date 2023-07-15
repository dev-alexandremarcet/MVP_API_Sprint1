# Como executar 


É necessário que todas as bibliotecas (libs) do python listadas no `requirements.txt` sejam instaladas.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É recomendável o uso de ambientes virtuais do tipo [virtualenv]    
> Segue o link para instalação:(https://virtualenv.pypa.io/en/latest/installation.html).

Devemos executar o comando a seguir para a instalação das dependências/bibliotecas, descritas no arquivo `requirements.txt`.

```
(env)$ pip install -r requirements.txt
```

Devemos executar o comando a seguir para executarmos a API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

```
Observação:
O teste da API via Swagger deverá considerar quantidades específicas de digitos para os seguintes campos:
i) campo turma do aluno: 3 dígitos numéricos (Ex.:601, 701, 802);
ii) campo CPF do responsável: 11 dígitos numéricos sem traço e sem pontos (Ex.:12345678901);
iii) campo telefone do responsável: 11 dígitos numéricos começando com DDD, sem hífen e sem parêntesis (Ex.:21987654321).
```
