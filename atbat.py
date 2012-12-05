class AtBat:
	def __init__(self, pitches):
		self._pitches = pitches
		self._pitch_count = 0
		self._strikes = 0
		self._balls = 0
	
	def take_pitch(self):
		if self._pitch_count <= len(self._pitches) and self._strikes < 3 and self._balls < 4:
			pitch = self._pitches[self._pitch_count]
			if pitch == 'B': # Ball		
				self._balls += 1
			if pitch == 'F': # Foul
				if self._strikes < 2:
					self._strikes += 1
			if pitch in ['C', 'T', 'S']: # Check swings, foul tips, strikes
				self._strikes += 1
			self._pitch_count += 1
	
	def get_count(self):
		if self._strikes < 3 and self._balls < 4:
			status = 'Batting'
		if self._strikes >= 3:
			status = 'Out'
		if self._balls >= 4:
			status = 'Walked'
		return {
			'status': status,
			'pitches': self._pitch_count,
			'balls': self._balls,
			'strikes': self._strikes
		}
	