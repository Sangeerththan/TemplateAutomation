import FindRegexlListFromWord

if __name__ == '__main__':
    words = FindRegexlListFromWord.getCapitalWordsFromDoc("file")

    for word in words:
        print(word)
