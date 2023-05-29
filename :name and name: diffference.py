There is no difference between name: and :name in Ruby. Both are valid ways to specify a symbol.
    A symbol is a data type that represents a name. Symbols are immutable,
    which means that they cannot be changed once they have been created. Symbols are often used as keys in hash tables.

In Ruby, symbols can be created using either the :name syntax or the name: syntax. 
    The :name syntax is the older syntax, and it is still supported in Ruby. 
      However, the name: syntax is the preferred syntax, and it is the syntax that is used in most Ruby code.

Here is an example of how to create a symbol using the :name syntax:

Ruby
name = :name
Use code with caution. Learn more
Here is an example of how to create a symbol using the name: syntax:

Ruby
name = "name".to_sym
Use code with caution. Learn more
The to_sym method converts a string to a symbol.

In Ruby, symbols are often used as keys in hash tables.
A hash table is a data structure that maps keys to values. When you use a symbol as a key in a hash table, 
the hash table will use the symbol's name to look up the value.

Here is an example of how to use a symbol as a key in a hash table:

Ruby
hash = {}

hash[:name] = "John Doe"

puts hash[:name]
Use code with caution. Learn more
This code will print the following output:

Code snippet
John Doe
Use code with caution. Learn more
As you can see, the hash table was able to look up the value for the key name using the symbol's name.
