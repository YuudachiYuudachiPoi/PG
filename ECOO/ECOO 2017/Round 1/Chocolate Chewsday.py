f = open('/home/xili/PG/ECOO/ECOO 2017/Round 1/DATA/DATA22.txt','r')
data = f.read().split('\n')
for loop_time in range(0,10):
	number_of_chocolates = int(data[0])
	data.pop(0)
	chocolates_scores = {} 
	for judge_time in range(0,number_of_chocolates):
		name = data[0]
		data.pop(0)
		scores_list = []
		
		n = 0
		while True:
			if data[n][0] == 'J':
				scores_list.append(data[n])
				n +=1
			else:
				break
		for k in range(0,n):
			data.pop(0)
		#print(scores_list,data,'\n')
		
		G = 0
		F = 0
		P = 0
		for n in scores_list:
			scores = n.split(' ')
			P += int(scores[1])
			F += int(scores[2])
			G += int(scores[3])
		chocolates_scores[name] =  str(P)+' '+str(F)+' '+str(G)
	
	#print(chocolates_scores)
	total_scores_list=[]
	for values in chocolates_scores.values():
		values = values.split(' ')
		G = int(values[2])
		F = int(values[1])
		P = int(values[0])
		total_scores_list.append(G+F+P)
	hightest_scores = sorted(total_scores_list)[len(total_scores_list)-1]
	
	hightest_chocolates_list = []
	for key in chocolates_scores.keys():
		values = chocolates_scores[key].split(' ')
		G = int(values[2])
		F = int(values[1])
		P = int(values[0])
		if hightest_scores == G+F+P:
			hightest_chocolates_list.append(key)
	
	if len(hightest_chocolates_list) == 1:
		print(hightest_chocolates_list[0])
	else:
	
		G_list=[]
		for n in hightest_chocolates_list:
			G_list.append(int(chocolates_scores[n].split(' ')[2]))
		hightest_G = sorted(G_list)[len(G_list)-1]
		
		hightest_G_list=[]
		for key in hightest_chocolates_list:
			values = chocolates_scores[key].split(' ')
			G = int(values[2])
			if hightest_G == G:
				hightest_G_list.append(key)
		#print(hightest_G)
		if len(hightest_G_list) == 1:
			print(hightest_G_list[0])
		else:
			F_list=[]
			for n in hightest_G_list:
				F_list.append(int(chocolates_scores[n].split(' ')[1]))
			hightest_F = sorted(F_list)[len(F_list)-1]
			
			hightest_F_list=[]
			for key in hightest_G_list:
				values = chocolates_scores[key].split(' ')
				F = int(values[1])
				if hightest_F == F:
					hightest_F_list.append(key)
			if len(hightest_F_list) == 1:
				print(hightest_F_list[0])

			else:
				P_list=[]
				for n in hightest_F_list:
					P_list.append(int(chocolates_scores[n].split(' ')[0]))
				hightest_P = sorted(P_list)[len(P_list)-1]
				
				hightest_P_list=[]
				for key in hightest_F_list:
					values = chocolates_scores[key].split(' ')
					P = int(values[0])
					if hightest_P == P:
						hightest_P_list.append(key)
				if len(hightest_P_list) == 1:
					print(hightest_P_list[0])
				else:
					print(','.join(hightest_P_list))
	data.pop(0)