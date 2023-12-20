from tkinter import Tk, Entry, Button, StringVar

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

    # Configura la función de retorno de llamada para rastrear cambios en la entrada
    self.equation.trace_add("write", self.update_entry_value)


    # Configura el peso de las filas y columnas

    num_columns = 4
    num_rows = 7

    for i in range(num_rows): # Sets weight to all the rows
      master.grid_rowconfigure(i, weight=1)
    for i in range(num_columns): # Sets weight to all the columns
      master.grid_columnconfigure(i, weight=1)


    # creates and inserts the Entry at the first row and column, with 4 columns width and with sticky on North, South, East and West
    Entry(bg='#221133', justify="right", fg='#ffffff', font=('Arial Bold', 28), textvariable=self.equation).grid(row=0, column=0,rowspan=1, columnspan=4, pady=(0, 1), sticky='nsew')

    self.create_buttons(master)

  
  def create_buttons(self, master):
          num_columns = 4

          operators = ['ⁿ','','','←','(', ')', '%', '/', '1', '2', '3', '*', '4', '5', '6', '-', '7', '8', '9', '+', 'C', '0', '.', '=']
          row = 1
          col = 0

          for operator in operators:
              Button(
                  text=operator,
                  font=('Arial Bold', 16),
                  relief='flat',
                  activebackground='#221133',
                  activeforeground='#ffffff',
                  bg='#332244',
                  fg='#ffffff',
                  command=lambda o=operator: self.show(o) if (o not in ['=', 'C', '←', 'ⁿ']) else self.solve() if (o == '=') else self.delete_one() if (o == '←') else self.handle_pow() if (o == 'ⁿ') else self.clear()
              ).grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
              col += 1
              if col == num_columns:
                  col = 0
                  row += 1


  def show(self,value):
    length = len(self.equation.get())
    last_digit = self.equation.get()[length-1:length]
    
    # if the value is '*', '/', '%' or '.'
    if value in ['*', '/', '%', '.', '²']:
      # if the length of the variable is lower or equal to 1
      if (length < 1):
        # avoid non '+' or '-' operators at the start of the variable
        return
    
    # if the last digit is an operator
    if last_digit in ['+', '-', '*', '/', '%', '.']:
      if value in ['*', '/', '%', '.','+', '-']:
        # avoid multiple operators
        self.entry_value = self.entry_value[:length-1]


    if self.equation.get() == '0': # '0' at the start fix
      self.entry_value=str(value)
    else:
      self.entry_value+=str(value)
    self.equation.set(self.entry_value)


  def delete_one(self):
    value = self.entry_value
    self.entry_value = value[0:len(value)-1]
    self.equation.set(self.entry_value)

  def clear(self):
    self.entry_value=''
    self.equation.set(self.entry_value)

  def solve(self):
    print(len(self.entry_value))
    if(len(self.entry_value)>0):
      expression = self.entry_value.replace('%','/100*')
      result=eval(expression)
      self.equation.set(result)
  
  def update_entry_value(self, *args):
    # Actualiza la variable entry_value cuando la variable de cadena (StringVar) cambia
    self.entry_value = self.equation.get()


root = Tk()
calculator = Calculator(root)
root.mainloop()