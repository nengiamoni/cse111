import random

# I Lists of possible words for each part of the sentence
determiners = ["One", "A", "The", "Some"]
nouns = ["boy", "bird", "dog", "children", "child", "rabbits", "car", "cats", "woman"]
verbs = ["talked", "drank", "drinks", "laugh", "run", "will talk"]
prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                "beyond", "by", "despite", "except", "for", "from", "into", "in", "near", "of", "off", "on",
                "onto", "over", "out", "past", "to", "under", "with", "without"]
adjectives = ["beautiful", "smart", "funny", "happy", "quick", "tall", "friendly", "curious"]
adverbs = ["quickly", "happily", "loudly", "carefully", "always", "usually"]

# Function to get a random word from a list
def get_random_word(word_list):
    return random.choice(word_list)

# Function to get a random preposition
def get_preposition():
    return get_random_word(prepositions)

# Function to get a random adjective
def get_adjective():
    return get_random_word(adjectives)

# Function to get a random adverb
def get_adverb():
    return get_random_word(adverbs)

# Function to build a prepositional phrase
def get_prepositional_phrase(quantity):
    determiner = "one" if quantity == "single" else "some"
    noun = get_random_word(nouns)
    preposition = get_preposition()
    return f"{preposition} {determiner} {noun}"

# Function to create a sentence
def make_sentence(quantity, verb_tense):
    determiner = get_random_word(determiners)
    adjective = get_adjective()
    noun = get_random_word(nouns)
    verb = get_random_word(verbs)
    adverb = get_adverb()
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)

    if verb_tense == "past":
        verb += "ed"

    sentence = f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

# Main function
def main():
    sentence_quantities = ["single", "single", "single", "plural", "plural", "plural"]
    verb_tenses = ["past", "present", "future", "past", "present", "future"]

    for i in range(6):
        sentence = make_sentence(sentence_quantities[i], verb_tenses[i])
        print(sentence)

if __name__ == "__main__":
    main()
