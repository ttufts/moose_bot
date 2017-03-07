 # -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://landing.shmoocon.org/")

known_links = [
]

tab_opened = False

while True:
    driver.refresh()

    try:
        tbody = driver.find_element_by_id("main-section")
        links = tbody.find_elements_by_tag_name("a")
    except:
        continue

    for link in links:
        if hasattr(link, "text"):
            if link.text not in known_links and (link.is_displayed() == True):
                tab_opened = True
                actions = ActionChains(driver)
                actions.move_to_element(link)
                actions.send_keys(Keys.COMMAND)
                actions.click(link)
                actions.perform()

        if tab_opened:
            print "Opened tab. Sleeping 10 seconds"
            time.sleep(10)

    time.sleep(.1)
