Modules is a group of methods put togeter .
This methods module can be in the same file or in an excternal file

1.IF IN THE SAME FILE- 
Use the includes method and the module name
The use the dot module name to access the methods in the module.

INDEX,rb


module Tools
    def cook()
      puts "Yoo George am Cooking "
    end
  end
  

include Tools

Tools.cook()




2. IF THE MODULE IS IN A DIFFERENT FILE THERE ARE TWO WAYS OF IMPORTIN  THE MODULE
    (A) USING ABSOLUTE PATH
         E.G
        require('D:\ruby\ruby1\MODULE.rb')


          include Tools

          Tools.cook()

      (B) USING RELATIVE PATH
      
      require_relative('./MODULE.rb')


           include Tools

           Tools.cook()







MORE EXPLANTION
***********************************************************************************************************************

In Ruby, modules are used to package and organize related methods, constants, and classes. 
They provide a way to group similar functionalities and make them available for reuse in different parts of the program. 
Heres an explanation of modules in Ruby, how to import them using require and require_relative, and how to use the include statement:

  
  
  
  
  
Creating a Module:

To define a module, you use the module keyword followed by the module name. Inside the module,
you can define methods, constants, and classes.
Example:

module MathUtils
  PI = 3.14159

  def self.double(num)
    num * 2
  end

  def square(num)
    num * num
  end
end






Importing a Module using require:

The require statement is used to load and import a module from an external file.
It searches for the module in Ruby's load path.
Example:

require 'math_utils'
puts MathUtils::PI
puts MathUtils.double(5)










Importing a Module using require_relative:

The require_relative statement is used to load and import a module from a relative path
. It allows you to specify the path relative to the current file.
Example:

require_relative 'math_utils'
puts MathUtils::PI
puts MathUtils.double(5)








Using include to Mix in a Module:

The include statement is used to mix in the methods and constants from a module into a class or another module,
making them available for use.
Example:

module MathUtils
  def square(num)
    num * num
  end
end

class Calculator
  include MathUtils
end

calculator = Calculator.new
puts calculator.square(5)






Differences between require and require_relative:

require is used to load modules from Rubys load path, while require_relative is used to load modules from a relative path.
require is typically used for loading core Ruby libraries or external gems, while require_relative is used for
loading modules within your project.
Example:

require 'date'                   # Loads the core 'date' library
require_relative 'my_module'     # Loads 'my_module.rb' from the same directory as the current file
Modules in Ruby help organize and encapsulate related code, promote code reuse, and avoid naming conflicts.
They allow you to separate concerns and make your code more modular and maintainable. 
Importing modules using require and require_relative allows you to access the functionalities defined in those modules.
The include statement is used to mix in module methods and constants into classes or other modules.










MORE EXPLANTION
***********************************************************************************************************************



Modules in Ruby are used to organize and separate code. They can be used to group related methods, classes, and constants. To import a module, you can use the require or require_relative methods.

require is used to load an external file, usually a gem or a file from another project. It also ensures that the file is loaded only once.

require_relative is used to load a file from the same directory as the current file. It is useful for loading files that are part of the same project.

Here's an example of using require and require_relative:

# File: utils.rb
module Utils
  def greet(name)
    "Hello, #{name}!"
  end
end

# File: main.rb
require 'utils'

puts Utils.greet('John') # => Hello, John!

# File: project_root/lib.rb
require_relative 'lib/utils'

puts Utils.greet('Jane') # => Hello, Jane!
In this example, we have a Utils module that provides a greet method. We use require to load the utils.rb file in the main.rb file, and require_relative to load the same file in the lib.rb file, which is in the same directory as the main.rb file.

The include method is used to bring the methods of a module into a class. This is useful for extending a class with the methods of another module.

Here's an example of using include:

module A
  def say_hello
    puts "Hello, #{name}!"
  end
end

class Person
  include A

  def initialize(name)
    @name = name
  end

  def greet
    say_hello
  end
end

person = Person.new('John')
person.greet # => Hello, John!
In this example, we include the A module in the Person class using the include method. This makes the say_hello method available as an instance method of the Person class stackoverflow.com.

In summary, require and require_relative are used to import modules from external files or from the same directory, respectively. The include method is used to bring the methods of a module into a class, extending the class with the methods of the module.













MORE EXPLANTION
--------------------------------------------------


Sure, modules in Ruby are a way to group together related constants, methods, and classes. They can be used to organize code and make it easier to reuse.

To import a module in Ruby, you can use the require or require_relative keyword.

The require keyword imports a module from the current directory or from a path specified by the -I flag. For example, to import the Math module:

Ruby
require 'math'
Use code with caution. Learn more
The require_relative keyword imports a module from the directory that the current file is in. For example, to import the MyModule module:

Ruby
require_relative 'my_module'
Use code with caution. Learn more
Once a module has been imported, its constants, methods, and classes can be accessed using the module's name. For example, to access the pi constant from the Math module:

Ruby
pi = Math::pi
Use code with caution. Learn more
To access the add method from the MyModule module:

Code snippet
result = MyModule.add(1, 2)
Use code with caution. Learn more
To access the Person class from the MyModule module:

Code snippet
person = MyModule::Person.new
Use code with caution. Learn more
Modules can also be used to mixin functionality into classes. To do this, you use the include keyword. For example, to mixin the Enumerable module into the MyClass class:

Ruby
class MyClass
  include Enumerable
end
Use code with caution. Learn more
Once a module has been included in a class, its methods can be called on objects of that class. For example:

Ruby
my_object = MyClass.new
my_object.each { |element| puts element }
Use code with caution. Learn more
The require and require_relative keywords are similar, but there are some key differences.

The require keyword will always look for the module in the current directory or in the directories specified by the -I flag. The require_relative keyword will only look for the module in the directory that the current file is in.

The require keyword will also raise an error if the module cannot be found. The require_relative keyword will not raise an error if the module cannot be found.

Here is a table summarizing the differences between require and require_relative:

Keyword	Description
require	Imports a module from the current directory or from a path specified by the -I flag.
require_relative	Imports a module from the directory that the current file is in.
require	Will raise an error if the module cannot be found.
require_relative	Will not raise an error if the module cannot be found.
I hope this helps!














