import sys
import os
import boto.ec2
from boto.ec2.connection import EC2Connection
import boto.rds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from random import randint
import sqlite3
import pymysql
from warnings import filterwarnings, resetwarnings
import poplib
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from urllib.request import urlretrieve, urlopen
import subprocess
from cv2 import cv2
import numpy as np
import imutils
import aws_credentials.py



def create_account(self):

    signup_first_name_xpath = ".//input[@class='inputtext _58mg _5dba _2ph-' and @aria-label='First name']"
    signup_last_name_xpath = ".//input[@class='inputtext _58mg _5dba _2ph-' and @aria-label='Last name']"
    signup_username_xpath = (".//input[contains(@class, 'inputtext _58mg _5dba _2ph-') "
                             "and @aria-label='Mobile number or email']")
    # signup_username_alternate_xpath = (".//input[@class='inputtext _58mg _5dba _2ph- focused' "
    #                          "and @aria-label='Mobile number or email']")
    signup_username_confirm_xpath = (".//input[contains(@class, 'inputtext _58mg _5dba _2ph-') "
                                     "and contains(@aria-label, 'Re-enter')]")
    signup_password_xpath = ".//input[@class='inputtext _58mg _5dba _2ph-' and @aria-label='New password']"
    signup_month_id = "month"
    signup_day_id = "day"
    signup_year_id = "year"
    signup_sex_female_xpath = ".//input[@name='sex' and @value='1']"
    # Confirm button can be "Sign Up" or "Create Account" so its better to use css
    signup_confirm_button_css = "._6j.mvm._6wk._6wl._58mi._3ma._6o._6v"
    signup_confirm_button_xpath = ".//button[text()='Create Account']"
    # Cant use the signup_confirm_button_css for this one since the old element still exists
    signup_captcha_confirm_button_xpath = ".//button[@id='u_0_n']"
    # Can use it now?
    signup_captcha_confirm_button_css = "._6j.mvm._6wk._6wl._58me._58mi._3ma._6o._6v"

    signup_find_your_friends_xpath = ".//span[text()='Find your friends']"
    fb_early_code_entry_check_xpath = ".//h2[text()='Enter the code from your email']"
    fb_early_code_entry_not_now_button_css = ".mls._42ft._4jy0._4jy4._517h._51sy"
    fb_early_code_entry_not_now_link_xpath = ".//a[text()='Not Now']"
    fb_needs_phone_verification_check_xpath = ".//div[text()='Use a phone to verify your account']"

    tuta_signup_email_xpath = ".//input[@id='mailAddress']"
    tuta_signup_password_xpath = ".//input[@id='newpassword']"
    tuta_signup_password_confirm_xpath = ".//input[@id='newpassword2']"
    tuta_signup_terms_checkbox_xpath = ".//input[@id='termsInput']"
    tuta_signup_age_checkbox_xpath = ".//input[@id='ageInput']"
    tuta_signup_confirm_button_xpath = ".//button[@class='single fontImage confirm' and @type='submit']"
    tuta_signup_captcha_textbox_xpath = ".//input[@id='captchaInput']"
    tuta_signup_captcha_image_xpath = ".//img[@id='captchaDisplay']"

    fb_signup_captcha_image_xpath = ".//img[@style='display:block;']"
    fb_signup_captcha_textbox_xpath = ".//input[@id='captcha_response']"

    tuta_signup_loading_alert_xpath = ".//h2[text()='Loading Tutanota...']"
    tuta_signup_creating_account_alert_xpath = ".//h2[text()='Account is being created ...']"

    tuta_signup_ip_ban_alert_message = "Registration is temporarily blocked"

    tuta_signup_ip_ban_alert_xpath = ".//div[contains(text(), '%s')]" % tuta_signup_ip_ban_alert_message

    tuta_fb_confirmation_number_xpath = ".//div[contains(text(), 'is your Facebook confirmation code')]"
    tuta_fb_confirmation_subject2_xpath = ".//div[contains(text(), 'Just one more step to get started')]"
    tuta_fb_confirmation_number2_xpath = ".//td[contains(@style, 'lucidagrande')]"

    fb_enter_code_xpath = ".//a[text()='Enter Code']"
    fb_code_textbox_xpath = ".//input[@name='code']"
    fb_code_confirm_button_css = "._42ft._4jy0.layerConfirm._2z1w.uiOverlayButton._4jy3._4jy1.selected._51sy"
    fb_code_confirm_button_xpath = ".//button[@type='submit']"
    "_42ft mls _4jy0 _4jy4 _4jy1 selected _51sy"
    fb_account_confirmed_xpath = ".//div[text()='Account Confirmed']"
    fb_account_confirmed_okay_button_xpath = ".//a[@data-testid='confirm_code_dialog_submit_close']"
    fb_account_confirmed_okay_button_css = "._42ft._42fu.layerCancel.uiOverlayButton.selected._42g-._42gy"
    fb_top_left_icon_css = "._2md"
    fb_find_friends_next_button_xpath = ".//a[text()='Next']"
    fb_find_friends_next_button_css = "._42ft._4jy0.rfloat._ohf._4jy4._517h._51sy"
    fb_find_friends_skip_button_xpath = ".//a[text()='Skip step']"
    fb_find_friends_skip_button_css = "._42ft._4jy0.layerConfirm.uiOverlayButton._4jy3._517h._51sy"
    fb_enter_mobile_number_button_css = "._42ft._42fu.selected._42g-"
    fb_phone_number_entry_textbox_css = ".inputtext"
    fb_phone_number_confirm_button_css = "._42ft._42fu.layerConfirm.uiOverlayButton.selected._42g-._42gy"
    fb_phone_code_entry_textbox_css = ".inputtext.mts"
    # You can reuse the confirm button for this one. The first one is "Continue" and this one is "Confirm", if need

    tuta_login_email_textbox_xpath = ".//input[@id='loginMailAddress']"
    tuta_login_password_textbox_xpath = ".//input[@id='loginPassphrase']"
    tuta_login_confirm_button_xpath = ".//button[@id='submitLogin']"

    first_names = ["Emily", "Emma", "Madison", "Abigail", "Olivia", "Isabella", "Hannah", "Samantha", "Ava",
                   "Ashley", "Sophia", "Elizabeth", "Eli", "Alexis", "Grace", "Sarah", "Alyssa", "Natalie",
                   "Chloe", "Bri", "Lauren", "Ella", "Anna", "Kayla", "Hailey", "Jessica", "Victoria", "Jasmine",
                   "Sydney", "Julia", "Morgan", "Kaitlyn", "Savannah", "Katherine", "Alexandra", "Rachel", "Lily",
                   "Megan", "Kaylee", "Jennifer", "Angelina", "Makayla", "Allison", "Brooke", "Lillian", "Faith"]
    last_names = ["Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                  "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Robinson", "Clark",
                  "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Hill", "Green", "Adams",
                  "Baker", "Nelson", "Carter", "Mitchell", "Roberts", "Turner", "Phillips", "Campbell", "Parker"]

    first_name_index = randint(0, len(first_names) - 1)
    last_name_index = randint(0, len(last_names) - 1)
    first_name = first_names[first_name_index]
    last_name = last_names[last_name_index]

    email_rand_int = randint(100, 99999)
    email = first_name + last_name + str(email_rand_int) + "@tutanota.com"
    tuta_email = first_name + last_name + str(email_rand_int)
    full_name = first_name + " " + last_name

    captcha_exists = False
    tuta_pass = "idontkn0w22"
    fb_pass = str(randint(1000000, 9999999))
    captcha_id = str(randint(1000000, 9999999))
    captcha_id_fb = str(randint(1000000, 9999999))

    try:

        # Tuta Signup

        driver.get("https://app.tutanota.com/#register")

        # Wait for the loading alert to appear then disappear
        # i = 0
        # while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_loading_alert_xpath, 0):
        #     print("Loading alert has not appeared yet.")
        #     time.sleep(1)
        #     i += 1
        #     if i > 30:
        #         print("Been waiting for loading alert to appear for 30 seconds. Giving up")
        #         break
        # i = 0
        # while selenium_api.element_is_clickable(By.XPATH, tuta_signup_loading_alert_xpath, 0):
        #     print("Loading alert is still active")
        #     time.sleep(1)
        #     i += 1
        #     if i > 30:
        #         print("Been waiting for loading alert to disappear for 30 seconds. Giving up.")
        #         break
        # time.sleep(3)  # Wait after the alert is gone for good measure

        # Start filling in the signup form
        wait()
        selenium_api.wait_and_send_keys_on_element(By.XPATH, tuta_signup_email_xpath, key=tuta_email)
        # wait()
        # driver.find_element_by_xpath(tuta_signup_email_xpath).send_keys(tuta_email)
        wait()
        driver.find_element_by_xpath(tuta_signup_password_xpath).send_keys(tuta_pass)
        wait()
        driver.find_element_by_xpath(tuta_signup_password_confirm_xpath).send_keys(tuta_pass)
        wait()
        driver.find_element_by_xpath(tuta_signup_terms_checkbox_xpath).click()
        wait()
        driver.find_element_by_xpath(tuta_signup_age_checkbox_xpath).click()
        wait()

        # Wait for the confirm button to be active, then click on it
        i = 0
        while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_confirm_button_xpath, 0):
            time.sleep(1)
            i += 1
            if i > 30:
                print("Couldn't click on tuta signup confirm button for over 30 seconds. Giving up.")
                return "Couldn't click on tuta signup confirm button for over 30 seconds"

        wait()

        # Wait for the creating account alert to appear unless the captcha or IP ban elements are present
        i = 0
        while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_creating_account_alert_xpath, 0):
            if selenium_api.element_is_present(By.XPATH, tuta_signup_captcha_textbox_xpath):
                print("Captcha element exists")
                captcha_exists = True
                break
            if selenium_api.element_is_present(By.XPATH, tuta_signup_ip_ban_alert_xpath):
                print("IP Ban alert exists")
                return "Tuta IP Ban"
            print("Creating account alert has not appeared yet. Captcha element has not appeared yet.")
            time.sleep(1)
            i += 1
            if i > 30:
                print("Been waiting for creating account alert or captcha element to appear for 30 seconds. "
                      "Giving up.")
                return "Been waiting for creating account alert or captcha element to appear for 30 seconds"

        wait()

        # If captcha exists, solve it
        if captcha_exists:
            # Solve the captcha
            print("Solving Captcha...")
            captcha_image = driver.find_element_by_xpath(tuta_signup_captcha_image_xpath)
            image_link = captcha_image.get_attribute("src")
            save_captcha_location = r"C:\temp\captcha-example.png"
            urlretrieve(image_link, save_captcha_location)
            time.sleep(5)
            captcha_answer = get_time_from_image(save_captcha_location)
            # email_bot.send_email_attachment(save_captcha_location, subject="Cap " + captcha_id)
            # captcha_answer = email_bot.check_email(email_subject_check="Re: Cap " + captcha_id)
            driver.find_element_by_xpath(tuta_signup_captcha_textbox_xpath).send_keys(captcha_answer)

            wait()

            # Wait for the confirm button to be active, then click on it
            i = 0
            while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_confirm_button_xpath, 0):
                time.sleep(1)
                i += 1
                if i > 30:
                    print("Couldn't click on tuta signup confirm button for over 30 seconds. Giving up.")
                    return "02 - Couldn't click on tuta signup confirm button for over 30 seconds"

            wait()

            # Wait for the creating account alert to appear
            i = 0
            while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_creating_account_alert_xpath, 0):
                print("Creating account alert has not appeared yet. Captcha element has not appeared yet.")
                time.sleep(1)
                i += 1
                if i > 30:
                    print("Been waiting for creating account alert to appear for 30 seconds. Giving up")
                    return "Been waiting for creating account alert to appear for 30 seconds"

        wait()

        # Waiting for the creating account alert to disappear
        i = 0
        print("Waiting 5 minutes for the creating account alert to disappear...")
        while selenium_api.element_is_clickable(By.XPATH, tuta_signup_creating_account_alert_xpath, 0):
            time.sleep(1)
            i += 1
            if i > 300:
                print("Been waiting for creating account alert to disappear for 5 minutes. Giving up.")
                return "Been waiting for creating account alert to disappear for 5 minutes"

        wait()

    except Exception as e:
        print("Something went wrong during account creation process.")
        print(e)
        return "Uncaught exception during Tuta account creation"
