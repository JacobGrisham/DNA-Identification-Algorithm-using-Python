# DNA Identification Algorithm using Python
### Homework from [Harvard's Introduction to Computer Science CS50 hosted on eDX](https://www.edx.org/course/cs50s-introduction-to-computer-science)
### 🎓 [Problem Set 6](https://cs50.harvard.edu/x/2020/psets/6/)
- [DNA](https://cs50.harvard.edu/x/2020/psets/6/dna/): Program takes a sequence of DNA and a CSV file containing Short Tandem Repeats (STR) counts for a list of individuals and then outputs to whom the DNA (most likely) belongs.
- I wrote the code in dna.py. The other files were provided by the instructor.

![DNA Program Demo](img/demo.gif)

## 💡Lessons Learned
- Array and dictionary data structures in python
- Parsing data from csv file using `enumerate()`, `.strip()`, and `.split()`
- Substring `s[i:j]` iteration and multiple nested iterations in python

## 🚀 Getting Started
To run this project locally:
- In your terminal, navigate to the root program directory and run the following commands
```
$ python dna.py databases/large.csv sequences/#.txt
```
Where `#` is a number between 1 and 20. Refer to the txt files in the sequences directory. The sequences directory contains a targeted DNA sequence. The database directory contains data on individuals.

The output can be compared for accuracy against the list under the header "Testing" in the specifications (near the end of the file)

- Quick use examples
```
python dna.py databases/large.csv sequences/11.txt
python dna.py databases/large.csv sequences/17.txt
python dna.py databases/large.csv sequences/20.txt
```
