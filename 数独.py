import time
f = open('C:\sd2.txt','r')
all = f.read()
data = all.split('\n')
f.close
poi=1
start = time.time()
while poi==1:
	for num in range(1,10): #宫摒除法
		for y in range(0,3):
			for x in range(0,3):
				have = 0
				for sy in range(y*3,y*3+3):
					for sx in range(x*3,x*3+3):
						if data[sy][sx]=='%d'%num:
							have = 1
				if have == 1:
					continue	  
				abbox = []
				for p in range(0,3):
					for k in range(0,3):
						if data[y*3+k][x*3+p]=='-':
							abbox.append('%d,'%p + '%d'%k)
				for sy in range(0,3):
					for sss in range(0,9):
						if data[y*3+sy][sss] == '%d'%num:
							for p in range(0,3):
								if ('%d,'%p + '%d'%sy) in abbox:
									abbox.remove('%d,'%p + '%d'%sy)
				for sx in range(0,3):
					for qwe in range(0,9):
						if data[qwe][x*3+sx] == '%d'%num:
							for k in range(0,3):
								if ('%d,'%sx + '%d'%k) in abbox:
									abbox.remove('%d,'%sx + '%d'%k)
				if len(abbox)==1:
					sx = int(abbox[0][0])
					sy = int(abbox[0][2])
					t = list(data[y*3+sy])
					t[x*3+sx] = '%d'%num
					data[y*3+sy]=''.join(t)
				
	for y in range(0,9): # 余数法
		for x in range(0,9):
			if data[y][x]=='-':
				noab = []
				find = [1,2,3,4,5,6,7,8,9] 
				for n in range(0,9):
					if data[y][n]!='-':
						noab.append(data[y][n])
				for n in range(0,9):
					if data[n][x]!='-':
						noab.append(data[n][x])
				for sy in range((y//3)*3,(y//3)*3+3):
					for sx in range((x//3)*3,(x//3)*3+3):
						if data[sy][sx]!='-':
							noab.append(data[sy][sx])
				for n in noab:
					if int(n) in find:
						find.remove(int(n))
				if len(find)==1:
					t = list(data[y])
					t[x]= '%d'%find[0]
					data[y]=''.join(t)

	for y in range(0,9): #行摒除法
		for num in range(1,10):
			abbox=[]
			for sx in range(0,9):
				if data[y][sx]=='-':
					abbox.append(sx)
			tt=[]
			find=abbox
			if str(num) in list(data[y]):
				continue
			for n in abbox:
				for sy in range(0,9):
					if data[sy][n]==str(num):
						tt.append(n)
			for n in abbox:
				for sx in range((n//3)*3,(n//3)*3+3):
					for sy in range((y//3)*3,(y//3)*3+3):
						if data[sy][sx]==str(num):
							tt.append(n)
			for n in tt:
				if n in find:
					find.remove(n)
			if len(find)==1:
				break
		if len(find)==1:
			t = list(data[y])
			t[find[0]]= '%d'%num
			data[y]=''.join(t)
#	print('bug ',data)			
	for x in range(0,9):  #列摒除法(有bug）
		for num in range(0,9):
			abbox=[]
			for sy in range(0,9):
				if data[sy][x]=='-':
					abbox.append(sy)
			if abbox==[]:
				continue
			tt=[]
			pp=[]
			find=abbox
			for sy in range(0,9):
				pp.append(data[sy][x])
			if str(num) in pp:
				continue
			for n in abbox:
				for sx in range(0,9):
					if data[n][sx]==str(num):
						tt.append(n)
			for n in abbox:
				for sy in range((n//3)*3,(n//3)*3+3):
					for sx in range((x//3)*3,(x//3)*3+3):
						if data[sy][sx]==str(num):
							tt.append(n)
#			print(abbox)
			for n in tt:
				if n in find:
					find.remove(n)
			if len(find)==1:
				break
#		if len(find)==1:
#			t = list(data[find[0]])
#			t[x] = '%d'%num
#			data[find[0]]=''.join(t)
#	print(data)
	poi=0 #检查完成度
	for n in range(0,9):
		for q in range(0,9):
			if data[n][q]=='-':
				poi=1
	
	end = time.time() #超时计算
	if end-start >= 5:
		print('timeout')
		break
for n in range(0,9): #输出
	print(data[n])