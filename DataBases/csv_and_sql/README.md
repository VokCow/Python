# Python: CSV and SQL
This very simple exercise illustrates several facts:
  * how the processes of retreiving data from a csv file works
  * how easier it is to connect to a MySQL server using the mypysql API (quite more simple than in Java and Scala cases when one has to deal with jdbc)

First, the app connects to SQL sys database (which is already there by default) and then allow user to choose a name for the database 
in which the information retreived from the csv file will be stored.
The csv is also in this repositroy. It is data about the taxi fleet in Madrid, avalible at https://datos.madrid.es/portal/site/egob/
