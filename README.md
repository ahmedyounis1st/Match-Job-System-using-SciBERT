# Match-Job-System-using-SciBERT

1. Kindly, add MySQL Tables to your database schema
you will find them in the MySQL folder

Notes about the database: 
- publications_tab table has the same values that publications_tab_2018 
which both are vectorized from 2018.xlsx file 
thats why i have created the strategy of getting the value the four years and save them in 4 tables
instead of loading them each time you run the project which will impact very very much time "can reach 1 hour for 1 query" 

- candidate table stores the results the we got from SciBert2 model and paths for plots 
Please don't change any of that 


2. install requirements through 
pip install -r requirements.txt

3. Change password and port in mysql_manager.py
PASSWORD = ""
PORT = ""

4. in app.py 
change mysql config to your configuration
