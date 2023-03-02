#!/usr/bin/env python
# coding: utf-8

# # Python
# 
# This first chapter outlines the basic ways to work in Python. If you're familiar with other programming languages, you'll likely spot some overlap.
# 
# ```{seealso}
# For more on anything you see here, you can check out the [Python documentation](https://docs.python.org/3/).
# ```
# 
# ## Variables
# 
# Use the `=` sign to store anything inside a variable.

# In[1]:


myvar = 5
print(myvar)


# Use descriptive variable names and avoid spaces! You can try:
# 
# ```
# snake_case
# camelCase
# OrEven_mix_it_up
# ```
# 
# Variables have distinct types, and you can find out a variable's data type with the `type()` function.

# In[2]:


type(myvar)


# In[3]:


stringvar = "five"
type(stringvar)


# ## Comments
# 
# Use the `#` sign at the start of a line to create a comment. 

# In[4]:


# This variable contains a continuous value
some_variable = 2.5


# You can use comments to keep track of what you're using, leave a note for someone working after you, and especially to *create a citation if the code you're using isn't your own*.
# 
# ## Data Structures
# 
# Python contains several useful data structures. These overlap with the data structures available in other languages, but they often have different names.
# 
# ### Lists
# 
# Lists are analogous to arrays in other languages. They use brackets to contain ordered lists of data.

# In[5]:


mylist = [5,6,7]

secondlist = ["cat","dog","fish"]

print(mylist)


# In a list, you can easily access items using "list slicing," a bracket notation that lets you access list items with their index.

# In[6]:


# Get the first item in a list, at index 0
mylist[0]


# In[7]:


# Get several items in a list, with a range of values
secondlist[1:3]


# In[8]:


# Get items from the end of a list with negative values
mylist[-1]


# You can also create a list of numbers (starting at 0) with the `range()` function:

# In[9]:


list(range(10))


# ```{note}
# Python also has *tuples*, which are a lot like lists but use parentheses instead of brackets: i.e. `(1, 2, 3)`. Tuples often include just 2 items at a time.
# ```

# ### Sets
# 
# Sets are like lists, but they include only unique items. They use braces instead of brackets.

# In[10]:


myset = {1, 2, 3, 4}
print(myset)


# You can turn a list into a set to get only the unique items in that list:

# In[11]:


repeating_list = [1, 2, 1, 3, 3, 5, 4, 6, 4, 1]
set(repeating_list)


# Sets have special operators to combine sets and find intersections.

# In[12]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Items in either set
set1 | set2


# In[13]:


# Items in both sets
set1 & set2


# In[14]:


# Items in one set but not the other
set1 - set2


# In[15]:


# Items in either set but not both
set1 ^ set2


# ### Dictionaries
# 
# Dictionaries are analogous to objects in other languages. They contain key-value pairs, and they're also surrounded by brackets.

# In[16]:


mydictionary = {"pet_name": "Fido", "age": 5, "pet_type": "dog"}
print(mydictionary)


# You can access items in a dictionary using bracket notation, similar to list slicing.

# In[17]:


mydictionary["pet_name"]


# In[18]:


mydictionary["age"]


# If you have two lists or sets of the same length, you can use `zip()` to combine them as the keys and values of a new dictionary.
# 
# ```{note}
# The zip function returns a generator (see below), so you need to convert it to a dictionary with the `dict()` function.
# ```

# In[19]:


# Keep in mind that dictionary keys must be unique values

zipped_dictionary = zip(secondlist, mylist)
dict(zipped_dictionary)


# ### Generators/Iterators
# 
# Some functions and methods in Python output generators instead of a distinct data type. These generators often need to be converted to a specific data type before they can be used.
# 
# For example, the dictionary method `.values()` gets the values of a dictionary as an iterator:

# In[20]:


mydictionary.values()


# We can see those values above, but we can't access them in the way we would a list. The code below will throw an error:

# In[21]:


mydictionary.values()[1]


# To make this work, we need to convert the generator into a list:

# In[24]:


dict_values = mydictionary.values()
dict_values = list(dict_values)

dict_values[1]


# ## Manipulating Data Structures
# 
# Once you know how to create and access data structures, you can use some basic python concepts to create them.
# 
# ### Loops
# 
# The statements `for` and `in` let you loop through a list. This is called, straightforwardly, a "for loop."

# In[25]:


# The variable name after the word `for` is a new name you're creating
for x in mylist:
    print(x)


# You can do anything you want inside a for loop to manipulate each item:

# In[26]:


for x in mylist:
    y = x*5
    print(y)


# If your goal is to create a *new* list with some altered items, you can put a for loop into brackets and run all your code on a single line. This is a special Python concept called a "list comprehension." They keep your code concise and easy to read. The code below does the same thing as above, but puts the items into a brand new list:

# In[27]:


newlist = [x*5 for x in mylist]
newlist


# For loops aren't just for lists! You can use for loops with dictionaries, but you need to use the `.items()` method:

# In[30]:


for k,v in mydictionary.items():
    print(k,v)


# ### Conditions
# 
# Commonly used inside loops, conditions let you evaluate true or false statements. They will perform one action `if` a statement is true and a different action if the statement is false (`else`).
# 
# Conditions typically use operators to compare things to one another. These operators include:
# 
# - `==` is equal to
# - `!=` is not equal to
# - `>` is greater than
# - `>=` is greater than or equal to
# - `<` is less than
# - `<=` is less than or equal to

# In[38]:


for x in mylist:
    if x == 7:
        print("Hooray!")
    else:
        print("Hip")


# You can also use `elif` to create a chain of multiple conditions.

# In[39]:


for x in [5, 6, 7, 8]:
    if x/2 == 3 or x/2 == 4:
        print(x*10)
    elif x < 6:
        print("small and odd")
    else:
        print("This is seven.")


# ### Functions
# 
# Functions are simply reusable bits of code. In Python, they're generally a word followed by parentheses. Inside the parentheses are *arguments*: bits of data or information that the function needs to work. You've used functions already: `print()`, `range()`, and `type()` are all built-in Python functions:

# In[40]:


type(mydictionary)


# You can easily create your own functions in Python using the `def` statement. You give your function a name and some arguments, and then you tell it what to do. The function should also `return` a value.

# In[41]:


# As in a for loop, the `arg` variable is one you're creating on the spot.
def myFunction(arg):
    x = arg*10
    return x


# Once you create a function, it will be stored in memory for you to use later.

# In[42]:


myFunction(5)


# In[43]:


myFunction(8)


# ```{note}
# Methods are a lot like functions, but they are attached to an object with a period. For example, in `mydictionary.values()`, `.values()` is a method that gets the dictionary's values.
# ```

# ### Libraries
# 
# Sometimes you will write functions yourself, and often you will use functions that others have written. The Python community is very large, full of people who've made helpful code that you can reuse. They've packaged this code into *libraries*. Libraries include sets of methods and functions that you can use. In the rest of this book, we'll focus on three large data analysis libraries: `pandas`, `seaborn`, and `networkx`.
# 
# To import a library, you can simply use the `import` statement. If you like, you can also abbreviate the name of the library using `as`.

# In[44]:


import pandas as pd


# Generally importing libraries is the first thing you do, at the very top of your code. Once you've imported a library, you can use any of its functions.

# In[47]:


# More on what this function does in the next chapter!
pd.Series(mylist)


# You can also import just small parts of very large libraries. For example, `networkx` as bipartite functions that you can import like so:

# In[48]:


from networkx.algorithms import bipartite


# This can save time and memory when you only need one or two functions.
# 
# ---
# 
# That's it for Python basics! In the next chapters, we'll see how to use Python to manipulate tabular data.
