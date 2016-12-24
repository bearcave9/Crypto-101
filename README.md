
# Other Python features

##[The difference between sys.stdout.write and print]( http://stackoverflow.com/questions/3263672/python-the-difference-between-sys-stdout-write-and-print )

 ``` print ``` is just a thin wrapper that formats the inputs (space between args and newline at the end) and calls the write function of a given object. By default this object is ``` sys.stdout ```, but you can pass a file for example:

``` print >> open('file.txt', 'w'), 'Hello', 'World', 2+3 ```

 In Python 3.x, ``` print ``` becomes a function, but it is still possible to pass something else than sys.stdout. _See http://docs.python.org/library/functions.html_

In Python 2.7, ``` print ``` is still a statement, but it can be used as a function with

```from __future__ import print_function ```

 There is a little difference between the print function and the print statement 

 In case of error when evaluating arguments:

 ``` print "something", 1/0, "other" ``` #prints only something because 1/0 raise an Exception. <br>
 ``` print("something", 1/0, "other") ``` #doesn't print anything. The func is not called
