In Ruby, variables can hold different types of values, and the type of a variable is determined 
dynamically based on the value assigned to it. Ruby is a dynamically-typed language,
meaning you dont need to explicitly declare the type of a variable. Here are the common types of variables in Ruby:

Local Variables:
Local variables begin with a lowercase letter or an underscore (_). They have a local scope and
are accessible only within the block, method, or class where they are defined.

Example:


name = "John"
age = 30
Instance Variables:
Instance variables begin with a single @ character. They are used within classes and can be accessed by 
any instance method of the class. Instance variables have a different value for each instance (object) of the class.

Example:


class Person
  def initialize(name)
    @name = name
  end

  def greet
    puts "Hello, #{@name}!"
  end
end

person = Person.new("John")
person.greet
Class Variables:
Class variables begin with @@ and are shared among all instances of a class and its subclasses.
They are accessible within the class and its subclasses.

Example:


class Person
  @@count = 0

  def initialize
    @@count += 1
  end

  def self.total_count
    @@count
  end
end

person1 = Person.new
person2 = Person.new
puts Person.total_count  # Output: 2

Global Variables:
Global variables begin with a dollar sign ($) and have a global scope, accessible from anywhere in the program. 
However, they are generally avoided as they can lead to naming conflicts and make code harder to maintain.

Example:


$global_variable = 10

def some_method
  puts $global_variable
end

some_method  # Output: 10



Constants:
Constants begin with an uppercase letter and are used to represent fixed values that should not be
changed during the execution of the program. They have a lexical scope and can be accessed from 
anywhere within the scope in which they are defined.

Example:


MY_CONSTANT = 100

def print_constant
  puts MY_CONSTANT
end

print_constant  # Output: 100
These are the most commonly used variable types in Ruby. Its important to note that Ruby supports
dynamic typing, allowing variables to hold different types of values throughout their lifetime.






















































































































...
