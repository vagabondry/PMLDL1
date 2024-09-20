FROM python:3.12-slim

WORKDIR /app

COPY api.py ./
COPY feature.py ./
COPY model.pkl ./  

RUN pip install fastapi uvicorn scikit-learn pydantic requests beautifulsoup4 python-whois googlesearch-python

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
