f = open ('DATA20.txt','r')
all = f.read()
data = all.split("\r\n")
f.close()
for n in range(0,5):
  lines = data[n].split('TATAAT')
  #print lines
  finds = lines[1][4:]
  l= len(finds)
  for a in range(0,l):
    teo = finds[a:a+6]
    #print teo
    py = teo[::-1].replace('A','1').replace('T','2').replace('C','3').replace('G','4')
    tet = py.replace('1','T').replace('2','A').replace('3','G').replace('4','C')
    p=finds[a+7:].find(tet)
    if p>0:
      break
  #print finds[0:a]
  rep = finds[0:a].replace('G','1').replace('A','2').replace('T','3').replace('C','4')
  re = rep.replace('1','C').replace('2','U').replace('3','A').replace('4','G')
  print re
