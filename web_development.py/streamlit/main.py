import streamlit as sl

sl.sidebar.title('Menu')
pagina_selecionada = sl.sidebar.selectbox('Selecione a página', ['Página 1', 'Página 2'])

if pagina_selecionada == 'Página 1':
    sl.title('Exemplo de APP-WEB com STREAMLIT')
    sl.selectbox('Selecione uma opção', ['opção 1', 'opção 2'])
else:
    x = sl.slider('x')
    y = sl.slider('y')
    sl.write(x, 'x', y, '=', x*y)