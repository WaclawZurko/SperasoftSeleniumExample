from unicodedata import name
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC	

MAIN_MENU_ABOUT = "//a[contains(text(), 'About')]"
FANCY_TITLE = '//*[@id="fancy-title-4"]'
FANCY_DESCRIPTION = '//*[@id="fancy-title-5"]'
LEADERSHIP_TEAM_TITLE = '//*[@id="fancy-title-9"]'
EMPLOYEES = '//ul[@class="employees-grid__items"]'
OUR_CLIENTS_TITLE = '//*[@id="clients"]'
OUR_CLIENTS = '//div[@class="clients clients--columns-5 mk-animate-element fade-in mk-in-viewport"]'


@given('we start at mainpage')
def open_mainpage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://sperasoft.com/')
    context.driver.maximize_window()

@when('we click at about page')
def click_at_about_page(context):
    context.driver.find_element("xpath", MAIN_MENU_ABOUT).click()

@then('we should land on about page')
def assert_landing_on_about_page(context):
    WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, FANCY_TITLE)))
    assert context.driver.find_element('xpath', FANCY_TITLE).is_displayed()

@then('we should see first company description')
def assert_company_description_is_visible(context):
    WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, FANCY_DESCRIPTION)))
    assert context.driver.find_element('xpath', FANCY_DESCRIPTION).is_displayed()

@then('we should see leadership {name} and {position}')
def assert_leadership_team_is_visible(context, name, position):
    WebDriverWait(context.driver, 15).until(EC.presence_of_element_located((By.XPATH, LEADERSHIP_TEAM_TITLE)))
    element = context.driver.find_element('xpath', LEADERSHIP_TEAM_TITLE)
    element.location_once_scrolled_into_view
    WebDriverWait(context.driver, 15).until(EC.presence_of_element_located((By.XPATH, EMPLOYEES)))
    assert name in context.driver.page_source
    assert position in context.driver.page_source

@then('we should see {brand} logo')
def assert_brand_logo_is_visible(context, brand):
    WebDriverWait(context.driver, 15).until(EC.presence_of_element_located((By.XPATH, OUR_CLIENTS_TITLE)))
    element = context.driver.find_element('xpath', OUR_CLIENTS)
    element.location_once_scrolled_into_view
    WebDriverWait(context.driver, 15).until(EC.presence_of_element_located((By.XPATH, OUR_CLIENTS)))
    assert brand in context.driver.page_source