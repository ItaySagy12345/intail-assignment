init:
	python3 -m venv server/venv
	server/venv/bin/pip install --upgrade pip
	server/venv/bin/pip install -r server/requirements.txt

destroy:
	rm -rf server/venv