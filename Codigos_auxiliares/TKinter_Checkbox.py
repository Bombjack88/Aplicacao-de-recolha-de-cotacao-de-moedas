import tkinter as tk

janela=tk.Tk()

var_promocoes=tk.IntVar() # valor que armazzena o valor da checkbox, se marcado=1, caso contrário=0
checkbox_promocoes=tk.Checkbutton(text='Deseja receber e-mails promocionais?',variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

#exemplo2
var_politicas=tk.IntVar() # valor que armazzena o valor da checkbox, se marcado=1, caso contrário=0
checkbox_politocas=tk.Checkbutton(text='Aceitar termos de uso e Políticas de Provacidade',variable=var_politicas)
checkbox_politocas.grid(row=1, column=0)




def enviar():
    #print(var_promocoes.get()) # diferença das checkbox -> fica guradada na variável auxiliar 
    if var_promocoes.get():
        print(f'Usuário deseja receber promoções.')
    else:
        print(f'Usuário não deseja receber promoções.')

    if var_politicas.get():
        print(f'Usuário concordou com Termos de Uso e Políticas de Privacidade.')
    else:
        print(f'Usuário não concordou.')




botao_enviar=tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()
