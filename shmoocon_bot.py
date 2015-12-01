 # -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.shmoocon.org/human-registration")

known_links = [
    u"General Ticket Information",
    u"here",
    u"Ticket Oddities",
    u"Call For Papers Closes Today",
    u"Payment Issues with Firefox",
    u"First Round Stats and Info",
    u"First Round of Tix Sales Tomorrow….",
    u"Early Accepts – ShmooCon 2016",
    u"CFP Early Bird Deadline is Friday",
    u"Hotel Block is Open",
    u"Call for Papers 2016",
    u"New site – more to come.",
    u"Tweets by @ShmooCon",
    u"General Ticket Information"
]

tab_opened = False

while True:
    driver.refresh()

    try:
        tbody = driver.find_element_by_id("main-section")
        links = tbody.find_elements_by_tag_name("a")
    except:
        pass

    for link in links:
        if hasattr(link, "text"):
            if link.text not in known_links and link.is_displayed() == True:
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
