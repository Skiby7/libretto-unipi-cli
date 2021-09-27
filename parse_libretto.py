from bs4 import BeautifulSoup as bs
import re
from terminal_colors import COLORS as COLOR
class SEPARATORS:
	LEFT_MID = "├"
	RIGHT_MID = "┤"
	UPPER_LEFT_CORNER = "┌"
	UPPER_RIGHT_CORNER = "┐"
	LOWER_LEFT_CORNER = "└"
	LOWER_RIGHT_CORNER = "┘"
	CENTER = "┼"
	TOP_CENTER = "┬"
	BOTTOM_CENTER = "┴"

FORMAT = "│ %-10s │ %-70s │ %-7s │ %-20s │ %-5s │ %-25s │"
SUB_STRING = "<[^>]+?>"


def parse_grades(content):
	exams = []
	soup = bs(content, "lxml")
	table = soup.find("table", {"class" : "table"})
	entries = table.find_all("tr")
	del entries[0]
	for entry in entries:
		attributes = entry.find_all("td")
		attr_dict = {
			"Data" : re.sub(SUB_STRING, '',str(attributes[0])),
			"Insegnamento" : re.sub(SUB_STRING, '',str(attributes[1])),
			"Voto" : re.sub(SUB_STRING, '',str(attributes[2])),
			"Professore" : re.sub(SUB_STRING, '',str(attributes[3])),
			"CFU" : re.sub(SUB_STRING, '',str(attributes[4])),
			"Stato" : re.sub(SUB_STRING, '',str(attributes[5]))
		}
		exams.append(attr_dict)
	return exams


def print_sep(first, intermediate, last):
	print(first, end="")
	for i in range(0, 154):
		if i == 12 or i == 85 or i == 95 or i == 118 or i == 126:
			print(intermediate, end="")
		else:
			print("─", end="")
	print(last)
	

def print_exams(exams):
	print_sep(SEPARATORS.UPPER_LEFT_CORNER, SEPARATORS.TOP_CENTER, SEPARATORS.UPPER_RIGHT_CORNER);

	print(FORMAT % ("Data", "Insegnamento", "Voto", "Presidente", "CFU", "Stato"))

	for exam in exams:
		print_sep(SEPARATORS.LEFT_MID, SEPARATORS.CENTER, SEPARATORS.RIGHT_MID);
		if exam["Stato"] == "OK":
			print(FORMAT % (exam["Data"], exam["Insegnamento"], exam["Voto"], exam["Professore"], re.sub('.00', '', exam["CFU"]), COLOR.GREEN + exam["Stato"] + '                       ' + COLOR.RESET))
		else:
			print(FORMAT % (exam["Data"], exam["Insegnamento"], exam["Voto"], exam["Professore"], re.sub('.00', '', exam["CFU"]), COLOR.RED + exam["Stato"] + ' ' + COLOR.RESET))

	print_sep(SEPARATORS.LOWER_LEFT_CORNER, SEPARATORS.BOTTOM_CENTER, SEPARATORS.LOWER_RIGHT_CORNER);
	input(COLOR.ITALIC + "\nPremi invio per continuare" + COLOR.RESET)

	    
 

