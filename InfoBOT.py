
name = input("Hello, what is your name? ")
print("Hello there, " + name)


age = input("Hi there, " + name + ". If I may ask, what is your age? ")
birth_year = 2024 - int(age)


correct_age = input(f"So you were born in {birth_year} correct? (yes/no): ").strip().lower()


if correct_age == "yes":
    print("Nice!")
elif correct_age == "no":
    print("Fuck, I'm wrong!")
else:
    print("Please respond with 'yes' or 'no'.")
