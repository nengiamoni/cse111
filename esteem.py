def display_intro():
    # Display introductory text to user
    print("Welcome to the Rosenberg Self-Esteem Scale.")
    print("Please respond to the following statements:")
    print("D: Strongly Disagree \nd: Disagree \nA: Strongly Agree \na: Agree")


def get_response():
    # Prompt the user for a response and return the score
    response = input("Your response: ")
    response_dictionary = {"D": 0, "d": 1, "A": 3, "a": 2}
    response_value = response_dictionary.get(response, -1)

    return response_value


def main():

    display_intro()

    statements = [
        "I feel that I am a person of worth, at least on an equal plane with others.",
        "I feel that I have a number of good qualities.",
        "All in all, I am inclined to feel that I am a failure.",
        "I am able to do things as well as most other people.",
        "I feel I do not have much to be proud of.",
        "I take a positive attitude toward myself.",
        "On the whole, I am satisfied with myself.",
        "I wish I could have more respect for myself.",
        "I certainly feel useless at times.",
        "At times I think I am no good at all."
    ]

    total_score = 0

    for statement in statements:
        print(statement)
        response_score = get_response()

        if response_score < 0:
            print("Invalid response. Please use D, d, a, or A.")
        else:
            total_score = total_score + response_score

    print(f"Your total score is: {total_score}")
    if total_score < 15:
        print("You may have a problematic low self-esteem.")


main()
