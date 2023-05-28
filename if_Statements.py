In Ruby, if statements are used to conditionally execute blocks of code based on a certain condition. 
They allow you to control the flow of your program by making decisions.
Heres an explanation of if statements in Ruby with code samples:

Basic if Statement:

The most basic form of an if statement checks a condition and executes a block of code if the condition is true.
Example:

if condition
  # Code to execute if condition is true
end




if-else Statement:

An if-else statement allows you to execute different code blocks based on whether the condition is true or false.
Example:

if condition
  # Code to execute if condition is true
else
  # Code to execute if condition is false
end





if-elsif-else Statement:

The if-elsif-else statement allows you to check multiple conditions and execute different code blocks based on the outcome.
Example:

if condition1
  # Code to execute if condition1 is true
elsif condition2
  # Code to execute if condition2 is true
else
  # Code to execute if all conditions are false
end





Conditional Expressions:

In Ruby, you can use various conditional expressions within if statements,
such as comparison operators (<, >, ==, etc.) and logical operators (&&, ||, !).
Example:

if x > 5 && y < 10
  # Code to execute if both conditions are true
end





Nested if Statements:

You can nest if statements inside one another to handle more complex conditions.
Example:

if condition1
  if condition2
    # Code to execute if both conditions are true
  else
    # Code to execute if condition2 is false
  end
else
  # Code to execute if condition1 is false
end
if statements provide a way to control the execution of your code based on specific conditions.
They allow you to make decisions and handle different scenarios. 
You can use comparison operators, logical operators, and nested statements to construct more complex conditions.




MORE EXPLANTION
**************************************************************************************************************************************


In Ruby, if statements are used to execute a block of code only if a certain condition is met.
They are a fundamental part of controlling the flow of your program. Heres a simple example of an if statement:

age = 18

if age >= 18
  puts "You are an adult."
else
  puts "You are not an adult."
end
In this example, the program checks if the value of age is greater than or equal to 18.
If the condition is true, it prints "You are an adult." Otherwise, it prints "You are not an adult."

You can also use elsif to check multiple conditions:

score = 85

if score >= 90
  puts "Grade: A"
elsif score >= 80
  puts "Grade: B"
elsif score >= 70
  puts "Grade: C"
else
  puts "Grade: F"
end
In this example, the program checks the value of score and prints the corresponding grade based on the conditions.

Ruby also supports the unless statement, which is the opposite of the if statement. 
It executes a block of code only if the condition is false:

number = 11

unless number == 5
  puts "Number is not 5"
else
  puts "Number is 5"
end
In this example, the unless statement checks if the number is not equal to 5.
If the condition is false, it prints "Number is 5." Otherwise, it prints "Number is not 5."

You can also use if and unless as modifiers for single lines of code:

puts "The condition is true" if true
puts "The condition is false" unless true
These are some examples of if and unless statements in Ruby.
For more information and examples, you can refer to the provided sources





































































































































































































































































..
