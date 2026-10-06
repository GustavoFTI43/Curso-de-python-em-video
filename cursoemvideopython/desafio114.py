from cordes import desafio
desafio(114)

import urllib.request
try:
    site = urllib.request.urlopen('https://pudim.com/')
except urllib.error.URLError:
    print('Não foi possivel acessar o site pudim')
else:
    print('O site pudim esta abrindo normalmente')
    # com site.read() voce consegue acessar todo conteudo/codigo do site html 