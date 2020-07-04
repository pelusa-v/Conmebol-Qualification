from classes import *
from interactions import main_menu, show_table, play_matches
from objects import countries
CURRENT_DATE = 0

def run():
	op = main_menu() # menu

	if op == '1': # show positons table
		show_table()
	elif op == '4': # play matches
		global CURRENT_DATE
		play_matches(countries, CURRENT_DATE)
		CURRENT_DATE += 1



if __name__ == '__main__':
	while(1): run()