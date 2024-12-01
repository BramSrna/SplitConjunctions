import spacy

nlp = spacy.load("en_core_web_trf")

def is_valid_subject_comp(token):
    # spacy pos types: https://github.com/explosion/spaCy/blob/master/spacy/glossary.py
    return token.pos_ in ["ADJ", "NOUN", "PROPN"] and token.dep_ != "ROOT"

def split_string_at_conjunctions(string_to_split):
    # 0. Return immediately if not conjunctions are present in the string
    if " AND " not in string_to_split.upper(): return [string_to_split]
    
    doc = nlp(string_to_split)
    and_ind = string_to_split.upper().split(" ").index("AND")
    
    # 1. Get first subject
    subject_parts = []
    for token in reversed(doc[:and_ind]):
        if not is_valid_subject_comp(token) and len(subject_parts) > 0: break
        subject_parts.insert(0, str(token))
    subject_1 = " ".join(subject_parts).strip()

    # 2. Get second subject
    subject_parts = []
    for token in doc[and_ind + 1:]:
        if not is_valid_subject_comp(token) and len(subject_parts) > 0: break
        subject_parts.append(str(token))
    subject_2 = " ".join(subject_parts).strip()

    # 3. Get leading descriptors
    leading_descriptors = string_to_split.split(subject_1)[0].strip()
    if leading_descriptors != "": leading_descriptors += " "

    # 4. Get trailing descriptors
    trailing_descriptors = string_to_split.split(subject_2)[1].strip()
    if trailing_descriptors != "": trailing_descriptors = " " + trailing_descriptors

    # 5. Form split strings
    split_string_1 = f"{leading_descriptors}{subject_1}{trailing_descriptors}"
    split_string_2 = f"{leading_descriptors}{subject_2}{trailing_descriptors}"

    # 6. Make recursive call for the cases where there were more than one conjunctions in the sentance
    split_strings = []
    split_strings += [split_string_1] if " AND " not in split_string_1.upper() else split_string_at_conjunctions(split_string_1)
    split_strings += [split_string_2] if " AND " not in split_string_2.upper() else split_string_at_conjunctions(split_string_2)
    return split_strings