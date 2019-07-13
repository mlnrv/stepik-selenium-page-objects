from math import log, sin
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def solve_quiz_and_get_code(self):
    # sleep(1)
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(log(abs((12 * sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    sleep(1)
    try:
        alert = self.browser.switch_to.alert
        print("Your code: {}".format(alert.text))
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")