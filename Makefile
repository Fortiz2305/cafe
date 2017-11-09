IMAGE_NAME := fortiz/cafe

build:
	docker build -t ${IMAGE_NAME} .

shell: build
	docker run --rm -it -v ${PWD}:/code ${IMAGE_NAME} /bin/bash

unit_test: build
	docker run --rm -it -v ${PWD}:/code ${IMAGE_NAME} bash -c "TESTING=true mamba -f documentation tests/unit/**/**"

test: build unit_test
