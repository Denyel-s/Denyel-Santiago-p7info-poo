"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal

class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
    def getId(self):
        return self._Id
    def getCodigo(self):
        return  self._codigo
    def getCliente(self):
        return self._cliente
    def getData(self):
        return self._data

    def getSeq(self):
        seq= []
        for item in self._itens:
            seq.append(item._sequencial)
        return seq
    def getNome(self):
        Nome = []
        for item in self._itens:
            Nome.append(item._sequencial)
        return Nome

    def getValor(self):
        return self.valorNota
     
    def imprimirNotaFiscal(self):       
        print("ID: {}".format(self.getId()))
        print(("Código: {}".format(self.getCodigo())))
        print("Cliente: {}".format(self.getCliente()))
        print("Data: {}".format(self.getData()))
        for seq in self.getSeq():
            print("Items: {}".format(seq))
        print("Valor nota fiscal: {}".format(self.getValor()))