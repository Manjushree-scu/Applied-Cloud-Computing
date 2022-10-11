# To build Database administrator.

docker build -t my_dba . 
docker run --name mydba --network mynetwork -itd -p 8081:80 -d  my_dba

# Create Network to connect all 3 containers

docket network ls
docker network create mynetwork

# To build Database
docker build -t my_db . 
docker run --name mydb --network mynetwork -itd -p 5432:5432  -d my_db


# To build Django web application

(base) Manjushrees-MacBook-Pro:Public manju$ pwd
/Users/manju/SCU-MSIS/Sep2022/Appplied_cloud/code/Week3/Public
(base) Manjushrees-MacBook-Pro:Public manju$ docker build -t my_django .

docker run -it -p 8000:8000 -v $(pwd)/app:/app my_django /bin/bash

django-admin startproject app
python /app/app/manage.py runserver 0.0.0.0:8000

 python /app/app/manage.py migrate
 python /app/app/manage.py runserver 0.0.0.0:8000

 root@883699ed256e:~# python /app/app/manage.py createsuperuser
Username (leave blank to use 'root'): 
Email address: a@a.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
root@883699ed256e:~# 

root@883699ed256e:~# python /app/app/manage.py runserver 0.0.0.0:8000

set the database details in the settings.py file under /app

python /app/app/manage.py runserver 0.0.0.0:8000

add psycopg2 to requirements.txt and exit 

rebuild the container

(base) Manjushrees-MacBook-Pro:Public manju$ docker run -it -p 8000:8000 --network mynetwork -v $(pwd)/app:/app my_django /bin/bash 

root@4f2801da60d7:/app# python /app/app/manage.py migrate

root@4f2801da60d7:/app# python /app/app/manage.py runserver 0.0.0.0:8000

