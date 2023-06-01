In Ruby, there are several ways to iterate over a hash and perform operations on its key-value pairs. 
Here are some common methods to iterate over a hash:

each Method:
The each method allows you to iterate over a hash by providing a block of code to be executed for each key-value pair.

person = { name: "John", age: 30 }

person.each do |key, value|
  puts "#{key}: #{value}"
end
Output:

makefile
Copy code
name: John
age: 30
each_key and each_value Methods:
If you only need to iterate over either the keys or the values of a hash, you can use the each_key or each_value methods.

person = { name: "John", age: 30 }

person.each_key do |key|
  puts key
end

person.each_value do |value|
  puts value
end
Output:

Copy code
name
age
John
30
each_pair Method:
The each_pair method is similar to each but provides a more explicit way to iterate over key-value pairs.
ruby
Copy code
person = { name: "John", age: 30 }

person.each_pair do |key, value|
  puts "#{key}: #{value}"
end
Output:

makefile
Copy code
name: John
age: 30
each_with_index Method:
If you need to access both the key and value along with their index, you can use the each_with_index method.
ruby
Copy code
person = { name: "John", age: 30 }

person.each_with_index do |(key, value), index|
  puts "#{index + 1}. #{key}: #{value}"
end
Output:

markdown
Copy code
1. name: John
2. age: 30
map or collect Method:
If you want to transform the hash into a new array based on some operation, you can use the map or collect method.
ruby
Copy code
person = { name: "John", age: 30 }

modified_values = person.map do |key, value|
  "#{key}: #{value}"
end

puts modified_values
Output:

css
Copy code
["name: John", "age: 30"]
These are just a few examples of the methods available for iterating over a hash in Ruby. Depending on your specific needs, 
you can choose the method that best suits your requirements and perform the desired operations on the key-value pairs of the hash.
