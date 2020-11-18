import mechanicalsoup
from secrets import vm_user, vm_pwd
import time

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.vanmoof.com/my-vanmoof/")
browser.select_form()

browser['email'] = vm_user
browser['password'] = vm_pwd

browser.submit_selected()

# with open('date.log', 'a') as log:
#     log.write(f'{int(time.time())},{browser.get_current_page().find_all("div", class_="m-info__
#     body-details m-info__side-by-side-details--item order-line")[-1].text.strip()}\n')

print(f'{int(time.time())},{browser.get_current_page().find_all("div", class_="m-info__body-details m-info__side-by-side-details--item order-line")[-1].text.strip()}')
