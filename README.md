# Autosym
Symbolic differentiation using automatic differentiation

This tool differentiates mathematical expressions symbolically. It can parse the following grammar:

 * \<formula\> ::= \<var\>|\<formula\>\<op\>\<formula\>|\<unary\>(\<formula\>)  
 * \<var\>     ::= [a-z]+  
 * \<op\>      ::= + | - | * | / | **  
 * \<unary\>   ::= "exp" | "log" | "sin" | "cos" | "tan" | "cot" | "asin" | "acos" | "atan" | "acot" | "sqrt" | "abs"  
 
Differentiation can be done by any \<var\> that is (or is not) in the formula.
 
After evaluating it generates a formula for the derivative with a similar syntax and prints it. The formula is not necessarily in its simplest form.
 
The theory behind the program is [automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation), done not on the field of numbers, but on formulas. (roughly described, I intend to write about it in detail)
