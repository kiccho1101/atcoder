start:
	docker-compose up -d

shell:
	docker-compose exec jupyter bash

run:
	docker-compose exec jupyter $(filter-out $@,$(MAKECMDGOALS))
