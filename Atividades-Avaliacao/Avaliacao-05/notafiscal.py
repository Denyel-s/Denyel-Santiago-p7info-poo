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
    def getItens(self):
        nome= []
        seq= []
        for item in self._itens:
            nome.append(item._descricao)
            seq.append(item._sequencial)
        return  nome

    def getValor(self):
        return self.valorNota
     
    def imprimirNotaFiscal(self):       
        print("ID: {}".format(self.getId()))
        print(("Código: {}".format(self.getCodigo())))
        print("Cliente: {}".format(self.getCliente()))
        print("Data: {}".format(self.getData()))
        print("Itens: {}".format(self.getItens()))
        for x in self.getItens():
            print("Items: {}".format(x))
        print("Valor nota fiscal: {}".format(self.getValor()))