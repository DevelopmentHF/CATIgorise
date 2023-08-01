# CATIgorise 🗄️

A tool used to categorise CATI verbatim responses into a set list of categories.

Inputted data should be in `csv` format, and outputted data retains all input data into a new file with the `category` column edited. 

## Usage

CATIgorise currently is based on the action of installing a new gas meter, but that is easily edited in the source code if needed.
To add another category, add it to the `prompt` **variable** in `main.py`.
You will also need your own API key from OpenAI, and a new file called `env.py` with the following line:

> Note: The program is based on test data csv file with the format:
> 
> id,response,score,category
> 
> For actual use, update this to your actual format, but make sure the string component retains the name "response"

```python
APIKEY = "YOUR_KEY_HERE" # replace with your own generated key
```

Make sure the inputted data filename is set correctly to your file name:

```python
with open("YOUR_FILE_NAME.csv")
```

To run the program, use the in-built IDE run button or execute it in the CLI as such:

#### MacOS
```shell
python3 main.py
```

#### Windows
```shell
python main.py
```

## Dependencies
Only the OpenAI library is needed, install with the following commands.

#### MacOS:
```shell
pip3 install openai
```

#### Windows:
```shell
pip install openai
```
