
I Recommend Using the First method, andusing the medos avalaible to the file class to read and modifiy the file

1. You can read the file and put it in a varialbe then use the read method to print the conent .
But at the end of using the varaible you ahve to run name.close() to close the file, 

book = File.open('./file.txt','r') 

puts book.read()

book.close()


2.Yo can do this , whichout worring about clossing the file
You can access the file  content using the vaiable between the two lines e.g |file|

File.open('./file.txt','r') do |file|
    puts file.readlines()

end


3.Diffferent File modes in file class
The file mode is that second parameter we put in File.open('path','r')

The differen file mode are

File Modes:

"r": Read-only mode. The file must exist.
"w": Write mode. Creates a new file or overwrites an existing file. Clears existing content.
"a": Append mode. Opens a file for appending. If the file doesn't exist, a new file is created.
"r+": Read and write mode. The file must exist.
"w+": Read and write mode. Creates a new file or overwrites an existing file. Clears existing content.
"a+": Read and append mode. Opens a file for reading and appending. If the file doesn't exist, a new file is created.



***********************************************************************
To read a file in Ruby, you can use the File class along with various methods provided by
Rubys standard library. Here's an example of how to read a file in Ruby:

Reading the Entire File:

Use the File.read method to read the contents of a file into a string.
Example:

content = File.read("example.txt")
puts content
Reading Line by Line:

Use the File.foreach method to read a file line by line. It iterates over each line in the file,
allowing you to perform operations on each line.
Example:

File.foreach("example.txt") do |line|
  puts line
end
Reading File into an Array:

Use the File.readlines method to read a file and store each line as an element in an array.
Example:

lines = File.readlines("example.txt")
puts lines.inspect
Reading File with a Block:

You can also use the File.open method with a block to automatically close the file after reading.
The block allows you to perform operations on the file contents.
Example:

File.open("example.txt", "r") do |file|
  file.each_line do |line|
    puts line
  end
end
In the above examples, "example.txt" represents the name of the file you want to read.
You can replace it with the actual file name or the file path.

Remember to handle file exceptions and close the file after reading, especially when using the File.open method without a block.






*******************************************************************************************************8
File.open('./file.txt','r') do |file|
    puts file.readlines()[1]

end














































































































































...
