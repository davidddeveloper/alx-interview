# Minimum Operations
> `question` In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
>
> `my understand` - you are only allowed to perform read or write operations on the file, the file will contain a single character H, the end goal is n Hs (n number of character(s))
>

## concepts that helped to solve the question
### `dynamic programming`
is a concept in math and computer science to solve complex problems by breaking it into smaller subproblems, solves them and save their result to avoid doing the same operation and finally build them up all together to solve the complex problem.
> Their are two types of approach to dynamic programming `top-down approach` and `bottom-up approach`
> 
> `memoization` or top-down approach - start from the complex problem and recursively breaks it down to smaller problems
> 
> `tabulation` or bottom-up approach - start from the smallest problem and gradually builds up to the complex the complex problem

### Recursion
> recursion in python is when a function calls itself. Think of it as another way of creating loops.
> The best way I understand recursion is when I think of them as stack (multiple books ontop of each other).
> imagine a function that takes a positive integer argument n and calls itself, each times it decrement n and print it out until n is zero (`break point`)
> now imagine calling that function and passing 4 as the argument for n. What would you think will happen? Alright lemme explain to you the stacking I mention earlier.
> 

### `prime factorization`
>`prime number` is any number that is divisible by only 1 and it self.
>
>`prime factorization` is a way of writing a number as the product of it prime factors (the prime factors of 10 is 2 and 5; ie prime factorization of 10 is (10 == 2 * 5))

