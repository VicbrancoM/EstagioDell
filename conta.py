class conta:
    def __init__(self, banco, agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0
        
    def __repr__(self):
        return str( self.banco) + ", " + str (self.agencia) + ", " + str (self.conta) + ", " + str (self.saldo)