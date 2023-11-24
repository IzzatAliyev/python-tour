def getLetterOrderNumber(letter):
    match letter:
        case 'a': return 1
        case 'b': return 2
        case 'c': return 3
        case 'd': return 4
        case 'e': return 5
        case _ : return 0
        
print(getLetterOrderNumber('a'))