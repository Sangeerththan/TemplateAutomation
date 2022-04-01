import docx2txt
import re
import openpyxl
import pandas as pd


def getCapitalWordsFromDoc(wordDocument):
    result = docx2txt.process(wordDocument)
    capital_letters = re.findall(r"\b[A-Z][A-Z]+\b", result)
    return set(capital_letters)


def readExcel(document, sheetName, columnIndex):
    read = pd.read_excel(document, sheet_name=sheetName)
    labels = read.iloc[:, columnIndex].tolist()
    return set(labels)
