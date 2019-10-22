import os
import time

from selenium import webdriver
from behave import given
from behave import when
from behave import then
from behave import runner


def setup_webdriver(context: runner.Context) -> None:
    path_to_chromedriver = os.path.join(os.getcwd(), 'tutorial/chromedriver')
    context.driver = webdriver.Chrome(executable_path=path_to_chromedriver)

@given(u'the user navigates to the URL {url}')
def step_impl(context: runner.Context, url: str) -> None:
    setup_webdriver(context)
    context.driver.get('http://127.0.0.1:5000')

@when(u'the user fills in the string {first_string} in the first-field')
def step_imp(context: runner.Context, first_string: str) -> None:
    time.sleep(1)
    context.driver.find_element_by_id('first_field').send_keys(first_string)

@when(u'the user fills in the string {second_string} in the second-field')
def step_impl(context: runner.Context, second_string: str) -> None:
    context.driver.find_element_by_id('second_field').send_keys(second_string)

@when(u'the user submits the form')
def step_impl(context:runner.Context):
    context.driver.find_element_by_name('submit').click()


@then(u'The URL the user is on is {end_url}')
def step_impl(context:runner.Context, end_url: str):
    url_value = context.driver.current_url
    context.driver.close()
    print('url value is ', url_value)
    assert url_value == end_url
