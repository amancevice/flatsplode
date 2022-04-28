PYFILES := $(shell find flatsplode tests -name '*.py')
SDIST   := dist/$(shell pipenv run python -m flatsplode --fullname).tar.gz

all: test

build: $(SDIST)

clean:
	rm -rf dist

test: | .venv
	pipenv run pytest

publish: $(SDIST)
	git diff HEAD --quiet
	pipenv run flit publish

.PHONY: all build clean test upload

$(SDIST): $(PYFILES) | .venv
	pipenv run pytest
	pipenv run flit build

.venv: Pipfile
	mkdir -p .venv
	pipenv install --dev
	touch .venv
