class Test:
    pass
 
a = Test()
 
for xx in range(97, 123):
    t = chr(xx) + '=Test()'
    print (t)
    exec(t)
 
print (a)
print (z)