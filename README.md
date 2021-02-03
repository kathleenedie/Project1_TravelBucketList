# Project1_TravelBucketList
a web app which allows users to add and manage their travel bucket list

# To run this app;
* to run the database, in Terminal run:
createdb bucket_list
psql -d bucket_list -f db/bucket)list.sql

* to populate the database seed data, in Terminal run:
python3 run console.py

* to run the flask environment, in Terminal run:
flask run


# The original brief was

## Travel Bucket List

Build an app to track someone's travel adventures.

### MVP:

 * The app should allow the user to track countries and cities they want to visit and those they have visited.
 * The user should be able to create and edit countries
 * Each country should have one or more cities to visit
 * The user should be able to create and delete entries for cities
 * The app should allow the user to mark destinations as visited or still to see

### Possible Extensions:

 * Have separate pages for destinations visited and those still to visit
 * Add sights to the destination cities
 * Search for destination by continent, city or country
 * Any other ideas you might come up with
 
 ######
 This app used psycopg, flask, python3.
 
