# rk_django_tabela_html_bd
Tabela HTML simples em Django utilizando banco SQLite3 (criado utilizando interface de administração)

virtualenv venv

source venv/bin/activate (Linux)

.\venv\Scripts\activate (Windows)

pip install django

python manage.py makemigrations registros

python manage.py migrate

python manage.py createsuperuser

* Criar Username/Password (acesso ao banco = tabela 'registros')

python manage.py runserver

(Acessar http://127.0.0.1:8000/admin)

Inserir registros no banco "Registros"

(Verificar Tabela HTML renderizada pelo Django a partir do BD: http://127.0.0.1:8000)
