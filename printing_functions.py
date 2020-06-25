def printing_models(unprinted_models, printed_models):
    while unprinted_models:
        current_printed = unprinted_models.pop()
        print(f" printing models books are : \n {current_printed}")
        printed_models.append(current_printed)


def Display_completed_models(completed_models):
    print("printing done then you can sell following books :")
    for completed_model in completed_models:
        print(completed_model)
