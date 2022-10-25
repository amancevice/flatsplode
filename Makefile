SDIST := dist/flatsplode-$(shell pipenv run python -m flatsplode --version).tar.gz

all: build test

build: $(SDIST)

clean:
	rm -rf dist

test: | .venv
	pipenv run black --check flatsplode tests
	pipenv run pytest

publish: $(SDIST)
	git diff HEAD --quiet
	pipenv run flit publish

.PHONY: all build clean test upload

$(SDIST): **/*.py | .venv
	pipenv run pytest
	pipenv run flit build

.venv: Pipfile
	mkdir -p .venv
	pipenv install --dev
	touch .venv
