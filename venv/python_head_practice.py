def search4vowels(word:str) -> set:
    """Display any vowels found in an asked for word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

'''
def search4vowels(word):
    """Display any vowels found in an asked for word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)
'''


search4vowels('hitch-hiker')
print(help(search4vowels))


