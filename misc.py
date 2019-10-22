



# Halting your program in Selenium for the shortest amount of time possible.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = '[test xpath]' # This is a test path that points to the element you want to target.
					  # This can be anything; Xpath, element_by_id or element_by_class tag etc.

wait_time = 300		  # This defines the max amount of seconds your script will 'sleep' for before
					  # giving up and throwing a TimeoutException error on the element not rendering.
					  # Note that this implies that your program will EITHER continue when the element
					  # being targeted becomes visible or will crash when 300 seconds are up.

# The WebDriverWait function is what makes this possible. It takes in the webdriver element
# created when Selenium is initialized as well as the wait_time you've specified.

# The until method allows you to specify what condition the wait_time is waiting for before
# it hits its timeout.

# EC.element_to_be_clickable is the specified condition. The wait will only break once the element
# specified in 'path' can be clicked/is clickable.

# By.XPATH specifies that the element you're targeting is an XPATH.
# there're various elements you can specify for your targeting;
# refer to selenium.webdriver.common.by.By's documention

target = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, path))
)
target.click()









