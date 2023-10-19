unless statement:
The unless statement executes a block of code if a given condition is false.

temperature = 25

unless temperature > 30
  puts "It's not too hot."
else
  puts "It's hot outside!"
end
Output:

Its not too hot.




In Ruby, the unless statement is used to execute a block of code if a given condition is false. 
It is the opposite of the if statement, which executes a block of code if a condition is true.
Heres an explanation of unless compared to if with code samples:

if statement:
The if statement executes a block of code if a given condition is true.

temperature = 25

if temperature > 30
  puts "It's hot outside!"
else
  puts "It's not too hot."
end
Output:


Its not too hot.








In the above examples, both if and unless statements check the condition temperature > 30.
In the if statement, the block of code executes when the condition is true, so it outputs "It's not too hot." 
In the unless statement, the block of code executes when the condition is false, so it also outputs "It's not too hot."

The choice between using if and unless depends on the clarity and readability of your code. Typically, 
if is used when you want to execute a block of code when a condition is true, and unless is used when you want 
to execute a block of code when a condition is false. Both if and unless can be combined with else and elsif to
handle multiple conditions.

Its important to note that you can achieve the same result with an if statement by negating the condition. 
However, using unless can make your code more readable and expressive, especially when the negative condition reads more naturally.
















































































...
