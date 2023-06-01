Ruby is often considered a "pure" object-oriented language because in Ruby, everything is an object.
Every value, including numbers, strings, and even classes, is an object with associated methods and properties.
This design philosophy makes Ruby consistent and uniform in its approach to programming.

In contrast, languages like C and C++ are not purely object-oriented.
While they have support for object-oriented programming, they also allow procedural programming and have primitive types
that are not objects. In C and C++, primitive types like integers and characters are not objects 
and dont have associated methods or properties.

Rubys object-oriented nature means that even basic operations like arithmetic are performed using methods.
For example, in Ruby, adding two numbers is done using the + method of the numeric object. 
This concept extends to all aspects of Ruby programming, allowing for a more consistent and expressive coding style.

Regarding arrays, in Ruby, arrays can store any data type because Rubys arrays are implemented as objects
and can hold a mixture of different types. You can store numbers, strings, objects, or even other arrays within a Ruby array.
This flexibility is achieved because each element of a Ruby array is an object in itself.

In languages like C++, arrays have a fixed type, meaning they can only store elements of a specific data type.
If you declare an array of integers in C++, you can only store integers in that array. 
If you want to store different types of data, you would need to use separate arrays or create a custom data structure.

In programming, an array is a data structure that allows you to store a collection of elements in a sequential manner.
Arrays typically have a fixed size, which is defined at the time of declaration. 
You can access individual elements of an array using an index, which represents the position of the element in the array.

Heres an example of using an array in Ruby:


numbers = [1, 2, 3, 4, 5]  # Creating an array of integers
puts numbers[2]  # Output: 3

names = ["Alice", "Bob", "Charlie"]  # Creating an array of strings
puts names[1]  # Output: Bob

mixed = [1, "hello", true]  # Creating an array of mixed data types
puts mixed[0]  # Output: 1
puts mixed[1]  # Output: hello
puts mixed[2]  # Output: true
In the above example, we have an array called numbers that stores integers,
an array called names that stores strings, and an array called mixed that stores a mix of integers,
strings, and a boolean value. Rubys array allows us to store and access elements of different types within a single array.

Overall, Rubys pure object-oriented nature and the flexibility of its arrays make it a powerful and expressive
language for developing a wide range of applications.





