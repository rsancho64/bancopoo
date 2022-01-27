#! /usr/bin/python3

class banco:

    """banco simple implementado con diccionarios.
    Se orienta a poder realizar, finalmente, fusiones bancarias
    """
    def __init__(self):
        self._D = {}    # conjunto de cuentas

    def imprimir(self):
        print("banco: ", self._D)

    def creaCuenta(self, cliente, ingresoInicial):
        if cliente in self._D.keys():
            raise Exception("ERROR: el cliente existe. Cuenta NO creada")
        self._D[cliente] = ingresoInicial
        
    def deposito(self, cliente, importe):
        if importe <= 0:
            raise Exception("IMPORTE INCORRECTO")
        if not cliente in self._D.keys():
            self.creaCuenta(cliente, importe)
        else:
            self._D[cliente] += importe

    def reintegro(self, cliente, importe):
        if not cliente in self._D.keys():
            print("ERROR: el cliente NO existe. Reintegro abortado")
            return
        if importe <= 0:
            raise Exception("importe incorrecto")
            self._D[cliente] -= importe            
            # pass

if __name__ == "__main__":

    b1 = banco()
    b1.imprimir()
    b1.creaCuenta("antonio", 10)
    b1.imprimir()
    b1.deposito("lucas",  300)
    b1.deposito("antonio", 20)    
    b1.imprimir()
    b1.reintegro("antonio", 20)
    b1.imprimir()    