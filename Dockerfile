FROM python:3.10

ADD Calc.py .
ADD webpage.html .
ADD webserver.py .

EXPOSE 8080

CMD ["python3","./webserver.py","-it", "-p"]
