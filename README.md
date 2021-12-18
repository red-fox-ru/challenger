# challenger_backend_app

### For use in Docker: 

```bash
docker build -t challenger .
docker-compose build
```

### Initial project:
```bash
docker-compose up
```

### First setup before use.
#### Open the second console and find the project:
```bash
docker ps -a
```
#### get interactive bash session from containers
```bash
docker exec -t -i CONTAINER_ID bash
```
#### initiate migration
```bash
 python manage.py makemigrations
 python manage.py makemigrations v1
 python manage.py migrate
```
#### create a new super user
```bash
python manage.py createsuperuser
```
#### settings completed can use.
