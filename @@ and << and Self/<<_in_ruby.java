In Ruby, the `<<` operator is used for various purposes, including appending elements to arrays, creating heredoc strings, and redirecting output. Below are examples of how `<<` is used in different contexts:

1. **Appending Elements to Arrays**:
   The `<<` operator is used to add elements to an array. It appends an element to the end of the array.

   ```ruby
   numbers = [1, 2, 3]
   numbers << 4
   puts numbers
   # Output: [1, 2, 3, 4]
   ```

2. **Creating Heredoc Strings**:
   Heredoc is a way to define multi-line strings. The `<<` operator is used to create heredoc strings.

   ```ruby
   message = <<~TEXT
     This is a multiline
     heredoc string.
   TEXT

   puts message
   # Output:
   # This is a multiline
   # heredoc string.
   ```

3. **Redirecting Output**:
   In the context of file operations, the `<<` operator can be used to redirect output to a file. It's often used in conjunction with the `File` class.

   ```ruby
   File.open('output.txt', 'w') do |file|
     file << "This text will be written to the file."
   end
   ```

4. **Bitwise Left Shift Operator**:
   In the context of binary operations, `<<` can be used as a bitwise left shift operator. It shifts the bits of a binary number to the left.

   ```ruby
   num = 3
   shifted_num = num << 2  # Left shift by 2 bits
   puts shifted_num
   # Output: 12 (Binary: 1100)
   ```

The behavior of the `<<` operator depends on the context in which it is used. It's a versatile operator in Ruby, with different meanings in different contexts, as demonstrated in the examples above.



  ....
