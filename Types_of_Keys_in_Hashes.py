In Ruby, a hash is a data structure that stores a collection of key-value pairs.
It allows you to associate values (the "values") with corresponding keys. 
Hashes are commonly used to represent structured data or to store and retrieve data in an organized manner. 
Heres an explanation of hashes in Ruby, along with examples of different types of keys and accessing the values:

Creating a Hash:
You can create a hash in Ruby using the curly braces {} or the Hash.new constructor.

# Using curly braces
person = { "name" => "John", "age" => 30 }

# Using Hash.new
person = Hash.new
person["name"] = "John"
person["age"] = 30


Types of Keys:
In Ruby, hashes can use various types of keys, including:
  
String Keys: These are enclosed in double quotes or single quotes.
Symbol Keys: These start with a colon (:) and are often used for efficiency and readability.
Numeric Keys: These can be integers or floats.
  

# String keys
person = { "name" => "John", "age" => 30 }

# Symbol keys
person = { name: "John", age: 30 }

# Numeric keys
grades = { 1: "A", 2: "B", 3: "C" }



Accessing Values:
  
You can access values from a hash using the keys. The syntax for accessing values depends on the type of key used.

person = { "name" => "John", "age" => 30 }

puts person["name"]  # Output: John
puts person["age"]   # Output: 30

person = { name: "John", age: 30 }

puts person[:name]   # Output: John
puts person[:age]    # Output: 30

grades = { 1 => "A", 2 => "B", 3 => "C" }

puts grades[1]       # Output: A
puts grades[2]       # Output: B


In the above examples, the values are accessed by providing the corresponding key within square brackets ([]).
The correct syntax depends on the type of key used: string keys are accessed using quotes, symbol keys are accessed using colons,
  and numeric keys are accessed directly.

Its worth noting that Ruby offers various methods for manipulating and accessing hashes, 
such as hash[key], hash[key] = value, hash.key?(key), hash.keys, hash.values, and more.
These methods provide flexibility for working with hashes and retrieving values based on different key types.

Overall, hashes in Ruby are versatile data structures that allow you to organize and retrieve data using key-value pairs. 
The choice of key type depends on your specific use case and the requirements of your program.








MORE EXPLANTION
*************************************************************************************************************


Hashes in Ruby are a data structure that allows you to organize information in key-value pairs. 
Each key in a hash is unique and is associated with a corresponding value webcodestack.com.
Hashes can have keys of different types, such as strings, symbols, and numbers altcademy.com.

Here are some examples of how to create and access hashes with different types of keys:

String keys:
grades = { "Mark" => 15, "Jimmy" => 10, "Jack" => 10 }
puts grades["Mark"]  # Output: 15
Symbol keys:
grades = { :Mark => 15, :Jimmy => 10, :Jack => 10 }
puts grades[:Mark]  # Output: 15
Number keys:
grades = { 1 => 15, 2 => 10, 3 => 10 }
puts grades[1]  # Output: 15
To access the hash values, you can use the corresponding key, 
whether its a string, symbol, or number. In Ruby 1.9 and later, you can use a more succinct syntax 
for constructing hashes with symbol keys odinschool.com:

grades = { Mark: 15, Jimmy: 10, Jack: 10 }
puts grades[:Mark]  # Output: 15
In summary, hashes in Ruby can have keys of different types, such as strings, 
symbols, and numbers. You can create and access hashes using these different key types, 
and Ruby offers a more succinct syntax for constructing hashes with symbol keys in Ruby 1.9 and later.





































































































































..
