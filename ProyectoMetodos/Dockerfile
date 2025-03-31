FROM python:3.9-slim

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]


#podman build -t ima .

#podman run -it -p 5000:5000 ima