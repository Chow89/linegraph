import pylab
import matplotlib.pyplot as plt

rank = {'Seahawks': [1, 2, 10, 1],
        'Broncos': [2, 3, 2, 4],
        'Patriots': [3, 10, 1, 2],
        'Saints': [4, 23, 16, 21],
        'Packers': [5, 5, 6, 3],
        '49ers': [6, 7, 13, 23],
        'Eagles': [7, 9, 4, 9],
        'Colts': [8, 4, 8, 10],
        'Chargers': [9, 1, 19, 13],
        'Bengals': [10, 6, 17, 8],
        'Bears': [11, 19, 28, 26],
        'Ravens': [12, 13, 15, 12],
        'Steelers': [13, 15, 12, 11],
        'Cardinals': [14, 11, 3, 6],
        'Lions': [15, 14, 5, 7],
        'Chiefs': [16, 18, 9, 15],
        'Panthers': [17, 16, 25, 20],
        'Falcons': [18, 20, 23, 22],
        'Giants': [19, 12, 24, 24],
        'Buccaneers': [20, 28, 31, 28],
        'Cowboys': [21, 8, 7, 5],
        'Rams': [22, 27, 21, 16],
        'Dolphins': [23, 24, 14, 18],
        'Texans': [24, 21, 20, 17],
        'Jets': [25, 30, 26, 27],
        'Vikings': [26, 25, 22, 19],
        'Redskins': [27, 26, 27, 29],
        'Titans': [28, 29, 29, 32],
        'Bills': [29, 17, 18, 14],
        'Raiders': [30, 32, 32, 30],
        'Browns': [31, 22, 11, 25],
        'Jaguars': [32, 31, 30, 31]
        }

fig, ax = plt.subplots()
pylab.gcf().canvas.set_window_title('Spox NFL-Ranking')
plt.title('Spox NFL-Ranking')
plt.gca().invert_yaxis()
plt.ylim(32, -1)
plt.grid(True)
# plt.legend(loc='upper right')
ax.set_xticklabels(['September', '', 'Oktober', '', 'November', '', 'Dezember'])
ax.set_yticklabels(['', 1, 6, 11, 16, 21, 26, 31])
plt.xlabel('Monat', fontdict={'size': 16})
plt.ylabel('Platzierung', fontdict={'size': 16})

for team in rank.keys():
        plt.plot(map(lambda x: x - 1, rank.get(team)), label=team)

plt.show()