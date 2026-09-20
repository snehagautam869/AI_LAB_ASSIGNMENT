def search4letters(phrase:str ,letters:str="aeiou") -> set:
    """ Return the set of letteers found in phrase."""
    return set(letters).intersection(set(phrase))
