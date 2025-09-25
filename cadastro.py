import tkinter as tk
from tkinter import ttk, messagebox

# Função para verificar se a pessoa é maior de idade
def verificar_maioridade(idade):
    try:
        idade = int(idade)
        if idade >= 18:
            return "Maior"
        else:
            return "Menor"
    except ValueError:
        return "Idade inválida"

# Função que será chamada ao clicar em "Cadastrar"
def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()
    parentesco = entry_parentesco.get()
    cidade = entry_cidade.get()  # campo opcional

    info_idade = verificar_maioridade(idade)

    familiar = f"Nome: {nome} | Idade: {idade} | Telefone: {telefone} | Parentesco: {parentesco} | Cidade: {cidade} | {info_idade}"
    lista_familiares.insert(tk.END, familiar)

    # limpa os campos
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_parentesco.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)

# Janela principal
root = tk.Tk()
root.title("Cadastro de Familiares")
root.geometry("850x650")
root.configure(bg="white")

# Estilo (usando ttk)
style = ttk.Style()
style.theme_use("clam")

# Cores personalizadas
style.configure("TLabel", background="black", foreground="white", font=("Arial", 11, "bold"))
style.configure("TButton", background="#2773F5", foreground="white", font=("Arial", 11, "bold"), padding=6)
style.map("TButton", background=[("active", "#2773F5")])

# Frame principal
frame = tk.Frame(root, bg="black", padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Título
titulo = tk.Label(frame, text="Cadastro de Familiares", bg="black", fg="white", font=("Arial", 18, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=15)

# Labels e campos de entrada
ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_nome = ttk.Entry(frame, width=40)
entry_nome.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Idade:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
entry_idade = ttk.Entry(frame, width=40)
entry_idade.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Telefone:").grid(row=3, column=0, sticky="e", pady=5, padx=5)
entry_telefone = ttk.Entry(frame, width=40)
entry_telefone.grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Parentesco:").grid(row=4, column=0, sticky="e", pady=5, padx=5)
entry_parentesco = ttk.Entry(frame, width=40)
entry_parentesco.grid(row=4, column=1, pady=5)

ttk.Label(frame, text="Cidade (opcional):").grid(row=5, column=0, sticky="e", pady=5, padx=5)
entry_cidade = ttk.Entry(frame, width=40)
entry_cidade.grid(row=5, column=1, pady=5)

# Botão cadastrar
btn_cadastrar = ttk.Button(frame, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=6, column=0, columnspan=2, pady=15)

# Lista para mostrar familiares
lista_familiares = tk.Listbox(frame, width=100, height=12, bg="white", fg="black", font=("Courier New", 10))
lista_familiares.grid(row=7, column=0, columnspan=2, pady=10)

# Dados iniciais (4 familiares)
familiares_iniciais = [
    {"nome": "Odilon", "idade": 62, "telefone": "91234-1234", "parentesco": "Pai", "cidade": "Pariquera-Açu"},
    {"nome": "Leonice", "idade": 42, "telefone": "99292-5678", "parentesco": "Tia", "cidade": "Pariquera-Açu"},
    {"nome": "Bruno", "idade": 25, "telefone": "98888-1221", "parentesco": "Primo", "cidade": "Registro"},
    {"nome": "Tânia", "idade": 71, "telefone": "99877-2112", "parentesco": "Avó", "cidade": "Pariquera-Açu"}
]

for f in familiares_iniciais:
    info_idade = verificar_maioridade(f["idade"])
    familiar = f"Nome: {f['nome']} | Idade: {f['idade']} | Telefone: {f['telefone']} | Parentesco: {f['parentesco']} | Cidade: {f['cidade']} | {info_idade}"
    lista_familiares.insert(tk.END, familiar)

root.mainloop()
