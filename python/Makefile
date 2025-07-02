.PHONY: test test-fast test-slow test-file coverage clean install

install:
	pip install -r requirements-test.txt

test:
	pytest -v

test-fast:
	pytest -v -m "not slow"

test-slow:
	pytest -v -m "slow"

test-file:
	pytest -v test/test_$(FILE).py

coverage:
	pytest --cov-report=html
	open htmlcov/index.html

test-parallel:
	pytest -n auto

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache htmlcov .coverage

# Test specific problem types
test-array:
	pytest -v -m "array"