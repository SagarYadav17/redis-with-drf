# Redis with Django Rest Framework

## Installation and Usage

- Create conda environment and install python

  ```bash
  conda create -n django-redis
  conda activate django-redis
  conda install python
  ```

- Install dependencies

  ```bash
  pip install -r requirements.txt --no-cache
  ```

- Host Redis Database server using Docker

  ```bash
    docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
  ```

- Migrate and Run the server
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```
