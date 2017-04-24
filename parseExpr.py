import re
import dualnumber as d
import codegen as c

def parseExpr(str, var, reserved):
  variables = {}
  regex = "[a-z]+"
  varlist = re.findall(regex, str)
  varlist = set(varlist) - reserved
  for v in varlist:
    variables[v] = d.Dualnumber(c.codegen(v), c.codegen("1") if (v == var) else c.codegen("0"))
  return variables
