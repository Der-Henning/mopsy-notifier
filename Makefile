start:
	docker-compose -f docker-compose.builder.yml build
	docker-compose -f docker-compose.builder.yml run --rm notifier
stop:
	docker-compose -f docker-compose.builder.yml down
build:
	docker build -t derhenning/mopsy-notifier:latest .