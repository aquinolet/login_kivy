from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

class Cadastro(App):
    def build(self):
        Window2 = BoxLayout(orientation='vertical', padding=[120,120], spacing=11)

        #textos
        label = Label(text='CADASTRO',font_size=40, font_name=('Arial'))
        label1 = Label(text='Nome:', font_size=20, color=get_color_from_hex('#8576FF'))
        label2 = Label(text='E-mail:', font_size=20, color=get_color_from_hex('#8576FF'))
        label3 = Label(text='Celular:', font_size=20, color=get_color_from_hex('#8576FF'))
        label4 = Label(text='Senha:', font_size=20, color=get_color_from_hex('#8576FF'))

        #caixa de inserir
        nome = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))
        email = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))
        celular = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))
        senha = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))

        #Botão
        botao = Button(text='Cadastrar', background_color=get_color_from_hex('#8576FF'))

        Window2.add_widget(label)
        Window2.add_widget(label1)
        Window2.add_widget(nome)
        Window2.add_widget(label2)
        Window2.add_widget(email)
        Window2.add_widget(label3)
        Window2.add_widget(celular)
        Window2.add_widget(label4)
        Window2.add_widget(senha)
        Window2.add_widget(botao)

        return Window2
    
if __name__ == '__main__':
    Cadastro().run()
