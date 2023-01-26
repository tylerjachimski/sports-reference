import json
from tabulate import tabulate

#open and load json file
data = open('team_record.json')
records = json.load(data)

#create a list of teams to search through
teams = list(records.keys())

#create lists to be used to populate table
overallRecord = []
winsList = []

#get each teams wins against other teams in a list and store this winsList into the overallRecords list
for i in teams:
    winsList.append(i)
    for j in teams:
        if (records.get(i).get(j) != None):
            winsList.append(records.get(i).get(j).get('W'))
        else:
            winsList.append("--")
    overallRecord.append(winsList.copy())
    winsList.clear()

#append "Tm" to beginning of list of teams and append to end of overallRecord list for table formatting
teams.insert(0, "Tm")
overallRecord.append(teams)

#populate table
print(tabulate(overallRecord, headers=teams, tablefmt="fancy_grid"))

#close data file
data.close()
