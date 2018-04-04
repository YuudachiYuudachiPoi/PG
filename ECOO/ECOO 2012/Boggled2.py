# -*- coding: cp936 -*-
f = open('C:\Users\XiLI\OneDrive\文档\编程\ECOO 2012\DATA42.txt','r')
all = f.read()
data = all.split('\n')
f.close
def is_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

for n in range(0,len(data)):
  g=0
  f=0
  s=0
  r=0
  mark=0
  
  if is_num(data[n]):
    boxs = data[n-4:n]
    words = data[n+1:n+1+int(data[n])]
    #print words
    for k in range(0,len(words)):

      nbox = ['1,1','1,2','2,1','2,2']#x照y
      for l in range(0,len(words[k])):#辨别words
        kbox = []
        for z in range(0,len(nbox)):
          x= int(nbox[z][0])
          y= int(nbox[z][2])
          for bx in range(-1,2):
            if x+bx<0 or x+bx>3:
              continue
            for by in range(-1,2):
              if y+by<0 or y+by>3:
                continue
              if words[k][l] == boxs[x+bx][y+by]:
                kbox.append('%.0f,'%(x+bx) +'%.0f'%(y+by))
        if kbox==[]:
          f+=1
          break
        nbox = kbox
      if kbox==[]:
        test=100
      else:
        for p in range(k+1,len(words)): #repeated
          if words[k] == words[p]:
            r += 1
            break
        else:
          if len(words[k])<3: #too short
            s+=1
            continue
          if len(words[k])==3 or len(words[k])==4:#3 or 4
            mark+=1
            g+=1
            continue
          if len(words[k])==5:#5
            mark+=2
            g+=1
            continue
          if len(words[k])==6:#6
            mark+=3
            g+=1
            continue
          if len(words[k])==7:#7
            mark+=4
            g+=1
            continue
          if len(words[k])>7:#more than 7
            mark+=11             
            g+=1
            continue
    print 'your score: %.0f'% mark + '(%.0f good, '%g + '%.0f not found, '%f + '%.0f too short, '%s + '%.0f repeated)'% r
     
