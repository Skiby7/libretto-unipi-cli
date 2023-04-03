from typing import get_args
from terminal_colors import COLORS as COLOR, print_color

class Proiezione:
	def __init__(self, nome, voto, cfu) -> None:
		self.nome = nome
		self.voto = voto
		self.cfu = cfu


def media_ponderata(exams):
	counter_real = 0;
	sum_real = 0;
	for exam in exams:
		if exam["Stato"] == "OK" and exam["Voto"] != "Idoneo":
			sum_real += float(exam["Voto"])*float(exam["CFU"])
			counter_real += float(exam["CFU"])
	print("La tua media ponderata è " + COLOR.GREEN + " %.2f" % (sum_real/counter_real))
	input(COLOR.RESET + COLOR.ITALIC + "\nPremi invio per continuare" + COLOR.RESET)

def get_media_ponderata(exams):
	counter_real = 0;
	sum_real = 0;
	for exam in exams:
		if exam["Stato"] == "OK" and exam["Voto"] != "Idoneo":
			sum_real += float(exam["Voto"])*float(exam["CFU"])
			counter_real += float(exam["CFU"])
	return sum_real/counter_real

def proietta_media(exams, materie):
	counter_real = 0;
	sum_real = 0;
	for exam in exams:
		if exam["Stato"] == "OK" and exam["Voto"] != "Idoneo":
			sum_real += float(exam["Voto"])*float(exam["CFU"])
			counter_real += float(exam["CFU"])
	for materia in materie:
		sum_real += materia.voto*materia.cfu
		counter_real += materia.cfu
	lista_materie = []
	for materia in materie:
		lista_materie.append(materia.nome)
	print("La tua media ponderata proiettando le seguenti materie " + str(lista_materie) + " è " + COLOR.GREEN + "%.2f" % (sum_real/counter_real))
	input(COLOR.RESET + COLOR.ITALIC + "\nPremi invio per continuare" + COLOR.RESET)

def proietta_voto_laurea(exams, rimanenti_3_cfu, rimanenti_6_cfu, rimanenti_9_cfu, rimanenti_12_cfu, obiettivo_media):
	counter_real = 0;
	sum_real = 0;
	
	for exam in exams:
		if exam["Stato"] == "OK" and exam["Voto"] != "Idoneo":
			sum_real += float(exam["Voto"])*float(exam["CFU"])
			counter_real += float(exam["CFU"])
	cfu_tot = counter_real + rimanenti_12_cfu*12 + rimanenti_6_cfu*6 + rimanenti_3_cfu*3
	media_30_lode = 32*(rimanenti_12_cfu*12 + rimanenti_9_cfu*9 + rimanenti_6_cfu*6 + rimanenti_3_cfu*3) + sum_real
	media_30 = 30*(rimanenti_12_cfu*12 + rimanenti_9_cfu*9 + rimanenti_6_cfu*6 + rimanenti_3_cfu*3) + sum_real
	media_obiettivo = obiettivo_media*(rimanenti_12_cfu*12 + rimanenti_6_cfu*6 + rimanenti_3_cfu*3) + sum_real

	print("La media finale se prendi tutti %d è %s%.2f%s e il voto di laurea massimo è %s%.2f%s - %s%.2f%s"  % (obiettivo_media, COLOR.GREEN, float(media_obiettivo/cfu_tot), COLOR.RESET, COLOR.GREEN, int(float(media_obiettivo/cfu_tot)*(11/3))+4, COLOR.RESET, COLOR.GREEN, int(float(media_obiettivo/cfu_tot)*(11/3))+7, COLOR.RESET))
	print("La media finale se prendi tutti 30 è %s%.2f%s e il voto di laurea massimo è %s%.2f%s - %s%.2f%s"  % (COLOR.GREEN, float(media_30/cfu_tot), COLOR.RESET, COLOR.GREEN, int(float(media_30/cfu_tot)*(11/3))+4, COLOR.RESET, COLOR.GREEN, int(float(media_30/cfu_tot)*(11/3))+7, COLOR.RESET))
	print("La media finale se prendi tutti 30L è %s%.2f%s e il voto di laurea massimo è %s%.2f%s - %s%.2f%s" % (COLOR.GREEN, float(media_30_lode/cfu_tot), COLOR.RESET, COLOR.GREEN, int(float(media_30_lode/cfu_tot)*(11/3))+4, COLOR.RESET, COLOR.GREEN, int(float(media_30_lode/cfu_tot)*(11/3))+7, COLOR.RESET))
	input(COLOR.RESET + COLOR.ITALIC + "\nPremi invio per continuare" + COLOR.RESET)
