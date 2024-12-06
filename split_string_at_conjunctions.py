import spacy

nlp = spacy.load("en_core_web_trf")

def is_valid_subject_comp(token):
    # Uses spacy's token.pos_ and token.dep_ values to identify if a token is a potential subject component.
    # In this case, tokens are words in the sentence.
    # The pos_ value stands for "part of speech". The potential values can be seen here: https://github.com/explosion/spaCy/blob/master/spacy/glossary.py.
    # Potential pos_ values are any nouns and adjectives as the adjectives may describe individual subjects.
    # The dep_ value stands for "dependencies" and describes the dependency relationships between tokens in the sentences.
    # The dependencies help identify if words are connected in the sentence. If the dependency is ROOT it means the token
    # may be related to multiple other tokens in the string so it would most likely be a descriptor as opposed to a subject.
    return token.pos_ in ["ADJ", "NOUN", "PROPN"] and token.dep_ != "ROOT"

def split_string_at_conjunctions(string_to_split):
    # 0. Return immediately if no conjunctions are present in the string
    if " AND " not in string_to_split.upper(): return [string_to_split]
    
    doc = nlp(string_to_split)
    and_ind = [str(token).upper() for token in doc].index("AND")
    
    # 1. Get first subject
    subject_parts = []
    token_to_append = None
    for token in reversed(doc[:and_ind]):
        if "'" in str(token):
            token_to_append = str(token)
            continue
        if not is_valid_subject_comp(token) and len(subject_parts) > 0: break
        token = str(token)
        if token_to_append is not None:
            token += token_to_append
            token_to_append = None
        subject_parts.insert(0, token)
    subject_1 = " ".join(subject_parts).strip()

    # 2. Get second subject
    subject_parts = []
    for token in doc[and_ind + 1:]:
        if "'" in str(token):
            subject_parts[-1] += str(token)
            continue
        if not is_valid_subject_comp(token) and len(subject_parts) > 0: break
        subject_parts.append(str(token))
    subject_2 = " ".join(subject_parts).strip()

    # 3. Get leading descriptors
    leading_descriptors = string_to_split.split(subject_1)[0].strip()
    if leading_descriptors != "": leading_descriptors += " "

    # 4. Get trailing descriptors
    trailing_descriptors = string_to_split.split(subject_2)[-1].strip()
    if trailing_descriptors != "": trailing_descriptors = " " + trailing_descriptors

    # 5. Form split strings
    split_string_1 = f"{leading_descriptors}{subject_1}{trailing_descriptors}"
    split_string_2 = f"{leading_descriptors}{subject_2}{trailing_descriptors}"

    # 6. Make recursive calls for the cases where there were multiple conjunctions in the sentence
    split_strings = []
    split_strings += [split_string_1] if " AND " not in split_string_1.upper() else split_string_at_conjunctions(split_string_1)
    split_strings += [split_string_2] if " AND " not in split_string_2.upper() else split_string_at_conjunctions(split_string_2)
    return split_strings