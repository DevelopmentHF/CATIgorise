import csv
import openai
import env

MODEL = "gpt-3.5-turbo"


def main():
    # define default prompt
    prompt = """The following message is reasoning for why a customer gave a Gas Company a
                certain score for the installation of a new gas meter. Please categorise
                their response into one of the following categories, and give me no more
                information. Please make sure it is the most appropriate category for the feedback.
                
                - General Satisfaction
                - General Dissatisfaction
                - Effort Required (positive)
                - Effort Required (negative)
                - Timeliness (positive)
                - Timeliness (negative)
                - Field Staff Professionalism (positive)
                - Field Staff Professionalism (negative)
                """

    # Setup api
    openai.api_key = env.APIKEY

    # open the data file
    with open("test_data.csv") as fp, open("new_data.csv", 'w') as nfp:
        reader = csv.DictReader(fp)

        fieldnames = reader.fieldnames  # Retrieve the fieldnames
        writer = csv.DictWriter(nfp, fieldnames=fieldnames)

        # skip the header being used
        next(reader)
        # loop over the rows of data
        for row in reader:
            feedback = row["response"]

            # feed into chat gpt
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=[
                    {"role": "user",
                     "content": f'{prompt}. This message is: {feedback}'},
                ]
            )

            output = response['choices'][0]['message']['content']

            print(feedback)
            print(output)
            print("\n----\n")

            # add back to the file
            row["category"] = output
            writer.writerow(row)


    return 0


main()

