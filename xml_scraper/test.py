from csv import DictWriter

players = [{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player1', 'bank': 0.06},
{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player2', 'bank': 4.0},
{'dailyWinners': 1, 'dailyFree': 2, 'user': 'Player3', 'bank': 3.1},
{'dailyWinners': 3, 'dailyFree': 2, 'user': 'Player4', 'bank': 0.32}]

with open('spreadsheet.csv','w') as outfile:
    writer = DictWriter(outfile, ('dailyWinners','dailyFreePlayed','dailyFree','user','bank'))
    writer.writeheader()
    writer.writerows(players)
