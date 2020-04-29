# generate random color using Python
# created by github.com/papanara
import tkinter as tk
from tkinter import ttk
from random import choice

def generate_color():
    root = tk.Tk()
    root.geometry('600x350')
    root.rezisable(False, False)
    root.title('Generate Random Color')
    root.background='#FFFFFF'

    def create_color():
        """Create hexa color code"""
        hexa_code = ('A','B','C','D','E','F','F','0','1','2','3','4','5','6','7','8','9')
        color_one_code = '#'+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)
        color_two_code = '#'+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)
        color_three_code = '#'+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)
        color_one.configure(background=color_one_code)
        color_two.configure(background=color_two_code)
        color_three.configure(background=color_three_code)
        color_one_hexa_code.delete(0, 7)
        color_one_hexa_code.insert(0, color_one_code)
        color_two_hexa_code.delete(0, 7)
        color_two_hexa_code.insert(0, color_two_code)
        color_three_hexa_code.delete(0, 7)
        color_three_hexa_code.insert(0, color_three_code)

        # create RGB Color code
        rgb1 = [int(color_one_code[1:3], 16),int(color_one_code[3:5], 16),int(color_one_code[5:7], 16)]
        rgb2 = [int(color_two_code[1:3], 16),int(color_two_code[3:5], 16),int(color_two_code[5:7], 16)]
        rgb3 = [int(color_three_code[1:3], 16),int(color_three_code[3:5], 16),int(color_three_code[5:7], 16)]
        color_one_rgb_code.delete(0, len(color_one_rgb_code.get()))
        color_one_rgb_code.insert(0, rgb1)
        color_two_rgb_code.delete(0, len(color_two_rgb_code.get()))
        color_two_rgb_code.insert(0, rgb2)
        color_three_rgb_code.delete(0, len(color_three_rgb_code.get()))
        color_three_rgb_code.insert(0, rgb3)

    # widgets
    heading_title = tk.Label(root, text='Generate Random Color', font=('', 14, 'bold'))
    heading_color = tk.Label(root, text='COLOR', font=('', 12, 'bold'))
    heading_rgb = tk.Label(root, text='RGB', font=('', 12, 'bold'))
    heading_hexa = tk.Label(root, text='HEXA', font=('', 12, 'bold'))
    color_one = tk.Label(root, background='#FF0000', width=40, height=2)
    color_two = tk.Label(root, background='#00FF00', width=40, height=2)
    color_three = tk.Label(root, background='#0000FF', width=40, height=2)
    color_one_rgb_code = tk.Entry(root)
    color_one_hexa_code = tk.Entry(root)
    color_two_rgb_code = tk.Entry(root)
    color_two_hexa_code = tk.Entry(root)
    color_three_rgb_code = tk.Entry(root)
    color_three_hexa_code = tk.Entry(root)
    generate_button = tk.Button(root, text='Give me a color', font=('', 14, 'bold'), background='#232323', foreground='#FFFFFF', width=23, command=create_color)
    footer = tk.Label(root, text='Created by @papanara')
    
    # grid position
    heading_title.grid(row=0, column=0, columnspan=3, pady=20)
    heading_color.grid(row=1, column=0)
    heading_rgb.grid(row=1, column=1)
    heading_hexa.grid(row=1, column=2)
    color_one.grid(row=2, column=0, pady=5, padx=5)
    color_two.grid(row=3, column=0, pady=5)
    color_three.grid(row=4, column=0, pady=5)
    color_one_rgb_code.grid(row=2, column=1, padx=10)
    color_one_hexa_code.grid(row=2, column=2, padx=10)
    color_two_rgb_code.grid(row=3, column=1, padx=10)
    color_two_hexa_code.grid(row=3, column=2, padx=10)
    color_three_rgb_code.grid(row=4, column=1, padx=10)
    color_three_hexa_code.grid(row=4, column=2, padx=10)
    generate_button.grid(row=5, column=0)
    footer.grid(row=6, column=0, columnspan=3, pady=20)
    # end widgets

    
    
    root.mainloop()

if __name__ == '__main__':
    generate_color()