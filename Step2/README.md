
# Setting Up Selenium on your Machine

So you’ve gotten Behave pretty much handled at this point? Great! If not and you’re skipping ahead anyway, go for it, I won’t judge. Paul might though.

For MacOS Users

If you’re using a Macbook/iMac, the script `Setting_up_Selenium_on_your_Machine/install_selenium.sh` will download and unzip the latest Chromedriver executable for MacOS that will be needed to interact with Chrome when running Selenium.



For everyone else (just kidding, For Windows Users)

If you’re on a Windows machine, you can use this link to manually download the zipped chromedriver.exe file by clicking this link:

	https://chromedriver.storage.googleapis.com/78.0.3904.11/chromedriver_win32.zip


# Testing Selenium

The following code in `Setting_up_Selenium_on_your_Machine/code` shows a short example of a ‘Hello world’ implementation using Selenium.

## How it works

The example code links to the chromedriver (already in this directory), opens a browser session and navigates to https://www.google.com.

Once there, it types a “Hello world” message into the search bar and hits “Search”.

And presto, you’ve seen/done your first Selenium test (in the past 20 seconds).

This is another light example of what the code does. To get a detailed explanation of each line of code, refer to the source code.`


Done? Onwards to Step3 : Running Behave Alongside Selenium





