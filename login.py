import time
from selenium.webdriver.common.by import By

def login(driver, location, usr, psw):
	"""
	It works fine and fast. If an exception occours (mainly the page hasn't been loaded yet), it keeps trying clicking the buttons.
	At the first good occasion it will success
	"""
	while True:
		time.sleep(0.5)
		try:
			driver.get(location)
			# print(dir(driver))
			mail = driver.find_element(By.ID, 'i0116')
			mail.send_keys(usr + '@studenti.unipi.it')
			next_b = driver.find_element(By.ID, 'idSIButton9')
			next_b.click()
			break
		except Exception:
			continue
	while True:
		time.sleep(0.1)
		try:
			username = driver.find_element(By.ID, 'username')
			password = driver.find_element(By.ID, 'password')
			submit = driver.find_element(By.NAME, '_eventId_proceed')
			username.send_keys(usr)
			password.send_keys(psw)
			submit.click()
			break
		except Exception:
			continue
	while True:
		time.sleep(0.1)
		try:
			driver.find_element(By.ID, 'idBtn_Back').click()
			break
		except Exception:
			continue
