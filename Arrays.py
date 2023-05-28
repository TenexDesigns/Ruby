In Ruby, an array is an ordered collection of objects. 
It can hold multiple elements of any type, such as numbers, strings, or even other arrays.
Heres an explanation of arrays in Ruby with code samples:

Creating Arrays:

Arrays can be created using square brackets ([]) or the Array.new constructor.
Example:

fruits = ['apple', 'banana', 'orange']   # Array of strings

numbers = [1, 2, 3, 4, 5]                # Array of integers

mixed = [1, 'apple', true]               # Array of mixed data types

empty_array = []                         # Empty array



Accessing Elements:

Elements in an array are accessed using their index, which starts from 0.
You can retrieve an element using square bracket notation ([]).
Example:

fruits = ['apple', 'banana', 'orange']

puts fruits[0]       # Output: apple

puts fruits[1]       # Output: banana






Modifying Elements:

You can modify an element in an array by assigning a new value to a specific index.
Example:

fruits = ['apple', 'banana', 'orange']

fruits[1] = 'grape'
puts fruits.inspect   # Output: ["apple", "grape", "orange"]






Array Methods:

Ruby provides a rich set of methods to work with arrays, such as push, pop, shift,
unshift, concat, join, sort, and many more.
Example:

fruits = ['apple', 'banana', 'orange']

fruits.push('mango')         # Add element to the end of the array

fruits.pop                   # Remove the last element from the array

first_fruit = fruits.shift   # Remove and return the first element

fruits.unshift('kiwi')       # Add element to the beginning of the array

fruit_string = fruits.join(', ')   # Convert array to a string

sorted_fruits = fruits.sort   # Sort the array in ascending order






Array Length:

The length or size methods can be used to determine the length of an array.
Example:

fruits = ['apple', 'banana', 'orange']

puts fruits.length      # Output: 3

puts fruits.size        # Output: 3
These are some basic operations and methods you can perform with arrays in Ruby.
Arrays are versatile data structures that allow you to store and manipulate collections of objects efficiently.





MORE EXPLANTION
****************************************************************************************************************************


Arrays in Ruby are ordered, integer-indexed collections of any object. 
They can store multiple values in a single variable and can contain any data type, 
including numbers, strings, and other Ruby objects digitalocean.com, tutorialspoint.com.

Here are some examples and explanations of common array methods in Ruby:

Creating an Array: You can create an array using square brackets [] or the Array.new method:
array1 = [1, 2, 3, 4]
array2 = Array.new(3) { |i| i + 1 }
Accessing Array Elements: You can access individual elements in an array using their index:
array = [0, 1, 2, 3, 4]
puts array[0] # Output: 0
puts array[1] # Output: 1
Iterating Over an Array: You can use the each method to iterate over the elements in an array:
array.each { |element| puts element }
Adding Elements to an Array: You can add elements to an array using the push method:
array.push(5)
puts array.last # Output: 5
Removing Elements from an Array: You can remove elements from an array using the pop, shift, or delete methods:
array.pop # Output: 5 (removes the last element)
array.shift # Output: [0, 1, 2, 3] (removes the first element)
array.delete(1) # Output: [0, 2, 3, 4] (removes the element at index 1)
Sorting an Array: You can sort an array using the sort method:
array.sort # Output: [0, 1, 2, 3, 4] (returns a new sorted array)
Reversing an Array: You can reverse an array using the reverse method:
array.reverse # Output: [4, 3, 2, 1, 0] (returns a new reversed array)
Searching for an Element: You can search for an element in an array using the include? method:
array.include?(3) # Output: true (returns true if the element is found, false otherwise)
These are just a few examples of working with arrays in Ruby. You can find more methods and examples in the provided sources
































































































































...
