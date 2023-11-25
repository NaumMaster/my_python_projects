import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

a = 3
b = 5
c = 7
d = 11
e = 13
f = 15
g = 19
dot = 21

d1 = 29
d2 = 31
d3 = 33
d4 = 35

GPIO.setup(a, GPIO.OUT, initial=False)
GPIO.setup(b, GPIO.OUT, initial=False)
GPIO.setup(c, GPIO.OUT, initial=False)
GPIO.setup(d, GPIO.OUT, initial=False)
GPIO.setup(e, GPIO.OUT, initial=False)
GPIO.setup(f, GPIO.OUT, initial=False)
GPIO.setup(g, GPIO.OUT, initial=False)
GPIO.setup(dot, GPIO.OUT, initial=False)
GPIO.setup(d1, GPIO.OUT, initial=True)
GPIO.setup(d2, GPIO.OUT, initial=True)
GPIO.setup(d3, GPIO.OUT, initial=True)
GPIO.setup(d4, GPIO.OUT, initial=True)

def zero():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, False)

def one():
    GPIO.output(a, False)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, False)

def two():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, False)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, False)
    GPIO.output(g, True)

def three():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, True)

def four():
    GPIO.output(a, False)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)
    
def five():
    GPIO.output(a, True)
    GPIO.output(b, False)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)

def six():
    GPIO.output(a, True)
    GPIO.output(b, False)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, True)

def seven():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, False)

def eight():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, True)
    GPIO.output(f, True)
    GPIO.output(g, True)

def nine():
    GPIO.output(a, True)
    GPIO.output(b, True)
    GPIO.output(c, True)
    GPIO.output(d, True)
    GPIO.output(e, False)
    GPIO.output(f, True)
    GPIO.output(g, True)

def clear():
    GPIO.output(a, False)
    GPIO.output(b, False)
    GPIO.output(c, False)
    GPIO.output(d, False)
    GPIO.output(e, False)
    GPIO.output(f, False)
    GPIO.output(g, False)
    GPIO.output(dot, False)
    GPIO.output(d1, True)
    GPIO.output(d2, True)
    GPIO.output(d3, True)
    GPIO.output(d4, True)

def twochartime(num):
    if num < 10:
        return f'0{num}'
    else:
        return f'{num}'
    
def chislo_on(num, ind):
    '''Включение числа

    принимает два аргумента
    num - число, которое необходимо отобразить
    ind - позиция секции в которой отображать число
    '''
    clear()
    match num:
        case '0':
            zero()
        case '1':
            one()
        case '2':
            two()
        case '3':
            three()
        case '4':
            four()
        case '5':
            five()
        case '6':
            six()
        case '7':
            seven()
        case '8':
            eight()
        case '9':
            nine()
            
    match str(ind):
        case '0':
            GPIO.output(d1, False)
        case '1':
            GPIO.output(d2, False)
            GPIO.output(dot, True)
        case '2':
            GPIO.output(d3, False)
        case '3':
            GPIO.output(d4, False)
        

def start_animation():
    '''Функция стартовой анимации

    '''
    DELAY = 0.1  
    
    sleep(DELAY)
    GPIO.output(d, True)
    sleep(DELAY)
    GPIO.output(c, True)
    sleep(DELAY)
    GPIO.output(b, True)
    sleep(DELAY)
    GPIO.output(a, True)
    sleep(DELAY)
    GPIO.output(f, True)
    sleep(DELAY)
    GPIO.output(e, True)
    sleep(DELAY*3)
    
def welkom_load():
    for ind in range(4):
        clear()
        match str(ind):
            case '0':
                GPIO.output(d1, False)
                start_animation()
            case '1':
                GPIO.output(d2, False)
                start_animation()
            case '2':
                GPIO.output(d3, False)
                start_animation()
            case '3':
                GPIO.output(d4, False)
                start_animation()
    
welkom_load()
    
while True:
    current_time = datetime.now()
    fourchars = twochartime(current_time.minute) + twochartime(current_time.second)

    for index, chislo in enumerate(fourchars):
        chislo_on(num=chislo, ind=index)
        sleep(0.001)

    
    
