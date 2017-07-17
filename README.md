# posostats
Tool to fetch and analyse data for German political parties and top-candidates from various social networks during the Bundestagswahl 2017.

It was created in the summer term 2017 at the HTW Berlin (Hochschule für Technik und Wirtschaft Berlin) [http://www.htw-berlin.de/](http://www.htw-berlin.de/) in the course 'Business software'.

# Authors

- Florian Nitschmann (s0544677@htw-berlin.de)

# Main features

The small library was mainly designed and develop to run permanently on a server to fetch continously the data.
Currently it offers the following features:
- it can fetch Facebook and Twitter accounts for all top parties and their candidates 
- update scripts to fetch post stats like Likes, Reations, Comments, Rewteets etc.
- updates for follower and likes counts for accounts

# Requirements

* Python ( version ` >= 3.0.0 `)
* MySQL as datastorge ( version should be ` >= 5.7.x `, other systems like PostgreSQL or SQLite should work as well)

# Technologies

* [Orator](https://orator-orm.com) ( ` 0.9.7 ` ) as ORM 
* [Python Twitter package](https://pypi.python.org/pypi/twitter) (`1.17.1`) for Twitter API communication
* [Pythons' native threading](https://docs.python.org/3/library/threading.html) to speed up to API calls and add concurrency

# Setup

To get the library running follow these steps:
1. Install the required ` pip ` packages in the root direcotry with ` pip install -r requirements.txt `
2. Copy all the ` .example. ` files under ` posostats/config ` and fill them with the need values (these are configs for the database and network APIs)
3. Change direcotory to ` posostats ` and run ` orator migrate -c config/orator.yml ` and ` orator db:seed -c config/orator.yml `. This sets up the database structure and fetches the first data from the networks. So relax a bit, it could take a while ;) 
4. Done. 
