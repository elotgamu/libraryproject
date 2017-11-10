#Run the django server on dev mode
serve:
	python manage.py runserver

#Create the migration file
makesql:
	python manage.py makemigrations

#Run the migrations
migrate:
	python manage.py migrate

#check for error
check:
	python manage.py check

#launch PostgreSQL
pgup:
	sudo systemctl start postgresql

#stop PostgreSQL
pgstop:
	sudo systemctl stop postgresql

pgstatus:
	sudo systemctl status postgresql

#see help
help:
	python manage.py help
