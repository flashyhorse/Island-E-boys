import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

ARQUIVO = "estoque.json"

# ---------- FUNÇÕES DE ARQUIVO ----------
def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_dados():
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

# ---------- DADOS ----------
estoque = carregar_dados()

# ---------- FUNÇÕES ----------
def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)
    for produto in estoque:
        tree.insert("", "end", values=produto)

def validar_campos():
    if not entry_id.get().isdigit():
        messagebox.showerror("Erro", "ID deve ser numérico")
        return False
    if entry_nome.get() == "":
        messagebox.showerror("Erro", "Nome não pode ser vazio")
        return False
    if not entry_qtd.get().isdigit():
        messagebox.showerror("Erro", "Quantidade deve ser número inteiro")
        return False
    try:
        float(entry_preco.get().replace(",", "."))
    except:
        messagebox.showerror("Erro", "Preço inválido")
        return False
    return True

def adicionar_produto():
    if not validar_campos():
        return

    novo = (
        entry_id.get(),
        entry_nome.get(),
        f"R$ {entry_preco.get()}",
        int(entry_qtd.get()),
        entry_local.get()
    )
    estoque.append(novo)
    atualizar_tabela()
    limpar_campos()

def excluir_produto():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto para excluir")
        return

    item = tree.item(selecionado)
    valores = item["values"]

    estoque.remove(list(valores))
    atualizar_tabela()

def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    entry_local.delete(0, tk.END)

# ---------- JANELA ----------
root = tk.Tk()
root.title("Gerenciamento de Estoque")
root.geometry("950x520")
root.configure(bg="#f5f5f5")

# ---------- HEADER ----------
header = tk.Frame(root, bg="#f57c00", height=70)
header.pack(fill="x")

titulo = tk.Label(header, text="Gerenciamento de Estoque",
                  bg="#f57c00", fg="white",
                  font=("Arial", 18, "bold"))
titulo.pack(side="left", padx=20)

data_label = tk.Label(header,
                      text=datetime.now().strftime("%d/%m/%Y %H:%M"),
                      bg="#f57c00", fg="white")
data_label.pack(side="right", padx=20)

# ---------- BOTÕES ----------
frame_botoes = tk.Frame(root, bg="#f5f5f5")
frame_botoes.pack(pady=10)

btn_add = tk.Button(frame_botoes, text="Adicionar",
                    bg="#ff9800", fg="white", width=15,
                    command=adicionar_produto)
btn_add.grid(row=0, column=0, padx=5)

btn_del = tk.Button(frame_botoes, text="Excluir",
                    bg="#e53935", fg="white", width=15,
                    command=excluir_produto)
btn_del.grid(row=0, column=1, padx=5)

btn_save = tk.Button(frame_botoes, text="Salvar",
                     bg="#4caf50", fg="white", width=15,
                     command=salvar_dados)
btn_save.grid(row=0, column=2, padx=5)

# ---------- FORMULÁRIO ----------
form = tk.Frame(root, bg="#f5f5f5")
form.pack(pady=5)

labels = ["ID", "Produto", "Preço", "Qtd", "Localização"]
for i, text in enumerate(labels):
    tk.Label(form, text=text, bg="#f5f5f5").grid(row=0, column=i)

entry_id = tk.Entry(form, width=10)
entry_nome = tk.Entry(form, width=20)
entry_preco = tk.Entry(form, width=10)
entry_qtd = tk.Entry(form, width=5)
entry_local = tk.Entry(form, width=15)

entry_id.grid(row=1, column=0, padx=5)
entry_nome.grid(row=1, column=1, padx=5)
entry_preco.grid(row=1, column=2, padx=5)
entry_qtd.grid(row=1, column=3, padx=5)
entry_local.grid(row=1, column=4, padx=5)

# ---------- TABELA ----------
colunas = ("ID", "Produto", "Preço", "Quantidade", "Localização")

tree = ttk.Treeview(root, columns=colunas, show="headings", height=12)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True, padx=20, pady=10)

# ---------- ESTILO ----------
style = ttk.Style()
style.configure("Treeview", rowheight=28)
style.map("Treeview", background=[("selected", "#ffe0b2")])

# ---------- INICIAR ----------
atualizar_tabela()
root.mainloop()