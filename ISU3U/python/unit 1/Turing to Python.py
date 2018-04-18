#var apples :int
#put "How many apples did you buy? "
#get apples
#put "Your cost is $",0.25*apples

apples = int(input('How many apples did you buy? '))
print('Your cost is $'+str(0.25*apples))