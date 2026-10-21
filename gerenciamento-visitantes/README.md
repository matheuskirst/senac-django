# Projeto Crud de Gerenciamento de visitantes com Django

## Primeiros passos

### Configuração de ambiente

---
Criar ambiente virtual chamado venv
```bash
py -m venv venv
```
---
Ativar o ambiente virtual criado
```bash
./venv/Scripts/Activate
```
---
Instalar pacotes necessários
```bash
pip install django
```
---
Listar pacotes instalados no ambiente virtual
```bash
pip freeze
```
---
Escrever pacotes em arquivo requirements.txt
```bash
pip freeze > requirements.txt
```
---
Criar projeto django
```bash
django-admin startproject setup .
```
---
Criar Api
```bash
py manage.py startapp app
```

## Execução do projeto

---
Executar projeto localmente com configurações padrão
```bash
py manage.py runserver
```
URL da aplicação:
```text
http://localhost:8000
```
---
Criar primeira página dentro de `app/templates/home.html`.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página inicial</title>
</head>
<body>
    <h1>Página inicial - Gerenciamento de Visitantes</h1>
    <p>Bem vindo ao nosso site</p>
</body>
</html>
```
---
Dentro de `views.py`, criar primeiro método para renderizar página `home.html`.
```python
from django.shortcuts import render

from .models import Visitor

def home(request):
    return render(request, 'home.html')
```
---
Configurar urls na aplicação e no projeto
- Na aplicação, criar arquivo `urls.py` configurar conforme abaixo:
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home')
]
```

- No projeto, alterar arquivo `urls.py` para relacionar com `urls.py` da aplicação `api_rest`.
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'), name='app_urls'),
]
```
---
Adicionar app em `settings.py`.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]
```
---
Criar modelos no arquivo models.py. Exemplo:
```python
class Visitor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    ticket_date = models.DateField()
    ticket_type = models.IntegerField()
    ticket_number = models.CharField(255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```
---
Cria arquivos de migração com base nas alterações dos Models
```bash
py manage.py makemigrations
```

Exemplo de pasta onde serão criados os arquivos de migração
```text
app/
└── migrations/
    ├── __init__.py
    └── 0001_initial.py
```

Aplicar migrações criadas
```bash
py manage.py migrate
```
---
## Banco de dados
- Instalar extensão para melhor vizualiação do banco criado
    - SQLite Viewer
- Também é possível acessar o banco pelo Dbeaver.
    - Dbeaver -> Nova conexão -> SQLite -> Seleciona o arquivo `db.sqlite3` do projeto.