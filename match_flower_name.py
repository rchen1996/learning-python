# open flowers.txt
# read every line
# save it as a dictionary
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(': ')[0].lower()
            flower = line.split(': ')[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# function
# take user input (first and last name)
# parse user input to identify first letter of first name
# print flower name with same first letter
def main():
    flower_d = create_flowerdict('flowers.txt')
    full_name = input('Enter your first and last name: ')
    first_letter = full_name[0].lower()
    print('Your flower is: {}'.format(flower_d[first_letter]))

main()