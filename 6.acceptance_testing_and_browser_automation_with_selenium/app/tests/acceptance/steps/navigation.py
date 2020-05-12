from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url)



@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    # expected_url = 'http://127.0.0.1:5000/blog'
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    # expected_url = 'http://127.0.0.1:5000/'
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
