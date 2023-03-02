#!/usr/bin/env python
# coding: utf-8

# # Pandas
# 
# Pandas is a library for storing and manipulating tabular data, or data stored in rows and columns like a spreadsheet. Pandas is a huge library with many different functions and methods, so what follows is a brief introduction to the most important functions for data management.
# 
# ```{seealso}
# If you encounter any part of Pandas out in the wild that you don't see here, you can always refer to the [Pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html#user-guide).
# ```
# 
# ## DataFrames and Series
# 
# Instead of normal Python lists and dictionaries, Pandas stores data in its own specialized objects. The main one is a *DataFrame*, which is a lot like a spreadsheet with rows and columns.
# 
# You can create a DataFrame directly with the `DataFrame()` class in Pandas, but it's more likely that you'll read in a DataFrame from a CSV or spreadsheet file. First you must import the library, and it's a good idea to import the `numpy` library as well.
# 
# ```{note}
# Numpy is a Python library for efficiently handling arrays and matrices of numbers. Pandas uses it under the hood to run quickly. You usually won't need to use it directly, but it's good to have it installed to avoid any mysterious errors.
# ```

# In[1]:


import pandas as pd
import numpy as np


# Now you can use the `read_csv()` function to read in a comma-separated value (CSV) spreadsheet file. You must put the name of this file in quotes, and the file should be in the same directory as your Jupyter notebook (or else you should include a full path). The `read_csv()` function will also accept a URL that points to a CSV file online.
# 
# For this example, we'll use the file `mpg.csv` which comes from R's [ggplot2 library](https://www.rdocumentation.org/packages/ggplot2/versions/3.4.1/topics/mpg).

# In[2]:


mpg = pd.read_csv("data/mpg.csv")
mpg


# ```{note}
# Jupyter nicely formats DataFrames as tables when you type the name of a variable containing a DataFrame. But if you use the `print()` function, it won't display as well.
# ```
# 
# You can get basic information about your DataFrames columns using the `.info()` method.

# In[3]:


mpg.info()


# A *Series* is a lot like a Python list, and each column of a DataFrame is a Series. You can access the columns of a Dataframe with dot notation.

# In[4]:


mpg.model


# You can also turn a list into a Series with the `Series()` class.

# In[5]:


myseries = pd.Series([5, 6, 7, 8])
myseries


# ## Selecting Rows and Columns
# 
# Once you have a DataFrame, you'll typically want to filter and select different rows or columns.
# 
# To filter specific rows, Pandas uses a bracket notation. It takes conditional statements that are similar to [Python conditions](/python.html#conditions).

# In[6]:


# Get cars with fewer than 6 cylinders
four_cylinders = mpg[mpg.cyl < 6]
four_cylinders


# You can also use the operators `&` (and), `|` (or), and `!` (not) to combine conditional filters.

# In[7]:


# Get Volkswagens and Fords
vw_ford = mpg[(mpg.manufacturer == 'volkswagen') | (mpg.manufacturer == 'ford')]
vw_ford


# You can use a double bracket notation to select a subset of columns.
# 
# ```{note}
# Using single brackets or dot notation will get you a single column as a Series.
# ```

# In[8]:


class_cty_hwy = mpg[["class", "cty", "hwy"]]
class_cty_hwy


# ## Data Wrangling
# 
# In addtion to selecting rows and columns from DataFrames, you can also use Pandas to do a wide variety of data transformations.
# 
# ### Sorting

# In[9]:


mpg.sort_values("year", ascending=False)


# ### Counting

# In[10]:


mpg.value_counts("manufacturer")


# ### Renaming Columns

# In[11]:


# Note the use of a Python dictionary as this method's argument
mpg = mpg.rename({"cty":"city", "hwy": "highway"})
mpg


# ### Create new columns
# 
# You can use `assign()` to create new columns based on existing ones.

# In[12]:


mpg = mpg.assign(displ_per_cyl = mpg.displ/mpg.cyl)
mpg


# ### Grouping and Summarizing
# 
# This combines a couple functions that exist within Pandas to create *summary tables*.
# 
# Pandas has a wide range of summary statistics that you can apply to individual columns.

# In[13]:


# Average city fuel efficiency
mpg.cty.mean()


# In[14]:


# Standard deviation of highway fuel efficiency
mpg.hwy.std()


# Pandas also has a `.groupby()` method (which returns a generator) that groups categorical variables.

# In[15]:


mpg.groupby("manufacturer")


# By itself, `.groupby()` doesn't show anything. It needs to be combined with a summary statistic to create a summary table.

# In[16]:


# Averages by manufacturer
# set `numeric_only=True` to avoid a warning
mpg.groupby("manufacturer").mean(numeric_only=True)


# ```{seealso}
# Wes McKinney's excellent book *Python for Data Analysis* has lots more examples and many additional function. In particular, you can check out [Chapter 5](https://wesmckinney.com/book/pandas-basics.html#pandas_frame) and [Chapter 8](https://wesmckinney.com/book/data-wrangling.html).
# ```
