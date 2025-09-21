class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        person = Person (person["name"], person["age"])
        people_list.append(person)
    for person in people:
        person_instance = Person.people[person["name"]]
        if person.get("wife"):
            wife_instance = Person.people[person["wife"]]
            person_instance.wife = wife_instance
        if person.get("husband"):
            husband_instance = Person.people[person["husband"]]
            person_instance.husband = husband_instance
    return people_list

