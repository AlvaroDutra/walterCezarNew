import PySimpleGUI as sg
import main

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('message'),sg.Input()],
            [sg.Button('Enviar Mensagem')]
        ]

        Janela = sg.Window('Enviar Mensagens').layout(layout)
        self.button, self.values = Janela.Read()
        pass

    def Iniciar(self):
        print(self.values)
        main.sendMessage(self.values[0])

tela = TelaPython()
tela.Iniciar()