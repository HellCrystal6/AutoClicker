import customtkinter
import tkinter
import keyboard
import pyautogui as pyg
from colorama import Fore

def clicker():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("800x500")
    app.title("SimpleAutoClicker")
    
    def click():
        while True:
            if keyboard.is_pressed('r'):
                try:
                    while True:
                        pyg.click()
                        if keyboard.is_pressed('g'):
                            break
                except KeyboardInterrupt:
                    print('\n')
                    print("Exiting...")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Simple Auto Clicker")
    label_1.pack(pady=10, padx=10)
    startclick = customtkinter.CTkButton(master=frame_1, text="Click This Button To Start Clicker", command=click)
    howToStartIt = customtkinter.CTkLabel(master=frame_1, text="Press R To Start Clicking And G To Stop Clicking!")
    howToStartIt.pack(pady=10,padx=10)
    startclick.pack(pady=10,padx=10)

    app.mainloop()
    
clicker()

def quit():
    print("Exiting...")
    exit()