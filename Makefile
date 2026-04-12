install:
	pip install -r requirements.txt

run-api:
	uvicorn app.main:app --reload

run-pipeline:
	python run_pipeline.py