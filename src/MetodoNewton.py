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
        self.alpha = 0.003
        self.epsilon = 0.000000000001
        self.MAX_ITER= 10000
        self.numVar = 2
        self.mejoresSoluciones = []
        self.jacobiano = self.generarJacobiano()

    def RUN(self):
        print("------------------------------------------")
        print("ALGORITMO DE NEWTON PARA ENCONTRAR MINIMOS")
        print("------------------------------------------")
        print '|Numero de varaibles(d):',self.numVar,' Alpha:',self.alpha,' Epsilon:',self.epsilon,' MAX_ITER:',self.MAX_ITER,'|'
        print "Jacobiano:",self.jacobiano
        print "Generando primer solucion aleatoriamente - X(0) ... "
        x0 = self.generaSolAleatoria(-10,10)
        print "x0 =",x0
        valPendienteFunc = self.obtenerPendienteSolucion(x0)
        
        print "Proceso iniciado..."
        solAnterior = x0
        ITER = 0
        while ((valPendienteFunc > self.epsilon)  or  (self.MAX_ITER >= ITER)):
            Xj = self.generarNuevaSol(solAnterior)
            valPendienteFunc = self.obtenerPendienteSolucion(Xj)
            valAptitudSolucion = self.obtenerAptitudSolucion(Xj) 
            if valPendienteFunc <1:
                self.alpha = self.alpha = 0.000001
            if ITER % 150 == 0:
                print "|Nueva solucion| F(x1,x2) =",valAptitudSolucion,"en X* =",Xj," |Pendiente|:",valPendienteFunc
            ITER = ITER+1 
            solAnterior = Xj
        print "Proceso finalizado."

    def generarJacobiano(self): 
        #print("Calculando jacobiano de funcion...")
        x1 = Symbol('x1')
        x2 = Symbol('x2')
        Fx1x2 = Matrix([(x1**4) - (16*(x1**2)) + (5*(x1))  ,  (x2**4) - (16*(x2**2)) + (5*(x2))])
        variables = Matrix([x1, x2])
        jacobiano = Fx1x2.jacobian(variables)
        #tipo = type(jacobiano)
        #print("Jacobiano. Type:",tipo,"Resultado:",jacobiano)
        #print("Resultado Jacobiano:",jacobiano)
        return jacobiano
    
    def generaSolAleatoria(self,li,ls):
        solucionInic = []
        for i in range(self.numVar):
            solucionInic.append(random.randrange(li,ls,1))
        return solucionInic
    
    def obtenerPendienteSolucion(self,solucion):
        # Obtener valor de la derivada de la funcion, si el valor resultante es menor que self.Epsilon, la solucion es valida
        x1 = solucion[0]
        x2 = solucion[1]
        x1p = (4*(x1)**3) - (32*(x1)) + 5
        x2p = (4*(x2)**3) - (32*(x2)) + 5
        fxpend = 0.5 * (x1p + x2p)
        return abs(fxpend)
        
    
    def obtenerAptitudSolucion(self,solucion):
        # Obtener valor de la derivada de la funcion, si el valor resultante es menor que self.Epsilon, la solucion es valida
        x1 = solucion[0]
        x2 = solucion[1]
        sx1 = ((x1)**4) - (16*(x1)**2) + (5*(x1))
        sx2 = ((x2)**4) - (16*(x2)**2) + (5*(x2))
        fx = 0.5 * (sx1 + sx2)
        return fx
    
    def generarNuevaSol(self,solAnterior):
        nuevaSol = []
        xj0 = solAnterior[0] - (self.alpha * self.evaluarDerivadaParcial(0,"x1",solAnterior[0]))
        xj1 = solAnterior[1] - (self.alpha * self.evaluarDerivadaParcial(3,"x2",solAnterior[1]))
        nuevaSol.append(xj0)
        nuevaSol.append(xj1)
        return nuevaSol
        
        
    def evaluarDerivadaParcial(self,locDParcial,variable,valor):
        valor = self.jacobiano[locDParcial].evalf(subs={variable:valor})
        #print (valor)
        return valor
        
    
minimizar = MetodoNewtonMin()
minimizar.RUN()
#minimizar.probarJacobiano()


'''
    Ejemplo de calculo jacobiano
    http://docs.sympy.org/latest/modules/matrices/matrices.html?highlight=jacobian#sympy.matrices.matrices.MatrixBase.jacobian
    http://nullege.com/codes/search/sympy.Matrix.jacobian
    http://stackoverflow.com/questions/7006626/how-to-calculate-expression-using-sympy-in-python
'''
