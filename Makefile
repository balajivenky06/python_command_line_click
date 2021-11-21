install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mylib test_mathcode.py

format:
	black *.py

lint:
	pylint --disable=R,C mylib/mathcode.py
	#lint Dockerfile
	#docker run --rm -i hadolint/hadolint < Dockerfile

deploy:
	echo "deploy goes here"

all: install lint test format