
Loop 

A loop the repetitve excution of a chunk of code for a given amount of repetions or until a certain condtiton is met

Loop is almost avalilabe in all programing languages




In programming, a loop is a control structure that allows you to repeatedly execute a block of code.
It enables you to perform iterative tasks, such as iterating over a collection, executing code a specific number of times,
or running code until a certain condition is met. Ruby provides several ways to execute loops:




while loop:

The while loop executes a block of code repeatedly as long as a given condition is true.

counter = 0

while counter < 5 do
  puts counter
  counter += 1
end




until loop:

The until loop executes a block of code repeatedly until a given condition becomes true.

counter = 0

until counter == 5 do
  puts counter
  counter += 1
end




for loop:

The for loop iterates over a range, an array, or any object that responds to the each method.

for i in 0..4 do
  puts i
end

# Alternatively, using a range object directly
(0..4).each do |i|
  puts i
end




.times loop:

The .times loop executes a block of code a specified number of times.

5.times do |i|
  puts i
end




.each loop:


The .each loop iterates over an enumerable object, such as an array or a hash,
and executes a block of code for each element.

fruits = ["apple", "banana", "orange"]

fruits.each do |fruit|
  puts fruit
end






.loop:
The .loop method creates an infinite loop that can be exited using a break statement.

counter = 0

loop do
  puts counter
  counter += 1
  break if counter == 5
end
These are

some of the ways to execute loops in Ruby. Each loop construct has its own use cases and can be combined
with conditional statements, iterators, and other control structures to perform specific tasks. 
Loops provide a powerful mechanism for automating repetitive operations and iterating over collections in Ruby.



















