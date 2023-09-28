# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- A concrete class because it's not using ABC module and can be instantiated directly.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- This is a destructor and is used to delete the instance of the Image.
1. What class does Texture inherit from?
	- Image class.
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- Every methods and attributes from 'Image' will be inherited.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I personally think the texture here means the image used in a 3D model for games or movies, so I believe a texture 'is-a' image in nature.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, Python will generate constructors automatically.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

*edit the code directly*  
   - The singleton in this lab's code is not thread safe because if multiple threads are trying to generate an instance at the same time, multiple instances will be created. Adding a lock can help it be thread safe.
  
