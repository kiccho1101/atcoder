start:
	docker-compose up -d

shell:
	docker-compose exec jupyter bash

stop:
	docker-compose down

run:
	docker-compose exec jupyter $(filter-out $@,$(MAKECMDGOALS))
