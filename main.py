import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import pyautogui
import webbrowser

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def combo():
    login_clicked()
    #cxone()


def cxone():
    print(f'cxone function testing testing for {test_email}')
    print(f'cxone function testing testing for {test_password}')

    url_b2 = 'https://home-b2.incontact.com/inContact/Login.aspx?ReturnUrl=%2f'
    url_c28 = 'https://home-c28.incontact.com/inContact/Login.aspx?ReturnUrl=%2f'

    driver = webdriver.Chrome(executable_path=r"C:\Users\maxwl\Downloads\chromedriver.exe")
    driver.get(url_b2)
    driver.find_element_by_id("ctl00_BaseContent_msl_txtUsername")

    form = driver.find_element_by_id('aspnetForm')
    email_field = form.find_element_by_name("ctl00$BaseContent$msl_txtUsername")
    email_field.send_keys(email1)

    button = driver.find_element_by_id('ctl00_BaseContent_btnNext')
    button.click()

    password_field = driver.find_element_by_id('ctl00_BaseContent_mslp_tbxPassword')
    password_field.send_keys(password1)

    button_2 = driver.find_element_by_id('ctl00_BaseContent_mslp_btnLogin')
    button_2.click()

    driver.maximize_window()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"c:\Users\maxwl\sc.png")

    driver.get_screenshot_as_file("foo.png")


# root window
root = tk.Tk()
root.geometry("300x500")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    test_email = email.get()
    test_password = password.get()
    radio = var.get()

    # print(test_email)
    """ callback when the login button clicked
    """
    # msg = f'You entered email: {email.get()} and password: {password.get()}'
    # showinfo(
    # title='Information',
    # message=msg
    # )
    # print(test_email)

    url_b2 = 'https://home-b2.incontact.com/inContact/Login.aspx?ReturnUrl=%2f'
    url_c28 = 'https://home-c28.incontact.com/inContact/Login.aspx?ReturnUrl=%2f'

    driver = webdriver.Chrome(executable_path=r"C:\Users\maxwl\Downloads\chromedriver.exe")

    if radio == 'c28':
        driver.get(url_c28)
    elif radio == 'b2':
        driver.get(url_b2)


    driver.find_element_by_id("ctl00_BaseContent_msl_txtUsername")

    form = driver.find_element_by_id('aspnetForm')
    email_field = form.find_element_by_name("ctl00$BaseContent$msl_txtUsername")
    email_field.send_keys(test_email)

    button = driver.find_element_by_id('ctl00_BaseContent_btnNext')
    button.click()

    password_field = driver.find_element_by_id('ctl00_BaseContent_mslp_tbxPassword')
    password_field.send_keys(test_password)

    button_2 = driver.find_element_by_id('ctl00_BaseContent_mslp_btnLogin')
    button_2.click()

    driver.maximize_window()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"c:\Users\maxwl\sc.png")

    driver.get_screenshot_as_file("foo.png")


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()
print(email_entry)

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=combo)
login_button.pack(fill='x', expand=True, pady=10)

var = tk.StringVar()
var.set('not yet')
prod = tk.Radiobutton(root, text="Prod", variable=var, value='c28').pack(side='left')
non_prod = tk.Radiobutton(root, text="Non-Prod", variable=var, value='b2').pack(side='left')

root.mainloop()


'''
1. active contacts
2. active agents 
3. make multiple calls via Hammer scripts 
    a. test menus
    b. test keywords 
4. check for results, positive or negative 
5. send results via email 
6. attach the results 



'''