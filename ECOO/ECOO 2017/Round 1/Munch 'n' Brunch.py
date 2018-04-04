f = open('C:\\Users\XiLI\OneDrive\文档\编程\ECOO\ECOO 2017\Round 1\DATA\DATA11.txt','r')
data = f.read().split('\n')
for loop_time in range(0,10):

	cost = int(data[loop_time*3])
	percentages = data[loop_time*3+1].split(' ')
	for n in range(0,4):
		 percentages[n]= float(percentages[n])
	number_of_student = int(data[loop_time*3+2])
	
	year_one = int(number_of_student * percentages[0])
	year_two = int(number_of_student * percentages[1])
	year_three = int(number_of_student * percentages[2])
	year_four = int(number_of_student * percentages[3])
	
	tcost = 0.5*(year_one*12 + year_two*10 + year_three*7 + year_four*5)
	if tcost>=cost:
		print('NO')
	else:
		print('YES')