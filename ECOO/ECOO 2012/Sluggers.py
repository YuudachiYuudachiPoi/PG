f = open ('C:\Users\XILi\OneDrive\ÎÄµµ\±à³Ì\ECOO 2012\DATA12.txt','r')
all = f.readlines()
f.close
print all[0],
print '==========================='
Tba = 0
Tsa = 0
for n in range (1,11):
  line = all[n].split(' ')
  B = float(line[5])
  C = float(line[6])
  D = float(line[7])
  F = float(line[4])
  E = int(line[2])
  A = F - B - C - D
  ba = F/E
  sa = (A+2*B+3*C+4*D)/E
  Jba = '%.3f'%ba
  Jsa = '%.3f'%sa
  print line[0]+':'+' '+Jba[1:5]+' '+Jsa[1:5]
  Tba += ba
  Tsa += sa
AVba = '%.3f'%(Tba/10)
AVsa = '%.3f'%(Tsa/10)
print '==========================='
print 'Big 10 Av:',
print AVba[1:5],
print AVsa[1:5]
