"""
In this bite you will work with a list of names. 

First you will write a function to take out duplicates and title case them. 

Then you will sort the list in alphabetical descending order by surname 
and lastly determine what the shortest first name is. 
For this exercise you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it 'sorted' :)
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names_set = set()
    for name in NAMES:
        names_set.add(name.title())
    return list(names_set)

def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    names_tup_list = []
    result = []
    for name in names:
        (first, last) = name.split()
        names_tup_list.append((last,first))
    names_sorted_tup_list = sorted(names_tup_list, reverse=True)
    for n in names_sorted_tup_list:
        result.append("%s %s" %(n[1], n[0]))
    return (result)

def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    shortest = None
    for name in names:
        if shortest is None:
            shortest = name.split()[0]
        if name is not None and len(name.split()[0]) < len(shortest):
            shortest = name.split()[0]
    return shortest

n = (dedup_and_title_case_names(NAMES))
m = sort_by_surname_desc(n)
p = shortest_first_name(n)
print (p)



"""pytest tests

from names import (NAMES, dedup_and_title_case_names,
                   sort_by_surname_desc, shortest_first_name)


def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') == 1
    assert names.count('julian sequeira') == 0
    assert names.count('Brad Pitt') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Alec Baldwin'


def test_shortest_first_name():
    assert shortest_first_name(NAMES) == 'Al'
"""
