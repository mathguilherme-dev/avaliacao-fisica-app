import customtkinter as ctk
from banco import listar_alunos
from telas.tela_avaliacao import abrir_avaliacao


def abrir_busca(app):
    janela = ctk.CTkToplevel(app)
    janela.title('Buscar Aluno')
    janela.geometry('400x500')
    janela.after(100, janela.lift)

    ctk.CTkLabel(janela, text='Selecionar Aluno',
                font=ctk.CTkFont(size=20, weight='bold')).pack(pady=20)
    
    alunos = listar_alunos()
    alunos_ordenados = sorted(alunos, key=lambda a: a[1])

    for aluno in alunos_ordenados:
        ctk.CTkButton(
            janela,
            text=aluno[1],
            width=300,
            height=40,
            command=lambda a=aluno: [janela.destroy(), abrir_perfil(app, a)]
        ).pack(pady=5)

def abrir_perfil(app, aluno):
    janela = ctk.CTkToplevel(app)
    janela.title(f'Perfil - {aluno[1]}')
    janela.geometry('400x350')
    janela.after(100, janela.lift)

    ctk.CTkLabel(
        janela, 
        text=aluno[1],
        font=ctk.CTkFont(size=22,weight='bold')
        ).pack(pady=20)
    
    ctk.CTkLabel(janela, text=f"Idade: {aluno[2]} anos").pack(pady=5)
    ctk.CTkLabel(janela, text=f"Sexo: {aluno[3]}").pack(pady=5)
    ctk.CTkLabel(janela, text=f"Peso: {aluno[4]} kg").pack(pady=5)
    ctk.CTkLabel(janela, text=f"Altura: {aluno[5]} m").pack(pady=5)

    ctk.CTkButton(
        janela,
        text='Nova Avaliação',
        width=300,
        height=45,
        command=lambda: [janela.destroy(), abrir_avaliacao(app, aluno)]
    ).pack(pady=15)

    ctk.CTkButton(
        janela,
        text='Ver Avaliações Anteriores',
        width=300,
        height=45
    ).pack(pady=5)

    ctk.CTkButton(
        janela,
        text='<- Voltar',
        width=300,
        height=40,
        fg_color='transparent',
        border_width=2,
        command=janela.destroy
    ).pack(pady=5)
