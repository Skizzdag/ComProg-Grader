def CountWord(word,sen):
    count = 0
    #prepare sentence
    sen_copy = list(sen)
    sentence = ""
    for i in range(len(sen)):
        if sen_copy[i] == '"' or sen_copy[i] == '(' or sen_copy[i] == ')' or sen_copy[i] == ',' or sen_copy[i] == '.' or sen_copy[i] == "'":
            sen_copy[i] = " "
        sentence += sen_copy[i]
    sentence = sentence.split()
    #Countword
    for j in sentence:
        if word == j:
            count += 1
    return print(count)
CountWord((input()),str(input()))