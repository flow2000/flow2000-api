FROM python:3.8.5

RUN pip install fastapi uvicorn aiofiles fastapi-async-sqlalchemy python-multipart requests pymongo aiohttp colorama beautifulsoup4

EXPOSE 8888

COPY . .

CMD ["python", "api/main.py"]
