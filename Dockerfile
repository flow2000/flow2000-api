FROM python:3.8.5

# 维护者
MAINTAINER 1982989137@qq.com

COPY . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8888

CMD ["python", "api/main.py"]