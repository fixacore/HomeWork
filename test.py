﻿from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get("https://www.ultimateqa.com/complicated-page/")
button1=chrome.find_element_by_class_name("et_pb_button_0")
button1.click()
button2=chrome.find_element_by_xpath("//a[@class='et_pb_button et_pb_button_1 et_pb_bg_layout_light']")
button2.click()
chrome.back()
twit1=chrome.find_element_by_xpath("//li[@class='et_pb_social_media_follow_network_0 et_pb_social_icon et_pb_social_network_link  et-social-twitter et_pb_social_media_follow_network_0']/a")
twit1.click()
chrome.back()
face1=chrome.find_element_by_xpath("//li[@class='et_pb_social_media_follow_network_1 et_pb_social_icon et_pb_social_network_link  et-social-facebook et_pb_social_media_follow_network_1']/a")
face1.click()
chrome.back()
field1=chrome.find_element_by_id("s")
search1=chrome.find_element_by_id("searchsubmit")
search1.click
img1=chrome.find_element_by_css_selector('img.widgets-list-layout-blavatar')
img1.click()
link1=chrome.find_element_by_css_selector("a.bump-view")
link1.click()
field2=chrome.find_element_by_css_selector("input.required")
field2.click()
subscribe1=chrome.find_element_by_name('jetpack_subscriptions_widget')
subscribe1.click()
fieldName1=chrome.find_element_by_id('et_pb_contact_name_0')
fieldName1.click()
fieldEmail1=chrome.find_element_by_id('et_pb_contact_email_0')
fieldEmail1.click()
massage1=chrome.find_element_by_name('et_pb_contact_message_0')
massage1.click()
capcha1=chrome.find_element_by_name('et_pb_contact_captcha_0')
capcha1.click()
submit1=chrome.find_element_by_xpath("//button[@class='et_pb_contact_submit et_pb_button']")
submit1.click()
fieldUser1=chrome.find_element_by_xpath("//input[@placeholder='Username']")
fieldUser1.click
fieldPass1=chrome.find_element_by_xpath("//input[@placeholder='Password']")
fieldPass1.click()
forgot=chrome.find_element_by_link_text('Forgot your password?')
forgot.click()
Login1=chrome.find_element_by_xpath("//button[@class='et_pb_newsletter_button et_pb_button']")
Login1.click()
toggle=chrome.find_element_by_tag_name('h5')
toggle.click()
