# from setuptools import setup, find_packages
#
# setup(
#     name='DataForge',
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         # Add dependencies here.
#         # e.g. 'numpy>=1.11.1
#     ]
# )
#

import json
from deep_translator import GoogleTranslator
from tqdm import tqdm

def contains_arabic(text):
    return any('\u0600' <= c <= '\u06FF' for c in text)

def batch_translate(arabic_texts):
    translation_dict = {}
    for text in tqdm(arabic_texts, desc="Translating Arabic Texts", ncols=100):
        try:
            translated = GoogleTranslator(source='ar', target='en').translate(text)
            translation_dict[text] = translated
        except Exception as e:
            print(f"Translation failed for '{text}': {e}. Removing it.")
            translation_dict[text] = ""  # Remove (blank) if translation fails
    return translation_dict

def process_records(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fields_to_translate = ['First Name', 'Last Name', 'State', 'City', 'Address']

    # Step 1: Collect unique Arabic strings
    arabic_texts = set()
    for record in data:
        for field in fields_to_translate:
            text = record.get(field, "")
            if text and contains_arabic(text):
                arabic_texts.add(text)

    print(f"Unique Arabic texts found: {len(arabic_texts)}")

    # Step 2: Translate once with progress bar
    translation_map = batch_translate(arabic_texts)

    # Step 3: Apply translations to records
    for record in data:
        for field in fields_to_translate:
            original = record.get(field, "")
            if original in translation_map:
                record[field] = translation_map[original]

    # Step 4: Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Processing complete. Output saved to '{output_file}'")

if __name__ == "__main__":
    input_json_file = 'C:/Users/rrana/PycharmProjects/DataForge/src/data_libraries/fake_person_profiles.json'
    output_json_file = '/src/data_libraries/fake_person_profiles.json'
    process_records(input_json_file, output_json_file)
