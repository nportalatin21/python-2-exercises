from pprint import pprint
from WordCounter import WordCounter
from TaxMan import TaxMan
from Calculator import Calculator
from CarCollector import CarCollector



    
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]


    def sort_people(people, field, direction):

        if direction == "asc":
             people.sort(key=lambda p: p[field])
        else:

            people.sort(key = lambda p: p[field], reverse=True)


    sort_people(people_list, "weight", "desc")
    print(people_list)

    # pass #TODO:

#-----------------------------------------------------------------------------------------------


def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def filter_males(people): 
            
            new_list = list(filter(lambda p: p["sex"] == 'male', people))
            return new_list

    filtered_list = filter_males(people_list)
    print(filtered_list)

#-----------------------------------------------------------------------------------------------

def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    def calc_bmi(person):
        
        weight = person['weight_kg'] #It takes a person dictionary as input, retrieves the 'weight_kg' and 'height_meters' values from the dictionary.
        height = person['height_meters']
        bmi = round(weight / height ** 2, 1)
        person['bmi'] = bmi
        return person

    new_people_list = list(map(calc_bmi, people_list))
    print(new_people_list)

#----------------------------------------------------------------------------

def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    
    def get_people(people):
        # [{expression to be applied to each item} for {iteration} {filter condition}*]

     return [p['name'] for p in people if p ['age'] >= 15]

    
    print(get_people(people_list))

#--------------------------------------------------------------------------------------------

# def ex5():
#     sentence = "This is a test of the emergency broadcast system"
#     word_counter = WordCounter(sentence)
#     word_counter.count_words()
#     print(word_counter.get_word_count())    # Returns the number of all the words.
#     print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
#     print(word_counter.get_longest_word())  # Returns the length of the longest word.

# ex5()

#---------------------------------------------------------------------------------------------

# def ex6():
#     items = [
#         {"id": 1, "desc": "clock", "price": 1.00},
#         {"id": 2, "desc": "socks", "price": 2.00},
#         {"id": 3, "desc": "razor", "price": 3.00},
#     ]
#     tm = TaxMan(items, "10%")
#     tm.calc_total()
#     print(tm.get_total())

# ex6()

#------------------------------------------------------------------------------------------------

# def ex7():
#     calculator1 = Calculator(4, 3)
#     calculator1.add()
#     print(calculator1.get_result())

#     calculator2 = Calculator(4, 3)
#     calculator2.sub()
#     print(calculator2.get_result())

#     calculator3 = Calculator(2, 3)
#     calculator3.mul()
#     print(calculator3.get_result())

#     calculator4 = Calculator(8, 2)
#     calculator4.div()
#     print(calculator4.get_result())

# ex7()

#-------------------------------------------------------------------------

def ex8():

    pprint(CarCollector.get_data())

ex8()