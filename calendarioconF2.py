import calendar
import holidays
from colorama import Fore, Style


def highlight_holidays(s, year, month, co_holidays):
    """Resalta en rojo los días festivos"""
    try:
        day = int(s)  # Convertimos a número el día
        date_str = f"{year}-{month:02d}-{day:02d}"  # Formato YYYY-MM-DD
        if date_str in co_holidays:
            return Fore.RED + s + Style.RESET_ALL  # Colorear en rojo
        return s
    except ValueError:
        return s  # Devolver sin cambios si no es un número


def print_full_year_with_holidays(year):
    """Imprime todos los meses del año con los festivos resaltados"""
    co_holidays = holidays.Colombia(years=year)  # Obtener festivos de Colombia
    cal = calendar.TextCalendar(firstweekday=0)  # Lunes como primer día

    for month in range(1, 13):  # Iterar de enero (1) a diciembre (12)
        print(f"\n{calendar.month_name[month]} {year}".center(20, "="))  # Título del mes
        print("Lu Ma Mi Ju Vi Sa Do")  # Encabezado de días de la semana

        month_calendar = cal.monthdayscalendar(year, month)  # Obtener semanas del mes

        for week in month_calendar:
            week_str = " ".join(
                highlight_holidays(f"{day:2}" if day != 0 else "  ", year, month, co_holidays)
                for day in week
            )
            print(week_str)


# Llamamos a la función para imprimir el año completo con festivos resaltados
print_full_year_with_holidays(2025)
