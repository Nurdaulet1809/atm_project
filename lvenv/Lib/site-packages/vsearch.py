def vowle_search(phrase: str) -> list:
    '''Выводит гласные которые найдутся в фразе'''
    vowels = 'aeiou'
    exists = []
    for char in vowels:
        if char in phrase:
            exists.append(char)
    return exists
    
    