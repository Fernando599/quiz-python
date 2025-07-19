import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import messagebox

import json

class Quiz:
    def __init__(self):
        self.quest = 0
        self.display_title()
        self.display_questions()
        self.buttons()
        
        self.opt_selected = tk.IntVar()
        self.opts=self.radio_buttons()
        
        self.display_options()
        self.correct = 0
        self.data_size = len(question)
        
    def display_title(self):
        container = tk.Frame(app, bg="#1e1e1e")
        container.pack(fill='x')

        title = tk.Label(
            container,
            text='📊 Big O Quiz - Teste seus conhecimentos!',
            font=('Segoe UI', 18, 'bold'),
            bg="#1e1e1e",
            fg="#00ff99",
            pady=20
        )
        title.pack()

        
    def display_results(self):
        wrong_count = self.data_size - self.correct
        correct = f'Respostas corretas: {self.correct}'
        wrong = f'Respostas erradas: {wrong_count}'
        
        score = int(self.correct / self.data_size * 100)
        result = f'Pontos arrecadados: {score}'
        
        mb.showinfo('Resultado', f'{result}\n{correct}\n{wrong}')
        
    def check_ans(self, quest):
        if self.opt_selected.get() == answer[quest]:
            return True
        
    def next_btn(self):
        if self.check_ans(self.quest):
            self.correct += 1
            messagebox.showinfo("Informação", "Correto!")
            self.quest += 1
        else:
            resposta_index = answer[self.quest] - 1 
            resposta_correta = options[self.quest][resposta_index]
            explicacao = explanations[self.quest]
            
            messagebox.showinfo("Informação", f"Errado!\nA resposta correta é: {resposta_correta}\n\n{explicacao}")
            self.quest += 1
                
        
        if self.quest == self.data_size:
            self.display_results()
            app.destroy()
            
        else:
            self.display_questions()
            self.display_options()
            
        
    def buttons(self):
        next_button = ttk.Button(app, text='Proximo', command=self.next_btn, width=15)
        next_button.place(x=700, y=380)
        
        quit_button = ttk.Button(app, text='Sair', command=app.destroy, width=10)
        quit_button.place(x=50, y=380)
             
    def display_questions(self):
        quest = tk.Label(app, text=question[self.quest], width=90, font=('arial', 10, 'bold'))
        quest.place(x=60, y=100)
        
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        
        for option in options[self.quest]:
            self.opts[val]['text'] = option
            val += 1
            
    def radio_buttons(self):
        options_list = []
        
        first_option_position = 150
        
        while len(options_list) < 4:
            radio_btn = ttk.Radiobutton(app, text=' ', variable=self.opt_selected, value=len(options_list)+1)
            
            options_list.append(radio_btn)
            radio_btn.place(x=100, y=first_option_position)
            
            first_option_position += 40
        return options_list
        
app = tk.Tk()
app.geometry("850x450")
app.resizable(width=False, height=False)
app.title('Quiz')

style = ttk.Style(app)
app.call('source', 'Quiz/forest-dark.tcl')
style.theme_use('forest-dark')

#tratamento de dados de json
with open('Quiz/data.json', encoding='utf-8') as f:
    data = json.load(f)
    
question = (data['question'])
options = (data['options'])
answer = (data['answer'])
explanations = (data['explanations'])

quiz = Quiz()
app.mainloop()