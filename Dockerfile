FROM python:3.8.5

RUN pip install fastapi uvicorn aiofiles fastapi-async-sqlalchemy python-multipart requests pymongo dnspython aiohttp colorama apscheduler ddddocr beautifulsoup4 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

EXPOSE 8080

COPY . .

CMD ["python", "api/main.py"]