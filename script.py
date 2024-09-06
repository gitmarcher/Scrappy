import requests
from bs4 import BeautifulSoup
import pymysql
import getpass
from peewee import *

#**READ THE README BEFORE RUNNING THE SCRIPT**
#**RECOMMENDED TO TUN THIS SCRIPT IN A LINUX-BASED ENVIRONMENT AND FOLLOWINF THE INSTRUCTIONS IN THE README
#Read the how_to_run.txt file for further info.

DBName = input("Enter the name of the db(One is created if it doesn't already exist):")
userName = input("Enter the username(of sql):")
passwordSql = getpass.getpass("Enter the password(passowrd isn't echoed back):")
option = int(input("1.Premier league \n 2.LaLiga \n 3.Bundesliga \n Select the option: "))
league = None

if option == 1:
    league = "premier-league"
elif option ==2:
    league = "la-liga"
elif option == 3:
    league = "bundesliga"
else:
    print("Select the correct option.")



conn = pymysql.connect(host='localhost', user=userName, password=passwordSql)
conn.cursor().execute(f'CREATE DATABASE {DBName};')
conn.close()

db = MySQLDatabase(DBName, user=userName, password=passwordSql)

class BaseModel(Model):
    class Meta:
        database = db

def create_standings_class(db, class_name, attributes):
    new_class = type(class_name, (BaseModel,), attributes)
    return new_class

standings_attributes = {
    'standing': IntegerField(),
    'team': CharField(),
    'matches_played': IntegerField(),
    'matches_won': IntegerField(),
    'matches_drawn' :IntegerField(),
    'matches_lost': IntegerField(),
    'goals_for' : IntegerField(),
    'goals_against' : IntegerField(),
    'goal_difference' : IntegerField(),
    'points' : IntegerField()
}

db.connect()

for year in range(2000, 2023):
    url = f'https://www.skysports.com/{league}-table/{year}'
    response = requests.get(url)

    data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        for table in tables:
            for row in table.find_all('tr'):
                columns = row.find_all(['td', 'th'])
                if columns:
                    data.append([column.text.strip() for column in columns])
    else:
        print(f"Failed to retrieve the webpage for {year}.")
        continue

    league.replace('-','-')
    Standing = create_standings_class(db, f"{league}_{year}", standings_attributes)

    db.create_tables([Standing])

   
    for i in range(1, len(data)):

        Standing.create(
            standing=int(data[i][0]),
            team=data[i][1],
            matches_played=int(data[i][2]),
            matches_won=int(data[i][3]),
            matches_drawn=int(data[i][4]),
            matches_lost=int(data[i][5]),
            goals_for=int(data[i][6]),
            goals_against=int(data[i][7]),
            goal_difference=int(data[i][8]),
            points=int(data[i][9])
            )
    print(f"standongs for year {year} inserted")



db.close()
