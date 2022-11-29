all: build test

build: .venv
	pipenv run flit build

clean:
	rm -rf dist

test: .venv
	pipenv run black --check $(shell basename $$PWD) tests
	pipenv run pytest

publish: build test
	git diff HEAD --quiet
	pipenv run flit publish

.PHONY: all build clean test publish

Pipfile.lock: Pipfile
.venv: Pipfile.lock
	mkdir -p $@
	pipenv install --dev
	touch $@
