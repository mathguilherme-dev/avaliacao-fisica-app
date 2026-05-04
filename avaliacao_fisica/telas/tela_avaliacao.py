import customtkinter as ctk
from banco import salvar_aluno
from telas.tela_resultados import abrir_resultados
from calculos import (
    calcular_imc,
    calcular_rcq,
    calcular_densidade,
    calcular_gordura,
    classificar_imc,
    classificar_rcq,
    classificar_gordura
)

def abrir_avaliacao(app, aluno):
    janela = ctk.CTkToplevel(app)
    janela.title(f'Nova Avaliaçao - {aluno[1]}')
    janela.geometry('480x600')
    janela.after(100, janela.lift)

    scroll = ctk.CTkScrollableFrame(janela)
    scroll.pack(pady=10, padx=10, fill='both', expand=True)

    ctk.CTkLabel(
        scroll,
        text=f'Avaliaçao - {aluno[1]}',
        font=ctk.CTkFont(size=20, weight='bold')
    ).pack(pady=15)

    ctk.CTkLabel(
        scroll,
        text='-- Perimetria (cm) --',
        font=ctk.CTkFont(size=14, weight='bold')
    ).pack(pady=10)

    campos_perimetria = [
        'Ombro', 'Torax', 'Braco direito', 'Braco Esquerdo', 'Cintura', 'Abdomen', 'Quadril', 'Coxa direita', 'Coxa esquerda',
    ]

    entries_perimetria = {}
    for campo in campos_perimetria:
        ctk.CTkLabel(scroll, text=f'{campo}:').pack()
        entry = ctk.CTkEntry(scroll, width=300)
        entry.pack(pady=3)
        entries_perimetria[campo] = entry

    ctk.CTkLabel(
        scroll,
        text='- Dobras Cutaneas (mm) -',
        font=ctk.CTkFont(size=14, weight='bold')
    ).pack(pady=10)

    campos_dobras = [
        'Peitoral', 'Axilar Media', 'Tricipital', 'Subescapular', 'Abdominal', 'Supra-iliaca', 'Coxa'
    ]

    entries_dobras = {}
    for campo in campos_dobras:
        ctk.CTkLabel(scroll, text=f'{campo}:').pack()
        entry = ctk.CTkEntry(scroll, width=300)
        entry.pack(pady=3)
        entries_dobras[campo] = entry

    ctk.CTkButton(
        scroll,
        text='Calcular e ver Resultados',
        width=300,
        height=45,
        font=ctk.CTkFont(size=15, weight='bold'),
        command=lambda: calcular(app, aluno, entries_perimetria, entries_dobras, janela)
    ).pack(pady=20)

    ctk.CTkButton(
        scroll,
        text='<- Voltar',
        width=300,
        height=40,
        fg_color='transparent',
        border_width=2,
        command=janela.destroy
    ).pack(pady=5)

def calcular(app, aluno, entries_perimetria, entries_dobras, janela):
    soma = sum([float(e.get().replace(',', '.')) for e in entries_dobras.values()])
    cintura = float(entries_perimetria['Cintura'].get().replace(',', '.'))
    quadril = float(entries_perimetria['Quadril'].get().replace(',', '.'))

    densidade = calcular_densidade(soma, aluno[2], aluno[3])
    gordura = calcular_gordura(densidade)
    massa_gorda = aluno[4] * (gordura / 100)
    massa_magra = aluno[4] - massa_gorda
    imc = calcular_imc(aluno[4], aluno[5])
    rcq = calcular_rcq(cintura, quadril)

    class_gordura = classificar_gordura(gordura, aluno[3], aluno[2])
    class_imc = classificar_imc(imc)
    class_rcq = classificar_rcq(rcq, aluno[3])

    resultados = {
        'gordura': gordura,
        'class_gordura': class_gordura,
        'massa_gorda': massa_gorda,
        'massa_magra': massa_magra,
        'imc': imc,
        'class_imc': class_imc,
        'rcq': rcq,
        'class_rcq': class_rcq
    }
    abrir_resultados(app, aluno, resultados)
