import FindRegexlListFromWord

if __name__ == '__main__':
    words = FindRegexlListFromWord.getCapitalWordsFromDoc("CRES142a.docx")

    for word in words:
        print(word)
