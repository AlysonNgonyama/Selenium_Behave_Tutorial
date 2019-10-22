


# The first step, like any Python script, is to import all the modules you'll be using.
# In this case, you'll need the selenium.webdriver, which will help initialize a Chrome browser session,
# the os command that'll help us make a path that points at our recently downloaded chromdriver
# and time to help us halt our program as the browser loads; but more on this a little later.


# Import webdriver (needed to initialize a Chrome session)
from selenium import webdriver

# Import OS (We'll need this for dynamically making a path that points to our chromedriver executable.

import os

# We'll need a few delays to coordinate with page loads or else our script will break as it
# executes too quickly
import time

# For Selenium's webdriver to function, we need the chromedriver to exist in one of the directories
# listed in our PATH env variable (in the command line, type 'env').
# One method is to manually open one of these directories (i.e /bin/usr, /bin/) and drop our
# chromedriver in here.
# The other approach is to temporarily add the chromedriver to the path (as done below).

# this creates the string.
exe_path = os.path.join(os.getcwd(), 'chromedriver')

# and this line both initializes the Chrome webdriver session, while pointing the
# executable path to the one we set above.
# Note that if you choose to put the chromedriver directly into a directory listed
# in your PATH, you can initialize the webdriver like (webdriver.Chrome()) without
# an extra arguments.

driver = webdriver.Chrome(executable_path=exe_path)


# Once our session's been established, the get() method will take us to whatever
# URL is passed to it as a parameter; (in this case https://www.google.com)
driver.get('https://www.google.com')

# Our first arbitrary sleep. We wait 5 seconds while Google's homepage loads.
# There's a better way to do this but more on that some other time.
time.sleep(5)

# driver.find_element_by_name scans the "HTML" of the page for an element with the page name
# passed in as a parameter; in this case, the name 'q'.
# This is the name of the search bar.
element = driver.find_element_by_name('q')

# send_keys() allows us to send a string of text to the targeted element, in this case
# the search bar with the element name 'q'. This is the same as typing 'Hello Webdriver; into
# your Google search bar.

element.send_keys('hello Webdriver;')

# We finally submit our incredibly complex query and have our search results returned.
element.submit()

# And just like that, you've run a Google search telekinetically. It's a huge achievement.
# Now the gloves come off..
