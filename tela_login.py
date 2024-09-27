from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

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

        # Criar um frame para centralizar a interface
        self.frame = ctk.CTkFrame(self.janela, fg_color="#FFFFFF")
        self.frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8, relheight=0.8)  # Centraliza o frame na janela

        # Configurar a única coluna que centralizará os widgets
        self.frame.grid_columnconfigure(0, weight=1)

        # Carregar e redimensionar a imagem
        self.logo = Image.open("D:/Users/Aluno/Documents/SIS-POS-SAU/file.png")
        self.logo = self.logo.resize((150, 150), Image.LANCZOS)

        # Convertê-la para um CTkImage
        self.logo_image = ctk.CTkImage(self.logo, size=(150, 150))

        # Criar o label com a imagem
        self.label_logo = ctk.CTkLabel(self.frame, image=self.logo_image, text="")
        self.label_logo.grid(row=0, column=0, pady=(0, 10), sticky="n")  # Centralizado

        # Entry para o usuário
        self.entry_usuario = ctk.CTkEntry(self.frame, placeholder_text="Usuário", width=200)
        self.entry_usuario.grid(row=1, column=0, padx=10, pady=10)

        # Entry para a senha
        self.entry_senha = ctk.CTkEntry(self.frame, show="*", placeholder_text="Senha", width=200)
        self.entry_senha.grid(row=2, column=0, padx=10, pady=10)
        
        self.btn_login = ctk.CTkButton(self.frame, text="Login", command=self.verificar_login, width=200)
        self.btn_login.grid(row=3, column=0, padx=10, pady=10)

    
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

# Para rodar a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = SistemaLogin(root)
    root.mainloop()
