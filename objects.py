from classes import Country
import json

#variables to export:
countries = []

with open('file.json','r') as file:
	data = json.load(file)
	for country in data.values():
		countries.append(Country(country))


