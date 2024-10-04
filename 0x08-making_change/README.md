# making change
>`question`: Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total
>
  > prototype: `def makeChange(coins: List[int], total: int)`

>`idea`: the simple way to understand this is to think of each piles of coins as actual piles in a piece of sac that you cannot split. If that is still complex you, then simply think of them as notes ($1 notes $100 notes etc).

>`goal`: find out the minimum number of notes or set of coins or piles of coins, I should add to result into the total.

>`example`: say you have coins = [1, 2, 25] and you want a change for 37.
>
>So you have\
>coins = [1, 2, 25]\
>total = 37

>You can use all 2 notes/pile of coin and 1 notes/pile of coins to change 37.\
which is\
2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+1 = 37\
As you can see, the number of notes/pile of coins would be too many.\
`goal` - so your goal is to find the minimum number of pile of coins you can use.

## my algorithm in pseudocode
    sort coins ascending
    loop through coins starting from end going to start
        break if total is zero

        value in current index < total:
            reset total with 
        value in current index - total
            track this block by incrementing counter

        otherwise:
            decrement loop - going to start
    
    return counter


## solution
> [python](0-making_change.py)
