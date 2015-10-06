import random, pickle, os
from datetime import datetime

class setPicker:
	def __init__(self):
		self.pickNum = 1
		self.picked = []
		self.coreSets	=	[
							'Alpha',
							'Beta',
							'Revised',
							'Ultd',
							'IV',
							'V',
							'VI',
							'7th',
							'8th',
							'9th',
							'Xth',
							'M10',
							'M11',
							'M12',
							'M13',
							'M14',
							'M15',
							'Origins'
							]

		self.smallSets = 	[	
							'Arabian Nights',
							'Antiques',
							'The Dark',
							'Fallen Empires',
							'Homelands',
							'Alliances',
							'Coldsnap',
							'Visions',
							'Weatherlight',
							'Stronghold',
							'Exodus',
							'Urzas Legacy',
							'Urzas destiny',
							'Nemesis',
							'Prophecy',
							'Planeshift',
							'Apocalypse',
							'Torment',
							'Judgement',
							'Legions',
							'Scourge',
							'Darksteel',
							'5thDawn',
							'Betrayers',
							'Saviors',
							'Guildpact',
							'Dissention',
							'Planar Chaos',
							'Future Sight',
							'Morningtide',
							'Eventide',
							'Conflux',
							'Alara Reborn',
							'Worldwake',
							'Beseiged',
							'Phyrexia',
							'Dark Ascension',
							'Dragon Maze',
							'Born of the Gods',
							'Journey into Nyx',
							'Fate Reforged'
							]

		self.largeSets = 	[
							'Legends',
							'Ice Age',
							'Mirage',
							'Tempest',
							'Urzas saga',
							'Masques',
							'Invasion',
							'Oddysey',
							'Onslaught',
							'Mirrodin',
							'Champions of Kamigawa',
							'Ravnica: city of guilds',
							'Time Spiral',
							'Lorwyn',
							'Shadowmoor',
							'Shards',
							'Zendikar',
							'Eldrazi',
							'Scars',
							'Innistrad',
							'Avacyn Restored',
							'Return to Ravnica',
							'Gatecrash',
							'Theros',
							'Khans',
							'Dragons'
							]

	def __pickCore(self):
		pick = random.choice(range(len(self.coreSets)))
		theSet = self.coreSets[pick]
		del self.coreSets[pick]
		return theSet

	def __pickSmall(self):
		pick = random.choice(range(len(self.smallSets)))
		theSet = self.smallSets[pick]
		del self.smallSets[pick]
		return theSet

	def __pickLarge(self):
		pick = random.choice(range(len(self.largeSets)))
		theSet = self.largeSets[pick]
		del self.largeSets[pick]
		return theSet

	def __save(self):
		try:
			os.mkdir('./pickles')
		except OSError:
			pass
		
		attrName = 'picked_'+str(self.pickNum)
		self.pickNum += 1
		setattr(self, attrName, self.picked)

		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		file = open('./pickles/'+timestamp+'.sav', 'w')
		pickle.dump(self, file)
		file.close()

	def pick(self):
		self.picked = [self.__pickLarge(), self.__pickLarge(), self.__pickSmall(),  self.__pickSmall(),  self.__pickSmall(),  self.__pickSmall(), self.__pickCore(), self.__pickCore()]
		print self.picked		
		self.__save()

