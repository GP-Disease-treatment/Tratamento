
# Backend - Gerência de Projetos - Tratamento de doenças

Backend desenvolvido para o projeto de tratamento de doenças, parte da disciplina de Gerência de Projetos, utilizando o framework Django para integração com a API do Gemini.


## Rodando localmente (backend)

Clone o projeto

```bash
  git clone https://github.com/GP-Disease-treatment/Tratamento.git
```

Entre no diretório do projeto

```bash
  cd Tratamento/tratamento
```

Instale a virtualenv
```bash
  pip install virtualenv
```
Crie a virtualenv
```bash
  python -m venv venv
```
Acesse a virtualenv
- Para windows
```bash
  venv/Scripts/activate
```
O retorno será algo como:
```bash
  (venv) C:/.../Tratamento
```
- Para sistemas baseados em Linux
```bash
  source venv/bin/activate
```
O retorno será algo como:
```bash
  (venv) usuario@ubuntu:~/.../Tratamento$
```

Instale as dependências
```bash
  pip install -r requirements.txt
```

Aplique as migrations
```bash
  python manage.py migrate
```

Crie um superuser
```bash
  python manage.py createsuperuser
```

Inicie o servidor
```bash
  python manage.py runserver
```

No terminal você receberá algo como:
```bash
  Watching for file changes with StatReloader
  Performing system checks...
  
  System check identified no issues (0 silenced
  November 05, 2024 - 17:33:08
  Django version 5.1.2, using settings 'tratamento.settings'
  Starting development server at http://127.0.0.1:8000
  Quit the server with CONTROL-C.
```
Acesse a URL retornada (nesse caso: http://127.0.0.1:8000)