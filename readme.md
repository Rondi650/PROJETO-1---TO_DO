# Projeto To-Do List Flask

Aplicação web para gerenciamento de tarefas pessoais, desenvolvida com Python Flask e SQL Server.

## Funcionalidades

- Cadastro e autenticação de usuários
- Criptografia de senhas com Bcrypt
- Proteção contra CSRF em formulários (Flask-WTF + CSRFProtect)
- CRUD completo de tarefas (criar, listar, alternar status, deletar)
- ORM SQLAlchemy para integração com banco de dados SQL Server
- Templates dinâmicos com Jinja2
- Mensagens flash para feedback ao usuário

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Flask
- **Banco de Dados:** SQL Server
- **ORM:** SQLAlchemy
- **Formulários:** Flask-WTF
- **Template Engine:** Jinja2
- **Criptografia:** Flask-Bcrypt
- **Proteção Web:** CSRFProtect

## Como executar

1. Clone o repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Configure o acesso ao banco de dados em `config.py`
4. Execute a aplicação:
   ```
   python app.py
   ```
5. Acesse `http://localhost:5000` no navegador

## Estrutura de Pastas

- `app.py` — Arquivo principal da aplicação
- `models.py` — Modelos do banco de dados
- `routes_users.py` — Rotas de autenticação e usuários
- `routes_todo.py` — Rotas de tarefas
- `forms.py` — Formulários WTForms
- `templates/` — Templates HTML (Jinja2)
- `static/` — Arquivos estáticos (CSS, imagens)
- `config.py` — Configuração do banco de dados

## Créditos

Projeto desenvolvido para estudos, com apoio dos cursos da [Alura](https://www.alura.com.br/).

---

Sinta-se à vontade para contribuir ou enviar