# instructions on how to run the server
## create superuser
* open terminal
* type cd .\backend\ 
* type pip install -r requirements.txt    
* type python manage.py createsuperuser      
* enter email and password of your choice   
* type python .\manage.py runserver
* click on the link that will show in the terminal like this (http://127.0.0.1:8000/ )
* type /admin after the link (http://127.0.0.1:8000/admin/)

#

## how to make migrations

After changing anything in the code you should make migrations,
the server must not be running when you make migrations.
* open terminal
* type cd .\backend\  
* type python manage.py makemigrations todo
* type python manage.py migrate
* type python .\manage.py runserver to check your migrations
