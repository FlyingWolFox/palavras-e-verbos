import unicodedata

import requests
from bs4 import BeautifulSoup

# parte do código foi escrito por pythonprobr
# o código original no arquivo converter.py

ENTRADA = 'verbos_medievais.txt'
SAIDA = 'verbos.txt'


def normalizar(txt):
    """Remove acentos e transforma 'A' ou 'ª' em 'a'."""
    norm_txt = unicodedata.normalize('NFKD', txt).lower()
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def chave(txt):
    """Manter palavras acentuadas após as não acentuadas"""
    codigos = tuple(ord(c) for c in txt)
    return (codigos, normalizar(txt))


verbos = set()

# pegar verbos online

# urls de todas as páginas contendo os verbos
urls = set()
for i in range(1, 51):
    urls.add('https://www.conjugacao.com.br/verbos-populares/' + str(i) + '/')

print('Pegando os verbos online...')

# pega os verbos de todas as 50 páginas
# de conjugacao.c
progressso = 2
for url in urls:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    pages = soup.findAll('li')
    for page in pages:
        verb = page.get_text()
        verbos.add(verb)
    print('Progresso: ' + str(progressso) + '%')
    progressso = progressso + 2

qt_original = len(verbos)

# pegar verbos do português medieval
with open(ENTRADA, encoding='UTF-8') as entrada:
    for i, linha in enumerate(entrada):
        linha = linha.strip()
        linha = linha.split('/')[0]
        partes = linha.split('-')
        if linha:  # para evitar palavra vazia
            if len(partes) < 2:
                verbos.add(linha.lower())  # incluir palavra composta
        if len(partes) > 1:
            for palavra in partes:
                if palavra:
                    verbos.add(palavra.lower())  # para evitar palavra vazia

verbos = sorted(verbos, key=chave)

msg = '{} palavras na lista original, {} na lista gerada: {} adicionadas'
extra = len(verbos) - qt_original
print(msg.format(qt_original, len(verbos), extra))

verbos = sorted(verbos, key=chave)

with open(SAIDA, 'wt', encoding='utf-8') as saida:
    saida.write('\n'.join(verbos))
    saida.write('\n')
