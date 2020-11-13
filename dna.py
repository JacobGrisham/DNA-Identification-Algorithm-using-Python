import sys
from sys import argv

# User Error handling
if len(argv) < 3:
    print("Usage: python dna.py data.csv sequence.txt")
if "csv" in argv[1] == False:
    print("Usage: python dna.py data.csv sequence.txt")
# For quick use, copy and paste: python dna.py databases/small.csv sequences/1.txt

# Read files into memory
database = argv[1]
sequences = argv[2]

people = open(database, "r")
sequence = open(sequences, "r")

# Data Structures
# Create array to store STR values of people
STRs = []
# Create array to store STR values of the DNA sequence. Will compare against STR array above
final_STR = []
# Create dictionary to store names and frequency of STR values
individuals = {}

# Parse data in people database/csv file
for idx, rows in enumerate(people):
    # Populate array of stored STR values
    if idx == 0:
        STRs = [STR for STR in rows.strip().split(",")][1:]
    # Populate dictionary of stored names and frequency of STR values
    else:
        row = rows.strip().split(",")
        # use int(x) to convert string to integer
        individuals[row[0]] = [int(freq) for freq in row[1:]]

# Open DNA sequence/txt file
dna_sequence = sequence.read()

# Compute longest run of STRs
for STR in STRs:
    i = 0
    final_max_STR = -1
    max_STR = 0
    while i < len(dna_sequence):
        # For each position, find STR
        # s[i:j] to to get the substring with all characters from i to j (not including j)
        position = dna_sequence[i: i + len(STR)]
        if position == STR:
            # For each position in sequence, count how many times STR repeats
            max_STR += 1
            final_max_STR = max(final_max_STR, max_STR)
            i += len(STR)
        else:
            # For each position, keep checking successive substrings until STR stops repeating
            max_STR = 0
            i += 1
    final_STR.append(final_max_STR)

# Compare longest run of STR to people
for key, values in individuals.items():
    if values == final_STR:
        print(key)
        sys.exit()
# If no matches at all, print no match
print("No match")