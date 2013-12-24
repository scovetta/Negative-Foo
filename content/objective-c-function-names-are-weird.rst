Objective C Function Names Are Weird
####################################
:date: 2013-01-05 21:56
:author: scovetta
:category: Uncategorized
:slug: objective-c-function-names-are-weird

It took me a while before I "got it", but Objective C function names
aren't like names in other languages:

.. code-block:: javascript

    function changeHeadlight(car, side) {
        ...
    }

In JavaScript, the function name is changeHeadlight. It takes two
parameters, car and side. These parameters can be of any time (and are
optional, in fact).

.. code-block:: java

    public void changeHeadlight(Vehicle car, int side) {
        ...
    }

Similarly in Java, the function name is changeHeadlight. It takes two
parameters, car and side, but neither are optional and both are strongly
typed. Now let's take an Objective-C function:

.. code-block:: objective-c

    - (void)changeHeadlight:(Vehicle *)car forSide:(int)side {
        ...
    }

What always confused me was, what is the purpose of "forSide"? It seems
obvious that:

-  void: Return type of the function
-  changeHeadlight: Name of the function
-  (Vehicle \*): Type of first parameter
-  car: Name of first parameter
-  **forSide: ????**
-  (int): Type of second parameter
-  side: Name of second parameter

It made more sense when I started thinking about the first as being
named **changeHeadlight:forSide** instead of just **changeHeadlight**.
You could think of forSide as the "external parameter name" and side as
the "internal parameter name".

I still don't understand why this is necessary, it seems much simpler to
just identify the function uniquely by the function name and parameter
types.

.. code-block:: java

    void addNumbers(int x, int y)

In the case above, the full function name is "addNumbers(int, int)".
Perhaps in Objective C you could have two functions with the same
initial name and same parameter types?

.. code-block:: objective-c

    -(void) performOperation:(int)x addedTo:(int)y
    -(void) performOperation:(int)x subtractedFrom:(int)y
    ...

