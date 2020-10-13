# Pull official base image
FROM python:3.8.2-alpine

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
# Prevents Python from writing pyc files to disc === python -B option
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr === python -u option
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project
COPY . /usr/src/app

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
