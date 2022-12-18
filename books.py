import pandas as pd
from colorama import init, Fore

init(autoreset=True)

def diagram(year):
    data = pd.read_csv('books-en.csv', delimiter=';', encoding='Latin_1')
    output = pd.DataFrame()

    total = len(data)
    output = data[data['Year-Of-Publication'] <= year]
    before = len(output)
    after = total - before

    before_percent = int(before/total*100)
    after_percent = int(after/total*100)

    print()
    print('before ', year, ' :', Fore.LIGHTCYAN_EX+'0'*before_percent)
    print('after  ', year, ' :', Fore.LIGHTYELLOW_EX+'0'*after_percent)