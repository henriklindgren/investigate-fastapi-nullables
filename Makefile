.PHONY: build test


build:
	venv/bin/pip install .

test:
	venv/bin/python -m pytest tests.py
