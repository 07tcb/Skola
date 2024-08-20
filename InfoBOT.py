#ta reda på namn
name = input("Hello, what is your name? ")
print("Hello there, " + name)

#ta reda på ålder
age = input("Hi there, " + name + ". If I may ask, what is your age? ")
birth_year = 2024 - int(age)

#är födelsedagsåret korrekt uträknat?
correct_age = input(f"So you were born in {birth_year} correct? (yes/no): ").strip().lower()

#bottens respons till svaret
if correct_age == "yes":
    print("Nice!")
elif correct_age == "no":
    print("Ah, I'm wrong!")
else:
    print("Please respond with 'yes' or 'no'.")
#inget syfte med denna bot än, framtidsplanen är att förvara namn o ålder i en .txt eller liknande
