from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 4 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in plural_nouns

def test_get_verb():
    
    present_verbs_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, 'present')

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in present_verbs_1
    
    present_verbs_2 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(2, 'present')

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in present_verbs_2

    past_verbs=["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, 'past')

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in past_verbs

    future_verbs=["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, 'future')

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in future_verbs
    



def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    for _ in range(4):

        word = get_preposition()

        assert word in prepositions

def test_get_prepositional_phrases():
    
    for _ in range(4):
        #make a singular and plural phrase
        phrase_1 = get_prepositional_phrase(1)
        phrase_2 = get_prepositional_phrase(2)

        #split those into lists to test each element
        word_list_1 = phrase_1.split(" ")
        word_list_2 = phrase_2.split(" ")

        #test the preposition
        prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
        word = word_list_1[0]
        assert word in prepositions

        #test the singular determiner
        single_determiners = ["a", "one", "the"]
        word = word_list_1[1]
        assert word in single_determiners

        #test the single noun
        single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        word = word_list_1[2]
        assert word in single_nouns

        #test the plural prepositions
        prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
        word = word_list_2[0]
        assert word in prepositions

        #test the plural determiner
        plural_determiners = ["two", "some", "many", "the"]
        word = word_list_2[1]
        assert word in plural_determiners

        #test the plural nouns
        plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        word = word_list_2[2]
        assert word in plural_nouns

        









pytest.main(["-v", "--tb=line", "-rN", __file__])