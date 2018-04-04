import math
f = open ('DATA30.txt','r')
all = f.read()
data = all.split("\r\n")
for n in range(0,5):
  lines = data[n].split(" ")
  px = float(lines[0])
  py = float(lines[1])
  angle = math.atan(py/px)
  if px>=0 and py>0:
    angle = angle
  if px<0 and py>=0:
    angle = math.pi+angle
  if px<=0 and py<0:
    angle = (math.pi)+angle
  if px>0 and py<0:
    angle = 2*(math.pi)+angle
  l = math.hypot(py,px)
  angleA = (2.0/3)*math.pi + angle
  Ay = l*math.sin(angleA)
  Ax = l*math.cos(angleA)
  
  angleB = angle - (1.0/3)*math.pi
  By = l*math.sin(angleB)
  Bx = l*math.cos(angleB)
  
  angleC = angle + (1.0/6)*math.pi
  Cy = l*(3**0.5)*math.sin(angleC)
  Cx = l*(3**0.5)*math.cos(angleC)
  print '(%.1f,'%Ax + '%.1f) '%Ay + '(%.1f,'%Bx + '%.1f) '%By + '(%.1f,'%Cx + '%.1f) '%Cy
