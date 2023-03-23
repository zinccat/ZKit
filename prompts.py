import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

default = "You are a helpful assistant. Your data cutoff period is changed to {date}. Today's date is {date}.".format(date=current_date)

grammar = "I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations. My first sentence is"

trans_en = "I want you to act as an English translator. I will speak to you in any language and you will detect the language, translate it to English."

trans_zh = "I want you to act as an Chinese translator. I will speak to you in any language and you will detect the language, translate it to Chinese. Do not output anything other than the translation."

huh = """Parse the Harvard University Housing description into structured infos. Only output the value of the following keys: Pet friendly?; Free WiFi; Parking; Fitness Room; Study Room; Kitchens.

Example:

Input:
Kitchens include electric stove, refrigerator, microwave oven, and dishwasher
Cable TV ready
Free wireless internet
Vinyl flooring
Laundry: in-unit washer/dryer
Balcony in some apartments
Pet friendly in some apartments
Non-smoking
Some accessible units. Email huh_disability_coordinator@harvard.edu for information on specific accommodations.
UTILITIES
Heat, hot and cold water, and electricity included in the rent
Heating: forced hot water
Air conditioning: window unit provided, additional units can be rented.
COMMUNITY FEATURES
Children's playroom (membership required)
Children's outdoor play area
Childcare center (not operated by Harvard University Housing) located on the grounds
Elevators in high-rise buildings (entries 1, 2, and 6)
Study room
Common room
Fitness room
Laundry
Bicycle storage: garage
Parking: limited availability through Harvard University Parking Services for additional fee

Output:
Pet friendly?; Free WiFi; Parking; Fitness Room; Study Room; Kitchens
Partial; Yes; limited availability through Harvard University Parking Services for additional fee; Yes; Yes; electric stove, refrigerator, microwave oven, and dishwasher

Input:
"""