# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, I think all the name of functions of dict and list clearly descibe the action the code is doing. I can easily understand the function by just viewing the name.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A list is an ordered, mutable collection of elements stored in a dynamic array, accessible by index, while a dictionary is an unordered, mutable collection of unique key-value pairs implemented as a hash table, offering efficient value retrieval based on keys.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, as long as the inputed index is valid.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

A library that can work with any data type offers versatility and reduced redundancy, making it adaptable to various applications and simplifying code maintenance. However, it may introduce performance overhead, sacrifice type safety, and increase complexity due to the need for generic handling.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes, I think most commonly used functions are named clear and concise and easy to understand.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

No, I think the function with largest number of arguments only has three arguments for input.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

`**kwargs` is a converter in function definitions to collect keyword arguments into a dictionary. kwargs is good because it provides flexibility when calling a function and makes code forward-compatible. It's not good because sometimes it makes function harder to understand and difficult to debug.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


Q1 - Because in most cases arguments set to 'None' are considered to be optional so that developers can only focus on the essential arguments.

Q2 - Yes, arguments can be set to other values if developers want to input a meaningful value.

Q3 - In general predetermined value can help a function more flexible and backward-compatible. From a developer's perspective, I think predetermined values helps an API easier to use and debug, reduce the amount of code when calling it, and improve the performance without too much worry on input errors.
