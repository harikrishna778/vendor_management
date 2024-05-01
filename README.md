# vendor_management

Create Bashrce file with below values

export MYSQL_DATABASE=database_name
export MYSQL_USER=use_name
export MYSQL_PASSWORD=password

source bashrc_file_name

run sh setup.sh

then run
  sh django.sh init_db
  sh django.sh setup_db
  sh django.sh init_db

run migrations: python3 manage.py makemigrations
python3 manage.py migrate


create super user : python3 manage.py createsuperuser

run server python3 manage.py runserver
  
