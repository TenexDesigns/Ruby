IRB (Interactive Ruby) is a command-line tool that provides an interactive environment for running Ruby code and experimenting with Ruby expressions, methods, and objects. It's a valuable tool for learning Ruby, testing code snippets, debugging, and exploring Ruby's features and libraries.

Here's how you can use IRB and some examples:

1. **Starting IRB**:
   To start IRB, open your command prompt or terminal and simply type `irb` followed by the Enter key. This will launch the interactive Ruby session, and you'll see a prompt where you can enter Ruby code.

   ```ruby
   $ irb
   irb(main):001:0>
   ```

2. **Running Ruby Code**:
   You can enter and run Ruby code directly in IRB. For example:

   ```ruby
   irb(main):001:0> 2 + 2
   #=> 4
   irb(main):002:0> "Hello, IRB!"
   #=> "Hello, IRB!"
   ```

3. **Defining Variables and Methods**:
   You can define variables and methods within the IRB session, and they will be available for later use:

   ```ruby
   irb(main):001:0> a = 5
   #=> 5
   irb(main):002:0> def square(x)
   irb(main):003:1>   x * x
   irb(main):004:1> end
   #=> :square
   irb(main):005:0> square(a)
   #=> 25
   ```

4. **Exploring Objects**:
   You can create and manipulate objects, and inspect their properties:

   ```ruby
   irb(main):001:0> hash = { name: "John", age: 30 }
   #=> {:name=>"John", :age=>30}
   irb(main):002:0> hash.keys
   #=> [:name, :age]
   irb(main):003:0> "Hello, #{hash[:name]}! You are #{hash[:age]} years old."
   #=> "Hello, John! You are 30 years old."
   ```

5. **Loading Files**:
   You can load external Ruby files using the `require` or `load` commands to access and execute code from other files within the IRB session.

   ```ruby
   irb(main):001:0> require './my_script.rb'
   ```

6. **Exiting IRB**:
   To exit IRB, type `exit` or press Ctrl+D (on Unix-like systems) or Ctrl+Z (on Windows).

IRB is a great tool for interactively working with Ruby code, especially when you want to experiment, debug, or learn the language. It's also commonly used for testing small code snippets and exploring Ruby libraries.
