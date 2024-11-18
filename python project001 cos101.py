def area_of_triangle():
    lenght1 = int(input('enter a number    '))
    length2 = int(input('enter a number    '))
    area_2 = '1/2' * height * breath
    print(area_2)
    
def pressure_formula():
    force = int(input('enter the force  '))
    area = int(input('enter the area  '))
    pressure = force/area
    print(pressure)
    
def area_of_rectangle():
    height = int(input('enter a number    '))
    breadth = int(input('enter a number   '))
    area_5 = breadth * height
    print(area_5)
    
def density_formula():
    mass = int(input('enter the mass'))
    volume = int(input('enter the volume'))
    density = mass/volume
    print(density)
    
def capacitance_formula():
    quantity = int(input('enter the quantity'))
    voltage = int(input('enter the voltage'))
    capacitance = quantity/voltage
    print(capacitance)
    
    options = input("enter a letter   ")
    
if options == "a":
   area_of_triangle()
elif options == 'b':
    pressure_formula()
elif options == 'c':
    area_of_rectangle()
elif options == 'd':
    density_formula()
elif options == 'e':
    capacitance_formula()
else:
    print('letter is invalid')



    
    
    