import sqlite3 
import customtkinter as ctk 

    
#criar funcionalidades 
def cadastro_clientes(): 
    nome = nome.get()
    data_nascimento = data.get() 
    CPF = cpf.get() 
    contato = contato.get() 
    email = email.get() 

#configurar aparencia 
ctk.set_appearance_mode('dark') 

#criar janela principal 
app = ctk.CTk() 
app.title('Cadastro de Clientes') 
app.geometry('800x600') 

#criar os campo 
label_nome = ctk.CTkLabel(app,text='Nome') 
label_nome.pack(pady=10) 
campo_nome = ctk.CTkEntry(app,placeholder_text='Digite o nome') 
campo_nome.pack(pady=10) 

label_data = ctk.CTkLabel(app,text='Data') 
label_data.pack(pady=10)
campo_data = ctk.CTkEntry(app,placeholder_text='Digite a data de nascimento') 
campo_data.pack(pady=10)

label_cpf = ctk.CTkLabel(app,text='CPF') 
label_cpf.pack(pady=10) 
campo_cpf = ctk.CTkEntry(app,placeholder_text='Digite o CPF') 
campo_cpf.pack(pady=10)

label_contato = ctk.CTkLabel(app,text='Contato') 
label_contato.pack(pady=10)
campo_contato = ctk.CTkEntry(app,placeholder_text='Digite o contato') 
campo_contato.pack(pady=10)   

label_email = ctk.CTkLabel(app,text='Email') 
label_email.pack(pady=10)   
campo_email = ctk.CTkEntry(app,placeholder_text='Digite o email') 
campo_email.pack(pady=10)  

botao_cadastro = ctk.CTkButton(app,text='Cadastrar',command=cadastro_clientes) 
botao_cadastro.pack(pady=10) 

app.mainloop()