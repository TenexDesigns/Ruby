Syntax 1
--------------------------------------------


names = {:name => "George"}

puts names[:name]




Syntax 2
--------------------------------------------

names  = { name: "George" }

puts names[:name]








In Ruby, symbols are a data type that represents names or identifiers. They are lightweight and immutable,
often used as keys in hashes o
r to represent method names. Symbols start with a colon (:) followed by the symbol name.

Regarding the position of the colon in symbols and hashes:

Symbol Syntax: The position of the colon matters when defining symbols. The colon should come before the symbol name
  without any space in between. For example: :george.

Hash Syntax: In Ruby, there are multiple syntaxes to define hashes. The two common ones are using the => (rocket) or the colon syntax. 
  The position of the colon matters in the colon syntax, where the colon comes after the key name without any space.
  For example: george: "Gavay".

Now, let's analyze the code snippets you provided:


names = {george: "Gavay"}
puts names[:george]
In this code, a hash named names is defined using the colon syntax. The symbol :george is used as the key,
  and the corresponding value is "Gavay". Later, puts names[:george] is used to retrieve and output the value associated with
  the key :george, which is "Gavay". This code works correctly because the colon is used in the correct position when 
    defining the symbol and the hash.


names = {:george => "Gavay"}
puts names[:george]
In this code, the hash names is defined using the => syntax, where :george is the key and "Gavay" is the value.
  Later, puts names[:george] is used to retrieve and output the value associated with the key :george, which
    is "Gavay". This code also works correctly.

In both cases, the position of the colon in the symbol definition is correct, and the retrieval of the value
using names[:george] works because the symbol key matches the defined key in the hash.

Its important to note that the two syntaxes ({george: "Gavay"} and {:george => "Gavay"}) are equivalent
and can be used interchangeably. The choice between them often comes down to personal preference or code style conventions.


































































































































...
