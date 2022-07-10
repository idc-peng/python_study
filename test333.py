try :
    10/0
except ZeroDivisionError as e:
    print(e)
    
try :
    a = 'a'
    b = 1
    a + b
except ZeroDivisionError as e:
    print(e)
