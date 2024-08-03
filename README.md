<p align="center">
<a href="https://github.com/Mectoche/MTFLOOD"><img src="https://i.ibb.co/rvZynSh/watching.gif" alt="watching" border="0"></a>
</p>

#       *MTFLOOD*

# About.

- **[MTFLOOD](https://github.com/Mectoche/MTFLOOD)** é um programa para trollar seus amigos em qualquer rede social.

- Feito para aqueles que gostam de uma boa brincadeira.

- Nota: lembre-se de instalar o Python e suas dependências

# Download
- para baixar o programa, clique [AQUI](https://github.com/Mectoche/MTFLOOD/tree/main/MTFLOOD/EXE)

#

# Flood of words.

- Eu usei esse sistema para saída de uma palavra por segundo.

```python

# Function to send messages.
# @Mectoche

 def on_flood(self, message):
        self.flood = True
        for _ in range(50):
            py.typewrite(message + '\n')
            py.press("Enter")
            time.sleep(random.uniform(0.1, 0.3))
            if not self.flood:
                break


```
# Imagem para retratar


<a href="https://github.com/Mectoche/MTFLOOD/"><img src="https://i.ibb.co/5Rf7wq9/Sem-t-tulo.png" alt="Sem-t-tulo" border="0"></a>


# Stop Flood.

-Função para parar o flood.

```python

# Stop to send Message.
# @Mectoche

def button_exit(self):
        self.flood = False
        messagebox.showwarning(f"{titl}", "Você finalizou o flood!")



```

# Sistema de animação de menu

- Essa função foi criada apenas para melhorar a aparência do programa.

```python
# @Mectoche
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


```

  
