<p align="center">
<a href="https://github.com/Mectoche/MTFLOOD"><img src="https://i.ibb.co/rvZynSh/watching.gif" alt="watching" border="0"></a>
</p>

#       *MTFLOOD*

# About.

- **[MTFLOOD](https://github.com/Mectoche/MTFLOOD)** It's a program to troll your friends on any social network.

- Made for those who like a good prank.

- Note: remember to install python and its dependencies

# Dowload
- To download the program click [HERE](https://github.com/Mectoche/MTFLOOD/tree/main/MTFLOOD/EXE)

#

# Flood of words.

- I used this system to output one word per second.

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
# Image to retract.


<a href="https://github.com/Mectoche/MTFLOOD/"><img src="https://i.ibb.co/5Rf7wq9/Sem-t-tulo.png" alt="Sem-t-tulo" border="0"></a>


# Stop Flood.

- Function to stop the flood.

```python

# Stop to send Message.
# @Mectoche

def button_exit(self):
        self.flood = False
        messagebox.showwarning(f"{titl}", "Você finalizou o flood!")



```

# Menu animation system.

- This function was created just to improve the appearance of the program.

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

  
