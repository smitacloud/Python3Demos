#Counter allows us to count the occurrences of a particular item. For instance it can be used to count the number of individual favourite colours:

from collections import Counter

specializations = (
    ('Smita', 'Java'),
    ('Mahi', 'Azure'),
    ('Meenal', 'Oracle'),
    ('Amit', 'Android'),
    ('Chandra', 'Spark'),
    ('Satya', 'Casendra'),
    ('Makarand', 'Java'),
    ('Smita', 'Selenium'),
)

technology = Counter(name for name, skill in specializations)
print(technology)


#We can also count the most common lines in a file using it. For example:

with open('names.txt', 'rb') as f:
    line_count = Counter(f)
print(line_count)
