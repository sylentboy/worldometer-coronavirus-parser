import urllib.request
import re

try:
    p = urllib.request.urlopen('https://www.worldometers.info/coronavirus/')

except:
    print('We have some problems, try again later!')
    exit()

cases = re.findall(r'[\d]{1,3},[\d]{3}', str(p.read()))

print('COVID-19')

print('''
Всего было заражено {0} 
В реальном времени под наблюдением {1}
Зараженные находящиеся в хорошем состоянии {2}
Находится в критическом состоянии {3}
'''.format(cases[0], cases[5], cases[6], cases[7]))

print('Смертей {0}. Выздоровевших {1}.'.format(cases[1], cases[4]))