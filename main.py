import csv
import openai


def main():
    # define default prompt
    prompt = """The following message is reasoning for why a customer gave a Gas Company a
                certain score for the installation of a new gas meter. Please categorise
                their response into one of the following categories, and give me no more
                information. Respond with "1" if the score was given due to the workers. 
                Respond with "2" if the score was given due to duration.
                Respond with "3" otherwise."""

    # open the data file
    with open("test_data.csv") as fp:
        reader = csv.reader(fp)
        # loop over the rows of data
        for row in reader:
            print(row)

    return 0


main()

