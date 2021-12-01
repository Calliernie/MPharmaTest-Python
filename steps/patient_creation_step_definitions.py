import time

from locators.patient_creation_page_locators import PatientCreationPageLocators
from helpers.date_destructurer import DateDestructurer
from helpers.month_destructurer import MonthDestructurer
from config.set_up import Setup
from behave import given, when, then
from selenium.webdriver.common.by import By

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
    context.driver = Setup.get_driver()
    context.driver.get("http://localhost:3000/")
    context.driver.maximize_window()


@when("I type the patient's first name")
def type_patient_first_name(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.first_name_xpath).send_keys(first_name)


@then("I type the patient's middle name")
def type_patient_middle_name(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.middle_name_xpath).send_keys(middle_name)


@then("I type the patient's last name")
def type_patient_last_name(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.last_name_xpath).send_keys(last_name)


@then("I type the patient's phone number")
def type_patient_phone_number(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.phone_number_xpath).send_keys(phone_number)


@then("I type the patient's date of birth")
def type_patient_date_of_birth(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.date_of_birth_xpath).send_keys(date_of_birth)


@then("I type the patient's address")
def type_patient_address(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.address_xpath).send_keys(address)


@when("I click on the add new user button")
def click_add_new_user_button(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.add_new_user_button_xpath).click()


@then("I should see the added patient's full name")
def check_patient_full_name(context):
    text_to_check = context.driver.find_element(By.XPATH, PatientCreationPageLocators.created_user_full_name_xpath).text
    assert full_name == text_to_check


@then("I should see the added patient's address")
def check_patient_address(context):
    text_to_check = context.driver.find_element(By.XPATH, PatientCreationPageLocators.created_user_address).text
    assert address in text_to_check


@then("I should see the added patient's date of birth")
def check_patient_date_of_birth(context):
    final_date = DateDestructurer.format_day(day) + " " + MonthDestructurer.get_month(month) + " " + year
    print(final_date)
    text_to_check = context.driver.find_element(By.XPATH, PatientCreationPageLocators.created_user_date_of_birth).text
    assert final_date in text_to_check
    time.sleep(5)
