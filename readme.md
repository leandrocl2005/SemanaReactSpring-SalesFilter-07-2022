# Django + React Web App para filtro de vendas

Projeto desenvolvido durante a <a href="https://devsuperior.com.br/">Semana Spring React</a> trocando o Java Spring no backend por Python Django.

Nesse projeto foi estudado a customização de filtros, paginações e ordenação com Django Rest Framework.

## Como executar este projeto?

As instruções são para execução em ambiente de desenvolvimento.

- Na pasta backend:
```
python -m venv env
. env/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Na pasta frontend:
```
yarn
yarn start
```