.DEFAULT_GOAL := build

build:
	docker build -t python-solid-app .
.PHONY: build

run:
	docker run python-solid-app
.PHONY: run
