import customtkinter as ctk

def abrir_resultados(app, aluno, resultados):
    janela = ctk.CTkToplevel(app)
    janela.title(f'Resultados - {aluno[1]}')
    janela.geometry('500x600')
    janela.after(100, janela.lift)

    scroll = ctk.CTkScrollableFrame(janela)
    scroll.pack(pady=10, padx=10, fill='both', expand=True)

    ctk.CTkLabel(scroll, text=f'Resultados - {aluno[1]}', font=ctk.CTkFont(size=20, weight='bold')).pack(pady=15)

    ctk.CTkLabel(scroll, text=f"% Gordura: {resultados['gordura']:.2f}% — {resultados['class_gordura']}", font=ctk.CTkFont(size=14)).pack(pady=5)
    ctk.CTkLabel(scroll, text=f"Massa Gorda: {resultados['massa_gorda']:.2f} kg", font=ctk.CTkFont(size=14)).pack(pady=5)
    ctk.CTkLabel(scroll, text=f"Massa Magra: {resultados['massa_magra']:.2f} kg", font=ctk.CTkFont(size=14)).pack(pady=5)
    ctk.CTkLabel(scroll, text=f"IMC: {resultados['imc']:.2f} — {resultados['class_imc']}", font=ctk.CTkFont(size=14)).pack(pady=5)
    ctk.CTkLabel(scroll, text=f"RCQ: {resultados['rcq']:.2f} — {resultados['class_rcq']}", font=ctk.CTkFont(size=14)).pack(pady=5)

    ctk.CTkButton(
        scroll,
        text='<- Voltar',
        width=300,
        height=40,
        fg_color='transparent',
        border_width=2,
        command=janela.destroy
    ).pack(pady=10)