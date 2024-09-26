from tkinter import messagebox
import customtkinter  as ctk



class SistemaLogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Login")
        self.janela.geometry("400x400")

        # Simulação de banco de dados de usuários (credenciais armazenadas como dicionário)
        self.usuarios = {
            "admin": {"senha": "admin123", "cargo": "Administrador"},
            "medico": {"senha": "medico123", "cargo": "Médico"},
            "recepcionista": {"senha": "recepcao123", "cargo": "Recepcionista"}
        }

        # Criar a interface de login
        self.criar_interface_login()

    def criar_interface_login(self):
        # Limpar a janela atual para trocar de interface
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        # Interface de Login
        
        
        label_usuario = ctk.CTkLabel(self.janela, text="Usuário:")
        label_usuario.grid(row=0, column=0, padx=10, pady=10)

        self.entry_usuario = ctk.CTkEntry(self.janela, placeholder_text="Digite seu ID")
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        label_senha = ctk.CTkLabel(self.janela, text="Senha:")
        label_senha.grid(row=1, column=0, padx=10, pady=10)

        self.entry_senha = ctk.CTkEntry(self.janela, show="*", placeholder_text="Digite sua senha")
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10)

        btn_login = ctk.CTkButton(self.janela, text="Login", command=self.verificar_login)
        btn_login.grid(row=2, column=1, padx=10, pady=10)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario in self.usuarios and self.usuarios[usuario]["senha"] == senha:
            cargo = self.usuarios[usuario]["cargo"]
            self.abrir_painel(cargo)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    
    def abrir_painel_admin(self):
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Administrador!")
        # Adicionar aqui os elementos da interface para administradores

    def abrir_painel_medico(self):
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Médico!")
        # Adicionar aqui os elementos da interface para médicos

    def abrir_painel_recepcionista(self):
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Recepcionista!")
        # Adicionar aqui os elementos da interface para recepcionistas

    
    
