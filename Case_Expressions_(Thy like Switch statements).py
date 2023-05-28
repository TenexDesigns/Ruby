In Ruby, case expressions are used to compare a value against multiple possible options and execute different 
code blocks based on the matching condition. They provide a concise way to handle multiple conditions.
Heres an explanation of case expressions in Ruby with code samples:
  
  
  
  
  
  

Basic case Expression:

The basic case expression compares a value against multiple when clauses and executes the code
block associated with the first matching condition.
Example:

grade = "B"

case grade
when "A"
  puts "Excellent"
when "B"
  puts "Good"
when "C"
  puts "Average"
else
  puts "Below Average"
end
# Output: Good







Using Ranges:

You can use ranges in when clauses to specify a range of values.
Example:

score = 85

case score
when 90..100
  puts "Excellent"
when 80..89
  puts "Good"
when 70..79
  puts "Average"
else
  puts "Below Average"
end
# Output: Good





Matching Patterns:

case expressions can also use pattern matching with regular expressions to compare against a pattern.
Example:

email = "john@example.com"

case email
when /\A[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\z/
  puts "Valid email"
else
  puts "Invalid email"
end
# Output: Valid email





Value Capture:

You can capture the matching value using the case expression and assign it to a variable for further use.
Example:

fruit = "apple"

case fruit
when "apple"
  puts "It's an apple"
when "banana"
  puts "It's a banana"
else
  puts "Unknown fruit"
end
# Output: It's an apple
case expressions provide a clean and readable way to handle multiple conditions in Ruby. 
They allow you to compare a value against different options and execute the corresponding code block. 

You can use simple values, ranges, regular expressions, and pattern matching to define 
the conditions. case expressions are useful when you have multiple possible outcomes based on a single value.


































































































































































































































































..
