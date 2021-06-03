from dataclasses import dataclass

from tasks import ocr_documento

@dataclass
class Pessoa:
    nome: str
    telefone: str
    documento: str

def cadastro(pessoa: Pessoa):
    dados = ocr_documento.delay(pessoa.documento)


p = Pessoa('fulano','123456', 'cnh.jpg')

cadastro(p)