# Palavras e Verbos PT-BR

O arquivo `palavras.txt` neste repositório contém mais de 320.000 palavras do idioma português brasileiro (obtidas pela [lista de palavras do corretor ortográfico LibreOffice](https://cgit.freedesktop.org/libreoffice/dictionaries/plain/pt_BR/pt_BR.dic)).

O arquivo `verbos.txt` contém 5379 verbos do idioma português brasileiro, sendo 5000 os verbos mais usados da lingua (obtidos em [conjugação.com.br](conjugacao.com.br/verbos-populares/)) e  578 do portugues medieval (obtidos no  [site do Corpus Informatizado do Português Medieval](https://cipm.fcsh.unl.pt/gencontent.jsp?id=27)), que, retirando duplicadas dá um total de 5161 (5000 + 161)

O dicionário foi processado pelo programa `converter.py` para:

1. converter a codificação de Latin-1 para UTF-8

2. remover os códigos alfabéticos apensados a algumas palavras, após uma `/`

3. remover nomes de cidades (ex. "Carnaubal-CE")

4. acrescentar em linhas separadas as palavras que formam termos compostos (ex. casa-forte)

5. reordenar tudo alfabeticamente

O motivo do passo 4 é que a palavra "casa" não tem uma entrada individual no arquivo original! Se alguém souber o motivo, cadastre um *issue* explicando em que parte do código-fonte do corretor ortográfico do LibreOffice está a informação de que "casa" é uma palavra.

Já `getVerbos.py` :

1. processa o arquivo verbos1.txt, contendo os verbos do português medieval 

2. pega 5000 verbos do site conjunção.com.br utilizando BeaultifulSoup

3. junta num arquivo sem repetições

Mais verbos podem ser adicionados, colocando-os em verbos1.txt, adicionando outro arquivo ao script ou adicionando um website e configurando o BeaultifulSoup. 

Qualquer contribuição é bem-vinda! Ajude este repositório chegar mais longe! 
Inclusive, se quiser ajudar ainda mais, pode-se adicionar outras classes de palavras, mas isso requer mais trabalho
