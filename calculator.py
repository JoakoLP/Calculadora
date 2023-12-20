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

    self.equation= StringVar()
    self.entry_value=''

    # Configura la función de retorno de llamada para rastrear cambios en la entrada
    self.equation.trace_add("write", self.update_entry_value)

    num_columns = 4
    num_rows = 6

    cell_width = (1 / num_columns) - 0.01
    cell_height = (1 / num_rows) - 0.01


    Entry(width=17,bg='#221133',fg='#ffffff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0, relheight= cell_height , relwidth=1)

    Button(text='(',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('(')).place(relx=0/num_columns, rely=1/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text=')',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(')')).place(relx=1/num_columns, rely=1/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='%',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('%')).place(relx=2/num_columns, rely=1/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='1',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(1)).place(relx=0/num_columns, rely=2/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='2',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(2)).place(relx=1/num_columns, rely=2/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='3',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(3)).place(relx=2/num_columns, rely=2/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='4',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(4)).place(relx=0/num_columns, rely=3/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='5',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(5)).place(relx=1/num_columns, rely=3/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='6',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(6)).place(relx=2/num_columns, rely=3/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='7',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(7)).place(relx=0/num_columns, rely=4/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='8',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(8)).place(relx=1/num_columns, rely=4/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='9',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(9)).place(relx=2/num_columns, rely=4/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='0',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show(0)).place(relx=1/num_columns, rely=5/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='.',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('.')).place(relx=2/num_columns, rely=5/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='+',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('+')).place(relx=3/num_columns, rely=4/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='-',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('-')).place(relx=3/num_columns, rely=3/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='/',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('/')).place(relx=3/num_columns, rely=1/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='*',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=lambda:self.show('*')).place(relx=3/num_columns, rely=2/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='=',font=('Arial Bold',16),relief='flat',activebackground='#441155',activeforeground='#ffffff',bg='#552266',fg='#ffffff',command=self.solve).place(relx=3/num_columns, rely=5/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='C',font=('Arial Bold',16),relief='flat',activebackground='#221133',activeforeground='#ffffff',bg='#332244',fg='#ffffff',command=self.clear).place(relx=0/num_columns, rely=5/num_rows, relheight=cell_height,relwidth=cell_width)
    Button(text='←',font=('Arial Bold',16),relief='flat',activebackground='#441155',activeforeground='#ffffff',bg='#552266',fg='#ffffff',command=self.delete_one).place(relx= (3.5/num_columns)-0.01, rely=(0/num_rows)+0.01, relheight= cell_height-0.02 , relwidth=cell_width/2)

  def show(self,value):
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