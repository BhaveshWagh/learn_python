def car_information(manufacturer, model, *color):
    """"MAKE A DICTIONARY ABOUT CAR """
    information = {"manufacturer":manufacturer, "model:":model, "features": color }
    print(f"\n car information: \n{information}")
    return information

about_car = car_information('Subaru', 'outback', 'color: blue',)
about_car = car_information('Audi', 'Audi: R8','color: black')
about_car = car_information('Honda', 'Honda: City', 'color: white')



