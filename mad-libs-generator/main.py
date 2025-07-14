def mad_libs():
    print("🎉 Welcome to the Mad Libs Generator!\n")

    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ")
    noun = input("Enter a noun: ")
    place = input("Enter a place: ")

    story = f"""
    One day, a {adjective} {animal} was walking through the forest.
    Suddenly, it stopped and shouted, "{exclamation.upper()}!"
    It had seen a {noun} trying to {verb} near the {place}.
    What a strange sight!
    """

    print("\nHere’s your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
