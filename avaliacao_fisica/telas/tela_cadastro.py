import customtkinter as ctk
from banco import salvar_aluno


def abrir_cadastro(app):
    janela = ctk.CTkToplevel(app)
    janela.after(100, janela.lift)
    janela.title('Cadastrar Aluno')
    janela.geometry('400x500')

    ctk.CTkLabel(janela, text='Cadastrar Aluno',
                 font=ctk.CTkFont(size=20, weight='bold')).pack(pady=20)
    
    ctk.CTkLabel(janela, text='Nome:').pack()
    entry_nome = ctk.CTkEntry(janela, width=300)
    entry_nome.pack(pady=5)
    
    ctk.CTkLabel(janela, text='Idade:').pack()
    entry_idade = ctk.CTkEntry(janela, width=300)
    entry_idade.pack(pady=5)

    ctk.CTkLabel(janela, text='Sexo (M/F):').pack()
    entry_sexo = ctk.CTkEntry(janela, width=300)
    entry_sexo.pack(pady=5)

    ctk.CTkLabel(janela, text='Altura (m):').pack()
    entry_altura = ctk.CTkEntry(janela, width=300)
    entry_altura.pack(pady=5)

    ctk.CTkLabel(janela, text='Peso (kg):').pack()
    entry_peso = ctk.CTkEntry(janela, width=300)
    entry_peso.pack(pady=5)

    def salvar():
        nome = entry_nome.get()
        idade = int(entry_idade.get())
        sexo = entry_sexo.get().upper()
        altura = float(entry_altura.get().replace(',', '.'))
        peso = float(entry_peso.get().replace(',', '.'))
        salvar_aluno(nome, idade, sexo, peso, altura)
        janela.destroy()

    ctk.CTkButton(janela, text='Salvar Aluno',
                  width=300, height=45,
                  command=salvar).pack(pady=20)
    

