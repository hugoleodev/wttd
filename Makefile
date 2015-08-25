
run:
	docker-compose up -d


test:
	docker-compose run web python manage.py syncdb --noinput
	docker-compose run web python manage.py migrate
	docker-compose run web python manage.py test core

clean:
	docker-compose kill
	docker-compose rm -f
	docker ps -a | grep 'Exited' | cut -f 1 -d' '| xargs docker rm