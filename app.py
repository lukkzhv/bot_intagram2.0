import pyautogui
from time import sleep
import webbrowser

def deslogar():
    pyautogui.click(x=1397, y=113, duration=1)
    pyautogui.sleep(0.5)
    pyautogui.click(x=88, y=818, duration=1)
    sleep(0.5)
    pyautogui.click(x=88, y=760, duration=1)
def curtir():
    pyautogui.click(x=700, y=710, duration=1)
    sleep(0.3)
def comentar():
    comentario = pyautogui.prompt(title='comentario', text='Comentario desejado')
    sleep(0.5)
    pyautogui.typewrite(comentario, interval=0.1)
    pyautogui.press('enter')

# aviso inializador
inicial = pyautogui.alert(title='inicializando', text='Enquanto o bot estiver rodando, não mexer na maquina.')
for loop in range(1, 5+1):
    while True:
        sleep(2)
        webbrowser.open('www.instagram.com.br')
        sleep(2)
        pyautogui.click(x=909, y=280, duration=1)
        user = pyautogui.prompt(title='Informacoes', text='Telefone, nome de usuário ou email')
        sleep(0.5)
        pyautogui.typewrite(user, interval=0.1)
        sleep(0.5)
        pyautogui.press('tab')
        password = pyautogui.password(title='Informacoes', text='Senha', mask='*')
        sleep(0.5)
        pyautogui.typewrite(password, interval=0.1)
        pyautogui.press('enter')
        sleep(3)
        pyautogui.click(x=830, y=525, duration=0.8)
        # sleep(0.8)
        # pyautogui.click(x=712, y=617, duration=0.8)
        sleep(1)
        pyautogui.click(x=91, y=270, duration=0.8)
        sleep(0.5)

        # pesquisar user
        search_user = pyautogui.prompt(title='search', text='Usuário desejado')
        sleep(1)
        pyautogui.typewrite(search_user, interval=0.1)
        sleep(1.2)
        pyautogui.click(x=177, y=280, duration=1)
        sleep(2.2)
        pyautogui.scroll(-600)
        pyautogui.click(x=513, y=500, duration=1)

        sleep(3)
        coracao = pyautogui.locateCenterOnScreen('coracao.png')
        if coracao:
            # se encontrar imagem, não fazer nada e deslogar da conta.
            deslogar()
            sleep(1440)
        else:
            # codigo pra curtir e comentar
            curtir()
            pyautogui.click(x=800, y=820, duration=1)
            sleep(0.3)
            comentar()
            sleep(1)
            deslogar()
            sleep(1440)
        
