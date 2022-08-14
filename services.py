import requests
import shutil
import csv

def downloadPokemonImage(pokemonName):
    pokemonName = pokemonName.lower()
    URL = "https://img.pokemondb.net/artwork/large/" + pokemonName + ".jpg"
    filePath = "Images/Pokemon/" + pokemonName + ".jpg"
    r = requests.get(URL, stream=True)
    if r.status_code == 200:
        with open(filePath, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def typeDefinitions(type1, type2):
    with open('typeChart.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        typeList = []
        interactions1 = []
        interactions2 = []
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                for column in row:
                    typeList.append(column)
            else:
                if typeList[lineCount] == type1:
                    columnCount
                    for column in row:
                        interactions[]
                        
                    
            lineCount = lineCount + 1
                    

typeDefinitions("Fire", "None")