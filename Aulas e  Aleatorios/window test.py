import tkinter as tk

# Criando a janela principal
root = tk.Tk()
root.title("Tkinter Teste com Widgets")
root.geometry("400x400")

# Rótulo (Label)
label = tk.Label(root, text="Se você está vendo isso, Tkinter está funcionando!")
label.pack(pady=10)

# Botão (Button)
def on_button_click():
    label.config(text="Você clicou no botão!")  # Alterando o texto do rótulo

button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=10)

# Caixa de entreda de texto (Entry)
entry = tk.Entry(root)
entry.pack(pady=10)

#Caixa de Selecao (Checkbutton)
check_var = tk.BooleanVar()  # Variável para armazenar o estado (checked ou unchecked)
check_button = tk.Checkbutton(root, text="Aceito os termos", variable=check_var)
check_button.pack(pady=10)

# Botões de Opção (Radiobutton)
radio_var = tk.StringVar()  # Variável para armazenar a opção selecionada
radio_button1 = tk.Radiobutton(root, text="Opção 1", variable=radio_var, value="1")
radio_button2 = tk.Radiobutton(root, text="Opção 2", variable=radio_var, value="2")

radio_button1.pack(pady=5)
radio_button2.pack(pady=5)

# Exibindo a janela
root.mainloop()
