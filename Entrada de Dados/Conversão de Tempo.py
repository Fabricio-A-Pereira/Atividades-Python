segundos_str = input("\nInsira a quantidade de segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
dias = horas // 24
horas_total = horas % 24
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas_total, "horas,", minutos, "minutos e", segs_restantes_final, "segundos")
