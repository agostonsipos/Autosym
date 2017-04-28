from dualnumber import *
from parseExpr import parseExpr

operations = {"exp": exp, "log": log, "sin": sin, "cos": cos, "tan": tan, "cot": cot, "asin": asin, "acos": acos, "atan": atan, "acot": acot, "sqrt": sqrt, "abs": abs}

while(1):

  cmd = raw_input("> ")

  if(cmd == "diff"):
    fun = raw_input("Give an expression! ")
    var = raw_input("Differentiate by this variable: ")

    env = parseExpr(fun, var, set(operations))
    env.update(operations)

    try:

      exec "__value = "+fun in env

      print(env["__value"].ipart().str)

    except BaseException as err:
      print("Error happened: " + format(err))

  elif(cmd == "help"):
    print("This program differentiates mathematical expressions. Type `diff`.")
    print("\tVariables should be sequences of noncapital letters.")
    print("\tAvailable operations: ")
    print("\t\t+, -, *, /, **")
    print("\t\t"+str(sorted(list(operations))))

  elif(cmd == "quit"):
    break
