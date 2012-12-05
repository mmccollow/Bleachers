from atbat import AtBat

class Inning:
	""" This is really a half-inning """
	def __init__(self, at_bats):
		self._at_bats = at_bats
		self._outs = 0
		self._runs = 0
		self._hits = 0
		self._errors = 0
		self._lob = 0
		self._score = {}
		self._half_inning = 0	
	
	def play_inning(self):
		for at_bat in self._at_bats:
			ab = AtBat(at_bat)
			ab.play()
	
	def summary(self):
		return {
			'runs': self._runs,
			'hits': self._hits,
			'errors': self._errors,
			'lob': self._lob,
			'score': self._score
		}
	