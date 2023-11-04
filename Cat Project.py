MAX_KAT = 20
cat_breeds = ['Siamese', 'Persian', 'Puspin', 'Bengal', 'Sphynx', 'Ragdoll', 'British Shorthair', 'Scottish Fold', 'Abyssinian', 'Burmese', 'Russian Blue', 'Norwegian Forest', 'Siberian', 'Egyptian Mau', 'Devon Rex', 'Oriental', 'Exotic Shorthair', 'Cornish Rex', 'American Shorthair', 'Tonkinese']

def pets():
    while True:
        cats = input("How many cats do you have?: ")
        if cats.isdigit():
            cats = int(cats)
            if cats > 0:
                break
            else:
                print("Amount must be greater than zero because this question is only for those who have a cat. If you don't have a cat, you can go away now. Thanks! Just kidding. Hehehe.")
        else:
            print("Please let me know how many cats you have.")

    return cats

def get_number_of_kat():
    while True:
        print("Choose a breed for your cat (1-" + str(MAX_KAT) + "):")
        for i, breed in enumerate(cat_breeds):
            print(str(i+1) + ". " + breed)
        kat = input("Enter the number corresponding to the breed: ")
        if kat.isdigit():
            kat = int(kat)
            if 1 <= kat <= MAX_KAT:
                break
            else:
                print("Please enter a valid breed number.")
        else:
            print("Enter a valid breed number.")

    return kat


def main():
    amount = pets()
    kats = get_number_of_kat()
    breed = cat_breeds[kats-1]
    print('You have', amount, 'cat(s), and the breed of your cat is:', breed)


main()
