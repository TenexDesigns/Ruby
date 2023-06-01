Symbols in Ruby are lightweight identifiers represented by a colon (:) followed by a name. 
They are immutable, meaning their value remains constant throughout the programs execution.
Symbols are commonly used in Ruby for a variety of purposes, such as representing method names,
keys in hashes, or as unique identifiers.

Here are some examples of how symbols are used in Ruby:

Method Names:

def greet(name)
  puts "Hello, #{name}!"
end

method_name = :greet
send(method_name, "John")
In this example, the symbol :greet represents the name of the method greet. 
  The send method is used to dynamically invoke the method using the symbol as the method name.

Keys in Hashes:

person = {
  name: "John",
  age: 30,
  city: "New York"
}

puts person[:name]  # Output: "John"
In this example, symbols (:name, :age, and :city) are used as keys in a hash. 
Symbols are commonly preferred as keys in hashes because they are immutable and have a unique identity
, making them efficient for hash lookups.

Enumerators:

fruits = %i[apple banana orange]
fruits.each do |fruit|
  puts "I love #{fruit}!"
end
In this example, %i notation is used to define an array of symbols. 
The symbols :apple, :banana, and :orange represent different fruits. 
      The each method is used to iterate over the symbols and print a message for each fruit.

Constants:

MAX_VALUE = 100
puts MAX_VALUE  # Output: 100
Symbols are often used to define constants in Ruby.
In this example, MAX_VALUE is a symbol representing a constant value of 100. 
The symbol is named in uppercase to indicate it as a constant.

Symbols provide a memory-efficient way to represent and refer to identifiers in Ruby.
They are commonly used in scenarios where identity and immutability are desired, 
such as method names, hash keys, enumerators, and constants.
Using symbols can improve performance and readability in certain situations,
especially when dealing with large datasets or frequently accessed identifiers.








88 WHY ARE COLONS USED ON DIFFRENT SIDE
*********************************************************************************
The usage of colons on different sides (:set_task vs. only: [:show, :edit]) is a result of the syntax conventions
in Ruby and Ruby on Rails. The symbol syntax using a colon (:) before the symbol name is a common convention in Ruby, 
while the hash notation with a colon (:) followed by the key and value is a common convention in Ruby on Rails.

The code

class TasksController < ApplicationController
  before_action :set_task, only: [:show, :edit]

  def show
  end

  def edit
  end

  def set_task
  end
end



MORE EXPLANTION

**********************************************

The code snippet provided is a simplified example of a Rails controller, specifically the TasksController. 
Lets go through the code and explain the different parts:


class TasksController < ApplicationController
  before_action :set_task, only: [:show, :edit]

  def show
  end

  def edit
  end

  def set_task
  end
end


Class Definition: The code starts with the declaration of the TasksController class, which inherits from ApplicationController.
  In Rails, controllers handle the logic and actions for a specific model or resource.

before_action: This is a Rails callback method that specifies a method to be executed before specific controller actions.
  In this case, the before_action is used to set up the set_task method to run before the show and edit actions.

:set_task: This is a symbol representing the method name set_task. Symbols in Ruby are lightweight identifiers 
    and are commonly used in Rails for referring to method names, keys in hashes, or other identifiers.

only: [:show, :edit]: This is a hash option passed to the before_action method.
    It specifies that the set_task method should only be invoked before the show and edit actions. The symbols :show and :edit represent the names of the actions in the controller.

Regarding the syntax used for :set_task and only: [:show, :edit]:

:set_task is a symbol representing the method name. It is preceded by a colon (:) to indicate that it is a symbol.

only: [:show, :edit] is a hash notation, where only is the key and [:show, :edit] is the value. 
  The square brackets [] are used to define an array of symbols representing the actions to which the set_task 
  method should be applied.

The usage of colons on different sides (:set_task vs. only: [:show, :edit]) is a result of the syntax conventions 
in Ruby and Ruby on Rails. The symbol syntax using a colon (:) before the symbol name is a common convention in Ruby, 
while the hash notation with a colon (:) followed by the key and value is a common convention in Ruby on Rails.




















