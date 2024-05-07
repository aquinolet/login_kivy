from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class MeuApp(App):
    def build(self):
        tela = BoxLayout(orientation='vertical',spacing=20, padding=[300,200])
        texto = Label(text='Login', font_size=70,size_hint=(None, None), halign='center')
        email = TextInput(text='Digite seu E-mail')
        senha = TextInput(text='Digite sua Senha')
        botao_login = Button(text='Login')
        botao_cadastro = Button(text='Cadastro')
        botao_login.bind(on_press=self.login)
        botao_cadastro.bind(on_press=self.cadastro)
        imagem = Image(source='imagem.png')

       
        tela.add_widget(texto)
        tela.add_widget(email)
        tela.add_widget(senha)
        tela.add_widget(botao_login)
        tela.add_widget(botao_cadastro)
        return tela

    def login(instance):
        print("Login feito com sucesso!")

    def cadastro(instance):
        print("Faça seu cadastro")



if __name__=='__main__':
    MeuApp().run()
