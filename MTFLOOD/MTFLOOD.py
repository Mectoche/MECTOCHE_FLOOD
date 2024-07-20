# __  __ _______   ______ _      ____   ____  _____  
# |  \/  |__   __| |  ____| |    / __ \ / __ \|  __ \ 
# | \  / |  | |    | |__  | |   | |  | | |  | | |  | |
# | |\/| |  | |    |  __| | |   | |  | | |  | | |  | |
# | |  | |  | |    | |    | |____ |__| | |__| | |__| |
# |_|  |_|  |_|    |_|    |______\____/ \____/|_____/ 

# Ⓡ Developed by: @Mectoche Ⓡ

import time
import random

import tkinter as tk
import pyautogui as py

from tkinter import Canvas, messagebox

titl = "𝑴𝑬𝑪𝑻𝑶𝑪𝑯𝑬 𝑭𝑳𝑶𝑶𝑫"

class MTFLOOD:
    
    def __init__(self, menu):
        self.menu = menu
        self.menu.title(f"{titl}")
        self.menu.geometry("390x720")
        self.menu.attributes("-toolwindow", True)

        self.canvas = Canvas(menu, bg="purple")
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.recta = []
        self.create_rectangles()

        self.create_buttons()

        self.flood = False
        

        
    def create_buttons(self):
        message = "Insira a mensagem: "
        label_ = tk.Label(self.menu, text=f"{message}", font=("Arial", 20))
        label_.pack(pady=40)

        self.prohibited = tk.Entry(self.menu, width=50, font=("Arial", 20))
        self.prohibited.pack(pady=20)

        self.button = tk.Button(self.menu, text="✅", width=30, height=4, command=self.button_click)
        self.button.pack(pady=10)

        self.button_exit = tk.Button(self.menu, text="❌", width=30, height=5, command=self.button_exit)
        self.button_exit.pack(pady=10)

        self.button_info = tk.Button(self.menu, text="⚠️", width=1, height=1, command=self.button_info)
        self.button_info.pack(side=tk.RIGHT, pady=0)

        
        
    def create_rectangles(self):
        numer = 50
        for _ in range(numer):
            x1 = random.randint(0, 340)
            y1 = random.randint(0, 370)
            x2 = x1 + random.randint(20, 40)
            y2 = y1 + random.randint(10, 20)
            color = random.choice(['lavender', 'lavender blush'])
            vector = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.recta.append(vector)
            
            

    def bgAnimation(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        for rect in self.recta:
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            self.canvas.move(rect, dx, dy)
            x1, y1, x2, y2 = self.canvas.coords(rect)
            if x1 < 0 or x2 > canvas_width:
                dx = -dx
            if y1 < 0 or y2 > canvas_height:
                dy = -dy

            self.canvas.move(rect, dx, dy)
        self.menu.after(50, self.bgAnimation)

        
        
    def button_click(self):
        if not self.flood:
            message = self.prohibited.get()
            if message:
                messagebox.showinfo(f"{titl}", f"O flood com a mensagem '{message}' foi iniciado com sucesso!")
                self.flood = True
                self.on_flood(message)
            else:
                messagebox.showwarning(f"{titl}", "Por favor, insira uma mensagem para iniciar o flood.")
        else:
            messagebox.showwarning(f"{titl}", "O flood já está em execução!")
            
            

    def on_flood(self, message):
        self.flood = True
        for _ in range(50):
            py.typewrite(message + '\n')
            py.press("Enter")
            time.sleep(random.uniform(0.1, 0.3))
            if not self.flood:
                break

                
    def button_exit(self):
        self.flood = False
        messagebox.showwarning(f"{titl}", "Você finalizou o flood!")
        
        

    def button_info(self):
        messagebox.showwarning(f"{titl}", "--------------------------------------------------------------------------\n"
                                          "Um software de flood, que incessantemente reproduzirá a mesma mensagem,\n"
                                          "foi desenvolvido com o intuito de trolar seus amigos.\n"
                                          "Este software é projetado para automatizar o envio repetitivo de informações específicas,\n"
                                          "assegurando que a mensagem seja amplamente enviada sem interrupções,\n"
                                          "--------------------------------------------------------------------------\n"
                                          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
                                          "Sistema criado pelo Mectoche!\n"
                                          "[Discord, Twitter, Youtube, Instagram, Github] = @Mectoche\n"
                                          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
                               )


if __name__ == "__main__":
    menu = tk.Tk()
    
    app = MTFLOOD(menu)
    app.bgAnimation()  
    
    menu.mainloop()
