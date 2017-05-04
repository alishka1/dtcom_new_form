# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as beatsop
import re

driver = webdriver.Chrome("chromedriver")
driver.set_page_load_timeout(30)
driver.get("https://www.diplomtime.com")
driver.implicitly_wait(10)
driver.maximize_window()

select_type = "top_select_type"
select_type_not_error = ".top_select_type.js--validator:not(.error)"
select_type_value = "js--type_work"
date = "date_rk_top"
date_not_error = ".date_rk_top:not(.error)"
date_value = "js--date_work"
find_out_the_price = '.js--loadorder_top'
btn_theme_next ='.but_theme_requir'
btn_theme_not_disabled = ".button.green.big-text.but_theme:not(.disabled)"
theme_textarea = ".txt_theme"
theme_val = "theme_val"
extra_requirement_not_disabled = '.button.green.big-text.but_requir.but_requir_attach:not(.disabled)'
toggle_origin = './/*[@id="body"]/div[3]/div/div[2]/div/form[1]/div[7]/div[2]/div/div[1]/div/div/div[1]/label/span/span[1]/span'
toggle_origin_is_selected = '.toggle_origin'
toggle_origin_value = "origin_val"
toggle_size = './/*[@id="body"]/div[3]/div/div[2]/div/form[1]/div[7]/div[2]/div/div[2]/div/div/div[1]/label/span/span[1]/span'
toggle_size_is_selected = '.toggle_size'
toggle_size_value = "size_val"
btn_extra_wishes_next_not_disabled = '.button.green.big-text.but_attach:not(.disabled)'
btn_extra_wishes_textarea = '.txt_direction'
btn_extra_wishes_textarea_value = 'have_comment'
phone = '.phone_rk'
phone_not_error = '.phone_rk.js--validator:not(.error)'
email = '.email_rk'
email_not_error = '.email_rk.js--validator:not(.error)'
promo_code = ".//*[@id='body']/div[3]/div/div[2]/div/form[1]/div[9]/div[3]/div[3]/div/span"
promo_code_value = '.txt_promo'
get_the_price = '.button.green.big-text.but_call.but_next_call'
toggle_btn_skip = '.tag.big-text.center.but_skip_requir'
btn_extra_wishes_skip = '.tag.big-text.center.but_skip_attach.but_skip_attach'
btn_yes = '.button.button-small.green.true_call'
btn_back = '.tag.tag-small.center.close_rk'
promo_code_link = "js__bonus_link"
vk = '.sharediscount_modal__sharebutton.iconbase.iconsize40.iconvkcolor.js__soc_share'
ok = '.sharediscount_modal__sharebutton.iconbase.iconsize40.iconokcolor.js__soc_share'
telegram = '.sharediscount_modal__sharebutton.iconbase.iconsize40.icontelegramcolor.js__soc_share'
facebook = '.sharediscount_modal__sharebutton.iconbase.iconsize40.iconfbcolor.js__soc_share'
twiter = '.sharediscount_modal__sharebutton.iconbase.iconsize40.icontwcolor.js__soc_share'




try:
	driver.find_element_by_css_selector(select_type_not_error)
	print(u'1. Выберите тип - Не_ерор найден!               ОК')
except:
	print(u'1. Выберите тип - Не_ерор не найден!            ОШИБКА')

try:
	driver.find_element_by_css_selector(date_not_error)
	print(u'2. Дата - Не_ерор найден!                       ОК')
except:
	print(u'2. Дата - Не_ерор не найден!                    ОШИБКА')

try:
	driver.find_element_by_class_name(select_type).click()
	print(u'3. Выберите тип активирован                     ОК')
except:
	print(u'3. Выберите тип активирован                     ОШИБКА')

try:
	driver.find_element_by_class_name(date).click()
	print(u'4. Дата активирован                             ОК')
except:
	print(u'4. Дата активирован                             ОШИБКА')

try:
	driver.find_element_by_css_selector(select_type_not_error)
	print(u'5. Выберите тип - Не_ерор найден!               ОШИБКА')
except:
	print(u'5. Выберите тип - Не_ерор не найден!            ОК')

try:
	select = Select(driver.find_element_by_class_name(select_type))
	select.select_by_visible_text('Реферат')
	print(u'6. Тип работы выбран реферат                    ОК')
except:
	print(u'6. Тип работы выбран реферат                    ОШИБКА')

try:
	driver.find_element_by_css_selector(date_not_error)
	print(u'7. Дата - Не_ерор найден!                       ОК')
except:
	print(u'7. Дата - Не_ерор не найден!                    ОШИБКА')

try:
	send = driver.find_element_by_class_name(date)
	send.send_keys(u"11.03.2017")
	print(u'8. Некорректная дата напечатана -               ОК')
except:
	print(u'8. Некорректная дата напечатана -               ОШИБКА')

try:
	driver.find_element_by_class_name(select_type).click()
	print(u'9. Выберите тип активирован                     ОК')
except:
	print(u'9. Выберите тип активирован                     ОШИБКА')

try:
	driver.find_element_by_css_selector(date_not_error)
	print(u'10. Дата - Не_ерор найден!                      ОШИБКА')
except:
	print(u'10. Дата - Не_ерор не найден!                   ОК')

try:
	send = driver.find_element_by_class_name(date)
	send.send_keys(Keys.CONTROL + "a");
	send.send_keys(Keys.BACK_SPACE)
	print(u'11. Некорректная дата очищена -                 ОК')
except:
	print(u'11. Некорректная дата очищена -                 ОШИБКА')

try:
	send = driver.find_element_by_class_name(date)
	send.send_keys(u"11.03.2088")
	print(u'12. Корректная дата напечатана -                ОК')
except:
	print(u'12. Корректная дата напечатана -                ОШИБКА')

try:
	driver.find_element_by_class_name(select_type).click()
	print(u'13. Выберите тип активирован                    ОК')
except:
	print(u'13. Выберите тип активирован                    ОШИБКА')

try:
	driver.find_element_by_css_selector(date_not_error)
	print(u'14. Дата - Не_ерор найден!                      ОК')
except:
	print(u'14. Дата - Не_ерор не найден!                   ОШИБКА')

try:
	driver.find_element_by_css_selector(find_out_the_price).click()
	print(u'15. Узнать                                      ОК')
except:
	print(u'15. Узнать                                      ОШИБКА')


element = driver.find_element_by_class_name(select_type_value)
html = element.get_attribute("outerHTML")

soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= select_type_value).next

if desired_text == u'Реферат':
	print u"16. Шапка реферат                               ОК"
else:
	print u"16. Шапка реферат                               ОШИБКА"



element = driver.find_element_by_class_name(date_value)
html = element.get_attribute("outerHTML")
soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= date_value).next

if desired_text == u'к 11 марта 2088':
	print u"17. Шапка дата                                  ОК"
else:
	print u"17. Шапка дата                                  ОШИБКА"


try:
	driver.find_element_by_css_selector(btn_theme_not_disabled)
	print(u'18. Тема кнопка далее - not Disable найден      ОШИБКА')
except:
	print(u'18. Тема кнопка далее - not Disable не найден   ОК')

try:
	send = driver.find_element_by_css_selector(theme_textarea)
	send.send_keys(u"Тест")
	print(u'19. Тест напечатан -                            ОК')
except:
	print(u'19. Тест напечатан -                            ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_theme_not_disabled)
	print(u'20. Тема кнопка далее - not Disable найден      ОК')
except:
	print(u'20. Тема кнопка далее - not Disable не найден   ОШИБКА')

try:
	send = driver.find_element_by_css_selector(theme_textarea)
	send.send_keys(Keys.CONTROL + "a");
	send.send_keys(Keys.BACK_SPACE)
	print(u'21. Тема очищена -                              ОК')
except:
	print(u'21. Тема очищена -                              ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_theme_not_disabled)
	print(u'22. Тема кнопка далее - not Disable найден      ОШИБКА')
except:
	print(u'22. Тема кнопка далее - not Disable не найден   ОК')

try:
	send = driver.find_element_by_css_selector(theme_textarea)
	send.send_keys(u"Тест")
	print(u'23. Тест напечатан -                            ОК')
except:
	print(u'23. Тест напечатан -                            ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_theme_not_disabled)
	print(u'24. Тема кнопка далее - not Disable найден      ОК')
except:
	print(u'24. Тема кнопка далее - not Disable не найден   ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_theme_next).click()
	print(u'25. Далее нажато                                ОК')
except:
	print(u'25. Далее нажато                                ОШИБКА')


element = driver.find_element_by_class_name(theme_val)
html = element.get_attribute("outerHTML")

soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= theme_val).next

if desired_text == u'Тест':
	print u"26. Шапка тест                                  ОК"
else:
	print u"26. Шапка тест                                  ОШИБКА"

try:
	driver.find_element_by_css_selector(extra_requirement_not_disabled)
	print(u'27. Доп.кнопка далее - not Disable найден       ОШИБКА')
except:
	print(u'27. Доп.кнопка далее - not Disable не найден    ОК')






#Этап проверки checkbox оригинальность
if (driver.find_element_by_css_selector(toggle_origin_is_selected).is_selected()):
	print(u'28. Checbox origin активирован                  ОШИБКА')
else:
	print(u'28. Checbox origin деактивирован                ОК')

if (driver.find_element_by_css_selector(toggle_size_is_selected).is_selected()):
	print(u'29. Checbox size активирован                    ОШИБКА')
else:
	print(u'29. Checbox size деактивирован                  ОК')


try:
	driver.find_element_by_xpath(toggle_origin).click()
	print(u'30. Checbox origin включен                      ОК')
except:
	print(u'30. Checbox origin не включен                   ОШИБКА')


if (driver.find_element_by_css_selector(toggle_origin_is_selected).is_selected()):
	print(u'31. Checbox origin активирован                  ОК')
else:
	print(u'31. Checbox origin деактивирован                ОШИБКА')

if (driver.find_element_by_css_selector(toggle_size_is_selected).is_selected()):
	print(u'32. Checbox size активирован                    ОШИБКА')
else:
	print(u'32. Checbox size деактивирован                  ОК')

try:
	driver.find_element_by_css_selector(extra_requirement_not_disabled)
	print(u'33. Доп.кнопка далее - not Disable найден       ОК')
except:
	print(u'33. Доп.кнопка далее - not Disable не найден    ОШИБКА')


try:
	driver.find_element_by_xpath(toggle_origin).click()
	print(u'34. Checbox origin выключен                     ОК')
except:
	print(u'34. Checbox origin не выключен                  ОШИБКА')


if (driver.find_element_by_css_selector(toggle_origin_is_selected).is_selected()):
	print(u'35. Checbox origin активирован                  ОШИБКА')
else:
	print(u'35. Checbox origin деактивирован                ОК')

if (driver.find_element_by_css_selector(toggle_size_is_selected).is_selected()):
	print(u'36. Checbox size активирован                    ОШИБКА')
else:
	print(u'36. Checbox size деактивирован                  ОК')

try:
	driver.find_element_by_css_selector(extra_requirement_not_disabled)
	print(u'37. Доп.кнопка далее - not Disable найден       ОШИБКА')
except:
	print(u'37. Доп.кнопка далее - not Disable не найден    ОК')






#Этап проверки checkbox объем работы
try:
	driver.find_element_by_xpath(toggle_size).click()
	print(u'38. Checbox size включен                        ОК')
except:
	print(u'38. Checbox size не включен                     ОШИБКА')


if (driver.find_element_by_css_selector(toggle_size_is_selected).is_selected()):
	print(u'39. Checbox size активирован                    ОК')
else:
	print(u'39. Checbox size деактивирован                  ОШИБКА')

if (driver.find_element_by_css_selector(toggle_origin_is_selected).is_selected()):
	print(u'40. Checbox origin активирован                  ОШИБКА')
else:
	print(u'40. Checbox origin деактивирован                ОК')

try:
	driver.find_element_by_css_selector(extra_requirement_not_disabled)
	print(u'41. Доп.кнопка далее - not Disable найден       ОК')
except:
	print(u'41. Доп.кнопка далее - not Disable не найден    ОШИБКА')


try:
	driver.find_element_by_xpath(toggle_size).click()
	print(u'42. Checbox size выключен                       ОК')
except:
	print(u'42. Checbox size не выключен                    ОШИБКА')


if (driver.find_element_by_css_selector(toggle_size_is_selected).is_selected()):
	print(u'43. Checbox size активирован                    ОШИБКА')
else:
	print(u'43. Checbox size деактивирован                  ОК')

if (driver.find_element_by_css_selector(toggle_origin_is_selected).is_selected()):
	print(u'44. Checbox origin активирован                  ОШИБКА')
else:
	print(u'44. Checbox origin деактивирован                ОК')


try:
	driver.find_element_by_css_selector(extra_requirement_not_disabled)
	print(u'45. Доп.кнопка далее - not Disable найден       ОШИБКА')
except:
	print(u'45. Доп.кнопка далее - not Disable не найден    ОК')


try:
	driver.find_element_by_xpath(toggle_origin).click()
	print(u'46. Checbox origin включен                      ОК')
except:
	print(u'46. Checbox origin не включен                   ОШИБКА')


try:
	driver.find_element_by_xpath(toggle_size).click()
	print(u'47. Checbox size включен                        ОК')
except:
	print(u'47. Checbox size не включен                     ОШИБКА')


try:
	driver.find_element_by_css_selector(extra_requirement_not_disabled).click()
	print(u'48. Доп.кнопка далее - нажата                   ОК')
except:
	print(u'48. Доп.кнопка далее - не нажата                ОШИБКА')


element = driver.find_element_by_class_name(toggle_origin_value)
html = element.get_attribute("outerHTML")

soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= toggle_origin_value).next

if desired_text == u'Оригинальность: 30-40%':
	print u"49. Шапка origin                                ОК"
else:
	print u"49. Шапка origin                                ОШИБКА"


element = driver.find_element_by_class_name(toggle_size_value)
html = element.get_attribute("outerHTML")

soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= toggle_size_value).next

if desired_text == u'Объём работы: 15-20 стр.':
	print u"50. Шапка size                                  ОК"
else:
	print u"50. Шапка size                                  ОШИБКА"

try:
	driver.find_element_by_css_selector(btn_extra_wishes_next_not_disabled)
	print(u'51. Доп.кнопка далее - not Disable найден       ОШИБКА')
except:
	print(u'51. Доп.кнопка далее - not Disable не найден    ОК')

try:
	send = driver.find_element_by_css_selector(btn_extra_wishes_textarea)
	send.send_keys(u"Тест")
	print(u'52. Тест напечатан -                            ОК')
except:
	print(u'52. Тест напечатан -                            ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_extra_wishes_next_not_disabled)
	print(u'53. Доп.кнопка далее - not Disable найден       ОК')
except:
	print(u'53. Доп.кнопка далее - not Disable не найден    ОШИБКА')

try:
	send = driver.find_element_by_css_selector(btn_extra_wishes_textarea)
	send.send_keys(Keys.CONTROL + "a");
	send.send_keys(Keys.BACK_SPACE)
	print(u'52. Тема очищена -                              ОК')
except:
	print(u'52. Тема очищена -                              ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_extra_wishes_next_not_disabled)
	print(u'53. Доп.кнопка далее - not Disable найден       ОШИБКА')
except:
	print(u'53. Доп.кнопка далее - not Disable не найден    ОК')

try:
	send = driver.find_element_by_css_selector(btn_extra_wishes_textarea)
	send.send_keys(u"Тест")
	print(u'54. Тест напечатан -                            ОК')
except:
	print(u'54. Тест напечатан -                            ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_extra_wishes_next_not_disabled).click()
	print(u'55. Доп.кнопка далее - нажата                   ОК')
except:
	print(u'55. Доп.кнопка далее - не нажата                ОШИБКА')

element = driver.find_element_by_class_name(btn_extra_wishes_textarea_value)
html = element.get_attribute("outerHTML")

soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= btn_extra_wishes_textarea_value).next

if desired_text == u'Комментарий: Тест':
	print u"56. Шапка пожелания                             ОК"
else:
	print u"56. Шапка пожелания                             ОШИБКА"


try:
	driver.find_element_by_css_selector(phone_not_error)
	print(u'57. Телефон - Не_ерор найден!                   ОК')
except:
	print(u'57. Телефон - Не_ерор не найден!                ОШИБКА')

try:
	driver.find_element_by_css_selector(email_not_error)
	print(u'58. Email - Не_ерор найден!                     ОК')
except:
	print(u'58. Email - Не_ерор не найден!                  ОШИБКА')

time.sleep(1)
try:
	driver.find_element_by_css_selector(phone).click()
	print(u'59. Телефон - активирован                       ОК')
except:
	print(u'59. Телефон - не активирован                    ОШИБКА')

time.sleep(1)
try:
	driver.find_element_by_css_selector(email).click()
	print(u'60. Email - активирован                         ОК')
except:
	print(u'60. Email - не активирован                      ОШИБКА')

try:
	driver.find_element_by_css_selector(phone_not_error)
	print(u'61. Телефон - Не_ерор найден!                   ОШИБКА')
except:
	print(u'61. Телефон - Не_ерор не найден!                ОК')

time.sleep(1)
try:
	driver.find_element_by_css_selector(phone).click()
	print(u'62. Телефон - активирован                       ОК')
except:
	print(u'62. Телефон - не активирован                    ОШИБКА')

try:
	driver.find_element_by_css_selector(email_not_error)
	print(u'63. Email - Не_ерор найден!                     ОШИБКА')
except:
	print(u'63. Email - Не_ерор не найден!                  ОК')

try:
	send = driver.find_element_by_css_selector(phone)
	send.send_keys("77777777777")
	print(u'64. Телефон номер напечатан -                   ОК')
except:
	print(u'64. Телефон номер напечатан -                   ОШИБКА')

try:
	driver.find_element_by_css_selector(phone_not_error)
	print(u'65. Телефон - Не_ерор найден!                   ОК')
except:
	print(u'65. Телефон - Не_ерор не найден!                ОШИБКА')

try:
	send = driver.find_element_by_css_selector(email)
	send.send_keys("test@diplomtime.ru")
	print(u'66. Email напечатан -                           ОК')
except:
	print(u'66. Email напечатан -                           ОШИБКА')

try:
	driver.find_element_by_css_selector(email_not_error)
	print(u'67. Email - Не_ерор найден!                     ОК')
except:
	print(u'67. Email - Не_ерор не найден!                  ОШИБКА')

try:
	send = driver.find_element_by_css_selector(phone)
	send.send_keys(Keys.BACK_SPACE)
	print(u'68. Телефон одна цифра удалена -                ОК')
except:
	print(u'68. Телефон одна цифра удалена -                ОШИБКА')

try:
	driver.find_element_by_css_selector(phone_not_error)
	print(u'69. Телефон - Не_ерор найден!                   ОШИБКА')
except:
	print(u'69. Телефон - Не_ерор не найден!                ОК')

try:
	send = driver.find_element_by_css_selector(phone)
	send.send_keys("7")
	print(u'70. Телефон номер напечатан -                   ОК')
except:
	print(u'70. Телефон номер напечатан -                   ОШИБКА')

try:
	driver.find_element_by_css_selector(phone_not_error)
	print(u'71. Телефон - Не_ерор найден!                   ОК')
except:
	print(u'71. Телефон - Не_ерор не найден!                ОШИБКА')

try:
	send = driver.find_element_by_css_selector(email)
	send.send_keys(Keys.BACK_SPACE)
	print(u'72. Email одна буква удалена -                  ОК')
except:
	print(u'72. Email одна буква удалена -                  ОШИБКА')

try:
	driver.find_element_by_css_selector(email_not_error)
	print(u'73. Email - Не_ерор найден!                     ОШИБКА')
except:
	print(u'73. Email - Не_ерор не найден!                  ОК')

try:
	send = driver.find_element_by_css_selector(email)
	send.send_keys("u")
	print(u'74. Email одна буква добавлена -                ОК')
except:
	print(u'74. Email одна буква добавлена -                ОШИБКА')

try:
	driver.find_element_by_css_selector(email_not_error)
	print(u'75. Email - Не_ерор найден!                     ОК')
except:
	print(u'75. Email - Не_ерор не найден!                  ОШИБКА')

time.sleep(1)
try:
	driver.find_element_by_xpath(promo_code).click()
	print(u'76. Промо-код нажат                             ОК')
except:
	print(u'76. Промо-код не нажат                          ОШИБКА')

promo = driver.find_element_by_css_selector(promo_code_value)
promo_value = promo.get_attribute('value')
if promo_value == u'':
	print u"77. Промо-код пуст                              ОК"
else:
	print u"77. Промо-код не пус                            ОШИБКА"

time.sleep(2)
try:
	driver.find_element_by_css_selector(get_the_price).click()
	print(u'78. Кнопка получить стоимость нажата            ОК')
except:
	print(u'78. Кнопка получить стоимость нажата            ОШИБКА')



time.sleep(2)


element = driver.find_element_by_class_name(promo_code_link)
html = element.get_attribute("outerHTML")
soup = BeautifulSoup(html, "html.parser")
# anchors = soup.find_all('a', {'class': 'js__bonus_link', 'href': True})
# for anchor in anchors:
#     print (anchor['href'])
anchors = soup.find('a', {'class': promo_code_link, 'href': True})
link = anchors['href']
print(link)
# print(re.search('\w{5}://\w{10}.\w{3}/\w{6}/', link))
result1 = re.search(r'\d+', link)
print u"79. Номер промо-кода:" + result1.group(0)

try:
	driver.find_element_by_class_name(promo_code_link).click()
	print(u'80. Новая ссылка открыта                        ОК')
except:
	print(u'80. Новая ссылка не открыта                     ОШИБКА')


try:
	select = Select(driver.find_element_by_class_name(select_type))
	select.select_by_visible_text('Реферат')
	print(u'81. Тип работы выбран реферат                   ОК')
except:
	print(u'81. Тип работы выбран реферат                   ОШИБКА')

try:
	driver.find_element_by_css_selector(find_out_the_price).click()
	print(u'82. Кнопка узнать                               ОК')
except:
	print(u'82. Кнопка узнать                               ОШИБКА')

try:
	send = driver.find_element_by_css_selector(theme_textarea)
	send.send_keys(u"Тест")
	print(u'83. Тест напечатан -                            ОК')
except:
	print(u'83. Тест напечатан -                            ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_theme_not_disabled).click()
	print(u'84. Кнопка далее                                ОК')
except:
	print(u'84. Кнопка далее                                ОШИБКА')

time.sleep(2)

try:
	driver.find_element_by_css_selector(toggle_btn_skip).click()
	print(u'85. Кнопка пропустить                           ОК')
except:
	print(u'85. Кнопка пропустить                           ОШИБКА')

time.sleep(2)

try:
	driver.find_element_by_css_selector(btn_extra_wishes_skip).click()
	print(u'86. Кнопка пропустить                           ОК')
except:
	print(u'86. Кнопка пропустить                           ОШИБКА')


input_promo = driver.find_element_by_css_selector(promo_code_value)
value_promo = input_promo.get_attribute('value')
print(value_promo)
if value_promo == result1.group(0):
	print u"87. Промо-код                                   ОК"
else:
	print u"87. Промо-код                                   ОШИБКА"
print result1.group(0)

input_phone = driver.find_element_by_css_selector(phone)
value_phone = input_phone.get_attribute('value')
if value_phone == u"+7(777)777-77-77":
	print u"88. Телефон                                     ОК"
else:
	print u"88. Телефон                                     ОШИБКА"



input_email = driver.find_element_by_css_selector(email)
value_email = input_email.get_attribute('value')
if value_email == u"test@diplomtime.ru":
	print u"89. Email                                       ОК"
else:
	print u"89. Email                                       ОШИБКА"

time.sleep(1)
try:
	driver.find_element_by_css_selector(get_the_price).click()
	print(u'90. Кнопка получить стоимость                   ОК')
except:
	print(u'90. Кнопка получить стоимость                   ОШИБКА')

time.sleep(31)
try:
	driver.find_element_by_css_selector(btn_yes).click()
	print(u'91. Вам удалось дозвониться нажата              ОК')
except:
	print(u'91. Вам удалось дозвониться нажата              ОШИБКА')

try:
	driver.find_element_by_css_selector(btn_back).click()
	print(u'92. Спасибо за обращение нажата                 ОК')
except:
	print(u'92. Спасибо за обращение нажата                 ОШИБКА')













# $.cookie('referer_oder', '777777', { expires: 365, path: '/', domain: '.diplomtime.com' });
