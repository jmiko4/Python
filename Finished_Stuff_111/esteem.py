
def main():
    print('This program is an implementation of the Rosenberg '
    'Self-Esteem Scale. This program will show you ten'
    'statements that you could possibly apply to yourself.'
    'Please rate how much you agree with each of the'
    'statements by responding with one of these four letters:')

    print('D means you strongly disagree with the statement.\n'
    'd means you disagree with the statement.\n' 
    'a means you agree with the statement.\n' 
    'A means you strongly agree with the statement.')
    pos,neg =take_test()
    score = calculate_score(pos,neg)
    print(score)


def take_test():
    '''Administers the  confidence test then returns two lists of the responses'''
    answers_pos=[]
    answers_neg=[]
    answers_pos.append(input('I feel that I am a person of worth, at least on an equal plane with others.'))
    answers_pos.append(input('I feel that I have a number of good qualities.'))
    answers_neg.append(input('All in all, I am inclined to feel that I am a failure.'))
    answers_pos.append(input('I am able to do things as well as most other people.'))
    answers_neg.append(input('I feel I do not have much to be proud of.'))
    answers_pos.append(input('I take a positive attitude toward myself.'))
    answers_pos.append(input('On the whole, I am satisfied with myself.'))
    answers_neg.append(input('I wish I could have more respect for myself.'))
    answers_neg.append(input('I certainly feel useless at times.'))
    answers_neg.append(input('At times I think I am no good at all.'))
    return answers_pos, answers_neg


def calculate_score(answers_pos,answers_neg):

    score = 0

    for i in answers_pos:
        if i == 'D':
            score+=0
        elif i == 'd':
            score+=1
        elif i == 'a':
            score+=2
        elif i == 'A':
            score+=3

    for i in answers_neg:
        if i == 'D':
            score+=3
        elif i == 'd':
            score+=2
        elif i == 'a':
            score+=1
        elif i == 'A':
            score+=0


    return score


main()