import unicodedata

import requests
from bs4 import BeautifulSoup

# parte do código foi escrito por pythonprobr
# o código original no arquivo converter.py

ENTRADA = 'verbos1.txt'
SAIDA = 'verbos2.txt'


def normalizar(txt):
    """Remove acentos e transforma 'A' ou 'ª' em 'a'."""
    norm_txt = unicodedata.normalize('NFKD', txt).lower()
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def chave(txt):
    """Manter palavras acentuadas após as não acentuadas"""
    codigos = tuple(ord(c) for c in txt)
    return (normalizar(txt), codigos)


verbos = set()
with open(ENTRADA, encoding='UTF-8') as entrada:
    for i, linha in enumerate(entrada):
        linha = linha.strip()
        linha = linha.split('/')[0]
        partes = linha.split('-')
        if linha:  # para evitar palavra vazia
            if len(partes) < 2:
                verbos.add(linha)  # incluir palavra composta
        if len(partes) > 1:
            for palavra in partes:
                if palavra:
                    verbos.add(palavra)  # para evitar palavra vazia

    qt_original = i

msg = '{} palavras na lista original, {} na lista gerada: {} adicionadas'
extra = len(verbos) - qt_original
print(msg.format(qt_original, len(verbos), extra))

# pergar verbos online

urls = set()
for i in range(1, 51):
    urls.add('https://www.conjugacao.com.br/verbos-populares/' + str(i) + '/')

i = 1
for url in urls:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    pages = soup.findAll('li')
    for page in pages:
        verb = page.get_text()
        verbos.add(verb)
    print(str(i) + " pages")
    i = i + 1

verbos = sorted(verbos, key=chave)

with open(SAIDA, 'wt', encoding='utf-8') as saida:
    saida.write('\n'.join(verbos))
    saida.write('\n')
