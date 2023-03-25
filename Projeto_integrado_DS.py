import tkinter as tk
from tkinter import ttk #para a combobox
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np


requisicao=requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas=requisicao.json()
                    
lista_moedas=list(dicionario_moedas.keys())


def procurarcotacao():
    try:
        moeda=combo_box_selecionarmoeda.get()
        data_cotacao=calendario_moeda.get()
        ano=data_cotacao[-4:]
        mes=data_cotacao[3:5]
        dia=data_cotacao[:2]
        link=f"https://economia.awesomeapi.com.br/json/daily/{moeda}-EUR/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
        requisicao_moeda=requests.get(link)
        cotacao=requisicao_moeda.json()
        valor_moeda=cotacao[0]['bid']
        label_textocotacao['text']= f'A cotação da moeda {moeda} no dia {data_cotacao} foi de €{valor_moeda}. ' 
    except:
        label_textocotacao['text']= f'Não existe cotação para a moeda selecionada nesse dia.' 

def selecionararquivo():
    caminho_arquivo=askopenfilename(title='Selecione um arquivo em excel para abrir')
    var_caminhoarquivo.set(caminho_arquivo) # gravo num variável tkinter o caminho
    if caminho_arquivo:
        Label_arquivoselecionado['text']=f"Arquivo selecionado: {caminho_arquivo}."

def atualizarcotacoes():
    try:
        #ler o dataframe de moedas
        df=pd.read_excel(var_caminhoarquivo.get())
        moedas=df.iloc[:,0]
        #obter a data de início e de fim
        datainicial=calendario_datainicial.get()
        ano_inicial=datainicial[-4:]
        mes_inicial=datainicial[3:5]
        dia_inicial=datainicial[:2]

        datafinal=calendario_datafinal.get()
        ano_final=datafinal[-4:]
        mes_final=datafinal[3:5]
        dia_final=datafinal[:2]
        
        #para cada moeda
        for moeda in moedas:
            #obter todas as cotações daquela moeda
            link=f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano_inicial}{mes_inicial}{dia_inicial}&end_date={ano_final}{mes_final}{dia_final}"
            requisicao_moeda=requests.get(link)
            cotacoes=requisicao_moeda.json() # é uma lista com um dicionário por dia em que eu quero apenas o bid 
            for cotacao in cotacoes: #percorrer a lista de cotações
                timestamp=int(cotacao['timestamp'])
                data=datetime.fromtimestamp(timestamp)
                data=data.strftime('%d/%m/%Y')
                bid=float(cotacao['bid'])
                
                if data not in df: #validar se já existe a coluna no dataframe
                    df[data]=np.nan

                df.loc[df.iloc[:,0]==moeda, data]=bid #acrecentar a cotação onde na primeira coluna a linha é igual à moeda e na coluna data

        df.to_excel(r"C:\Users\fiu126\Desktop\Impressionador\Modulo TKInter\projeto_integrado\Output.xlsx")
        Label_atualizarcotacoes['text']='Arquivo atualizado com sucesso.'
    except:
        Label_atualizarcotacoes['text']='Selecione um arquivo excel no formato correto.'


janela=tk.Tk()

janela.title('Ferramenta de Cotação de moedas')

# Parte 1 -> Cotação de 1 moeda específica

Label_cotacaomoeda=tk.Label(text='Cotação de uma moeda específica', borderwidth=2, relief='solid') #borda e o tipo de borda
Label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew', columnspan=3) #padx e pady a distância do objeto

Label_selecionarmoeda=tk.Label(text='Selecionar Moeda', anchor='e') 
Label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=2) 

combo_box_selecionarmoeda=ttk.Combobox(values=lista_moedas)
combo_box_selecionarmoeda.grid(row=1,column=2,padx=10, pady=10, sticky='nseW')

Label_selecionardia=tk.Label(text='Selecione o dia da cotação',anchor='e') 
Label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nseW', columnspan=2) 

calendario_moeda=DateEntry(year=2023,locale='pt_br')
calendario_moeda.grid(row=2,column=2, padx=10, pady=10, sticky='nseW')

label_textocotacao=tk.Label(text="")
label_textocotacao.grid(row=3,column=0,padx=10,pady=10, sticky='nsew',columnspan=2)

botao_vercotacao=tk.Button(text='Ver Cotação', command=procurarcotacao)
botao_vercotacao.grid(row=3,column=2,padx=10, pady=10,sticky='nsew')


# Parte 2 -> cotação de múltiplas moedas

Label_cotacavariasomoedas=tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
Label_cotacavariasomoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

Label_selecionararquivo=tk.Label(text='Selecione um arquivo em excel com as Moedas na coluna A')
Label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

var_caminhoarquivo=tk.StringVar() #variaa´vel aonde vou aramezar o caminho
botao_selecionararquivo=tk.Button(text='Clique para ', command=selecionararquivo)
botao_selecionararquivo.grid(row=5,column=2,padx=10, pady=10, sticky='nsew')

Label_arquivoselecionado=tk.Label(text='Nenhum arquivo selecionado.', anchor='e') #anchor para alinar a este
Label_arquivoselecionado.grid(row=6,column=0, columnspan=3 ,sticky='nsew',padx=10,pady=10)

Label_datainicial=tk.Label(text='Data Inicial',anchor='e')
Label_datafinal=tk.Label(text='Data Final',anchor='e')
Label_datainicial.grid(row=7,column=0,padx=10,pady=10,sticky='nsew')
Label_datafinal.grid(row=8,column=0,padx=10,pady=10,sticky='nsew')

calendario_datainicial=DateEntry(Year=2023, locale='pt_br')
calendario_datafinal=DateEntry(Year=2023, locale='pt_br')
calendario_datainicial.grid(row=7,column=1,padx=10,pady=10,sticky='nsew')
calendario_datafinal.grid(row=8,column=1,padx=10,pady=10,sticky='nsew')

botao_atualizarcotacoes=tk.Button(text='Atualizar Cotações', command=atualizarcotacoes)
botao_atualizarcotacoes.grid(row=9,column=0,padx=10,pady=10,sticky='nsew')

Label_atualizarcotacoes=tk.Label(text='')
Label_atualizarcotacoes.grid(row=9,column=2,columnspan=2, padx=10,pady=10,sticky='nsew')

botao_fechar=tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10,column=2,padx=10,pady=10,sticky='nsew')

janela.mainloop()