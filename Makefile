.PHONY: clean

Pipfile.lock:
	pipenv lock -r

clean:
	-pipenv --rm
	-rm Pipfile.lock
