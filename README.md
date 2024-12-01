# split_string_at_conjunctions
Python method for splitting strings around "and" while maintaining leading and trailing descriptors. For example:
- split_string_at_conjunctions("Apples and bananas") => ["Apples", "bananas"]
- split_string_at_conjunctions("3D positioning and navigation") => ["3D positioning", "3D navigation"]
- split_string_at_conjunctions("Apple and banana holders") => ["Apples holders", "banana holders"]
- split_string_at_conjunctions("Treatment and prevention of cancers and serious diseases") => ["Treatment of cancers", "Treatment of serious diseases", "prevention of cancers", "prevention of serious diseases"]
- split_string_at_conjunctions("Grand pianos") => ["Grand pianos"]

# Dependencies
Run `pip install -r .\requirements.txt` to install needed dependencies. The only dependencies are:
- spacy (https://spacy.io/usage) with the en_core_web_trf model for running part of speech identification against the string. You may be able to use a lighter spacy model like en_core_web_sm if you're splitting simple strings. By default it uses en_core_web_trf, which is one of the larger spacy models, as it seems to allow for the most variation in terms of capitilization in the strings while maintaining accurate part of speech identification. Lighter models tend to become inaccurate once the capitilzation changes.
- pytest for running tests

# Running tests
Run `pytest -k TestSplitStringAtConjunctions`
