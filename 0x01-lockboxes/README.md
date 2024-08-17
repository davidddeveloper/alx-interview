# Lockboxes
> lockboxes is rather a simple interview question that forces you to think.
All it means is to walk around your house to see if you can open all the doors, with all, zero or few keys from the first door which is going to be initially open.
> As you progress to different doors you are going to find keys to other doors. If you eventually find all the keys, it means you have successfully opened all the doors.


pseudocode of lockboxes - with loops

>    lockboxes:

>    viewedboxes = {}

>    main loop through boxes

>    >    if index not in viewedboxes

>    >    inner loop[index] through box

>    >    >    add idx of innerloop (key) to viewboxes
                
>    if length of viewedboxes equals boxes return true

>    otherwise return false


## Python solution
[iterative solution](0-lockboxes.py)

## Resources
[Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

[Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

[asymptotic-notation-and-analysis-based-on-input-size-of-algorithms](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)

[Python Recursion](https://realpython.com/python-recursion)

[Queue and Stack in python](https://www.geeksforgeeks.org/queue-in-python)

[Python set](https://docs.python.org/3/tutorial/datastructures.html#sets)

