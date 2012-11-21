PORTA = 8000
DOMINIO = '127.0.0.1'

run:
	@echo "instalando os pacotes necessarios"
	pip install -r requirements.txt
	@echo "run -> Aplicacao portal $(DOMINIO):$(PORTA)..."
	@export PYTHONPATH=`pwd`:`pwd`/dango_project:$$PYTHONPATH && \
		export DJANGO_SETTINGS_MODULE=portal.settings && \
		python manage.py syncdb && \
		python manage.py migrate galeria && \
		python manage.py runserver $(DOMINIO):$(PORTA)
