# cprint
### What is cprint?
cprint is an easy way to print using colors.
### How do I use it?
All you have to do is call the 
```python 
cprint()
```
function. It takes in 2 or 3 arguments. First, what you want to output. Second, what color you want the text to be, and last, if you desire a certain style you can enter it. 

### What are the colors?

###### The allowed colors are 
- red
- light_red
- yellow
- green
- lime
- blue
- cyan
- purple
- brown

# What are the styles?

###### The allowed styles are 
- bold
- faint
- italic
- underline
- blink
- negative
- striketrough


#### Ex:

```python
from cprint import cprint
cprint("Hello World!", "cyan", "negative")
```
This outputs the following:
![Command line with code output](https://i.ibb.co/27zD626/cprint.png)
###### Use it more it see more options!