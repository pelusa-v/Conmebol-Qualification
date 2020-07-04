from objects import countries
from classes import Match, Country
import random
# main menu
# def main():
#	pass

def main_menu():
	print("\nSelect an option:\n")
	print(" ===========================")
	print("| 1 - Show table            |")
	print("| 2 - Show team history     |")
	print("| 3 - Next date             |")
	print("| 4 - Play match            |")
	print(" ===========================")
	ans = input()
	return ans


def show_table():
	countries_sorted = []
	def rule_points(e):	# order by points
		if isinstance(e, Country):
			return e.points
		#def rule_diff(a):	#order by diff
		#	return a.diff
	countries.sort(reverse=True,key=rule_points)

	print("Country		GF	GC	Diff	Points")
	for country in countries:
		# giving indentation
		new_name = country.name
		len_string = len(country.name)
		if len_string < 8:
			for i in range(0,8-len_string):
				new_name = new_name + ' ' 

		s = "{}	{}	{}	{}	{}"
		print(s.format(new_name, country.gf, country.gc, country.diff, country.points))


def matching_teams(countries):
	teams = countries
	size = len(countries)
	first_all_dates = []
	second_all_dates = []

	#Round-Robin tournament
	for i in range(0,size-1):
		first_matches = []
		second_matches = []
		for k in range(0,int(size/2)):
			first_matches.append((teams[k],teams[size-1-k]))
			second_matches.append((teams[size-1-k],teams[k]))

		first_all_dates.append(first_matches)
		second_all_dates.append(second_matches)
		teams.insert(1,teams[size-1])
		teams.pop()

	return first_all_dates+second_all_dates

MATCHES = matching_teams(countries)

def play_matches(countries,current_date):
	print("------------------------ round {} ------------------------".format(current_date))
	for match in MATCHES[current_date]:
		match = Match(match[0],match[1])
		match.play()
	print("----------------------------------------------------------")