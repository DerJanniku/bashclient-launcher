import tkinter as tk

class CustomHUD(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Custom HUD")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Customize your HUD")
        self.label.pack(pady=10)
        
        self.widget_button = tk.Button(self, text="Add Widget", command=self.add_widget)
        self.widget_button.pack(pady=10)
        
        self.widgets = []

    def add_widget(self):
        widget = tk.Label(self, text="New Widget")
        widget.pack(pady=5)
        self.widgets.append(widget)
        self.animate_widget(widget)

    def animate_widget(self, widget):
        for i in range(10):
            widget.config(fg=f"#{i*2:02x}{i*2:02x}{i*2:02x}")
            self.update()
            self.after(100)

if __name__ == "__main__":
    app = CustomHUD()
    app.mainloop()
