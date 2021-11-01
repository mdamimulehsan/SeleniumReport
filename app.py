# pip install pyhtmlreport
#18201066, 18201050, 18201063
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

report = Report()
s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)

report.setup(
    report_folder=r'E:\CSE 322\Selenium Testing\Reports',
    module_name='Report',
    release_name='Release 1',
    selenium_driver=driver
)


# Test case 1 Open The project
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Home Page Loading',
        status=report.status.Start,
        test_number=1
    )
    # print(driver.title)
    # time.sleep(5)
    assert (driver.title == 'Courses')
    report.write_step(
        'Perfactly landing in the home page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Perfactly not landing in the home page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 2 create a user with password error
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Create a user with password not matching error',
        status=report.status.Start,
        test_number=2
    )
    driver.find_element(By.LINK_TEXT, 'Signup').click()
    driver.find_element(By.ID, "id_first_name").send_keys('Amimul')
    # time.sleep(3)
    driver.find_element(By.ID, "id_last_name").send_keys('Ehsan')
    # time.sleep(2)
    driver.find_element(By.ID, "id_username").send_keys('ehsan')
    # time.sleep(2)
    driver.find_element(By.ID, "id_email").send_keys('ehsan@gmail.com')
    # time.sleep(2)
    driver.find_element(By.ID, "id_password1").send_keys('ehsan1234')
    # time.sleep(2)
    driver.find_element(By.ID, "id_password2").send_keys('ehsan1256')
    # time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]').click()
    assert driver.title == 'Signup'
    report.write_step(
        'Password does not match result succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Password does not match result not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 3 create a user without error
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Create a User without error',
        status=report.status.Start,
        test_number=3
    )
    driver.find_element(By.LINK_TEXT, 'Signup').click()
    driver.find_element(By.ID, "id_first_name").send_keys('Amimul')
    # time.sleep(3)
    driver.find_element(By.ID, "id_last_name").send_keys('Ehsan')
    # time.sleep(2)
    driver.find_element(By.ID, "id_username").send_keys('ehsan')
    # time.sleep(2)
    driver.find_element(By.ID, "id_email").send_keys('ehsan@gmail.com')
    # time.sleep(2)
    driver.find_element(By.ID, "id_password1").send_keys('cse12345')
    # time.sleep(2)
    driver.find_element(By.ID, "id_password2").send_keys('cse12345')
    # time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]').click()
    assert driver.title == 'Login'
    report.write_step(
        'User Created',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'User Not created',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 4 login a user with both error
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Login a User with both user & pass error',
        status=report.status.Start,
        test_number=4
    )
    driver.find_element(By.LINK_TEXT, 'Login').click()
    driver.find_element(By.ID, "id_username").send_keys('mehrab')
    # time.sleep(3)
    driver.find_element(By.ID, "id_password").send_keys('cse1234')
    # time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]').click()
    assert driver.title == 'Login'
    report.write_step(
        'Both user & pass error succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Both user & pass error not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 5 Login a User with user couldn't find error
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Login a User with user could not find error',
        status=report.status.Start,
        test_number=5
    )
    driver.find_element(By.LINK_TEXT, 'Login').click()
    driver.find_element(By.ID, "id_username").send_keys('Mehrab')
    # time.sleep(3)
    driver.find_element(By.ID, "id_password").send_keys('amimul12345')
    # time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]').click()
    assert driver.title == 'Login'
    report.write_step(
        'User could not find error succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'User could not find error not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


# Test case 6 Login a User without error
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Login a User without error',
        status=report.status.Start,
        test_number=6
    )
    driver.find_element(By.LINK_TEXT, 'Login').click()
    driver.find_element(By.ID, "id_username").send_keys('ehsan@gmail.com')
    # time.sleep(3)
    driver.find_element(By.ID, "id_password").send_keys('cse12345')
    # time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div/form/input[2]').click()
    assert driver.title == 'Courses'
    report.write_step(
        'Login a User succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Login a User is not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# # Test case 7 Enroll a course unpaid course and check
# driver.get('http://127.0.0.1:8000/')
# try:
#     # Start of Test
#     report.write_step(
#         'Enroll a course unpaid course and check',
#         status=report.status.Start,
#         test_number=7
#     )
#     driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/a').click()
#     # time.sleep(3)
#     driver.find_element(By.LINK_TEXT, 'Home').click()
#     # time.sleep(2)
#     driver.find_element(By.LINK_TEXT, 'My Courses').click()
#
#     report.write_step(
#         'Course added succesfull',
#         status=report.status.Pass,
#         screenshot=True
#     )
# except Exception as e:
#     report.write_step(
#         f'Something went wrong during execution!</br>{e}',
#         status=report.status.Warn,
#         screenshot=True
#     )

# Test case 7 Enroll a course paid course and check payment system work
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Enroll a course paid course and check payment system work',
        status=report.status.Start,
        test_number=7
    )
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div/div[1]/a').click()
    # time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/a').click()
    # time.sleep(2)


    report.write_step(
        'Payment method working succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 8 Logout a user
driver.get('http://127.0.0.1:8000/')
try:
    # Start of Test
    report.write_step(
        'Logout a user',
        status=report.status.Start,
        test_number=8
    )
    driver.find_element(By.LINK_TEXT, 'Logout').click()

    assert driver.title == 'Courses'
    report.write_step(
        'Logout succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Logout not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
# Test case 9 Login a SuperUser
driver.get('http://127.0.0.1:8000/admin/')
try:
    # Start of Test
    report.write_step(
        'Login a SuperUser',
        status=report.status.Start,
        test_number=9
    )
    driver.find_element(By.ID, "id_username").send_keys('nabi')
    # time.sleep(3)
    driver.find_element(By.ID, "id_password").send_keys('nabi1234')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    assert driver.title == 'Site administration | Django site admin'
    report.write_step(
        'SuperUser login succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'SuperUser login is not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test case 10 Change password of a SuperUser
driver.get('http://127.0.0.1:8000/admin/')
try:
    # Start of Test
    report.write_step(
        'Change password of a SuperUser',
        status=report.status.Start,
        test_number=10
    )
    driver.find_element(By.LINK_TEXT, 'CHANGE PASSWORD').click()
    driver.find_element(By.ID, "id_old_password").send_keys('nabi1234')
    # time.sleep(2)
    driver.find_element(By.ID, "id_new_password1").send_keys('1234nabi')
    # time.sleep(2)
    driver.find_element(By.ID, "id_new_password2").send_keys('1234nabi')
    # time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="content-main"]/form/div/div/input').click()
    assert driver.title == 'Password change successful'
    report.write_step(
        'Password change succesfull',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Password change is not succesfull',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

finally:
    report.generate_report()
    driver.quit()
