#LIBRERIAS
from tkinter import *
import customtkinter as ctk


#----------------------------------------------------------------------------------------------------------------------



# Clase que representa el objeto calculadora
class Calculator:
    def __init__(self):
        ctk.set_appearance_mode("dark")#PARA CAMBIAR EL MODO DE APARENCIA DE LA VENTANA
        ctk.set_default_color_theme("blue")#PARA CAMBIAR EL COLOR DE LA VENTANA

        self.window = ctk.CTk() #Crea la ventana
        self.WIDTH = 300 #Ancho de la ventana
        self.HEIGHT = 450 #Alto de la ventana
        self.window.geometry('{}x{}'.format(self.WIDTH, self.HEIGHT)) #Asigna el tamaño de la ventana   
        self.window.title('Calculadora CAMPER') #Asigna el titulo a la ventana
        self.window.resizable(0, 0) #Evita que se pueda cambiar el tamaño de la ventana

        #Expresion total de la calculadora
        self.total = ''  #Expresion total de la calculadora
        #Expresion actual de la calculadora
        self.actual = '' #Expresion actual de la calculadora
    #frames
        #frame resultado y expresion    
        self.frame_resultado = ctk.CTkFrame(self.window, width=self.WIDTH, height=20)
        self.frame_resultado.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

        #label resultado
        self.label_resultado = ctk.CTkLabel(self.frame_resultado, text=self.total, fg_color='gray18',text_font=('Arial', 12, 'bold'))
        self.label_resultado.pack(side=TOP, fill=Y, expand=True, padx=5, pady=5, anchor=E)

        #label expresion
        self.label_expresion = ctk.CTkLabel(self.frame_resultado, text=self.actual, fg_color='gray18',text_font=('Arial', 20))
        self.label_expresion.pack(side=BOTTOM, fill=Y, expand=True, padx=5, pady=5, anchor="se")


        #frame botones
        self.frame_botones = ctk.CTkFrame(self.window, )
        self.frame_botones.pack(side=BOTTOM, fill=BOTH, expand=True, padx=2, pady=2)
        
        
        #Ordenacion de los botones
        for i in range(0,4):
            self.frame_botones.columnconfigure(i, weight=1)
            self.frame_botones.rowconfigure(i, weight=1)
        
        #Botones a crear y sus posiciones en la grilla
        self.numeros = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1)
        }

        #Agregar un numero a la expresion actual
        def agregar_numero(self, num):
            
            self.actual += str(num)
            self.update_expresion()



        #Crea el boton CLEAR

        self.boton_clear = ctk.CTkButton(self.frame_botones, text='CLEAR',fg_color='#ff5252', border_color='#BFBFBF', border_width=2, text_font = ('Arial', '20', 'bold'), text_color='#D9D9D9', command=self.clear) 
        self.boton_clear.grid(row=0, column=1, sticky=NSEW, columnspan=3)
        
        #Crea los botones numericos
        for numero, numero_grid in self.numeros.items():
            self.boton_numero = ctk.CTkButton(self.frame_botones, text=str(numero),fg_color='#546E7A', border_color='#BFBFBF', border_width=2,text_font= ('Arial', '14'), command=lambda num=numero: agregar_numero(self, num))
            self.boton_numero.grid(row=numero_grid[0], column=numero_grid[1], sticky=NSEW, padx=2, pady=2)
        

        #Operaciones y sus posiciones en la grilla
        self.operaciones = {
            '+':(0,4), '-':(1,4), '*':(2,4), '/':(3,4), 
        }
        
        #FUNCION PARA CONCATENAR OPERACIONES A LA EXPRESION
        
        def agregar_operacion(self, operacion):
            self.actual += str(operacion)
            self.total += self.actual
            self.actual = ''
            self.update_resultado()
            self.update_expresion()

        #CICLO QUE CREA LOS BOTONES DE OPERACIONES
        for operacion, operacion_grid in self.operaciones.items():
            self.boton_operacion = ctk.CTkButton(self.frame_botones, text=operacion,text_font=('Arial', '14', 'bold'), fg_color='#ACF0F2',text_color='#37474F', border_color='#37474F', border_width=2, command=lambda operacion=operacion: agregar_operacion(self, operacion))
            self.boton_operacion.grid(row=operacion_grid[0], column=operacion_grid[1], sticky=NSEW, padx=2, pady=4)


        #CREACION DEL BOTON '='
        self.boton_igual = ctk.CTkButton(self.frame_botones, text='=', text_font=('Arial', '14', 'bold'), fg_color='#289976',text_color='#37474F', border_color='#D9D9D9', border_width=1, command=self.calcular)
        self.boton_igual.grid(row=4, column=2, sticky=NSEW, columnspan=3, padx=5, pady=4)
    

    #FUNCION PARA CALCULAR LA EXPRESION ESCRITA
    def calcular(self):
        self.total += self.actual
        self.actual = str(eval(self.total)) #eval() evalua la expresion escrita
        self.total += ' ='
        self.update_resultado()
        self.update_expresion()

    #FUNCION PARA LIMPIAR EL PANEL
    def clear(self):
        self.actual = ''
        self.total = ''
        self.update_expresion()
        self.update_resultado()

    #FUNCION PARA ACTUALIZAR EL RESULTADO EN EL PANEL
    def update_resultado(self):
        self.label_resultado.config(text=self.total)
    
    #FUNCION PARA ACTUALIZAR LA EXPRESION EN EL PANEL
    def update_expresion(self):
        self.label_expresion.config(text=self.actual)
        
        
    #FUNCION PARA CENTRAR LA VENTANA EN LA PANTALLA

    def centrar_ventana(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    
    #FUNCION PARA ACTUALIZAR LA VENTANA
    def run(self):
        self.centrar_ventana()
        self.window.mainloop()

#Instancia de la clase
if __name__ == '__main__':

    calculator = Calculator()
    calculator.run()





        



        