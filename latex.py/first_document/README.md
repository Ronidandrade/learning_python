~~~python
# Importando os módulos necessários para trabalhar com latex dentro do  python.
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

# Definindo uma função que adiciona elementos no documento.
def fill_document(doc):
    '''Adiciona uma seção, uma subseção ou algum texto ao documento;
    Parâmetro doc: O próprio documento;
    Type(doc) --> <class pylatex.document.Document>;
    '''

    #Criando uma seção no documento.
    with doc.create(Section("Seção I")):
        doc.append("Meu Texto Inicial da seção I"+NoEscape(r"\newline"))
        doc.append(italic(" Meu texto em Itálico"))

        #Criando uma subseção no documento.
        with doc.create(Subsection("Subseção I")):
            doc.append("Alguns caracteres malucos: $&#{}")

# Condicional que inicializa a função.
if __name__ == "__main__":
    '''Condicional que inicializa a criação do documento e as funções dele pertencentes'''

    #Documento Básico.
    ##Veja que doc1 é um objeto setado na classe pylatex.document.Document.
    ###Definindo o tipo de documento
    doc = Document("basic")

    #Colocando as seções e subseções no docuemnto
    fill_document(doc)

    #Tentativa de gerar um '.pdf' do documento
    doc.generate_pdf('./generated.document/main_basic', clean_tex=False)

    #tentativa de gerar um arquivo '.tex' do doumento
    doc.generate_tex()

    #Documento com o comando \maketitle ativado
    ##Veja que doc2 é um objeto setado na classe pylatex.document.Document
    ###Definindo o tipo de documento
    doc = Document()

    #Contruindo o Preâmbulo do documento
    ##Construindo o \maketitle
    doc.preamble.append(Command('title', 'Aplicando LaTeX no Python'))
    doc.preamble.append(Command('author', 'Ronivaldo Domingues de Andrade'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))

    ##Inserindo o maketitle no corpo do documento
    doc.append(NoEscape(r'\maketitle'))

    #Colocando as seções e subseções no docuemnto
    fill_document(doc)

    #Tentativa de gerar um '.pdf' do documento
    doc.generate_pdf('./generated.document/main_with_maketitle', clean_tex=False)

    #tentativa de gerar um arquivo '.tex' do doumento
    doc.generate_tex()

    #Adicionamndo Coisas ao Documento
    with doc.create(Section("Seção II")):
        doc.append("Meu texto da seção II")
        pass

    #Tentativa de gerar um '.pdf' do documento
    doc.generate_pdf('./generated.document/main_with_maketitle2', clean_tex=False)

    #tentativa de gerar um arquivo '.tex' do doumento
    doc.generate_tex()

    ## Torna o documento uma string na sintaxe latex
    tex = doc.dumps()
~~~
