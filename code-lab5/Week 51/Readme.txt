If there is an error for import of SQLAlchemy then please run
docker-compose up --build

Consumer:
For meal recomendation, Please login to 
http://localhost:81

DB_Admin:
 To run pgadmin website: Please login to 
 http://localhost:80 

 username : admin@admin.com
 password : pass

Steps to do:
 1. Click on Add New Server.
 2. Enter "db" in the Name test field. 
 3. Rest remains default and click on connection tab.
 4. Enter db in the Host name/Address.
 5. Username : root and password : pass
 6. Keep the rest of the fields default and press on Save.


To insert an Entry into the database use the below SQL command.

INSERT INTO Meals(MealName, MealPrice) VALUES ('Munchies Manchuri', 15.99);



  