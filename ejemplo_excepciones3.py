def comprobar_tiempo(edad):
	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<60:
		return "Mayor"
	elif edad<100:
		return "Cuidate"
print (comprobar_tiempo(18))
