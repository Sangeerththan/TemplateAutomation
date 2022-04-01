import docx2txt
import re

# read in word file
result = docx2txt.process("BARA158b.docx")
capital_letters = re.findall(r"\b[A-Z][A-Z]+\b", result)
print(set(capital_letters))
