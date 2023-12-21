from tkinter import Tk, Entry, Button, StringVar
import re

class Calculator:
  def __init__(self,master):
    master.title("Calculator")
    # geometry('width x height + pos X screen + pos Y screen')
    master.geometry("300x400+810+340")
    master.config(bg='#221133')
    # minsize(width, height)
    master.minsize(300,400)
    # resizable(x=,y=)
    master.resizable(True,True)
    master['padx'] = 1
    master['pady'] = 1

    self.equation= StringVar()
    self.entry_value=''

    # Trace to entry changes
    self.equation.trace_add("write", self.update_entry_value)

    # Trace to run 'handle_button_color' when 'self.pow_trace' changes
    self.pow_trace = StringVar()
    self.pow_trace.trace_add("write", self.handle_button_color)

    self.pow = False


    # Sets rows and columns weight
    num_columns = 4
    num_rows = 7

    for i in range(num_rows): # Sets weight to all the rows
      master.grid_rowconfigure(i, weight=1)
    for i in range(num_columns): # Sets weight to all the columns
      master.grid_columnconfigure(i, weight=1)


    # creates and inserts the Entry at the first row and column, with 4 columns width and with sticky on North, South, East and West
    Entry(bg='#221133', justify="right", fg='#ffffff', font=('Arial Bold', 28), textvariable=self.equation).grid(row=0, column=0,rowspan=1, columnspan=4, pady=(0, 1), sticky='nsew')

    self.create_buttons(master)

    # Runs 'handle_button_color' to initialize the buttons colors
    self.handle_button_color()

  
  def create_buttons(self, master):
    num_columns = 4

    operators = ['ⁿ','','','←','(', ')', '%', '/', '1', '2', '3', '*', '4', '5', '6', '-', '7', '8', '9', '+', 'C', '0', '.', '=']
    row = 1
    col = 0

    self.buttons = []
    for operator in operators:
      button = Button(
          text=operator,
          font=('Arial Bold', 16),
          relief='flat',
          activebackground='#221133',
          activeforeground='#ffffff',
          # bg=self.handle_button_color(operator),
          fg='#ffffff',
          command=lambda o=operator: self.show(o) if (o not in ['=', 'C', '←', 'ⁿ']) else self.solve() if (o == '=') else self.delete_one() if (o == '←') else self.handle_pow() if (o == 'ⁿ') else self.clear()
      )
      button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
      col += 1
      if col == num_columns:
          col = 0
          row += 1
      # Adding the button to the list
      self.buttons.append(button)

  def show(self,value):
    length = len(self.equation.get())
    last_digit = self.equation.get()[length-1:length]
    
    # if the value is '*', '/', '%' or '.'
    if value in ['*', '/', '%', '.', ')'] or (self.pow == True and value.isdigit()):
      # if the length of the variable is lower or equal to 1
      if (length < 1):
        # avoid non '+' or '-' operators at the start of the variable
        return
    
    # if the last digit is an operator
    if last_digit in ['+', '-', '*', '/', '%', '.']:
      if value in ['*', '/', '%', '.','+', '-']:
        if (len(value) <= 1):
          if value in ['*', '/', '%', '.']:
            # Avoid inserting '*', '/', '%' or '.' at start by replacing
            return

        # avoid multiple operators
        self.entry_value = self.entry_value[:length-1]


    if self.equation.get() == '0': # '0' at the start fix
      self.entry_value=str(value)
    else:
      if self.pow == True:
        # Replace each digit with its superscript version
        if value == "1":
          value = '¹'
        elif value == "2":
          value = '²'
        elif value == "3":
          value = '³'
        elif value == "4":
          value = '⁴'
        elif value == "5":
          value = '⁵'
        elif value == "6":
          value = '⁶'
        elif value == "7":
          value = '⁷'
        elif value == "8":
          value = '⁸'
        elif value == "9":
          value = '⁹'
        elif value == "0":
          value = '⁰'
      self.entry_value+=str(value)
    self.equation.set(self.entry_value)

    
  def solve(self):
        print(self.entry_value)
        if len(self.entry_value) > 0:
            expression = self.entry_value
            # Find superscripts and convert them to powers
            match = re.findall(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+',expression)
            print(match)
            # while match:
            for pow in match:
              print(pow)
              this_pow = f'**{pow.replace('¹','1').replace('²','2').replace('³','3').replace('⁴','4').replace('⁵','5').replace('⁶','6').replace('⁷','7').replace('⁸','8').replace('⁹','9').replace('⁰','0')}'
              print(this_pow)
              expression = expression.replace(pow,this_pow)
            print(expression)
            result = eval(expression)
            self.equation.set(result)


  def delete_one(self):
    value = self.entry_value
    self.entry_value = value[0:len(value)-1]
    self.equation.set(self.entry_value)

  def clear(self):
    self.entry_value=''
    self.equation.set(self.entry_value)
  
  def update_entry_value(self, *args):
    # Updates the 'entry_value' variable when the 'self.equation' variable changes
    self.entry_value = self.equation.get()

  def handle_pow(self):
    self.pow = not self.pow
    # Updates the traced variable value
    self.pow_trace.set("")
  
  def handle_button_color(self, *args):
    for button in self.buttons:
      if button:
        color = self.calculate_button_color(button["text"])
        button.config(bg=color)

  def calculate_button_color(self, value):
      if value == 'ⁿ':
          return '#119999' if self.pow else '#553355'
      else:
          return '#332244'

root = Tk()
calculator = Calculator(root)
root.mainloop()