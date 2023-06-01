Hash methods in Ruby are used to manipulate and interact with hashes. Some common hash methods include:

Hash#initialize: Creates a new hash.
hash = Hash.new(0) # Creates a new hash with default value 0
Hash#[]=: Sets the value for a key.
hash[:key] = "value"
Hash#[]: Retrieves the value for a key.
value = hash[:key] # Returns the value associated with the key "key"
Hash#delete: Removes a key-value pair from the hash.
hash.delete(:key) # Removes the key-value pair with key "key"
Hash#clear: Removes all key-value pairs from the hash.
hash.clear # Removes all key-value pairs from the hash
Hash#key?: Checks if a key exists in the hash.
hash.key?(:key) # Returns true if the key "key" exists in the hash
Hash#values: Returns an array of all the values in the hash.
values = hash.values # Returns an array of all the values in the hash
Hash#keys: Returns an array of all the keys in the hash.
keys = hash.keys # Returns an array of all the keys in the hash
Hash#each: Iterates over each key-value pair in the hash.
hash.each { |key, value| puts "#{key}: #{value}" }
Hash#each_pair: Iterates over each key-value pair in the hash, yielding both the key and the value.
hash.each_pair { |key, value| puts "#{key}: #{value}" }
Hash#each_key: Iterates over each key in the hash.
hash.each_key { |key| puts key }
Hash#each_value: Iterates over each value in the hash.
hash.each_value { |value| puts value }
Hash#map: Creates a new hash with the results of calling a block on each key-value pair.
hash = {a: 1, b: 2, c: 3}
result = hash.map { |key, value| [key, value * 2] }
# result is now {a: 2, b: 4, c: 6}
Hash#reject: Creates a new hash with all key-value pairs for which the block returns false.
hash = {a: 1, b: 2, c: 3}
result = hash.reject { |key, value| value < 2 }
# result is now {b: 2, c: 3}
These are some of the common hash methods in Ruby that you can use to interact with and manipulate hashes






More Explantion
********************************************************************


  
  Certainly! Here are some common methods available for manipulating and accessing hashes in Ruby, along with code samples explaining their usage:

[] or fetch:
These methods retrieve the value associated with a specific key in a hash.

person = { name: "John", age: 30 }

puts person[:name]         # Output: John
puts person.fetch(:age)    # Output: 30
[]=
This method assigns a value to a specific key in a hash or creates a new key-value pair if the key doesnt exist.

person = {}
person[:name] = "John"

puts person     # Output: {:name=>"John"}
keys and values:
These methods return an array containing all the keys or values in a hash, respectively.

person = { name: "John", age: 30 }

puts person.keys      # Output: [:name, :age]
puts person.values    # Output: ["John", 30]
key? or has_key?:
These methods check if a specific key exists in a hash.
ruby
Copy code
person = { name: "John", age: 30 }

puts person.key?(:name)        # Output: true
puts person.has_key?(:address) # Output: false
delete:
This method removes a key-value pair from a hash and returns the corresponding value.

person = { name: "John", age: 30 }

age = person.delete(:age)

puts person     # Output: {:name=>"John"}
puts age        # Output: 30
length or size:
These methods return the number of key-value pairs in a hash.

person = { name: "John", age: 30 }

puts person.length    # Output: 2
puts person.size      # Output: 2
merge:
This method combines two hashes, creating a new hash with the merged contents.

person = { name: "John", age: 30 }
additional_info = { city: "New York", occupation: "Engineer" }

merged_hash = person.merge(additional_info)

puts merged_hash     # Output: {:name=>"John", :age=>30, :city=>"New York", :occupation=>"Engineer"}
These are just a few examples of the methods available for working with hashes in Ruby.
There are many more methods to explore, each providing different functionalities for manipulating, 
accessing, and transforming hashes.























