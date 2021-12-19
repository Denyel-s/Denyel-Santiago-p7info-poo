# Avaliação 06
Construir as Classes DBModel com a definição das tabelas:
TB_CLIENTE, TB_PRODUTO, TB_NOTA_FISCAL, TB_ITEM_NF

Observar os relacionamentos entre:
1) NotaFiscal e ItemNotaFiscal( Uma NotaFiscal possui 1 ou mais ItemNotaFiscal) ONE-to-MANY
     NotaFiscal vai ter uma coleção items que será implementado por um db.relationship

2) ItemNotaFiscal e NotaFiscal(Um ItemNotaFiscal está relacionado a uma NotaFIscal) ONE-to-ONE

3) ItemNotaFiscal e Produto (Um ItemNotaFiscal está relacionado a um Produto) ONE-to-ONE