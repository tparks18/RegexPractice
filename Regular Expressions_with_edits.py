#!/usr/bin/env python
# coding: utf-8

# Click <a href='https://www.dataquest.io/blog/web-scraping-tutorial-python/'>here</a> to learn about Regular Expressions (RegEx) using Python.

# In[ ]:


########################
# DO NOT RUN THIS CELL #
########################

a, X, 9, < -- ordinary characters just match themselves exactly.
. (a period) -- matches any single character except newline '\n'
\w -- matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
\W -- matches any non-word character.
\b -- matches word boundary (in between a word character and a non word character)
\s -- matches a single whitespace character -- space, newline, return, tab
\S -- matches any non-whitespace character.
\t, \n, \r -- tab, newline, return
\d -- matches any numeric digit [0-9]
\D matches any non-numeric character.
^ -- matches the beginning of the string, or specify omition of certain characters
$ -- matches the end of the string
\ -- escapes special character.
(x|y|z) matches exactly one of x, y or z.
(x) in general is a remembered group. We can get the value of what matched by using the groups() method of the object returned by re.search.
x? matches an optional x character (in other words, it matches an x zero or one times).
x* matches x zero or more times.
x+ matches x one or more times.
x{m,n} matches an x character at least m times, but not more than n times.
get_ipython().run_line_magic('pinfo', '')
get_ipython().run_line_magic('pinfo', '')
a(?=b) will match the "a" in "ab", but not the "a" in "ac"
In other words, a(?=b) matches the "a" which is followed by the string 'b', without consuming what follows the a.
get_ipython().run_line_magic('pinfo', '')
a(?!b) will match the "a" in "ac", but not the "a" in "ab"
get_ipython().run_line_magic('pinfo', '')
[] matches for groupings of consecutive characters
get_ipython().run_line_magic('pinfo', '')

########################
# DO NOT RUN THIS CELL #
########################


# What are word boundaries?
# --------------------------------------------------
# Before the first character in the string, if the first character is a word character.<br>
# After the last character in the string, if the last character is a word character.<br>
# Between two characters in the string, where one is a word character and the other is not a word character<br>

# In[126]:


import re
file = open('./names.txt', encoding='utf-8')
data = file.read()
file.close()
data


# In[4]:


# .match() - Checks for specific strings starting from the beginning of a string
re.match(r'Hawkins', data)


# In[5]:


re.match(r'Hawkins, Derek', data)


# In[6]:


re.match(r'Milliken', data)


# In[7]:


# .search() - Looks for FIRST matching string anywhere in the searchable text string
re.search(r'Johnson', data)


# In[8]:


re.search(r'\w, \w', data)


# In[10]:


re.search(r'\w\w\w\w\w\w\w, \w\w\w\w\w', data)


# In[15]:


#Recognize expressions don't recognize all special characters
re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data)


# In[16]:


"Nate's Sentence"


# In[17]:


'Nate's Sentence'


# In[18]:


'Nate\'s Sentence'


# <strong>Exercise 1</strong>:<br>
# Write a function that checks for n number of consecutive digits

# In[29]:


def search_num(n, search_text):
    return re.search('\d'*n, search_text)

search_num(7, '1127j6854v112344k44h5gr')  


# In[32]:


# find(4, data) => <re.Match object; span=(XX, XX), match='5555'>


# In[36]:


phone_number = "(555) 555-5555"
print(re.search(r'\(\d{3}\) \d{3}-\d{4}', phone_number))
re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', phone_number)


# In[ ]:





# In[48]:


# .findall() - Looks for matching string anywhere in the searchable text string and stores each instance into a list
phone_numbers = "555-555-5555 (555)555-5555 5555555555 nate derek (555) 555-5555 ripal (555) 555-5555"

re.findall(r'\(\d{3}\) \d{3}-\d{4}', phone_numbers)


# In[49]:


re.findall(r'\(?\d{3}\)?\s?-?\d{3}-?\d{4}', phone_numbers)


# In[50]:


names = "Hawkins, Derek Welter, Nate Patel, Ripal Davitt, Sam"

re.findall(r'\w+, \w+', names)


# In[59]:


emails = "dere'k@codingtemple.com natew@codingtemple.com Ripal.123@codingtemple.edu nate123@usa.co.com news@co.uk"

re.findall(r'[\'-+.\d\w]+@[-.\w\d]+', emails)


# In[60]:


data


# In[66]:


# re.VERBOSE/re.X - Allows multiline regular expressions
# re.IGNORECASE/re.I - Ignores casing

information = """
Patel, Ripal : ripalp@codingtemple.com : (555) 555-5555
Carter, Joel : joelc@codingtemple.com : (555) 555-5555
Welter, Nate : natew@codgintemple.com : (555) 555-5555
Butz, Ryan : ryan.b@codingtemple.co.us : 555-555-5555
Davitt, Sam : sam+d@codingtemple.edu : 555 555-5555
"""

re.findall(r'''
    @[-.\w\d]+ # @symbol, any number of characters/digits
''', information, re.X)


# In[67]:


re.findall(r'''
    [\w]+, # last name
    \s # space
    [\w]+ # first name any amount of word chars
    [^: ] # omits everything after colon
''', information, re.X)


# In[72]:


info = re.findall(r'''
    ([\w]+,\s[\w]+)    #lastname, first name
    (\s:\s[\'\-+.\w\d]+@[-.\w\d]+) #email address
    (\s:\s\(?\d{3}\)?\s?\d{3}-\d{4}) # phone number
    
''', information, re.X|re.I)

info


# In[73]:


for i in info:
    print(i)


# In[75]:


info = re.compile(r'''
    (?P<name>[\w]+,\s[\w]+)    #lastname, first name
    (?P<email>\s:\s[\'\-+.\w\d]+@[-.\w\d]+) #email address
    (?P<phone>\s:\s\(?\d{3}\)?\s?\d{3}-\d{4}) # phone number
    
''', re.X|re.I)


# In[77]:


for i in info.finditer(information):
    print(f"Name: {i.group('name')}\nEmail: {i.group('email')[3:]}\nPhone: {i.group('phone')[3:]}\n")


# In[ ]:


# [
#     (First and last name,
#      email, 
#      phone,
#      title,
#      Twitter handle)
# ]


# In[ ]:





# In[ ]:





# In[ ]:





# ##### In-class exercise 1: 
# 
# Use a regular expression to find every number in the given string

# In[86]:


my_string = "This string has 10909090 numbers, but - it is only 1 string. I hope you solve this 2day."

# Output: ['10909090','1',2]

pattern_num = re.compile('\d+')


found_num = pattern_num.findall(my_string)
print(found_num)


# ##### In-class Exercise 2:
# 
# Write a function using regular expressions to find the domain name in the given email addresses (and return None for the invalid email addresses)<br><b>HINT: Use '|' for either or</b>

# In[107]:


my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com", "yourfavoriteband@g6.org", "@codingtemple.com"]

def validateDomain(email):
    pattern = re.compile('[\w]+@[\w]+\W(com|org)$')
    if pattern.match(email):
        return re.findall('@[\w]+', email)[0][1:]
    else:
        return None
for email in my_emails:
    print(validateDomain(email))


# ### In-Class Exercise #3 <br>
# <p>Print each persons name and twitter handle, using groups, should look like:</p>
# <p>==============<br>
#    Full Name / Twitter<br>
#    ==============</p>
# <p>Derek Hawkins / @derekhawkins<br>
# Norrbotten Governor / @sverik<br>
# Ryan Butz / @ryanbutz</p>
# <p>etc.</p>

# In[133]:


# readlines() creates a list item for each line in your .txt file
with open("./names.txt") as f:
    data = f.readlines()
    print(data)


# In[1]:


import re
file = open('./names.txt', encoding='utf-8')
data = file.read()
file.close()
data


# In[7]:


def twitterHandles(data):
    dataLines = re.findall('.*', data)
    count = 0
    for i in dataLines:
        if len(i) > 1:
            name = re.findall('([\w\s]+|), ([\w\s-]+)\t.*', i)
            handle = re.findall('\t(@[\w]+)', i)
            count += 1
            print(f'{count} : {name[0][1]} {name[0][0]}: {"".join(handle)}')
            
twitterHandles(data)


# In[ ]:




