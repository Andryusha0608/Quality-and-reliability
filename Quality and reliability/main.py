import time

import warnings

warnings.simplefilter('ignore', category=UserWarning)
from pywinauto.application import Application
from pynput.keyboard import Key, Controller


# Отдельно заводим переменную порта, логин и пароль пользователя, IP-адрес подключения
PORT = '22'
LOGIN = 'andrysha0608'
PASSWORD = 'nKXdixrROzYp8Q'
IP = 'tty.sdf.org'
HOST = (LOGIN + '@' + IP)

# Запуск приложения
app = Application().start(cmd_line=r"C:\putty.exe")
time.sleep(5)

# Организация процесса подключения
window = app.top_window()
edit = window.Edit0
window.Edit2.set_text(PORT)
edit.type_keys(HOST)
window["Соединиться"].click()
time.sleep(5)

# Организация обработки автоматических нажатий на клавиатуре
ssh = app.top_window()

ssh.set_focus()
keybord = Controller()
keybord.type(PASSWORD)
keybord.press(Key.enter)
time.sleep(3)
keybord.press(Key.backspace)
time.sleep(2)
keybord.press(Key.enter)
time.sleep(2)
keybord.press(Key.enter)
time.sleep(2)
