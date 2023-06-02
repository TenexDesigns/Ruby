By using super, you can leverage and extend the functionality provided 
by the superclass while adding or overriding specific behavior in the subclass.


MORE EXPLANATION
***********************************************************************************************************************


In Ruby, the super keyword is used to call a method on the parent class with the same name as the method that calls super. 
When a method is called with super, Ruby looks for a method with the same name in the superclass of the current 
class and calls that method.

Here are some common uses of the super keyword in Ruby:

Calling a method with the same name from the superclass: When a method is overridden in a subclass,
  the super keyword can be used to call the original method from the superclass. 
  This can be useful when you want to add some behavior to the method in the subclass, 
  but still want to call the original behavior from the superclass. For example:
    
  class Animal
    def speak
      puts "Hello!"
    end
  end
  
  class Dog < Animal
    def speak
      super
      puts "Woof!"
    end
  end
  
  dog = Dog.new
  dog.speak
  # Output:
  # Hello!
  # Woof!
In this example, the Dog class overrides the speak method from the Animal class,
but still calls the original speak method from the Animal class using the super keyword. 
This allows the Dog class to add some behavior to the speak method without completely replacing it.

Passing arguments to the parent method: When calling a method with super,
  any arguments passed to the current method are automatically passed to the parent method.
  This can be useful when you want to pass some arguments to the parent method, 
but still add some behavior in the current method. For example:
  
  class Animal
    def speak(message)
      puts "#{message}!"
    end
  end
  
  class Dog < Animal
    def speak(message)
      super("Hello, #{message}")
      puts "Woof!"
    end
  end
  
  dog = Dog.new
  dog.speak("world")
  # Output:
  # Hello, world!
  # Woof!
In this example, the Dog class overrides the speak method from the Animal class and adds 
some behavior by prefixing the message with "Hello, ". The super keyword is used to call the original 
speak method from the Animal class and pass the modified message.

Using super with parentheses: When calling a method with super, 
  you can use parentheses to explicitly indicate that no arguments should be passed to the parent method.
  This can be useful when the current method takes arguments that are not needed in the parent method. For example:
    
  class Animal
    def speak
      puts "Hello!"
    end
  end
  
  class Dog < Animal
    def speak(message)
      super()
      puts "#{message} says Woof!"
    end
  end
  
  dog = Dog.new
  dog.speak("Rover")
  # Output:
  # Hello!
  # Rover says Woof!
In this example, the Dog class overrides the speak method from the Animal class and takes an extra argument message.
The super keyword is used with parentheses to call the original speak method from the Animal class without passing any arguments.

In summary, the super keyword in Ruby is used to call a method on the parent class with the same name as the method that calls super.
It can be used to call the original method from the superclass, pass arguments to the parent method, and indicate that 
no arguments should be passed to the parent method.



MORE EXPLANATION
***********************************************************************************************************************

In Ruby, the super keyword is used to call a method with the same name from the superclass.
It allows you to invoke and override the behavior of the superclasss method while providing additional
functionality in the subclass. Heres an example to demonstrate the usage of super:


class Vehicle
  def initialize(make, model)
    @make = make
    @model = model
  end

  def start_engine
    puts "Starting the engine."
  end
end

class Car < Vehicle
  def initialize(make, model, year)
    super(make, model)
    @year = year
  end

  def start_engine
    super
    puts "Warming up the engine."
  end
end

car = Car.new("Toyota", "Camry", 2022)
car.start_engine
In this example, we have a Vehicle superclass and a Car subclass that inherits from Vehicle.
The Vehicle class has an initialize method to set the make and model attributes,
and a start_engine method to output a simple message.

The Car class extends Vehicle and overrides the initialize method to include an additional year attribute. 
It also overrides the start_engine method to call the superclasss start_engine method using super and then adds its own behavior.

When we create a Car object and invoke the start_engine method, the following output is generated:

Copy code
Starting the engine.
Warming up the engine.
Here's how super works in this example:

In the Car classs initialize method, super(make, model) is called to invoke the initialize method of 
the superclass (Vehicle). This passes the make and model arguments to the superclasss initialize method,
allowing the superclass to set those attributes.

In the Car classs start_engine method, super is called to invoke the start_engine method of the superclass. 
This outputs the "Starting the engine." message defined in the Vehicle class.

After the super call, the Car class adds its own behavior by outputting the "Warming up the engine." message.

By using super, you can call the superclasss implementation of a method from within the subclass, 
allowing you to extend or modify the behavior while retaining the core functionality defined in the superclass.




























































































































...
