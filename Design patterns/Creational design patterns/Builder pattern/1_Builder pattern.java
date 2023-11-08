
The builder pattern is a design pattern that allows objects to be constructed gradually and step-by-step. It is also known as the "telescoping constructor pattern" because it allows you to build complex objects by nesting constructors.

The builder pattern is useful when you need to create objects with many different configurations or when you want to separate the creation of an object from its representation.

Problem

Consider the following class for creating a user:

Ruby
class User
  def initialize(name, email, address)
    @name = name
    @email = email
    @address = address
  end
end
Use code with caution. Learn more
Creating a new user with this class requires passing all three parameters to the constructor. This can become cumbersome if you need to create users with different configurations, such as users without addresses or users with different email addresses.

Solution

The builder pattern can be used to solve this problem by creating a builder class for the user. The builder class will have a method for each of the attributes of the user, and each method will return the builder object itself. This allows you to chain together method calls to create a user object with the desired configuration.

Here is an example of a builder class for the user:

Ruby
class UserBuilder
  def initialize
    @name = nil
    @email = nil
    @address = nil
  end

  def with_name(name)
    @name = name
    self
  end

  def with_email(email)
    @email = email
    self
  end

  def with_address(address)
    @address = address
    self
  end

  def build
    User.new(@name, @email, @address)
  end
end
Use code with caution. Learn more
To create a new user with this builder class, you can call the with_name, with_email, and with_address methods to set the desired values, and then call the build method to create the user object.

Here is an example of how to create a new user with the builder class:

Ruby
user = UserBuilder.new
  .with_name('John Doe')
  .with_email('johndoe@example.com')
  .build
Use code with caution. Learn more
When to use the builder pattern

The builder pattern is a good choice when:

You need to create objects with many different configurations.
You want to separate the creation of an object from its representation.
You want to make the creation of objects more readable and maintainable.
Code samples

Here is an example of how to use the builder pattern to create a car object:

Ruby
class Car
  attr_accessor :engine, :chassis, :body

  def initialize(engine, chassis, body)
    @engine = engine
    @chassis = chassis
    @body = body
  end
end

class Engine
  attr_accessor :type, :horsepower

  def initialize(type, horsepower)
    @type = type
    @horsepower = horsepower
  end
end

class Chassis
  attr_accessor :model, :material

  def initialize(model, material)
    @model = model
    @material = material
  end
end

class Body
  attr_accessor :color, :style

  def initialize(color, style)
    @color = color
    @style = style
  end
end

class CarBuilder
  def initialize
    @engine = nil
    @chassis = nil
    @body = nil
  end

  def with_engine(type, horsepower)
    @engine = Engine.new(type, horsepower)
    self
  end

  def with_chassis(model, material)
    @chassis = Chassis.new(model, material)
    self
  end

  def with_body(color, style)
    @body = Body.new(color, style)
    self
  end

  def build
    Car.new(@engine, @chassis, @body)
  end
end

car = CarBuilder.new
  .with_engine('V8', 300)
  .with_chassis('Model X', 'Steel')
  .with_body('Red', 'Sports')
  .build
Use code with caution. Learn more
This code creates a new car object with a V8 engine, a Model X chassis, and a red sports body.

Conclusion

The builder pattern is a powerful design pattern that can be used to make code more readable, maintainable, and flexible.



  ...
