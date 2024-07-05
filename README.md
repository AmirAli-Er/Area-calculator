There's a simple programming exercise on lambda function which is a small and anonymous function!
this is supposed to calculate the area for some geometric shapes for example:

 - square
 - circle
 - triangle
 - rectangle
 
this is how you can see the output:

```
ls = get_func(['square', 'circle', 'rectangle','triangle'])
print(ls[0](1))
print(ls[1](2))
print(ls[2](2, 4))
print(ls[3](4, 5))
```
