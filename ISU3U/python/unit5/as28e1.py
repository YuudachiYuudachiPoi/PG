pop_wilno = 500
pop_bbay = 1500
year = 0

print("Barry's Bay  Willno")
print('%.2f'%pop_bbay,'%.2f'%pop_wilno)
while pop_bbay >= pop_wilno:
    pop_bbay += pop_bbay*0.02
    pop_wilno += pop_wilno*0.1
    print('%.2f'%pop_bbay,'%.2f'%pop_wilno)