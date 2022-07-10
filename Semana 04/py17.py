#!/usr/bin/python3
#Vídeo 17 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

import datetime as dt
import pytz

d = dt.date(2016, 7, 24) #Os números devem conter somente os digitos significativos

print(d)

print()
tday = dt.date.today()

print(tday)
print(tday.year)
print(tday.day)

print()
print(tday.weekday())
print(tday.isoweekday())

print()
tdelta = dt.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

print()
bday = dt.date(2022, 10, 10)
till_bday = bday - tday

print(till_bday)

print()
print(till_bday.days)
print(till_bday.total_seconds())

print()
t = dt.time(9, 30, 45, 100000)

print(t)
print(t.hour)

print()
dat = dt.datetime(2016, 7, 26, 12, 30, 45, 100000)

print(dat)
print(dat.date())
print(dat.time())
print(dat.year)

print()
print(dat + tdelta)

tdelta = dt.timedelta(hours=12)
print(dat + tdelta)

print()
dt_tday = dt.datetime.today() #Data local sem o fuso horário (datetime.today() = datetime.now())
dt_now = dt.datetime.now() #Data local com/sem o fuso horário
dt_utcnow = dt.datetime.utcnow() #Data do fuso horário no formato UTC (Horário de Greenwich)

print(dt_tday)
print(dt_now)
print(dt_utcnow)

print()
dat = dt.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

print(dat)

dt_utcnow = dt.datetime.now(tz=pytz.UTC)

print(dt_utcnow)

dt_fn = dt_utcnow.astimezone(pytz.timezone('Brazil/DeNoronha'))

print(dt_fn)

#for tz in pytz.all_timezones:
	#print(tz)

dt_mg = dt.datetime.now()
mg_tz = pytz.timezone('America/Sao_Paulo')

dt_mg = mg_tz.localize(dt_mg)

dt_west = dt_mg.astimezone(pytz.timezone('Brazil/West'))

print(dt_west)

print()
dt_mg = dt.datetime.now(tz=pytz.timezone('America/Sao_Paulo'))

print(dt_mg.isoformat())
print(dt_mg.strftime('\nData:%d de %B de %Y\nSemana do ano: %W, Dia da Semana: %A\nHoras: %H:%M:%S, Fuso Horário: %Z (UTC %z)'))

print()
dt_str = '10 de July de 2022'

dat = dt.datetime.strptime(dt_str, '%d de %B de %Y')

print(dat)
