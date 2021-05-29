def check_valid_choices(possible_choices, user_choice):
    """check if is a valid choice"""

    indexes = [index for index in range(
        len(possible_choices)) if possible_choices[index] == user_choice.upper()]
    return len(indexes) > 0


def ask(question, possible_choices):
    """ask and check user choice"""

    is_valid = False
    response = ''
    while is_valid == False:

        response = input(question)
        is_valid = check_valid_choices(possible_choices, response)

        if is_valid == False:
            print(f'\n{response} is not a valid choice\n')

    return response.lower()


# questions

# question 1
question1_choice1 = 'RIGHT'
question1_choice2 = 'LEFT'
question1 = f'You are walking through a forest and need to find the map to go back to your home... You found two ways: {question1_choice1} and {question1_choice2}. Which one do you want to pick up? '
question1_possible_choices = [question1_choice1, question1_choice2]

# question 2 first scenario
question2_scenario1_choice1 = 'FISH'
question2_scenario1_choice2 = 'GLASS WATER'
question2_scenario1_choice3 = 'MAP'

question2_scenario1 = f'You went to {question1_choice1} and found three items: {question2_scenario1_choice1}, {question2_scenario1_choice2} and {question2_scenario1_choice3}. Which one do you want to pick up? '
question2_scenario1_possible_choices = [question2_scenario1_choice1,
                                        question2_scenario1_choice2, question2_scenario1_choice3]

# question 2 second scenario
question2_scenario2_choice1 = 'FINSHING ROAD'
question2_scenario2_choice2 = 'KNIFE'
question2_scenario2 = f'You pick up the {question1_choice2} and found two items: {question2_scenario2_choice1} and {question2_scenario2_choice2}. Which one do you want to pick up? '
question2_scenario2_possible_choices = [
    question2_scenario2_choice1, question2_scenario2_choice2]

question1_user_choice = ask(question1, question1_possible_choices)
question2_scenario1_user_choice = ''
question2_scenario2_user_choice = ''

# scenario 1
if question1_user_choice == question1_choice1.lower():
    question2_scenario1_user_choice = ask(
        question2_scenario1, question2_scenario1_possible_choices)

    # scenario 2
    if question2_scenario1_user_choice == question2_scenario1_choice1.lower():
        print(
            f'\nYou pick up the {question2_scenario1_choice1}... you satiate your hunger, but still haven\'t found your home, go back to the beginning\n')
    elif question2_scenario1_user_choice == question2_scenario1_choice2.lower():
        print(
            f'\nYou pick up the {question2_scenario1_choice2}... you quenched your thirst but you did not find your home yet, go back to the beginning\n')
    else:
        print(
            f'\nYou pick up the {question2_scenario1_choice3}... congrats now you can find your home!!! YOU WIN!!!!\n')

# scenario 3
else:
    question2_scenario2_user_choice = ask(
        question2_scenario2, question2_scenario2_possible_choices)

    if question2_scenario2_user_choice == question2_scenario2_choice1.lower():
        print(
            f'\nYou pick up the {question2_scenario2_choice1}... you can fish, but still haven\'t found your home, go back to the beginning\n')
    else:
        print(
            f'\nYou pick up the {question2_scenario2_choice2}... you have a knife, but still haven\'t found your home, go back to the beginning\n')
