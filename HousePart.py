# park's house class 박씨집

#class name : House park , last name, fullname 

class HousePark:
	lastname = "Park"
	def setName(self, name):
		self.fullname = name + self.lastname
	
pey = HousePark()
pey.setName("KK")

print(pey.fullname)
	