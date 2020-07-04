import random

class Country():

	def __init__(self, name, points = 0, gf = 0, gc = 0, diff = 0, playing=False):
		self.name = name
		self.diff = gf - gc
		self.gc = gc
		self.gf = gf
		self.points = points
		self.playing = playing
		self.played_with = [self]

	def __str__(self):
		return str(self.name)

	def update_diff(self):
		self.diff = self.gf - self.gc


class Match():

	def __init__(self, team1, team2, winner="Drow", goals1=0, goals2=0):
		if isinstance(team1, Country):
			self.team1 = team1
			self.team2 = team2
			self.winner = winner
			self.goals1 = goals1
			self.goals2 = goals2

	def play(self):
		self.team1.played_with.append(self.team2)
		self.team2.played_with.append(self.team1)
		goals1 = random.randrange(0,6)
		goals2 = random.randrange(0,6)
		self.team1.gf += goals1
		self.team1.gc += goals2
		self.team2.gf += goals2
		self.team2.gc += goals1
		self.goals1 = goals1
		self.goals2 = goals2
		self.team1.update_diff()
		self.team2.update_diff()

		if goals1 > goals2:
			self.winner = self.team1.name
			self.team1.points += 3
		elif goals2 > goals1:
			self.winner = self.team2.name
			self.team2.points += 3
		else:
			self.winner = "Drow" 
			self.team1.points += 1
			self.team2.points += 1

		self.show_summary() #show summary at the end of match

	def show_summary(self):
		# giving indentation
		new_name = self.team1.name
		len_string = len(self.team1.name)
		if len_string < 9:
			for i in range(0,9-len_string):
				new_name = new_name + ' '
		s = "		{} {} - {} {}"
		print(s.format(new_name, self.goals1, self.goals2, self.team2.name))