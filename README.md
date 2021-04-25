# Challenges

Group challenges for Practicum 100

# Challenge 1

## Version 1.0

Calculate the number of the least operations needed to reach from number X to number Y with only two operations
available:

Available operations:

- Multiply with 2
- Subtract by 1

**Method used:**

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBzdWJncmFwaCBvbmUgc3RlcFxuICAgIEFbNl0tLT58LTF8IEIoNSlcbiAgICBBWzZdLS0-fCoyfCBDKDEyKVxuICAgIGVuZFxuICAgIFxuICAgIHN1YmdyYXBoIHR3byBzdGVwc1xuICAgIEItLT58LTF8IEQoNClcbiAgICBCLS0-fCoyfCBFKDEwKVxuXG4gICAgXG4gICAgQy0tPnwtMXwgRigxMSlcbiAgICBDLS0-fCoyfCBHKDI0KVxuICAgIGVuZFxuXG4gICAgc3ViZ3JhcGggdGhyZWUgc3RlcHNcbiAgICBELS0-fC0xfCBJKDMpXG4gICAgRC0tPnwqMnwgSig4KVxuXG4gICAgRS0tPnwtMXwgSyg5KVxuICAgIEUtLT58KjJ8IEwoMjApIFxuICAgIHN0eWxlIEwgZmlsbDojYmJmLHN0cm9rZTojZjY2LHN0cm9rZS13aWR0aDoycHgsY29sb3I6I2ZmZixzdHJva2UtZGFzaGFycmF5OiA1IDVcblxuICAgIEYtLT58LTF8IE0oMTApXG4gICAgRi0tPnwqMnwgTigyMilcblxuICAgIEctLT58LTF8IE8oMjMpXG4gICAgRy0tPnwqMnwgUCg0OClcbiAgICBlbmQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBzdWJncmFwaCBvbmUgc3RlcFxuICAgIEFbNl0tLT58LTF8IEIoNSlcbiAgICBBWzZdLS0-fCoyfCBDKDEyKVxuICAgIGVuZFxuICAgIFxuICAgIHN1YmdyYXBoIHR3byBzdGVwc1xuICAgIEItLT58LTF8IEQoNClcbiAgICBCLS0-fCoyfCBFKDEwKVxuXG4gICAgXG4gICAgQy0tPnwtMXwgRigxMSlcbiAgICBDLS0-fCoyfCBHKDI0KVxuICAgIGVuZFxuXG4gICAgc3ViZ3JhcGggdGhyZWUgc3RlcHNcbiAgICBELS0-fC0xfCBJKDMpXG4gICAgRC0tPnwqMnwgSig4KVxuXG4gICAgRS0tPnwtMXwgSyg5KVxuICAgIEUtLT58KjJ8IEwoMjApIFxuICAgIHN0eWxlIEwgZmlsbDojYmJmLHN0cm9rZTojZjY2LHN0cm9rZS13aWR0aDoycHgsY29sb3I6I2ZmZixzdHJva2UtZGFzaGFycmF5OiA1IDVcblxuICAgIEYtLT58LTF8IE0oMTApXG4gICAgRi0tPnwqMnwgTigyMilcblxuICAgIEctLT58LTF8IE8oMjMpXG4gICAgRy0tPnwqMnwgUCg0OClcbiAgICBlbmQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

As seen on the above diagram the method that will use is a process of iterations throw the different steps needed from a
node to give us the result we are looking for. For this specific example, we see that the result 20 is reached after
three iterations.

## challenges

This code although succeeds to return the right number of operations has a big problem to calculate the processes for
big numbers as it uses list comprehensions and repetitions reaching O(n^2)

**To view this version use**

```cmd
git checkout 9485ec0d
```

# version 2.0

This time the code checks if the final number is odd or even. If it's even half the number, if it's odd increase the
number by one. Do this process till the end number is equal to start number.

## Run

```cmd
python main.py
```

# Challenge 2

Given three lists with random integer numbers, find the intersection between these three lists.

## Solution:

We use here the default methods from python's `set` Object: `intersection`

## Run
```cmd
python intersections.py
```
