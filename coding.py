# Step by step of the project
# Step 1: Enter in the company system
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui #pip install pyautogui (terminal)
import time

#pyautogui.click : Click with mouse
#pyautogui.write : Write a text
#pyautogui.press : Press a key
#pyautogui.hotkey : Shortcut (key combination)
#pyautogui.scroll() : use scroll 

pyautogui.PAUSE = 0.5

# open chorme
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=952, y=649)

# enter link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# await the site load
time.sleep(1.5)

# Step 2: Login
pyautogui.click(x=745, y=363)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.click(x=781, y=468)
pyautogui.write('sua senha aqui')
pyautogui.press('enter')

time.sleep(3)

# Step 3: Import database of products
# pip install numpy openpyxl (terminal)

import pandas

table = pandas.read_csv('produtos.csv')
print(table)

for line in table.index:
    # Step 4: Register product
    pyautogui.click(x=744, y=249)

    codigo = table.loc[line, 'codigo']
    
    # Fill in the fields
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[line, 'marca']))
    pyautogui.press('tab')  
    pyautogui.write(str(table.loc[line, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[line, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[line, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[line, 'custo']))
    pyautogui.press('tab')
    obs = table.loc[line, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    
    # Press to send
    pyautogui.press('tab')
    pyautogui.press('enter')

# Step 5: Repeat the register for all products
