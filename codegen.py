def is_zero(x):
  return str(x) == "0" or str(x) == "0.0"
def is_one(x):
  return str(x) == "1" or str(x) == "1.0"

class codegen:
  def __init__(self, s):
    if(type(s) is str):
      self.str = s
    else:
      self.str = str(s)

  def __str__(self):
    return self.str

  def __eq__(a, b):
    return a.str == b.str

  def __neg__(a):
    if(is_zero(a)):
      return a
    else:
      return codegen("(-"+a.str+")")

  def __add__(a, b):
    if(is_zero(a)):
      return b
    elif(is_zero(b)):
      return a
    elif(a == b):
      return codegen(2)*a
    else:
      return codegen("("+a.str+"+"+b.str+")")

  def __sub__(a, b):
    if(is_zero(a)):
      return codegen("-"+b.str)
    elif(is_zero(b)):
      return a
    elif(a == b):
      return codegen(0)
    else:
      return codegen("("+a.str+"-"+b.str+")")

  def __mul__(a, b):
    if(is_zero(a) or is_zero(b)):
      return codegen(0)
    elif(is_one(b)):
      return a
    elif(is_one(a)):
      return b
    elif(a == b):
      return a**codegen(2)
    else:
      return codegen("("+a.str+"*"+b.str+")")

  def __div__(a, b):
    if(is_zero(a)):
      return codegen(0)
    elif(is_zero(b)):
      raise(ZeroDivisionError("division by zero"))
    elif(is_one(b)):
      return a
    elif(a == b):
      return codegen(1)
    else:
      return codegen("("+a.str+"/"+b.str+")")

  def __pow__(a, b):
    if(is_zero(a) or is_one(a) or is_one(b)):
      return a
    elif(is_zero(b)):
      return codegen(1)
    else:
      return codegen("("+a.str+"**"+b.str+")")

  def exp(a):
    return codegen("exp("+a.str+")")

  def log(a):
    return codegen("log("+a.str+")")

  def sin(a):
    return codegen("sin("+a.str+")")

  def cos(a):
    return codegen("cos("+a.str+")")

  def tan(a):
    return codegen("tan("+a.str+")")

  def cot(a):
    return codegen("cot("+a.str+")")

  def asin(a):
    return codegen("asin("+a.str+")")

  def acos(a):
    return codegen("acos("+a.str+")")

  def atan(a):
    return codegen("atan("+a.str+")")

  def acot(a):
    return codegen("acot("+a.str+")")

  def sqrt(a):
    return codegen("sqrt("+a.str+")")

  def abs(a):
    return codegen("abs("+a.str+")")

  def sgn(a):
    return codegen("sgn("+a.str+")")
