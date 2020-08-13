import os
import json

def level(PKnum):
    multnum = 1.5

    os.chdir(r"C:\Users\Michael\Documents\coding\projects\games\knockoff pokeman\sources")

    base = open('base.json', 'r')
    stats = json.load(base)

    types = stats['stat types']

    m = open('player.json', 'r')
    file = json.load(m)
    total = 0
    for types in types:
        file['party'][PKnum]['stats'][types] *= multnum
        total += file['party'][PKnum]['stats'][types]
    file['party'][PKnum]['level'] += 1
    file['party'][PKnum]['stats']['Total'] = total
    m = open('player.json', 'w')
    json.dump(file, m, indent=4)

level('pikichoo')