test:
	venv/bin/python -m coverage run -m pytest && venv/bin/python -m coverage combine && venv/bin/python -m coverage report

type:
	venv/bin/python -m mypy --strict src tests