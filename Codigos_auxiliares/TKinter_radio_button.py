import tkinter as tk

janela=tk.Tk()



var_aviao=tk.StringVar(value='Classe Económca') # valor padrão por defeito

def Enviar():
    print(var_aviao.get())


botao_classeeconomica=tk.Radiobutton(text='Classe Económica',variable=var_aviao,value='Classe Económca', command=Enviar) # no value fica a resposata que quero quando seleciono a informação
botao_classeexecutiva=tk.Radiobutton(text='Classe Executiva',variable=var_aviao,value='Classe Executiva', command=Enviar)
botao_primeiraclasse=tk.Radiobutton(text='Primeira Classe',variable=var_aviao,value='Primeira Classe', command=Enviar)

botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)





#botao_enviar=tk.Button(text='Enviar', command=Enviar)
#botao_enviar.grid(row=1,column=0)


janela.mainloop()