import os
import time

from selenium import webdriver
from behave import given
from behave import when
from behave import then
from behave import runner


def setup_webdriver(context: runner.Context) -> None:
    path_to_chromedriver = os.path.join(os.getcwd(), 'code/chromedriver')
    context.driver = webdriver.Chrome(executable_path=path_to_chromedriver)

@given(u'the user navigates to the URL {url}')
def step_impl(context: runner.Context, url: str) -> None:
    pass


@when(u'the user fills in the string {first_string} in the first-field')
def step_imp(context: runner.Context, first_string: str) -> None:
    pass


@when(u'the user fills in the string {second_string} in the second-field')
def step_impl(context: runner.Context, second_string: str) -> None:
    pass


@when(u'the user submits the form')
def step_impl(context:runner.Context):
    pass


@then(u'The URL the user is on is {end_url}')
def step_impl(context:runner.Context, end_url: str):
    pass
