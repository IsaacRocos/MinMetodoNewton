'''
Created on 18/04/2015

@author: Isaac
'''
import random
import sympy as sp
from sympy import *

class MetodoNewtonMin(object):
    '''
    classdocs
    '''

    '''
    Constructor
    '''
    def __init__(self):
        self.alpha = 0.3
        self.epsilon = 0.001
        self.MAX_ITER= 10000
        self.numVar = 2
        self.mejoresSoluciones = []
        self.jacobiano = self.generarJacobiano()

    def RUN(self):
        print("ALGORITMO DE NEWTON PARA ENCONTRAR MINIMOS")
        print("Numero de varaibles:",self.numVar,"Alpha:",self.alpha,"Epsilon:",self.epsilon,"MAX_ITER:",self.MAX_ITER)
        print("Generando primer solucion - X(0) ... ")
        x0 = self.generaSolAleatoria(-100,100)
        print("x0 =",x0)

    def generaSolAleatoria(self,li,ls):
        solucionInic = []
        for i in range(self.numVar):
            solucionInic.append(random.randrange(li,ls,1))
        return solucionInic
    
    def generarJacobiano(self): 
        print("Inicio prueba jacob")
        x1 = Symbol('x1')
        x2 = Symbol('x2')
        Fx1x2 = Matrix([(x1**4) - (16*(x1**2)) + (5*(x1))  ,  (x2**4) - (16*(x2**2)) + (5*(x2))])
        variables = Matrix([x1, x2])
        jacobiano = Fx1x2.jacobian(variables)
        tipo = type(jacobiano)
        #print("Jacobiano. Type:",tipo,"Resultado:",jacobiano)
        print("Resultado Jacobiano:",jacobiano)
        print("Fin prueba jacob")
        return jacobiano

minimizar = MetodoNewtonMin()
minimizar.RUN()
#minimizar.probarJacobiano()



'''
    Ejemplo de calculo jacobiano
    http://nullege.com/codes/search/sympy.Matrix.jacobian
'''
