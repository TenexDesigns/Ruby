In Ruby, the "@" symbol is used to denote instance variables. Instance variables are used to store state or data that is associated with an instance (object) of a class. They have a scope that is limited to the instance of the class in which they are defined. Each instance of a class can have its own set of instance variables, and these variables are used to store and retrieve data specific to that instance.

In your provided code, you have defined instance variables like `@first_name` and `@last_name` within the `Student` class. Here's what each part of your code does:

```ruby
class Student
  # Setter method for @first_name
  def first_name=(value)
    @first_name = value
  end

  # Getter method for @first_name
  def first_name
    @first_name
  end

  # Setter method for @last_name
  def last_name=(value)
    @last_name = value
  end

  # Getter method for @last_name
  def last_name
    @last_name
  end

  # Returns the full name
  def full_name
    last_name + ", " + first_name
  end
end

@student = Student.new
@student.first_name = "Bob"
@student.last_name = "Jones"
puts @student.full_name
```

In this code, you have a `Student` class with instance variables `@first_name` and `@last_name`. The instance variables are used to store and retrieve the first name and last name of a student.

The setter methods (e.g., `first_name=` and `last_name=`) are used to set the values of the instance variables, and the getter methods (e.g., `first_name` and `last_name`) are used to retrieve the values of these variables. This encapsulation allows you to control access to the instance variables and provides a way to perform validation or other actions when setting or getting their values.

The `full_name` method uses the instance variables `last_name` and `first_name` to construct and return the full name of the student in the format "Last Name, First Name."

Finally, you create an instance of the `Student` class, set its first name and last name using the setter methods, and then use the `full_name` method to print the full name of the student.

The `@` symbol denotes instance variables, and `@@` is used for class variables, which have a scope that is shared among all instances of a class.
