calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    neger = (len(string), string.upper(), string.lower())
    count_calls()
    return neger



def is_contains(string, list_to_search):
    count_calls()
    list_to_search_lower = []
    string = string.lower()
    for i in list_to_search:
        list_to_search_lower.append(i.lower())
    if string in list_to_search_lower:
        return True
    else:
        return False





print(string_info('BObrE'))
print(string_info('BoReNgaTe'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
