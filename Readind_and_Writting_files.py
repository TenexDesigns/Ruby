
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

  
  
  
  
  
  
  
  
  WRITING TO A FILE
***************************************************************************************************88
Writing to a File:

Use the File.write method or File.open method with the appropriate file mode to write content to a file.

Example using File.write:


File.write("output.txt", "Hello, World!")


Example using File.open:


File.open("output.txt", "w") do |file|
  file.write("Hello, World!")
end
  
  
  
  MORE EXPLANATION
  ******************************************************************************************
  
  
  To read and write files in Ruby, you can use the File class along with various modes for file operations. 
  Heres an example of how to read from and write to files in Ruby, along with different file modes:

Reading a File:

Use the File.read method or File.open method with the appropriate file mode to read the contents of a file.

Example using File.read:


content = File.read("example.txt")
puts content
Example using File.open:


File.open("example.txt", "r") do |file|
  content = file.read
  puts content
end
Writing to a File:

Use the File.write method or File.open method with the appropriate file mode to write content to a file.

Example using File.write:


File.write("output.txt", "Hello, World!")
Example using File.open:

ruby
Copy code
File.open("output.txt", "w") do |file|
  file.write("Hello, World!")
end
File Modes:

"r": Read-only mode. The file must exist.
"w": Write mode. Creates a new file or overwrites an existing file. Clears existing content.
"a": Append mode. Opens a file for appending. If the file doesn't exist, a new file is created.
"r+": Read and write mode. The file must exist.
"w+": Read and write mode. Creates a new file or overwrites an existing file. Clears existing content.
"a+": Read and append mode. Opens a file for reading and appending. If the file doesn't exist, a new file is created.
When using the File.open method, you can specify the desired mode as the second argument. For example:


File.open("example.txt", "r") do |file|
  # Read from the file
end
Make sure to handle file exceptions and close the file after reading or writing, especially when using the
File.open method without a block.
  
  
  
  
  
  
    MORE EXPLANATION
  ******************************************************************************************
  
  
  In Ruby, there are several ways to read and write files, and different file modes for opening files. 
  Ill provide code samples for reading and writing files, as well as an explanation of file modes.

Reading files

Using File.read:
file_name = "example.txt"
content = File.read(file_name)
puts content
Using File.foreach:
file_name = "example.txt"
File.foreach(file_name) do |line|
  puts line
end
Using File.readlines:
file_name = "example.txt"
lines = File.readlines(file_name)
puts lines
Writing files

Using File.open and File.write:
file_name = "example.txt"
content = "This is an example text."
File.open(file_name, "w") do |file|
  file.write(content)
end
File modes in Ruby

When opening a file in Ruby, you can use different file modes to control how the file is accessed:

'r': Read mode. Opens the file for reading, but does not allow writing.
  If the file does not exist, it raises a FileNotFoundError.
'w': Write mode. Opens the file for writing, or creates a new file if it does not exist. 
  If the file already exists, it truncates the file to zero length or creates a new file if it does not exist.
'a': Append mode. Opens the file for writing, or creates a new file if it does not exist.
  If the file already exists, it appends to the file.
'x': Exclusive creation mode. Creates a new file, but raises a FileAlreadyExistsError if the file already exists.
'b': Binary mode. Opens the file for reading or writing in binary mode, 
  which means that the file is read or written in the raw format without any translation for line endings.
For more information and examples, you can refer to the provided sources 
  
  
  
  
  
  
  
  
  
  
  
  
