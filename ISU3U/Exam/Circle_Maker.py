def main():
    import math
    print('Circle Maker Hard')
    print()

    go = True
    while go:
        try:
            radius = int(input('What is the radius of the circle (5-100)? '))
        except:
            pass
        else:
            if radius in range(5,101):
                go = False

    units = ''
    while len(units) == 0:
        units = input('What are the units for your circle? ')
    
    colour = ''
    while len(colour) == 0:
        colour = input('What is the colour of your circle? ')

    #----------------------------------------------
    print()

    diameter = radius*2
    print('The diameter of the',colour,'circle is',diameter,units+'.')

    circumference = diameter * math.pi
    print('The circumference of the circle is %.1f'%circumference,units+'.')

    area = radius**2 * math.pi
    print('The area of the circle is %.1f'%area,units,'squared.')