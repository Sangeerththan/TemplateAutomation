import docx2txt
import re
import openpyxl
import pandas as pd


def getCapitalWordsFromDoc(wordDocument):
    result = docx2txt.process(wordDocument)
    capital_letters = re.findall(r"\b[A-Z][A-Z]+\b", result)
    return set(capital_letters)


words = getCapitalWordsFromDoc("BARA158b.docx")

for word in words:
    print(word)

def readExcel(document, columnIndex):
    read = pd.read_excel(document)
    labels = read.iloc[:, columnIndex].tolist()
    return set(labels)


print(set.intersection(readExcel("axxia.xlsx", 8),getCapitalWordsFromDoc("BARA158b.docx")))
print(getCapitalWordsFromDoc("CRES142a.docx"))
