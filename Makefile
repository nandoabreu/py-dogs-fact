
NAME = dogs-fact
CONTAINER := $(shell docker ps --all --quiet --filter="name=$(NAME)")
#CONTAINER := $(or ${CONTAINER},${CONTAINER},NO CONTAINER. To create: make)


.PHONY: clean test run scale stop start compose rm

run: #compose
	@echo "Building and running compose (up)..."
	docker-compose build --force-rm --pull | grep Step #--quiet
	docker-compose up --remove-orphans -d
	docker ps --filter="name=$(NAME)"
	@echo "Ready."

scale: #compose
	@echo "Building and running compose (up) with 3 instances..."
	docker-compose -f docker-compose-scale.yml build --force-rm --pull | grep Step #--quiet
	docker-compose -f docker-compose-scale.yml up -d --scale app=2
	@echo "Ready."

#compose:
#	@echo "Building compose image, please wait around 60 seconds..."
#	docker-compose build --force-rm --pull --quiet
#	@echo "Built."

start:
	@echo "Starting container..."
	docker container start "$(CONTAINER)"
	@echo "Ready."

stop:
	@echo "Stopping container..."
	docker container stop $(CONTAINER)
	@echo "Stopped."

rm:
	@echo "Cleaning up (docker-compose)..."
	docker-compose down --remove-orphans --rmi all
	make clean
	@echo "Done."

test:
	@echo "\n### Starting unittests... ###########"
	python3 -m unittest tests/test_*
	@echo "Done."

clean:
	@echo "Cleaning up (cache and virtualenv)..."
	-docker-compose down --remove-orphans --rmi all >/dev/null 2>&1
	find . -type d -name '__pycache__' -exec rm -rf {} + >/dev/null 2>&1
	find . -type d -name '.venv' -exec rm -rf {} + >/dev/null 2>&1
	@echo "Done."

default: run

