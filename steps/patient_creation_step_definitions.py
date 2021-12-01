import time

import unittest
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

first_name = "Ernest"
middle_name = "Kwame"
last_name = "Amuzu"
phone_number = '0543273508'
date_of_birth = '04181992'
address = "C/O RUTH ESI AMUZU, U.P.O.BOX 63, KNUST - KUMASI,GHANA"
full_name = first_name + " " + middle_name + " " + last_name

# destructuring the date of birth
month = date_of_birth[0:2]
day = date_of_birth[2:4]
year = date_of_birth[4:8]


@given('I open the a browser and navigate to the URL')
def navigate_to_url(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("http://localhost:3000/")
    context.driver.maximize_window()


@when("I type the patient's first name")
def type_patient_first_name(context):
    context.driver.find_element(By.XPATH, "//input[@data-test-id='first-name']").send_keys(first_name)


@then("I type the patient's middle name")
def type_patient_middle_name(context):
    context.driver.find_element(By.XPATH, "//input[@data-test-id='middle-name']").send_keys(middle_name)


@then("I type the patient's last name")
def type_patient_last_name(context):
    context.driver.find_element(By.XPATH, "//input[@data-test-id='last-name']").send_keys(last_name)


@then("I type the patient's phone number")
def type_patient_phone_number(context):
    context.driver.find_element(By.XPATH, "//input[@data-test-id='phone-number']").send_keys(phone_number)


@then("I type the patient's date of birth")
def type_patient_date_of_birth(context):
    context.driver.find_element(By.XPATH, "//input[@data-test-id='dob']").send_keys(date_of_birth)


@then("I type the patient's address")
def type_patient_address(context):
    context.driver.find_element(By.XPATH, "//textarea[@data-test-id='address']").send_keys(address)


@when("I click on the add new user button")
def click_add_new_user_button(context):
    context.driver.find_element(By.XPATH, "//a[@data-test-id='submit-btn']").click()


@then("I should see the added patient's full name")
def check_patient_full_name(context):
    text_to_check = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div[2]/main/div[1]/div[2]/h4").text
    assert full_name == text_to_check


@then("I should see the added patient's address")
def check_patient_address(context):
    text_to_check = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div[2]/main/div[1]/div[2]/p[1]").text
    assert address in text_to_check


@then("I should see the added patient's date of birth")
def check_patient_date_of_birth(context):
    final_date = format_day(day) + " " + get_month(month) + " " + year
    print(final_date)
    text_to_check = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div[2]/main/div[1]/div[2]/p[2]").text
    assert final_date in text_to_check
    time.sleep(5)


def format_day(dayton):
    if 10 <= int(dayton) <= 20:
        return dayton + "th"
    elif int(dayton) % 10 == 1:
        return dayton + "st"
    elif int(dayton) % 10 == 2:
        return dayton + "nd"
    elif int(dayton) % 10 == 3:
        return dayton + "rd"
    else:
        return dayton + "th"


def get_month(monthon):
    if int(monthon) == 1:
        return "January"
    elif int(monthon) == 2:
        return "February"
    elif int(monthon) == 3:
        return "March"
    elif int(monthon) == 4:
        return "April"
    elif int(monthon) == 5:
        return "May"
    elif int(monthon) == 6:
        return "June"
    elif int(monthon) == 7:
        return "July"
    elif int(monthon) == 8:
        return "August"
    elif int(monthon) == 9:
        return "September"
    elif int(monthon) == 10:
        return "October"
    elif int(monthon) == 11:
        return "November"
    elif int(monthon) == 12:
        return "December"
    else:
        return monthon + " wrong month"
