# WebScraper
Program for scraping information from the https://msc.com.pl/cezar/ website about the results in Polish bridge tournaments. The Program is designed to run in the background. It reads users' data from data.csv and then scrapes the website to get the number of users' PKLs(classification points) and views of the profiles. If the number has changed it writes it in logs.txt. The program also sends a notification email to the user if the number of PKLs has changed.

# Set up
## Refresh time
You can set a custom web refresh time in main.py.
## Email
To have working email sending you need to have a Gmail account and get a password from apppassword. then copy the email and password to the code in notifications.py.
## Users 
You must have users in the data.csv file. You can add it manually, copy it from Excel, or use the datamanager.py.
