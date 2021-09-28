def overtime_wage(ot_hours):
	pay = 0
	if ot_hours < 5:
		pay = 400 + (ot_hours * 15)
	if ot_hours >= 5 and ot_hours < 10:
		pay = 400 + (ot_hours * 20)
	else: 
		pay = 400 + (ot_hours * 25)
	return pay
