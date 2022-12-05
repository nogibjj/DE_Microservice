install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C main.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py
	
deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 589637869505.dkr.ecr.us-east-1.amazonaws.com
	docker build -t ids-ttquery .
	docker tag ids-ttquery:latest 589637869505.dkr.ecr.us-east-1.amazonaws.com/ids-ttquery:latest
	docker push 589637869505.dkr.ecr.us-east-1.amazonaws.com/ids-ttquery:latest

all: install format lint