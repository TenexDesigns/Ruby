Ruby provides various built-in methods for working with different data types, such as arrays, hashes, strings, and numbers. Here's an overview of common methods for these data types:

**Array Methods**:

- `push(element)` or `<<(element)`: Add an element to the end of the array.
- `pop`: Remove and return the last element of the array.
- `unshift(element)`: Add an element to the beginning of the array.
- `shift`: Remove and return the first element of the array.
- `length` or `size`: Get the length of the array.
- `first` and `last`: Get the first and last elements of the array.
- `include?(element)`: Check if an element is in the array.
- `each`: Iterate through each element of the array.
- `map` or `collect`: Create a new array with the results of applying a block to each element.
- `select`: Create a new array with elements for which a block returns true.
- `reject`: Create a new array with elements for which a block returns false.
- `sort`: Sort the array.
- `reverse`: Reverse the array.
- `delete(element)`: Remove all occurrences of an element.
- `join(separator)`: Convert the array to a string, joining elements with the given separator.

**Hash Methods**:

- `[]` or `fetch(key)`: Access the value associated with a key.
- `[]=` or `store(key, value)`: Set the value for a key.
- `keys`: Get an array of keys.
- `values`: Get an array of values.
- `each`: Iterate through key-value pairs.
- `has_key?(key)` or `key?(key)`: Check if a key exists in the hash.
- `has_value?(value)`: Check if a value exists in the hash.
- `delete(key)`: Remove a key-value pair.
- `merge(other_hash)`: Merge the hash with another hash.
- `to_a`: Convert the hash to an array of key-value pairs.
- `to_h`: Convert an array of key-value pairs to a hash.

**String Methods**:

- `length` or `size`: Get the length of the string.
- `upcase` or `downcase`: Convert the string to uppercase or lowercase.
- `capitalize`: Capitalize the first letter of the string.
- `reverse`: Reverse the characters in the string.
- `include?(substring)`: Check if a substring exists in the string.
- `split(delimiter)`: Split the string into an array of substrings.
- `gsub(pattern, replacement)`: Replace occurrences of a pattern with a replacement.
- `sub(pattern, replacement)`: Replace the first occurrence of a pattern with a replacement.
- `strip`: Remove leading and trailing whitespace.
- `chop` or `chomp`: Remove the last character or line ending.
- `concat(other_string)`: Append another string to the end.
- `to_i`, `to_f`, `to_s`: Convert the string to an integer, float, or string.

**Numeric Methods**:

- `+`, `-`, `*`, `/`: Perform arithmetic operations.
- `**`: Calculate exponentiation.
- `abs`: Get the absolute value.
- `round`, `ceil`, `floor`: Perform rounding operations.
- `to_s`: Convert the number to a string.
- `to_f`, `to_i`: Convert to a float or integer.
- `even?`, `odd?`: Check if the number is even or odd.

These are just a selection of commonly used methods for each data type. Ruby provides a rich set of methods to work with these data types, and you can find more methods and details in the official Ruby documentation.



  .....
