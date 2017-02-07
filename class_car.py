class Car(object):


    def __init__(self, car_name='General', car_model='GM' ,car_type='honda' ):
        self.car_type = car_type
        self.model = car_model
        self.name = car_name
        self.speed = 0

        if car_name== 'Porshe' or car_name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def doors(self, num_of_doors):
        pass

    def drive(self, moving_man):
        return moving_man

    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed

        return self

    def wheels(self, number_of_wheels):
        return number_of_wheels


    def is_saloon(self):
        if self.car_type == 'trailer':
            return False
        else:
            return True
