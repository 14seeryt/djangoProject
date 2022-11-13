In order to deploy the project create the docker containers using the following commands:

docker create --name pgadmin_container --network ca1_network --network-alias ca1_network_alias -t -v volume_ca1:/var/lib/
pgadmin -p 8008:80 -e 'PGADMIN_DEFAULT_EMAIL=C19420246@mytudublin.ie' -e 'PGADMIN_DEFAULT_PASSWORD=Tim@1452' dpage/pgadmin4

docker create --name postgis --network ca1_network --network-alias ca1_network_alias -t -p 25432:5432 -e POSTGRES_USER=docker -e POSTGRES_PASS=docker -v ca1_volume:/var/lib/postgresql kartoza/postgis

You must create a superuser before you can login to the application:

python manage.py createsuperuser

Proceed to the login screen and enter your credentials.

To view the Map press the view site button.

from here the Map is displayed and the user can press current location and the app will navigate to the current location of the user
(Couldn't figure out how to implement the geolocation Api unfortunately)

The map displays a pin of a hard coded location as well as a circle showing the accuracy of the fix

I was unable to keep a consistent look to the app due to problems with routing when using bootstrap.
When I attempted to make the application look more organised the functionality was unavailable
