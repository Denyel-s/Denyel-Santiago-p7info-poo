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
from cliente import Cliente
from produto import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota = valor

    def getId(self):
        return self._Id

    def getCodigo(self):
        return self._codigo

    def getData(self):
        return self._data

    def getClienteID(self):
        return self._cliente._id

    def getClienteNome(self):
        return self._cliente._nome

    def getClienteCodigo(self):
        return self._cliente._codigo

    def getClienteCpf(self):
        return self._cliente._cnpjcpf

    def getClienteTipo(self):
        return self._cliente._tipo

    def getSeq(self):
        seq = []
        for item in self._itens:
            seq.append(item._sequencial)
        return seq

    def getNome(self):
        nome = []
        for item in self._itens:
            nome.append(item._descricao)
        return nome

    def getQuantidade(self):
        quantidade = []
        for item in self._itens:
            quantidade.append(item._quantidade)
        return quantidade

    def getPreco(self):
        preco = []
        for item in self._itens:
            preco.append(item._valorItem)
        return preco

    def getValorU(self):
        valor = []
        for item in self._itens:
            valor.append(item._valorUnitario)
        return valor

    def getValorT(self):
        return self.valorNota

    def imprimirNotaFiscal(self):
        cliente_id = self.getClienteID()
        cliente_nome = self.getClienteNome()
        cliente_codigo = self.getClienteCodigo()
        cliente_cnpjcpf = self.getClienteCpf()
        cliente_tipo = self.getClienteTipo()
        seq = self.getSeq()
        nome = self.getNome()
        quantidade = self.getQuantidade()
        valor_u = self.getValorU()
        preco = self.getPreco()
        n = int(len(seq))

        print("+{}+".format("-" * 98))
        print("|Nota Fiscal  {:>85}|".format(str(self.getData())))
        print("|Cliente: {:^10} Nome: {:30}   {:>40}".format(self.getClienteID(), self.getClienteNome(), "|"))
        print("|CPF/CNPJ: {:<10}{:>75}".format(self.getClienteCpf(), "|"))
        print("+{}+\n|Itens {:>93}".format("-" * 98, "|"))
        print("+{}+".format("-" * 98))
        print("|{:10}  {:<40} {:<20} {:<10}    {:^10}|".format("Seq", "Descrição", "QTD", "Valor Unit", "Preço"))
        print("+{}+".format("-" * 98))
        for i in range(0, n):
            print(
                "|00{:<10}{:<40}  {:<20} {:^10}   {:>10}|".format(seq[i], nome[i], quantidade[i], valor_u[i], preco[i]))
        print("+{}+".format("-" * 98))
        print("|Valor nota fiscal: {}{:>75}".format(self.getValorT(), "|"))
        print("+{}+".format("-" * 98))
