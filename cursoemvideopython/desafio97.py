from cordes import desafio
desafio(97)
                # crie e defina uma função que receba um texto de qualquer parametro
                # personalize e adapte o texto
                # mostre texto personalizado

def escreva(txt):
    cr = len(txt) + 4
    print(f'{"~" * cr}\n{txt:^{cr}}\n{"~" * cr}')


escreva('Pronto so mostrar o texto')
escreva('Acho que agora ficou bom')
escreva('ficou com um espaco de 2 indice no começo e no final')
