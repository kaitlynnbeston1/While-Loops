age = " "
total = 0
party = []
print("Use this program to determine the price of your movie tickets.")
print('Enter "000" when you are finished.')
active = True
while active:
    age = int(input("Enter your age: "))
    if age <= 3 and age > 000:
        print(f"Added 1 infant. \n Cost: $0")
        party.append("infant: $0")
    if age >= 3 and age < 12:
        print(f"Added 1 child. \n Cost: $10")
        party.append("child: $10")
        total += 10
    elif age >= 12:
        print(f"Added 1 grown up. \n Cost: $15")
        party.append("grown up: $15")
        total += 15
    elif age == 000:
        print(f"Your party of {len(party)} includes the following:")
        for person in party:
            print(person)
        print(f"Total cost: {total}")
        active = False
        