up:
	docker-compose up -d

down:
	docker-compose down

ptw:
	poetry run ptw --ext=.py,.tmpl,.groovy -- -s
