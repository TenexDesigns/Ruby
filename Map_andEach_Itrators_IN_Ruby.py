Iterators in Ruby are methods that allow you to iterate over elements in a collection, such as arrays or hashes geeksforgeeks.org. 
They provide a more readable and functional way to work with collections of data,
allowing you to perform operations on each element in the collection without using explicit loops 





1..each:
The .each method is used to iterate over an enumerable object, such as an array or a hash. 
It executes a block of code for each element, passing each element as a parameter.

fruits = ["apple", "banana", "orange"]

fruits.each do |fruit|
  puts fruit
end




2..map or .collect:
The .map method applies a block of code to each element of an enumerable object and returns 
a new array containing the results.

numbers = [1, 2, 3, 4, 5]

squared_numbers = numbers.map do |num|
  num * num
end

puts squared_numbers






















































































































...
