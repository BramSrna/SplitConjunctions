import re
import spacy

nlp = spacy.load("en_core_web_trf") # https://spacy.io/models/en

def is_valid_subject_comp(token):
    # Uses spacy's token.pos_ and token.dep_ values to identify if a token is a potential subject component.
    # In this case, tokens are words in the sentence.
    # The pos_ value stands for "part of speech". The potential values can be seen here: https://github.com/explosion/spaCy/blob/master/spacy/glossary.py.
    # Potential pos_ values are any nouns and adjectives as the adjectives may describe individual subjects.
    # The dep_ value stands for "dependencies" and describes the dependency relationships between tokens in the sentences.
    # The dependencies help identify if words are connected in the sentence. If the dependency is ROOT it means the token
    # may be related to multiple other tokens in the string so it would most likely be a descriptor as opposed to a subject.
    return token.pos_ in ["ADJ", "NOUN", "PROPN"] and token.dep_ != "ROOT"

def extract_substring(text, start_str, end_str):
    if start_str == end_str: return start_str

    start_index = text.find(start_str)
    if start_index == -1:
        return None  # Start string not found
    
    end_index = text.find(end_str, start_index)
    if end_index == -1:
        return None  # End string not found
    
    # Include the end string in the result
    return text[start_index:end_index + len(end_str)]

def split_ignore_case(text, substring):
    return re.split(substring, text, flags=re.IGNORECASE)

def get_leading_descriptors(string_to_split):
    subject_1 = get_subject_one(string_to_split)
    leading_descriptors = string_to_split.split(subject_1)[0].strip()
    if leading_descriptors != "": leading_descriptors += " "
    return leading_descriptors

def get_subject_one(string_to_split):
    if " AND " not in string_to_split.upper(): return string_to_split
    doc = nlp(string_to_split)
    and_ind = [str(token).upper() for token in doc].index("AND")
    string_split_at_and = split_ignore_case(string_to_split, " AND ")

    token_array = list(reversed(doc[:and_ind]))
    start_token = None
    for token in token_array:
        print(token, token.pos_, token.dep_, token.head, list(token.children))
        #if not (start_token.dep_ == "compound" and token.head == start_token) and "'" not in str(token) and not is_valid_subject_comp(token) and start_token is not None: break
        if start_token is None:
            start_token = token
            continue
        if (token.pos_ == "ADJ" or token.dep_ == "compound") and token.head == start_token:
            start_token = token
            continue
        break
    subject_1 = extract_substring(string_split_at_and[0], str(start_token), str(token_array[0]))
    if subject_1 not in string_to_split: raise Exception(f"Error during subject creation. {subject_1} not in {string_to_split}")
    return subject_1

def get_subject_two(string_to_split):
    doc = nlp(string_to_split)
    and_ind = [str(token).upper() for token in doc].index("AND")
    string_split_at_and = split_ignore_case(string_to_split, " AND ")

    token_array = doc[and_ind + 1:]
    end_token = None
    for token in token_array:
        if not (token.dep_ == "compound" and end_token.head == start_token) and "'" not in str(token) and not is_valid_subject_comp(token) and end_token is not None: break
        end_token = token
    subject_2 = extract_substring(string_split_at_and[1], str(token_array[0]), str(end_token))
    if subject_2 not in string_to_split: raise Exception(f"Error during subject creation. {subject_2} not in {string_to_split}")
    return subject_2

def get_trailing_descriptors(string_to_split):
    subject_2 = get_subject_two(string_to_split)
    trailing_descriptors = string_to_split.split(subject_2)[-1].strip()
    if trailing_descriptors != "": trailing_descriptors = " " + trailing_descriptors
    return trailing_descriptors

def split_string_at_conjunctions(string_to_split):
    # 0. Return immediately if no conjunctions are present in the string
    if " AND " not in string_to_split.upper(): return [string_to_split]
    
    # 1. Get first subject
    subject_1 = get_subject_one(string_to_split)

    # 2. Get second subject
    subject_2 = get_subject_two(string_to_split)

    # 3. Get leading descriptors
    leading_descriptors = get_leading_descriptors(string_to_split)

    # 4. Get trailing descriptors
    trailing_descriptors = get_trailing_descriptors(string_to_split)

    # 5. Form split strings
    split_string_1 = f"{leading_descriptors}{subject_1}{trailing_descriptors}"
    split_string_2 = f"{leading_descriptors}{subject_2}{trailing_descriptors}"

    # 6. Make recursive calls for the cases where there were multiple conjunctions in the sentence
    split_strings = []
    split_strings += [split_string_1] if " AND " not in split_string_1.upper() else split_string_at_conjunctions(split_string_1)
    split_strings += [split_string_2] if " AND " not in split_string_2.upper() else split_string_at_conjunctions(split_string_2)
    return split_strings

def validate_string_part_selection(string_to_split, leading_descriptors, subject_1, subject_2, trailing_descriptors):
    original_tokens = nlp(string_to_split)
    reconstructed_string = f"{leading_descriptors} {subject_2} AND {subject_1} {trailing_descriptors}"
    print(string_to_split)
    print(reconstructed_string)
    reconstructed_tokens = nlp(reconstructed_string)
    for orig_token, recon_token in zip(original_tokens, reconstructed_tokens):
        print(orig_token, orig_token.pos_, orig_token.dep_, orig_token.head, list(orig_token.children))
        print(recon_token, recon_token.pos_, recon_token.dep_, recon_token.head, list(recon_token.children))
        if len(list(orig_token.children)) != len(list(recon_token.children)):
            return False

    return True