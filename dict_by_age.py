def by_age(persons, min_age, max_age):
    result = {}
    for name, age in persons.items():
        if age >= min_age and age <= max_age:
            if age in result.keys():
                existing_entry = result.get(age)
                result[age] = existing_entry + " and " + name
            else:
                result[age] = name
    return result
