.PHONY : clean env
ENV_NAME ?= test_env

clean:
	@py3clean .
env:
	virtualenv $(ENV_NAME ) -p python3
	pip install -r requirements.txt
superuser:
	python manage.py createsuperuser
migrations:
	python manage.py makemigrations
migrate: migrations
	python manage.py migrate

clean-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

dump-chartofaccount:
	./manage.py dumpdata finance.chartofaccount > finance/fixtures/chartofaccount.json --indent 4 --format json

load-codes:
	./manage.py loaddata codes