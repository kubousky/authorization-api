# everytime we change requirements.txt / Dockerfile / docker-compose.yml
docker-compose build
# then check
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"

# up
docker-compose up

# up, start and remove
docker-compose run --rm app sh -c "python manage.py test"

# public DNS
ec2-54-186-124-240.us-west-2.compute.amazonaws.com