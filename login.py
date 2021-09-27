import time

def login(driver, location, usr, psw):
	"""
	It works fine and fast. If an exception occours (mainly the page hasn't been loaded yet), it keeps trying clicking the buttons.
	At the first good occasion it will success
	"""
	while True:
		time.sleep(0.1)
		try:
			driver.get(location)
			mail = driver.find_element_by_id('i0116')
			mail.send_keys(usr + '@studenti.unipi.it')
			next_b = driver.find_element_by_id('idSIButton9')
			next_b.click()
			break
		except Exception:
			continue
	while True:
		time.sleep(0.1)
		try:
			username = driver.find_element_by_id('username')
			password = driver.find_element_by_id('password')
			submit = driver.find_element_by_name('_eventId_proceed')
			username.send_keys(usr)
			password.send_keys(psw)
			submit.click()
			break
		except Exception:
			continue
	while True:
		time.sleep(0.1)
		try:
			driver.find_element_by_id('idBtn_Back').click()
			break
		except Exception:
			continue
