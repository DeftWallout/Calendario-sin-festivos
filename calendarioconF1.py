import calendar
import locale
locale.setlocale(locale.LC_ALL,"es_CO.utf8")
import holidays
from colorama import Fore, Style

#Imprimir mes por mes con los días festivos resaltados
year = 2025
month = 2 # Cambia esto al mes que deseas ver

# Obtener festivos en Colombia para el año seleccionado
co_holidays = holidays.Colombia(years=year)

# Crear el calendario mensual
cal = calendar.TextCalendar(firstweekday=0)  # Semana comienza en lunes

# Función para colorear los días festivos
def highlight_holidays(s):
    try:
        day = int(s)  # Convertimos a número el día
        date_str = f"{year}-{month:02d}-{day:02d}"
        if date_str in co_holidays:
            return Fore.RED + s + Style.RESET_ALL  # Poner en rojo si es festivo
        return s
    except ValueError:
        return s  # Devolver sin cambios si no es un número

# Obtener el calendario como lista de semanas
month_calendar = cal.monthdayscalendar(year, month)

# Imprimir el nombre del mes
print(f"\n{calendar.month_name[month]} {year}".center(20, "."))

# Imprimir los días de la semana
weekdays = "Lu Ma Mi Ju Vi Sa Do"
print(weekdays)

# Imprimir el calendario con los días resaltados
for week in month_calendar:
    week_str = " ".join(
        highlight_holidays(f"{day:2}" if day != 0 else "  ") for day in week
    )
    print(week_str)