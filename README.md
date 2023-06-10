# Kitambulisho Trace & Reissue System
# About
This is a system that facilitates the recovery of lost/misplaced National Identity cards and Passports.
The system involves 3 entities 
1. client who has lost their ID
2. The Noble Citizen who finds the ID Card 
3. A Station that receives->records->posts the ID Details and Reissues it to Owners

# Getting Started
ENV: python3
Technologies: Flask, SQLAlchemy(ORM), Rest_API

## Setting up the Environment
 - Install python requirements 
 ```
 pip install -r requirements.txt
 ```
 - modify the file "web_dynamic_api.sh" and update the mysql Server Username, Password & Database Name
 - Setting the "HBNB_ENV=dev" will only creates the table structures once
 - setting the "HBNB_ENV=test" will Truncate all tables and recreate them each time Flask restarts or reloads after a code change.
 
## Running the Program and Bootstrapping the Database and running the API
```
sudo mysql -u root
```
> CREATE DATABASE kitambulisho_db;

>quit;

```
bash -x web_dynamic_api.sh
```

Api Endpoints are documented in the "api.txt" file provided.
 
