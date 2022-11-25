# everytime we changerequirements.txt / Dockerfile / docker-compose.yml
docker-compose build

# up
docker-compose up

# up, start and remove
docker-compose run --rm app sh -c "python manage.py test"

# public DNS
ec2-54-186-124-240.us-west-2.compute.amazonaws.com