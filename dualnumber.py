import codegen as c

def dualnumberify(a):
  if((type(a) is int) or type(a) is float):
    return Dualnumber(c.codegen(a), c.codegen("0"))
  else:
    return a

class Dualnumber:
  def __init__(self, a, b):
    self.x = a
    self.y = b

  def __str__(self):
    return "Dualnumber: ("+self.x.str+","+self.y.str+")"

  def realpart(self):
    return self.x
  def ipart(self):
    return self.y

  def __add__(a, b):
    b = dualnumberify(b)
    return Dualnumber(a.x+b.x, a.y+b.y)
  def __radd__(a, b):
    b = dualnumberify(b)
    return Dualnumber(a.x+b.x, a.y+b.y)


  def __sub__(a, b):
    b = dualnumberify(b)
    return Dualnumber(a.x-b.x, a.y-b.y)
  def __rsub__(a, b):
    b = dualnumberify(b)
    return Dualnumber(b.x-a.x, b.y-a.y)

  def __mul__(a, b):
    b = dualnumberify(b)
    return Dualnumber(a.x*b.x, a.x*b.y+a.y*b.x)
  def __rmul__(a, b):
    b = dualnumberify(b)
    return Dualnumber(a.x*b.x, a.x*b.y+a.y*b.x)

  def __div__(a, b):
    b = dualnumberify(b)
    return Dualnumber(a.x / b.x, (a.y*b.x - a.x*b.y) / (b.x*b.x))
  def __rdiv__(a, b):
    b = dualnumberify(b)
    return Dualnumber(b.x / a.x, (b.y*a.x - b.x*a.y) / (a.x*a.x))


  def __pow__(a, b):
    b = dualnumberify(b)
    return Dualnumber(pow(a.x, b.x), a.y*b.x*pow(a.x, (b.x - c.codegen(1))) + pow(a.x, b.x) * a.x.log() * b.y);
  def __rpow__(a, b):
    b = dualnumberify(b)
    return Dualnumber(pow(b.x, a.x), b.y*a.x*pow(b.x, (a.x - c.codegen(1))) + pow(b.x, a.x) * b.x.log() * a.y);

def exp(a):
  return Dualnumber(a.x.exp(), a.y*a.x.exp())

def log(a):
  return Dualnumber(a.x.log(), a.y/a.x)

def sin(a):
  return Dualnumber(a.x.sin(), a.y*a.x.cos())

def cos(a):
  return Dualnumber(a.x.cos(), -a.y*a.x.sin())

def tan(a):
  return Dualnumber(a.x.tan(), a.y/(a.x.cos()**c.codegen(2)))

def cot(a):
  return Dualnumber(a.x.cot(), a.y/(a.y.sin()**c.codegen(2)))

def asin(a):
  return Dualnumber(a.x.asin(), a.y/(c.codegen(1)-a.x**c.codegen(2)).sqrt())

def acos(a):
  return Dualnumber(a.x.acos(), -a.y/(c.codegen(1)-a.x**c.codegen(2)).sqrt())

def atan(a):
  return Dualnumber(a.x.atan(), a.y/(c.codegen(1)+a.x**c.codegen(2)))

def acot(a):
  return Dualnumber(a.x.acot(), -a.y/(c.codegen(1)+a.x**c.codegen(2)))

def sqrt(a):
  return Dualnumber(a.x.sqrt(), a.y/(c.codegen(2)*a.x.sqrt()))

def abs(a):
  return Dualnumber(a.x.abs(), a.x.sgn()*a.y)
