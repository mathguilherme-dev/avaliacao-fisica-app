import customtkinter as ctk
from telas.tela_cadastro import abrir_cadastro
from telas.tela_historico import abrir_busca

app = ctk.CTk()
app.title('Avaliaçao Matheus Guilherme Personal')
app.geometry('1100x700')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


titulo = ctk.CTkLabel(
    app,
    text='Avaliaçao Matheus Guilherme Personal',
    font=ctk.CTkFont(size=24, weight='bold')
)
titulo.pack(pady=40)

btn_novo = ctk.CTkButton(
    app,
    text='+ Novo Aluno',
    width=200,
    height=50,
    font=ctk.CTkFont(size=16),
    command=lambda: abrir_cadastro(app)
)
btn_novo.pack(pady=10)


btn_buscar = ctk.CTkButton(
    app,
    text='Buscar Aluno',
    width=200,
    height=50,
    font=ctk.CTkFont(size=16),
    command=lambda: abrir_busca(app)
)
btn_buscar.pack(pady=10)

app.mainloop()