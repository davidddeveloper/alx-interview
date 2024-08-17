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
