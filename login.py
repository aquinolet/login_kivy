from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from kivy.utils import get_color_from_hex

class MeuApp(App):
    def login(self):
        Window = BoxLayout(orientation='vertical', padding=[120,120], spacing=11)

        #imagem
        im = AsyncImage(source="https://cdn-icons-png.flaticon.com/512/9187/9187604.png")

        #textos
        texto = Label(text='LOGIN', font_size=40, font_name=('Arial'))
        texto1 = Label(text='Usuário:', font_size=20, color=get_color_from_hex('#8576FF'))
        texto2 = Label(text='Senha:',font_size=20, color=get_color_from_hex('#8576FF'))

        #caixa de inserir
        email = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))
        senha = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))

        #botoes
        botao_login = Button(text='Login', on_press=self.botao_l, background_color=get_color_from_hex('#8576FF'))
        botao_cadastro = Button(text='Fazer cadastro', background_color=get_color_from_hex('#8576FF'))

        #aparecer mensagem
        self.label_mensagem = Label(color=get_color_from_hex('#8576FF'))


        Window.add_widget(texto)
        Window.add_widget(im)
        Window.add_widget(texto1)
        Window.add_widget(email)
        Window.add_widget(texto2)
        Window.add_widget(senha)
        Window.add_widget(self.label_mensagem)
        Window.add_widget(botao_login)
        Window.add_widget(botao_cadastro)

        return Window
    
    def botao_l(self,instance):
        mensagem = 'Login feito com sucesso!'
        self.label_mensagem.text = mensagem

if __name__=='__main__':
    MeuApp().run()
