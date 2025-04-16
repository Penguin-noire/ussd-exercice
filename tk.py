import tkinter
import customtkinter
class Application:
    def __init__(self):
        self.fen = customtkinter.CTk()
        self.fen.title('Calculatrice')
        
    

    def run():
        Application().fen.mainloop()


app = Application
app.run()