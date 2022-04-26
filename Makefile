PYFILES := $(shell find flatsplode tests -name '*.py')
SDIST   := dist/$(shell python setup.py --fullname 2> /dev/null).tar.gz

all: $(SDIST)

clean:
	rm -rf dist

upload: $(SDIST)
	twine upload $<

.PHONY: all clean upload

$(SDIST): $(PYFILES) | .venv
	git diff HEAD --quiet
	pipenv run pytest
	python setup.py sdist

.venv: Pipfile
	mkdir .venv
	pipenv install --dev
