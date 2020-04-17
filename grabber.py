#all zip and coordinate information from OpenDataSoft
#only works for US locations

import csv
import string
import requests


def getLatLong():
    with open('us-zip-code-latitude-and-longitude.csv', newline = '') as csvfile:
        latLongReader = csv.reader(csvfile, delimiter=',')
        zCode = input("What is your zip code? ")
        print("\n")
        rawData = ""

        for row in csvfile:
            if zCode in row:
                print("Zip located: " + row) # Column 4 / 5 are lat/long
                rawData = row

        if rawData == "":
            print("Zip not found in table.\n")
            menu()
        
        index = 0
        firstindex = 0
        secondindex = 0
        counter = 0
        for letter in rawData:
            index += 1
            if letter == ";":
                counter += 1
                if counter == 3:
                    firstindex = index
                if counter == 4:
                    secondindex = index
                    lattitude = rawData[firstindex:secondindex-1]

        index = 0
        firstindex = 0
        secondindex = 0
        counter = 0
        for letter in rawData:
            index += 1
            if letter == ";":
                counter += 1
                if counter == 4:
                    firstindex = index
                if counter == 5:
                    secondindex = index
                    longitude = rawData[firstindex:secondindex-1]
        
        getWeather(lattitude, longitude)

def getWeather(lattit, longit):
    print(lattit, longit)

def menu():
    print("Geolocation weather finder based on zip code or longitude and lattitude.")
    choice = input("1. Zip Code \n2. Lattitude Longitude \n3. Quit \n")
    if "1" in choice:
        getLatLong()

    elif "2" in choice:
        lattitude = input("What is your lattitude? ")
        print("\n")
        longitude = input("What is your longitude? ")
        print("\n\n")
        getWeather(lattitude, longitude)

    elif "3" in choice:
        exit()

    else:
        print("Invalid input. Returning to menu...")
        menu()



menu()