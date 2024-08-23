# Minimum Operations
> `question` In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
>
> `my understand` - you are only allowed to perform read/write operation on the file, the file will contain a single character H, the end goal is to end up with n Hs (n number of Hs). Eventhough this is what the question means, it is not necessary to perform read/write operation or even work with fille(s) in your solution. It is just an assumption to say `In a text file, there is a single character H.` However, in the psuedocode below, I have include the read/write operation so you can really understand what's going on in the solution. But note also that including the read/write operation in the solution can be ineffective especially with larger values of n - `your cpu will get fried`. Regardless I have included it in the pseudocode - so it is your choice to make, wheather to include in your final solution or not.
>

## concepts that helped me to solve the question
### `dynamic programming`
is a method in math and computer science to solve complex problems by breaking it into smaller subproblems, solves them and save their result to avoid doing the same operation and finally build them up all together to solve the complex problem.
> Their are two types of approach to dynamic programming `top-down approach` and `bottom-up approach`
> 
> `memoization` or top-down approach - start from the complex problem and recursively breaks it down to smaller problems
> 
> `tabulation` or bottom-up approach - start from the smallest problem and gradually builds up to the complex problem

### Recursion
> recursion in python is when a function calls itself. Think of it as another way of creating loops.
> The best way I understand recursion is when I think of them as stack (multiple books ontop of each other).
> 
> imagine a function that takes a positive integer argument n and calls itself, each times it decrement n and print it out until n is zero (`break point`)
> 
> now imagine calling that function and passing 4 as the argument for n. What do you think will happen?
> This is what the stacking would look like and I thing the image is self explanatory - the function that call itself will have to wait for itself `the clone` to finish before continuing itself. - `synchronous` So it keeps stacking until the break point is reached. When the break point is reached the function rolls back to execute other part of the code after the call to itself.
> 
> ![code_stacking](https://github.com/user-attachments/assets/d7df4850-82dd-43c5-b355-10760b9cb29e)



### `prime factorization`
>`prime number` is any number that is divisible by only 1 and it self.
>
>`prime factorization` is a way of writing a number as the product of it prime factors (the prime factors of 10 is 2 and 5; ie prime factorization of 10 is (10 == 2 * 5))

## Solution
> The solution to this problem is very simple if you understanding the three concepts above plus your general coding skills.
> 
> `step 1` the first step is finding the prime factorization of n which by adding them will give us the minimum number of operations we can perform to make n Hs
> 
> `step 2` once we have the factors of n and we know the number of operation, the next thing is to recursively perform the operations (read/write) base on the factors. - `tabulation appraoch`
>
> example: take 75
>   - `step 1 ` factors of 75 is 3 * 5 * 5
>   - `note ` adding 3, 5 and 5 will give us 13 operations we can perform on 75 to get n Hs
>   - ` step 2` is to recursively perform the operations - meaning
>   - last factor 5 means `perform 5 operations - first is copy AND rest is paste`
>   -   - read/copy from the file -> H
>       - write/paste to the file four times -> HHHHH
>   - middle factor 5 means `perform 5 operations - first is copy AND rest is paste`
>   -   - read/copy from the file -> HHHHH
>       - write/paste to the file four times -> HHHHHHHHHHHHHHHHHHHHHHHHH
>   - first factor 3 means `perform 3 operations - first is copy AND rest is paste`
>   -   - read/copy  from the file -> HHHHHHHHHHHHHHHHHHHHHHHHH
>       - write/paste to the file 2 times -> HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
>   - lastly to prove that this solution is correct and it works efficiently go ahead and count the letters H, it should be equivalent to 75 characters

> ### pseudocode
> Recursive approach
> ![code_minoperation](https://github.com/user-attachments/assets/55e8d0a4-8b09-4232-956f-5cbd67b13e2c)

    > minOperations function with argument n:
    >    if n == 1:
    >        initially create the file with letter H
    >        return no_of_operation
    >
    >    loop ntimes:
    >        find prime factor:
    >            no_of_operation = call minOperations with n divide by prime factor
    >            increment no_of_operation
    >            perform read write operations:
    >                read/copy if loop is at index 0
    >                write/paste if loop is above index 0
    >            stop the loop
    >    
    >    return no_of_operation

> Iterative approach
![minoperations_iterative_approach](https://github.com/user-attachments/assets/7ef705b7-ffa5-479c-a29f-fab7690bbdb5)

> `python solution` [here](0-minoperations.py)
> `python iterative solution` [here](iterative_approach.py)
> `python recursive approach` [here](recursive_approach.py)
>  `python iterative with file-IO solution` [here](iterative_method_with_file_io.py)
>  `python recursive with file-IO solution` [here](recursive_method_with_file_io.py)
