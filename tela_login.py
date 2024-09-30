from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

class SistemaLogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Login")
        self.janela.geometry("400x400")

        # Simulação de banco de dados de usuários
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

        self.largura_tela = self.janela.winfo_screenwidth()
        self.altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{self.largura_tela}x{self.altura_tela}+0+0")
        
        # Criar um frame para centralizar a interface
        self.frame = ctk.CTkFrame(self.janela, border_width=3, border_color="#00CED1", fg_color="#FFFFFF")
        self.frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.2, relheight=0.5)

        # Configurar as colunas para centralizar os widgets
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Carregar e redimensionar a imagem
        self.logo = Image.open("D:/Users/Aluno/Documents/SIS-POS-SAU/file.png")
        self.logo = self.logo.resize((150, 150), Image.LANCZOS)

        # Convertê-la para um CTkImage
        self.logo_image = ctk.CTkImage(self.logo, size=(150, 150))

        # Carregar ícones
        self.icon_user = Image.open("D:/Users/Aluno/Documents/SIS-POS-SAU/user_login.png")
        self.icon_user = self.icon_user.resize((25, 25), Image.LANCZOS)
        self.icon_user = ImageTk.PhotoImage(self.icon_user)

        self.icon_password = Image.open("D:/Users/Aluno/Documents/SIS-POS-SAU/password_login.png")
        self.icon_password = self.icon_password.resize((25, 25), Image.LANCZOS)
        self.icon_password = ImageTk.PhotoImage(self.icon_password)

        # Criar o label com a imagem (logo)
        self.label_logo = ctk.CTkLabel(self.frame, image=self.logo_image, text="")
        self.label_logo.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="n")

        # Label para Usuário
        self.label_usuario = ctk.CTkLabel(self.frame, text="Usuário", font=("Arial", 12))
        self.label_usuario.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0))

        # Entry para o usuário
        self.entry_usuario = ctk.CTkEntry(self.frame, placeholder_text="Digite seu usuário", width=250, font=("Arial", 16))
        self.entry_usuario.grid(row=2, column=1, padx=10, pady=(0, 20), sticky="w")

        # Label Icon User
        self.label_user_icon = ctk.CTkLabel(self.frame, image=self.icon_user, text="")
        self.label_user_icon.grid(row=2, column=0, padx=(0, 5), pady=(0, 20), sticky="e")

        # Label para Senha
        self.label_senha = ctk.CTkLabel(self.frame, text="Senha", font=("Arial", 12))
        self.label_senha.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 0))

        # Entry para a senha
        self.entry_senha = ctk.CTkEntry(self.frame, show="*", placeholder_text="Digite sua senha", width=250, font=("Arial", 16))
        self.entry_senha.grid(row=4, column=1, padx=10, pady=(0, 20), sticky="w")

        # Label Icon Senha
        self.label_password_icon = ctk.CTkLabel(self.frame, image=self.icon_password, text="")
        self.label_password_icon.grid(row=4, column=0, padx=(0, 5), pady=(0, 20), sticky="e")

        # Botão de Login
        self.btn_login = ctk.CTkButton(self.frame, text="Login", command=self.verificar_login, width=200, font=("Arial", 16))
        self.btn_login.grid(row=5, column=0, columnspan=2, padx=10, pady=20, sticky="n")
        
        # Botão "Esqueci a Senha"
        self.btn_esqueci_senha = ctk.CTkButton(self.frame, text="Esqueci a Senha", command=self.esqueci_senha, width=150, fg_color="#e23a3b", font=("Arial", 12))
        self.btn_esqueci_senha.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 0))

    
    def esqueci_senha(self):
        messagebox.showinfo("Recuperação de Senha", "A opção de recuperação de senha não está implementada.")
    
    
    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario in self.usuarios and self.usuarios[usuario]["senha"] == senha:
            cargo = self.usuarios[usuario]["cargo"]
            self.abrir_painel(cargo)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    def abrir_painel(self, cargo):
        if cargo == "Administrador":
            self.abrir_painel_admin()
        elif cargo == "Médico":
            self.abrir_painel_medico()
        elif cargo == "Recepcionista":
            self.abrir_painel_recepcionista()

    def abrir_painel_admin(self):
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Administrador!")

    def abrir_painel_medico(self):
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Médico!")

    def abrir_painel_recepcionista(self):
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Recepcionista!")

