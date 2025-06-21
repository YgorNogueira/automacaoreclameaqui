import pyautogui
import pyperclip
import time
import os

# — Coordenadas (ajuste se necessário) —
x_start, y_start   = -1312, 711
x_end,   y_end     = -671, 855
x_button, y_button = -922, 904

# — Tempo para você posicionar a janela do navegador —
time.sleep(6)

# — Garante que o arquivo exista (e zera seu conteúdo) —
txt_path = 'reclamacoes.txt'
with open(txt_path, 'w', encoding='utf-8') as f:
    pass

for i in range(1, 19):
    # 1) Scroll inicial
    pyautogui.scroll(-850)
    time.sleep(0.5)

    # 2) Arraste “segurando” do ponto A ao ponto B
    pyautogui.moveTo(x_start, y_start, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(x_end, y_end, duration=1.0)
    pyautogui.scroll(-1800)
    pyautogui.mouseUp()
    time.sleep(0.5)

    # 3) Copiar seleção
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    texto = pyperclip.paste()

    # 4) Incrementar no arquivo
    with open(txt_path, 'a', encoding='utf-8') as f:
        f.write(f"--- Reclamação {i} ---\n")
        f.write(texto.strip() + "\n\n")

    # 5) Clicar no botão para próxima reclamação/página
    pyautogui.moveTo(x_button, y_button, duration=0.5)
    pyautogui.click()
    time.sleep(3)  # aguarda carregar a próxima seção

print(f"✅ Feito! Veja todas as reclamações em: {os.path.abspath(txt_path)}")
