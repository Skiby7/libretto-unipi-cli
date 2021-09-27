from json import load
from re import T
from selenium import webdriver 
from terminal_colors import COLORS as COLOR
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from login import login
import getpass
import signal
from selenium.webdriver.chrome.options import Options
from parse_libretto import parse_grades, print_exams
import pyfiglet
from simple_term_menu import TerminalMenu
import media
from threading import Thread, Lock
exams = []
media_attuale = 0
loading = False
stdout_lock = Lock()
def signal_handler(sig, frame):
		exit(0)


def print_welcome():
	global media_attuale
	print(COLOR.CLEAR_SCREEN)
	print(COLOR.CYAN + "Benvenuto su ")
	print(pyfiglet.figlet_format("Libretto CLI") + COLOR.RESET)
	if media_attuale != 0:
		print("-> La tua media ponderata è " + COLOR.GREEN + " %.2f" % (media_attuale))
		print(COLOR.RESET)
	elif media_attuale == 0 and len(exams) != 0:
		media_attuale = media.get_media_ponderata(exams)
		print("-> La tua media ponderata è " + COLOR.GREEN + " %.2f" % (media_attuale))
		print(COLOR.RESET)



def menu():
	global exams
	print_welcome()
	options = ["Stampa Libretto", "Calcola media ponderata", "Proietta voti", "Proietta voto di laurea", "Esci"]
	materie_da_proiettare = []
	terminal_menu = TerminalMenu(options)
	choice = terminal_menu.show()
	if choice == 0:
		print_exams(exams)
	if choice == 1:
		media.media_ponderata(exams)
	if choice == 2:
		while True:
			print_welcome()
			nome = input("Nome materia (inserisci" + COLOR.ITALIC + " fine" + COLOR.RESET + " per terminare): ")
			if nome == "fine":
				break
			while True:
				try:
					cfu = float(input("CFU: "))
					break
				except Exception:
					continue
			while True:
				try:
					voto = float(input("Voto da proiettare: "))
					break
				except Exception:
					continue
			materie_da_proiettare.append(media.Proiezione(nome, voto, cfu))
		print_welcome()
		media.proietta_media(exams, materie_da_proiettare)
	if choice == 3:
		while True:
			try:
				rimanenti_3_cfu = float(input("Esami da 3 cfu rimanenti: "))
				break
			except Exception:
				continue
		while True:
			try:
				rimanenti_6_cfu = float(input("Esami da 6 cfu rimanenti: "))
				break
			except Exception:
				continue
		while True:
			try:
				rimanenti_9_cfu = float(input("Esami da 9 cfu rimanenti: "))
				break
			except Exception:
				continue
		while True:
			try:
				rimanenti_12_cfu = float(input("Esami da 12 cfu rimanenti: "))
				break
			except Exception:
				continue
		while True:
			try:
				obiettivo_media = float(input("Voto che vorresti prendere a tutti gli esami rimanenti: "))
				break
			except Exception:
				continue
		media.proietta_voto_laurea(exams, rimanenti_3_cfu, rimanenti_6_cfu, rimanenti_9_cfu, rimanenti_12_cfu, obiettivo_media)
	if choice == 4:
		exit(0)

def print_loading():
	global loading, stdout_lock
	stdout_lock.acquire()
	print("\nLoading ")
	while loading:
		print(COLOR.UP_ONE_LINE + "Loading \\")
		time.sleep(0.2)
		print(COLOR.UP_ONE_LINE + "Loading |")
		time.sleep(0.2)
		print(COLOR.UP_ONE_LINE + "Loading /")
		time.sleep(0.2)
		print(COLOR.UP_ONE_LINE + "Loading -")
		time.sleep(0.2)
	stdout_lock.release()



def main():
	global exams, loading, stdout_lock
	signal.signal(signal.SIGINT, signal_handler)
	option = Options()
	option.add_argument("--disable-notifications")
	option.add_argument("--headless")
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
	print_welcome()
	user = input("Username: ")
	psw = getpass.getpass("Password: ")
	loading = True
	load_thread = Thread(target=print_loading)
	load_thread.start()
	login(driver, "https://libretto.unipi.it", user, psw)
	loading = False
	stdout_lock.acquire()
	stdout_lock.release()
	while os.get_terminal_size().columns < 157:
		print(COLOR.CLEAR_SCREEN + "Espandi il terminale, richieste almeno 157 colonne!".center(os.get_terminal_size().columns).center(os.get_terminal_size().lines))
		time.sleep(0.5)
	

	exams = parse_grades(driver.page_source)
	driver.close()
	while True:
		menu()


if __name__ == "__main__":
	main()


