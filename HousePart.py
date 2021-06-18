#park's house class 박씨집

#class HousePark, 이름 생성, 여행가고싶은곳

class HousePark:
	lastname = "Park"			#성은 박씨
	
	def setName(self, name):		#이름을 입력 받고 fullname 을 생성
		self.fullname = name + " " + self.lastname
	
	def travel(self, place):		#여행가고 싶은곳
		self.travel_place = place

	


pey = HousePark()				# pey 의 클래스 생성
pey.setName("pey")
pey.travel("Paris, France")

kw = HousePark()				#kw의 class생성
kw.setName("Kw")
kw.travel("London")

print(pey.fullname)
print(pey.travel_place)	
print(kw.fullname)
print(kw.travel_place)
