#constraint based programming language

#Description of the primitives of the programming language:

#connectors:
#   carry a value, either numeric or undefined
#   
#constraints, the functions of the language:
#   take in connectors as their arguments.
#   Whenever all but one of the connectors have a defined value,
#   finds the remaining value using the information.
#
#   primitives:
#   con (a,c)   //   a=c
#   add (a,b,c) // a+b=c
#   sub (a,b,c) // a-b=c
#   mul (a,b,c) // a*b=c
#   div (a,b,c) // a/b=c
#   pow (a,b,c) // a^b=c
#   log (a,b,c) // log_a(b) = c
#   
#implementation
#   Whenever a constraint is called on connectors
#   1: add a proc to the connectors
#   2: whenever a proc is added to a connector, or whenever a
#      connector tries to change value, it calls all procs in
#      its actions list.
#   3: a 'connector proc' consists of the following:
#      i)  check all related connectors.
#      iia) if n-1 of them are defined, set the remaining
#      iib) if <n-1 of them are defined, do nothing.
class InvalidConstraint(Exception):
    pass

class Connector():
    def __init__(self, val = None):
        self.val = val
        self.action_list = []
        
    def addAction(self, action):
        self.action_list.append(action)
        action()
        
    def setValue(self, val):
        #set value, call function list.
        self.val = val

        for x in self.action_list:
            x()

def con(a: Connector, c):
    a.setValue(c)

def add(a,b,c):
    def f():
        if   a.val == None and b.val == None and c.val == None:
            pass
        elif a.val == None and b.val == None and c.val != None:
            pass
        elif a.val == None and b.val != None and c.val == None:
            pass
        elif a.val != None and b.val == None and c.val == None:
            pass
        elif a.val != None and b.val != None and c.val == None:
            c.setValue(a.val + b.val)
        elif a.val != None and b.val == None and c.val != None:
            b.setValue(c.val - a.val)
        elif a.val == None and b.val != None and c.val != None:
            a.setValue(c.val - b.val)
        else:
            if a.val + b.val != c.val:
                raise InvalidConstraint()
        
    a.addAction(f)
    b.addAction(f)
    c.addAction(f)

def sub(a,b,c):
    add(b,c,a)
    
def mul(a,b,c):
    def f():
        if   a.val == None and b.val == None and c.val == None:
            pass
        elif a.val == None and b.val == None and c.val != None:
            pass
        elif a.val == None and b.val != None and c.val == None:
            pass
        elif a.val != None and b.val == None and c.val == None:
            pass
        elif a.val != None and b.val != None and c.val == None:
            c.setValue(a.val * b.val)
        elif a.val != None and b.val == None and c.val != None:
            b.setValue(c.val / a.val)
        elif a.val == None and b.val != None and c.val != None:
            a.setValue(c.val / b.val)
        else:
            if a.val * b.val != c.val:
                raise InvalidConstraint()
        
    a.addAction(f)
    b.addAction(f)
    c.addAction(f)
    
def div(a,b,c):
    mul(b,c,a)

def celciusToFahrenheit(c,f):
    #5*c = 9*(F-32)

    w = Connector()
    x = Connector()
    y = Connector()
    u = Connector()
    v = Connector()
    
    con(w, 9)
    con(x, 5)
    con(y, 32)

    mul(c,w,u)
    mul(x,v,u)
    add(v,y,f)

#testing
a = Connector()
b = Connector()
c = Connector()
d = Connector()
e = Connector()

celciusToFahrenheit(a,b)

