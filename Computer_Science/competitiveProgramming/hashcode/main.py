from re import sub
from data_types import ExamplePerson # TODO replace
import ingest
import submission

INPUT_DIRECTORY = 'input/' # make sure this directory exisits
OUTPUT_DIRECTORY = 'ouput/' # make sure this directory exisits
INPUT_FILES = [''] # TODO the names of the files

def solve(input):
    pass #TODO

def main():
    for file in INPUT_FILES:
        raw_input = ingest.ingest_from_file(INPUT_DIRECTORY+file)
        soltuion = solve(raw_input)
        submission.write_to_file(soltuion)

if __name__ == '__main__':
    main()

