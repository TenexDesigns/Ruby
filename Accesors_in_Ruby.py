
In Ruby, accessors are methods that provide a way to read or modify the value of an objects instance variables. 
They allow controlled access to an objects state, encapsulating the data and providing methods to interact with it. 
There are three types of accessors in Ruby: attr_reader, attr_writer, and attr_accessor.

  
Typers of accesors

attr_reader
attr_writer
attr_accesor
  
  
  
attr_reader:

Definition: attr_reader creates a getter method to access the value of an instance variable.
Usage: It is used when you want to provide read-only access to an instance variable.
Example:

class Person
  attr_reader :name

  def initialize(name)
    @name = name
  end
end

person = Person.new("John")
puts person.name  # Output: John







attr_writer:

Definition: attr_writer creates a setter method to modify the value of an instance variable.
Usage: It is used when you want to provide write-only access to an instance variable.
Example:

class Person
  attr_writer :name

  def initialize(name)
    @name = name
  end
end

person = Person.new("John")
person.name = "Alice"




attr_accessor:

Definition: attr_accessor creates both getter and setter methods for an instance variable.
Usage: It is used when you want to provide read and write access to an instance variable.
Example:

class Person
  attr_accessor :name

  def initialize(name)
    @name = name
  end
end

person = Person.new("John")
puts person.name  # Output: John
person.name = "Alice"
Accessors simplify the process of accessing and modifying object attributes, promoting encapsulation and object-oriented design principles. They provide a clean and consistent way to interact with instance variables, encapsulating the implementation details within the class.

It's worth noting that while attr_reader, attr_writer, and attr_accessor are convenient shorthand methods, you can also define custom getter and setter methods explicitly. This gives you more control over the behavior and validation of the attributes.

In addition to instance variables, accessors can be used with class variables and global variables as well, using the same attr_* methods within the context of a class or module.






























































































...
