from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import csv

filename = 'train_test1.csv'
headers = ["Title", "Question", "Examples", "Solution", "Python"]
leetcode_data = []
wrong = 0

def is_element_present(driver, value):
    try:
        driver.find_element(By.XPATH, value)
        return True
    except NoSuchElementException:
        return False

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

driver.get('https://leetcode.com/tag/array/')
driver.maximize_window()

table_tbody = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/table/tbody')
table_trs = table_tbody.find_elements(By.TAG_NAME, 'tr')
num_trs = len(table_trs)


# go through all the problems
for i in range(967, num_trs):
    title_td = driver.find_element(By.CSS_SELECTOR, '#app > div > div.ant-row.content__xk8m > div > div > div > table > tbody > tr:nth-child(' + str(i + 1) + ') > td:nth-child(3)')
    title = title_td.get_attribute("value")
    difficulty = driver.find_element(By.CSS_SELECTOR, '#app > div > div.ant-row.content__xk8m > div > div > div > table > tbody > tr:nth-child(' + str(i + 1) + ') > td:nth-child(5) > span').text
    if difficulty == "Hard":
        continue

    question_link = title_td.find_element(By.CSS_SELECTOR, 'div > a')

    # Perform action to open link in a new tab
    ActionChains(driver).key_down(Keys.COMMAND).click(question_link).key_up(Keys.COMMAND).perform()

    # Optionally, switch to the new tab (the last opened tab)
    driver.switch_to.window(driver.window_handles[-1])

    if is_element_present(driver, '//*[@id="__next"]/div[2]/div/div/div[4]/div[2]/div'):
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        continue


    question_div = driver.find_element(By.CLASS_NAME, 'elfjS')
    question_body = question_div.find_elements(By.XPATH, './*')

    contents = ""
    examples = ""
    read_content = True
    # constraints = []
    for p in question_body:
        p_text = p.text

        if read_content:
            if p_text == " ":
                read_content = False
            else:
                contents += p_text + "\n"
        else:
            if p_text == " ":
                break
            examples += p_text + "\n"

    # get solutions
    driver.find_element(By.XPATH, '//*[@id="solutions_tab"]/div[2]/div[2]').click()
    # get id first
    flexlayout_div = driver.find_element(By.XPATH, '//*[@id="qd-content"]/div')
    flexlayout_div_childs = flexlayout_div.find_elements(By.CLASS_NAME, 'flexlayout__tab')
    solution_id = flexlayout_div_childs[2].get_attribute('id')
    #print(solution_id)
    # click python choices
    python_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="'+solution_id+'"]/div/div/div[1]/div[2]/div/div[1]/span[3]'))
    )
    print(python_button.text)

    if python_button.text != 'Python3':
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        continue

    python_button.click()
    # FN9Jv = driver.find_element(By.XPATH, '//*[@id="' + solution_id+'"]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div')
    solutions_div = driver.find_element(By.XPATH, '//*[@id="'+solution_id+'"]/div/div/div[3]/div[3]/div[1]')
    solutions = solutions_div.find_elements(By.CLASS_NAME, 'group')

    # Here I'm thinking I just want to choose the second solution, first one has too many corner case
    solutions[5].find_element(By.TAG_NAME, 'span').click()

    solutions_code = ""
    # some solution does not have the choice
    # class_FN9Jv = driver.find_element(By.XPATH, '//*[@id="'+solution_id+'"]/div[2]/div/div/div/div[2]/div/div[1]/div[2]')
    class_FN9Jv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'FN9Jv') and contains(@class, 'WRmCx')]"))
        )
    # class_FN9Jv = driver.find_element()




    #
    # code_div = driver.find_element(By.XPATH, code_xpath)
    # language_options = code_div.find_element(By.CLASS_NAME, 'flex')
    # language_options_divs = language_options.find_elements(By.XPATH, './*')
    #
    # # find python language
    # for option in language_options_divs:
    #     if option.text == "Python":
    #         option.click()
    #
    # # start from here, i think all solution have the following
    # group_relative = code_div.find_element(By.CLASS_NAME, 'group')
    # solutions_code = group_relative.find_element(By.TAG_NAME, 'pre').text

    # group_relative = driver.find_element(By.XPATH, '//*[@id="'+solution_id+'"]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div/div')
    # mb_6 = WebDriverWait(class_FN9Jv, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'mb-6'))
    #     )
    mb6_divs = driver.execute_script("""
        var class_FN9Jv = arguments[0];
        return class_FN9Jv.getElementsByTagName('div');
        """, class_FN9Jv)

    # Convert the result to a list of WebElements
    mb6_divs = list(mb6_divs)
    # print(len(mb6_divs))

    for mb_6 in mb6_divs:
        pre_text = driver.execute_script("""
            var mb_6 = arguments[0];
            var preElement = mb_6.getElementsByTagName('pre')[0];
            return preElement ? preElement.textContent : null;
            """, mb_6)

        if pre_text != None and pre_text[: 14] == "class Solution":
            solutions_code = pre_text

    #print(solutions_code)
    # solutions_code = class_FN9Jv.find_element(By.TAG_NAME, 'pre').text

    # store this quesiton data
    is_python = "def" in solutions_code
    if is_python:
        wrong += 1

    curr_question = [title, contents, examples, solutions_code, is_python]
    leetcode_data.append(curr_question)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the headers
        writer.writerow(headers)
        # Write the data rows
        writer.writerows(leetcode_data)
    print(i)

    # close current page
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])








print(wrong)