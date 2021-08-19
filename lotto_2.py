#-*- coding: utf-8 -*-
# Manu
from random import *
import random

# 번호 List를 받아서 1~47 범위 및 6개 번호인지, 중복 숫자 여부 유효성 check, 유효시 1, 유효안하면 -1 을 return
def Valid_Num(Input_Num):
	for i in Input_Num:
		if i < 1 or i > 47:
			print("숫자 범위를 벗어났습니다")
			return -1

	if len(Input_Num)>6:
		print("번호 갯수 6개를 벗어났습니다")
		return -1
		
	elif len(Input_Num)!=len(set(Input_Num)) :
		print("중복된 숫자가 있습니다")
		return -1
	else:
		return 1

# 랜덤 숫자를 만들고 중복되지 않게 리스트에 추가하는 함수

def check_dupl(list_a):
	print(list_a)
	if len(list_a) == 6:
		return list_a

	flag = 0
	while(flag == 0):
		generate_num = randint(1,47)
		if generate_num in list_a:
			continue
		else:
			list_a.append(generate_num)
			if len(list_a) == 6:
				break
				
							
	list_a.sort()
	return list_a
	

#자동번호 추출
def Gen_auto():
	num = random.sample(range(1,47),6)
	num.sort()
	print(num)

#반자동번호 추출
def Gen_half():
	#번호 입력 받기
	User_num = [int(x) for x in input("반자동에 넣을 숫자를 입력하세요").split(" ")]

	#입력 번호 유효성 check 및 중복 check
	if Valid_Num(User_num) == 1:
		num = check_dupl(User_num )				
		print(num)
	else :
		print("번호가 유효하지 않습니다")
		return -1
	

#수동번호 추출
def Gen_manual():
	# 수동번호 입력 받기
	User_num = [int(x) for x in input("수동에 넣을 숫자를 입력하세요(1~47)").split(" ")]
	if len(User_num) != 6:
		print("6개의 숫자를 입력해야 합니다")
		return -1
	
	if Valid_Num(User_num) == 1:
		print(User_num)
	

#Main 코드
while True:
	Manu = int(input("\n메뉴번호를 입력하세요 1: 자동, 2: 반자동, 3: 수동 4: EXIT-> "))
	if Manu == 1:
		print("자동")
		Gen_auto()
		continue
	elif Manu == 2:
		print("반자동")
		Gen_half()
		continue
	elif Manu == 3:
		print("수동")
		Gen_manual()
		continue
	elif Manu == 0:
		print("종료")
		break
	else:
		print("Error")
		break