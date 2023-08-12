# Ex 1
class Employee: 
    def __init__(self,employee_name,employee_position):
        self.name = employee_name 
        self.position = employee_position
    def say_hi (self):
        print (f'Hi, my name is {self.name}.')
    def tell_position (self):
        print (f'I am a {self.position}.')
nameInput = input ('Input a MindX employee: ')
posInput = input ('Input his/her position: ')
result = Employee (nameInput, posInput)
result.say_hi ()
result.tell_position ()

# Ex 2
print ('-- Consider Pi number = 3.14 --')

class Circle: 
    def __init__ (self,circle_radius):
        self.rad = circle_radius
    def perimeter (self):
        print ('=> Perimeter: ',self.rad *2*3.14)
    def area (self):
        print ('=> Area: ',self.rad**2*3.14)

class Rectangle: 
    def __init__ (self,rectangle_length, rectangle_width):
        self.length = rectangle_length
        self.width = rectangle_width
    def perimeter (self):
        print ('=> Perimeter: ',(self.length + self.width) *2 )
    def area (self):
        print ('=> Area: ',self.length * self.width)

shapeInput = input ('Shape (Rectangle/Circle): ')
if shapeInput == 'Circle':
    radInput = float(input ('Radius: '))
    output = Circle (radInput)
    output.perimeter ()
    output.area ()
elif shapeInput == 'Rectangle':
    lenInput = float (input ('Length: '))
    widInput = float (input ('Width: '))
    output = Rectangle (lenInput, widInput)
    output.perimeter ()
    output.area ()
else: 
    print ('=> Invalid!')
    
# Ex3
# Em chưa hiểu tại sao cái %d lại màu xanh ạ 
from datetime import datetime
class CustomeDate:
    def get_date (str_date):
        now_date = datetime.now()
        date_format = '%d/%m/%y'
        now_date.strftime ('%d/%m/%y') 
        print (now_date)
    def get_time (now_time):
        now_time = datetime.now()
        now_time.strftime ('%H:%M:%S')
        print (now_time)

today = CustomeDate ()
today.get_date ()
today.get_time ()

# Ex4 
from datetime import datetime
class DateHandler ():
    def __init__ (self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def format_date(self):
        return (f'{self.year}/{self.month}/{self.day}')
    
    def get_days_between (date1,date2):
         print (f'Days between: {(date1 - date2).days}')

start = DateHandler(2020,1,1)
end = DateHandler (2021,1,1)
print ('Start:',DateHandler.format_date(start))
print ('End:',DateHandler.format_date (end))
start_day = datetime (2020,1,1)
end_day = datetime (2021,1,1)
DateHandler.get_days_between (end_day,start_day)

           
        
        
    
    
        