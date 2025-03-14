import calendar
import locale
locale.setlocale(locale.LC_ALL,"es_CO.utf8")
import holidays
aa = input("Imprimir el año que deseas mostrar: ")
aa = int(aa)


if aa < 0 or aa > 3000:
    print ("Imprime un año válido entre el año 0 y 3000")
else:
    print(calendar.calendar(aa))

#imprimir los días festivos como una lista.
co_holidays = holidays.Colombia()
for i in holidays.Colombia(years=2025).items():
    print(i)













