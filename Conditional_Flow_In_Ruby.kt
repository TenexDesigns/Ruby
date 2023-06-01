Condtional blocks or flow are used to amke decsions basd on certain conadiions



CONDITIONAL BLOCKS IN RUBY

if
if..else
if...elsif
unless
unless...else
enless...elsif
when...case




Conditional flow or blocks in Ruby allow you to control the flow of your code based on certain conditions.
They help you make decisions and execute specific blocks of code based on whether a condition evaluates to true or false.
There are several ways to implement conditional flow in Ruby:

if statement:

The if statement executes a block of code if a given condition is true.

if condition
  # Code to execute if the condition is true
else
  # Code to execute if the condition is false
end








unless statement:

The unless statement is the opposite of if. It executes a block of code if a given condition is false.

unless condition
  # Code to execute if the condition is false
else
  # Code to execute if the condition is true
end





elsif statement:

The elsif statement allows you to provide multiple conditions to be checked sequentially.
It is used in combination with if or unless.

if condition1
  # Code to execute if condition1 is true
elsif condition2
  # Code to execute if condition2 is true
else
  # Code to execute if none of the conditions are true
end





case statement:

The case statement is used when you have multiple conditions to evaluate against a single value or expression.

case expression
when value1
  # Code to execute if expression matches value1
when value2
  # Code to execute if expression matches value2
else
  # Code to execute if none of the values match expression
end



Ternary operators:

Ternary operators are used to evaluate a condition and return one of two values,
depending on whether the condition is met or not. The syntax for a ternary operator is as follows:


condition ? value_if_true : value_if_false



Conditional flow is a fundamental concept in programming. It is used in all programming languages,
including Ruby. By understanding how conditional flow works, you can write more readable, maintainable, and efficient programs.





Conditional flow is used to handle different scenarios and make decisions in your program.
It allows you to control the execution path based on specific conditions. 
This can be useful for implementing business logic, handling user input, error handling,
and many other scenarios. By using conditional flow, you can create more dynamic and responsive
programs that adapt their behavior based on different conditions and inputs.
























