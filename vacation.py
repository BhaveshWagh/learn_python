responses = {}

poll_user = True
while poll_user:
    name = input("What is your name ? : ")
    place = input("If you could visit one place in the world ? & where would you go ?: ")

    responses[name] = place

    repeat = input("would you like to let another presons respond ? (yes/no) ")
    if repeat == 'no':
        poll_user = False

print("\n .... Result ....")
for name, place in responses.items():
    print(f"{name} would like to visit {place}")