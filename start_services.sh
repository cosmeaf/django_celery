#!/bin/bash

# Ative seu ambiente virtual, se estiver usando um
# source /caminho/para/seu/env/bin/activate

# Inicie o Django
python manage.py runserver 0.0.0.0:8001 &

# Inicie o worker do Celery
celery -A core worker --loglevel=info &

# Inicie o beat do Celery, se você estiver usando tarefas agendadas
# celery -A core beat --loglevel=info &

 # lsof -i :8001 | awk '{print $2}' | grep -v 'PID' | xargs kill -9
 # ps -ef | grep celery | awk '{print $2}' | grep -v 'PID' | xargs kill -9