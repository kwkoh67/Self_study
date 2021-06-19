arr = [3,5,7,9,1]

result = []
dic = []
count = 0


for index in range(len(arr)): #Arr 길이만큼 index

	if index != 0 : # index 가 0이면 무조건 포함
		flag = 0 #중복 있으면 1 없으면 0
		for dic_index in range(len(dic)): #중복된 index 제거를 위한 배열
			
			if arr[index] == dic[dic_index]: 
				flag =1
				break
			else:
				continue

		if flag == 0: #중복된게 없으면 포함
			dic.append(arr[index]) 
		
	else:
		dic.append(arr[index])

for i in range(len(dic)): # dic 1개씩 호출
	for j in range(len(arr)): # Arr에서 비교
		if dic[i] == arr[j]: #같으면 카운트 1증가
			count +=1
		else:
			pass

	if ((count != 0)&(count !=1)): #count가 0이나 1이 아니면 포함
		result.append(count)
		

	else:
		pass
	count = 0

print("dict : %s " % dic)

if bool(result) == False : # 비어있는 list는 False 를 반환한다.
	result.append(-1)
	#print("NONE")
else:
	#result.append(-1)
	pass

print("result : %s " % result)	
	
