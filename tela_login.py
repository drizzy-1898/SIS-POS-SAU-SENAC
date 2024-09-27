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
        frame = ctk.CTkFrame(self.janela)
        frame.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o frame na janela

        # Adicionar a logo
        self.logo = Image.open("C:/Users/Clean Vision/Downloads/file.png")  # Corrigido o caminho
        self.logo = self.logo.resize((200, 200), Image.LANCZOS)  # Use Image.LANCZOS para redimensionar

        # Converter a imagem para CTkImage
        self.logo_image = ImageTk.PhotoImage(self.logo)

        label_logo = ctk.CTkLabel(frame, image=self.logo_image)
        label_logo.grid(row=0, column=0, columnspan=2, pady=(0, 10))  # Coloca a logo na primeira linha

        # Interface de Login
        label_usuario = ctk.CTkLabel(frame, text="Usuário:")
        label_usuario.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_usuario = ctk.CTkEntry(frame, placeholder_text="Digite seu ID", width=200)
        self.entry_usuario.grid(row=1, column=1, padx=10, pady=10)

        label_senha = ctk.CTkLabel(frame, text="Senha:")
        label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_senha = ctk.CTkEntry(frame, show="*", placeholder_text="Digite sua senha", width=200)
        self.entry_senha.grid(row=2, column=1, padx=10, pady=10)

        btn_login = ctk.CTkButton(frame, text="Login", command=self.verificar_login)
        btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

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
