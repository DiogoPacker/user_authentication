# Sistema de Autenticação de Usuários

## Descrição
Este projeto é um sistema de autenticação e autorização de usuários utilizando Django, Django Rest Framework e JWT para autenticação. O sistema oferece funcionalidades de registro de usuários, login, recuperação de senha e autorização baseada em papéis.

## Tecnologias Utilizadas
- Python
- Django
- Django Rest Framework
- JWT (JSON Web Tokens)

## Funcionalidades
- Registro de usuários
- Login
- Recuperação de senha
- Autorização baseada em papéis

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/DiogoPacker/user_authentication.git
    cd user_authentication
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # no Windows use `env\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    ```sh
    python manage.py makemigrations users
    python manage.py migrate users
    python manage.py makemigrations admin
    python manage.py migrate admin       
    python manage.py migrate
    ```

5. Execute a aplicação:
    ```sh
    python manage.py runserver
    ```

## Endpoints
A API oferece os seguintes endpoints:

- `POST /api/users/register/`: Registro de novos usuários
    ```sh
    curl -X POST http://127.0.0.1:8000/api/users/register/ -H "Content-Type: application/json" -d '{"username":"meu_usuario", "email":"meu_email@example.com", "password":"minha_senha"}'
    ```

- `POST /api/users/login/`: Login de usuários
    ```sh
    curl -X POST http://127.0.0.1:8000/api/users/login/ -H "Content-Type: application/json" -d '{"username":"meu_usuario", "password":"minha_senha"}'
    ```

- `POST /api/users/change_password/`: Mudança de senha
    ```sh
    curl -X POST http://127.0.0.1:8000/api/users/change_password/ -H "Authorization: JWT <seu_token>" -H "Content-Type: application/json" -d '{"old_password":"minha_senha_antiga", "new_password":"minha_nova_senha"}'
    ```

## Executando Testes
Para executar os testes, use o comando:

``python
python manage.py test users

## Contribuição
Sinta-se à vontade para contribuir com o projeto, abrindo uma issue ou enviando um pull request.