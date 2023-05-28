In Ruby, inheritance allows you to create a new class based on an existing class,
inheriting its attributes and behaviors. This promotes code reuse and allows you to create specialized classes 
that inherit and extend the functionality of their parent classes. 
Heres an explanation of inheritance and method overriding in Ruby with code samples:

Inheritance:

To create a subclass that inherits from a superclass, you use the < symbol followed by the name of the superclass.
Example:

class Animal
  def speak
    puts "Animal speaks."
  end
end

class Dog < Animal
  def bark
    puts "Dog barks."
  end
end





Method Inheritance:

Subclasses inherit all the methods defined in their superclass.
They can use those methods directly or override them with their own implementations.

Example:

class Animal
  def speak
    puts "Animal speaks."
  end
end

class Dog < Animal
  def bark
    puts "Dog barks."
  end
end

animal = Animal.new
animal.speak  # Output: "Animal speaks."

dog = Dog.new
dog.speak     # Output: "Animal speaks."
dog.bark      # Output: "Dog barks."





Method Overriding:

Method overriding allows a subclass to provide its own implementation of a method inherited from the superclass. 
This allows for customization and specialization.
Example:

class Animal
  def speak
    puts "Animal speaks."
  end
end

class Dog < Animal
  def speak
    puts "Dog barks."
  end
end

animal = Animal.new
animal.speak  # Output: "Animal speaks."

dog = Dog.new
dog.speak     # Output: "Dog barks."

Inheritance and method overriding enable you to build hierarchies of classes,
where subclasses inherit and extend the behavior of their parent classes. 
This helps in organizing code, promoting code reuse, and achieving polymorphism.
Subclasses can have their own unique behaviors while inheriting and reusing common functionalities defined in their superclasses.









MORE EXPLANTION
********************************************************************************************************************************



Object methods in Ruby are methods that are defined within a class but are not directly associated with an object.
Instead, they are associated with the class itself. 
These methods can be used to perform operations on the class or to maintain state information for the class geeksforgeeks.org.

Here's an example using a Person class with a class method:

class Person
  def initialize(name, age, sex)
    @name = name
    @age = age
    @sex = sex
  end

  def display_person
    puts "The name of the person is #{@name} and age is #{@age} also he is a #{@sex}"
  end

  def self.greater_than(other_person, attribute)
    @age > other_person.instance_variable_get(:@age)
  end
end

person1 = Person.new("John", 30, "male")
person2 = Person.new("Jane", 25, "female")

puts person1.greater_than(person2, :age) # => true
In this example, we define a class method greater_than within the Person class.
This method compares the age of self (the calling object) with the age of the other_person object passed as an argument. 
The instance_variable_get method is used to access the @age instance variable of the other_person object stackoverflow.com.

For more information and examples, you can refer to the provided sources










MORE EXPLANTION
********************************************************************************************************************************



Sure, object methods in Ruby are functions that are defined within a class and can be called on objects of that class.
They are used to perform actions on the object, such as changing its state or returning information about it.

Here is an example of an object method:

Ruby
class Person
  def initialize(name)
    @name = name
  end

  def say_hello
    puts "Hello, #{name}"
  end
end
Use code with caution. Learn more
In this example, the say_hello method is defined within the Person class. 
It takes no arguments and returns nothing. When an object of the Person class is created,
the say_hello method can be called on it. For example:

Ruby
person = Person.new("John Doe")
person.say_hello # => Hello, John Doe
Use code with caution. Learn more
The say_hello method is an example of an instance method. 
Instance methods are methods that are defined within a class and can only be called on objects of that class.

There are also class methods, which are methods that are defined within a class and can be called on the class itself.
Class methods are prefixed with the self keyword. For example:

Ruby
class Person
  def self.all
    # This method returns an array of all Person objects
  end
end

Person.all # => [Person(name: "John Doe"), Person(name: "Jane Doe")]
Use code with caution. Learn more
Object methods are a powerful way to add functionality to your classes.
They can be used to perform actions on objects, change their state, or return information about them.

Here are some additional things to note about object methods:

Object methods are defined within a class.
Object methods can take arguments and return values.
Object methods can be called on objects of the class they are defined in.
Object methods can be called on the class itself.
I hope this helps!
































































































































































































..p
