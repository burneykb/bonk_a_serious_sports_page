FROM python:3.13.0a1-alpine

# Copy the requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Set destination for COPY
WORKDIR /app

# copy the application to the working directory.
COPY . .

EXPOSE 8008

# Run
CMD [ "gunicorn", "--bind=0.0.0.0:8008", "--chdir=./app", "wsgi:app" ]
