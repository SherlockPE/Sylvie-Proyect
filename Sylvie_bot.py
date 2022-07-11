#NOTA: EL PROGRAMA QUE HICE SOLO SOPORTA LA MEDIDA DE PANTALLA 2088 X 1880
import pyautogui, time

cantidadDeVeces = 300
time.sleep(1)

def hacerClick(x, y, numDeCliks = 1):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left', clicks = numDeCliks)
    time.sleep(1)

def enviarTexto(archivo):
    with open(archivo, "r") as lineas:
        contenido = lineas.readlines()

    for i in range(len(contenido)):
        pyautogui.typewrite(contenido[i])
        pyautogui.press("enter")
        time.sleep(1)

def enviarSticker():
    hacerClick(466, 866)#Abrir panel
    hacerClick(595, 867)#Seleccionar enviar sticker
    hacerClick(682, 680)#Enviar sticker
    hacerClick(466, 866)#Cerrar panel

def enviarMensaje():
    time.sleep(1)
    enviarTexto("1.txt")
    pyautogui.press("enter")

    #Enviar foto
    hacerClick(508, 866)#Clip
    hacerClick(505, 800)#Fotos y videos
    hacerClick(1043, 91)#seleccionar foto
    hacerClick(1066, 424)#abrir foto
    hacerClick(720, 768)
    
    #Enviar texto
    enviarTexto("2.txt")
    enviarTexto("3.txt")
    enviarSticker()

    time.sleep(1)


def main():
    for n in range(cantidadDeVeces + 1):
        hacerClick(349, 26, 2)
        hacerClick(133, 133)
        pyautogui.press("down", presses = n)
        pyautogui.press("enter")

        #Enviar Mensaje
        enviarMensaje()

        time.sleep(2)
        #pyautogui.press("esc")

if __name__ == "__main__":
    main()
    