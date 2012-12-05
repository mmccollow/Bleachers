class Score:
	def __init__(self, home, away):
		self._home = home,
		self._away = away,
		self._home_runs,
		self._away_runs
	
	def __str__(self):
		return self._away, ": ", self._away_runs, ", ", self._home, ": ", self._home_runs
	
	def add_run(self, side):
		if side == "home":
			self._home_runs += 1
		if side == "away":
			self._away_runs += 1
	
	