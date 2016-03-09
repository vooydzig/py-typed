typed
==

Typed is little **python2** module that provides type checking for both function arguments and return values.

With `typed` You can feel like You're programming in C++ or Java but without using semicolons! 
**Say NO! to programming language prejudice** use `typed` today.  

Usage
--
	from typed import accepts, returns

	@returns(int)
    @accepts(a=int, b=int)
    def add(a, b):
        return a + b


    add(1, 2)

    try:
        add(1.0, 2)
    except TypeError:
        print("Float is not an integer")
    try:
        add('1', 2)
    except TypeError:
        print("String is not an integer")
 