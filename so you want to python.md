#[fit]SO YOU WANT TO PYTHON

---

## what this talk will be not 

- this talk will not be an exhaustive feature tour 
- I will not teach you syntax
- you won’t even be able to write python by the end of the talk


——

## what I am looking to do 

- I want to show you a few problems and how we solve them in python.
- I want to give you a few hooks so that you can get started with learning it , if you are interested.
- I want to expose you to the core principles and ideologies of python… 
- and the general culture of python

—

#[fit] import this?

——

# THE ZEN OF PYTHON 

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.

——

In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.

——

#[fit] quick survey

——

# Meta

- There will be a gradual ramp in difficulty 
- I will get geeky a few times 
- Each problem will expose something new 
- The idea is not to learn how to write python but understand what the point of this language is.
- there will be code but you don’t have to understand it , just take away the ideology. 

——

##[fit] Exchanging 2 values 

——

### The C way 


```C
main() {
int a = 10,b = 20,temp;

temp = a;
a = b;
b = temp;

}
```

——

## isn’t this hideous?

- An extra variable.
- Type declarations.
- Syntactic noise.

——

#[fit] There must be a better way!

——

> A high level language is one which doesn’t require attention to the irrelevant.

——

##let’s look at the pythonic way to do things 

<br></br>
<br></br>


```python
	x = 20 , y = 10
	x,y = y,x
```  

<br></br>

READABILITY COUNTS , BEAUTIFUL IS BETTER THAN UGLY, SIMPLE IS BETTER THAN COMPLEX

——

#Concept
- something that corresponds to a single unit of thought should be expressed in a single line , one logical step should be one LOC 
- Readability counts a lot . Code is *READ* a lot more than it is *WRITTEN* 

——


### lets take this idea for a spin 

```python

def fib(n):
	x,y = 1,1
	for i in range(n-2):
		x,y = y,x+y
	return y	

```

——

- Good code should be easy to read and in a way self documenting.

- Good code makes its meaning clear.

——

#[fit] reverse a string 

——

### The C way 

——

#[fit] There must be a better way!

——


### the pythonic way 

```python 

s = “this”

print(s[::-1])
```
———

#Concept

- Integrate powerful tools directly into the language 
- Actively enforce good programming practices 
- Higher level tools allow you to think on a more abstract level 
- Learning to use the tools will be harder but you can be sure that they are the state of the art 

——

### lets take this idea out for a spin 
<br></br>


```python
def pali(s):
	if s == s[::-1] :
		return True
	else: return False
```

—-

# Why does this matter 

- programming isn’t about solving small problems like this , instead it is about building systems and systemic solutions to problems…
- Problems much more complex than reversing a string…
- But all problems can be broken down into really small sub problems that rely on really simple pieces of code just like the one we saw.
- Not having to wrestle with the language allows us to think more clearly about the bigger picture.

——

#[fit] easy things should be easy

——

##let me show you what i mean.

code here for listing out the palindromes in the script of harry potter or something like that using that , just use a generator for the script feed.

——

# 

