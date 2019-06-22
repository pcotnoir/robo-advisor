# robo-advisor
Automate the process of providing stock trading recommendations.

Setup Instructions:

1. Use the GitHub.com online interface to generate a new project repository entitled "robo-advisor". Ensure that there is a Python .gitignore file as well as an MIT License selected.
2. After creating the new repository on GitHub, double check that your web address is in the format of https://github.com/YOUR_USERNAME/robo-advisor .
3. Clone the repository and open in GitHub Desktop.
4. Navigate to the repository folder on GitBash using the command line:
```
cd ~/Desktop/robo-advisor
```
5. Using Visual Studio Code, create a new file in the repository by right-clicking on the Visual Studio Code Explorer pane and selecting "New File". Name this file "robo_advisor.py".
6. Inside the new "robo_advisor.py" file, input the below text and save the file:
```
# app/robo_advisor.py

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
```
7. Using Visual Studio Code, create a new file in the repository by right-clicking on the Visual Studio Code Explorer pane and selecting "New File". Name this file "requirements.txt"
8. In the "requirements.txt" file, input the following:
```
requests
python-dotenv
```
9. Set-up the Anaconda virtual environment by running the below code in GitBash. If prompted with a [y/n] install option, select y:
```
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```
10. Also in GitBash, install the required packages from the "requirements.txt" file:
```
pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)
pip install requests
```
11. Practice running the Python script by entering the below in the GitBash command-line:
```
python app/robo_advisor.py
```
12. Confirm that the example output is displayed in GitBash once the robo_advisor.py script has run.

13. Obtain an AlphaVantage API Key (e.g. "abc123") to add security to your program. Unique keys can be obtained at: https://www.alphavantage.co/support/#api-key .

14. With your API Key, update the contents of the ".env" file with your API Key credentials. Your code should be something like:
```
ALPHAVANTAGE_API_KEY="abc123"
```
where "abc123" is your unique key.

15. Ensure that your project repository contains the following .gitignore code:
```
# .gitignore
# ignore secret environment variable values in the ".env" file:
.env
```
16. Ensure that your project repository contains the following .gitignore file within the "data" directory:
```
# data/.gitignore
# h/t: https://stackoverflow.com/a/5581995/670433
# ignore all files in this directory:
*

# except this gitignore file:
!.gitignore
```

