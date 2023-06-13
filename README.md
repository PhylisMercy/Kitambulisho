# Kitambulisho Trace & Reissue System
# About
This is a system that facilitates the recovery of lost/misplaced National Identity cards and Passports.
The system involves 3 entities 
1. client who has lost their ID
2. The Noble Citizen who finds the ID Card 
3. A Station that receives->records->posts the ID Details and Reissues it to claiming Owners

# Getting Started
ENV: python3
Technologies: Flask, SQLAlchemy(ORM), Rest_API

## Setting up the Environment
 - Install python requirements 
 ```
 pip install -r requirements.txt
 ```
 - modify the file "web_dynamic_api.sh" and update the mysql Server Username, Password & Database Name
 - Setting the "HBNB_ENV=dev" will only create the table structures once
 - setting the "HBNB_ENV=test" will Truncate all tables and recreate them each time Flask restarts or reloads after a code change/update.
 
## Running the Program and Bootstrapping the Database and running the API
```
sudo mysql -u root
```
> CREATE DATABASE kitambulisho_db;

>quit;

```
sudo mysql -u root kitambulisho_db < kitambulisho_db.sql
bash -x web_dynamic_api.sh
```
### INFO
NOTE: When you are making database schema modification set web_dynamic_api.sh HBNB_ENV=test - since any code modification
will cause the database to be truncated and DDL to be rerun to incorporate new updates Else just set it's value to
HBNB_ENV=dev to test out DQL and DRL.

Api Endpoints are documented in the [api.txt file provided](https://github.com/PhylisMercy/Kitambulisho/blob/main/api.txt).
 
# Project Resources
