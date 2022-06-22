from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

def fill_document(doc):
    '''Adiciona uma seção, uma subseção ou algum texto ao documento;
    Parâmetro doc: O próprio documento;
    Type(doc) --> <class pylatex.document.Document>;'''
    
    with doc.create(Section("Seção I")):
        doc.append("Meu Texto Inicial da seção I"+NoEscape(r"\newline"))
        doc.append(italic(" Meu texto em Itálico"))
        
        with doc.create(Subsection("Subseção I")):
            doc.append("Alguns caracteres malucos: $&#{}")
            pass
        pass
    pass

if __name__ == "__main__":
    '''Condicional que inicializa a criação do documento e as funções dele pertencentes'''
    
    doc = Document("basic")
    fill_document(doc)
    doc.generate_pdf('./generated.document/main_basic', clean_tex=False)
    doc.generate_tex()

    doc = Document()
    doc.preamble.append(Command('title', 'Aplicando LaTeX no Python'))
    doc.preamble.append(Command('author', 'Ronivaldo Domingues de Andrade'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))    
    doc.append(NoEscape(r'\maketitle'))
    fill_document(doc)
    doc.generate_pdf('./generated.document/main_with_maketitle', clean_tex=False)
    doc.generate_tex()

    with doc.create(Section("Seção II")):
        doc.append("Meu texto da seção II")
        pass    
    doc.generate_pdf('./generated.document/main_with_maketitle2', clean_tex=False)
    doc.generate_tex()
    tex = doc.dumps()
