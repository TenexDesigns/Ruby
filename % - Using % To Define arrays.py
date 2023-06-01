The % syntax variations are useful for quickly defining arrays without the need for explicit quotation marks or commas. 
The %w and %i syntaxes are also more efficient, because they do not need to create a new array for each string or symbol.
Instead, they create a single array that is reused for all of the strings or symbols.


e.g   %w(jpg jpeg gif png pdf mp4 wmv xls xlsx doc docx ppt pptx mov)   --> Arrsy of Strings

e.g   %i[ show edit update destroy ]   Array of  symbols







In the code snippet you provided, both %w and %i are used as shorthand notations for defining arrays in Ruby.

%w: It represents an array of strings. The elements inside %w() are separated by whitespace and treated as
  individual string elements within the resulting array. In the given code:

%w(jpg jpeg gif png pdf mp4 wmv xls xlsx doc docx ppt pptx mov)
This line creates an array containing the file extensions "jpg", "jpeg", "gif", "png", "pdf", "mp4", "wmv", "xls", "xlsx", "doc", "docx", "ppt", "pptx", and "mov".



%i: It represents an array of symbols. The elements inside %i() are also separated by whitespace, 
  and each element is prefixed with a colon (:) to indicate a symbol. In the given code:

%i[ show edit update destroy ]
This line creates an array containing the symbols :show, :edit, :update, and :destroy.
        It is commonly used in Rails for defining an array of actions or attributes as symbols.

Both %w and %i are convenient ways to define arrays without the need for explicit quotation marks or commas. 
They can improve code readability by providing a more concise syntax for representing arrays of strings or symbols.










MORE  EXPLANTION
*************************************************************************************************************************


In Ruby, %w and %i are special syntaxes that can be used to create arrays of strings or symbols, respectively.
In the first code sample, %w(jpg jpeg gif png pdf mp4 wmv xls xlsx doc docx ppt pptx mov) creates an array of 
strings with the values jpg, jpeg, gif, png, pdf, mp4, wmv, xls, xlsx, doc, docx, ppt, and pptx. 
The second code sample uses %i[ show edit update destroy ] to create an array of symbols with the values 
show, edit, update, and destroy.


































































































...
