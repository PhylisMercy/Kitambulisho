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

# API Enpoint Documentation.
``` #install asciinema to play the *.rec files
sudo apt install asciinema -y
# play Recording using the following: -s is for speed you can set to a lower value e.g 1 if you prefer.
ls {1..6}*.rec # Lists all asciinema recordings
asciinema play -s 5 1_report_lost_id.rec # Plays the first asciinema recording

```
Api Endpoints are documented in the [api.txt file provided](https://github.com/PhylisMercy/Kitambulisho/blob/main/api.txt).
 
# Project Resources

####  project proposal 
[Kitambulisho Trace & Reissue System Pitch Deck & Lean Canvas Model](https://docs.google.com/presentation/d/1sXeUJZmOe58-eWsL6o1cccubWsswPXanPoPfSGmYCHM/edit?usp=sharing)


#### Proposed web architecture & MVP
![ID Tracker flowChart (2)](https://github.com/PhylisMercy/Kitambulisho/assets/110587824/836a3b87-4729-49dc-9f94-74410f4544a7)



[Minimal Viable Product Specification Document](https://docs.google.com/document/d/1sEPgdIT1LoF1bAv-tHo5r54NwnhApaAszcrVONloFLM/edit?usp=sharing)
#### Project Management
[Trello board Detailing the Work BreakDown Structure & Timelines](https://trello.com/invite/b/1JZMmeeG/ATTI106daadbfdef4a64b569c3a5f0c025acEEF56A70/portfolio-project)


#### Demo Videos



https://github.com/PhylisMercy/Kitambulisho/blob/main/Videos/01_Getting_Started.mp4
https://github.com/PhylisMercy/Kitambulisho/blob/main/Videos/02_Report_Lost_n_Found.mov
https://github.com/PhylisMercy/Kitambulisho/Videos/03_Remit_Kitambulisho_to_huduma_station.mov
![ID Tracker flowChart (2)](https://github.com/PhylisMercy/Kitambulisho/Videos/04_Kitambulisho_Remit_Handling_Duplicate_remittance.mov)
![ID Tracker flowChart (2)](https://github.com/PhylisMercy/Kitambulisho/Videos/05_Search_Lost_ID_Get_Huduma_Station.mov)
[Project Demo Videos](https://drive.google.com/drive/folders/13cwyBdtJo-ZwpxggVc7oXQ9anfpiFxZl?usp=sharing)

#### Final Presentation slides

[project Summary Slides](https://docs.google.com/presentation/d/14CUWgDwO1ZzQcc9Qc8KbwXA9XePaWrZuexTRA3RP4p8/edit?usp=sharing)

