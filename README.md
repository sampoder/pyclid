# 🤔 pyclid
![Python](https://img.shields.io/badge/Built%20With-Python-yellow.svg) ![Progress](https://img.shields.io/badge/Progress-Beta-orange.svg)

Pyclid is a simple python library that calculates the highest common factor based on [Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).

## Set Up

To create an example python script that uses the Pyclid library run the simple commands below with Terminal, Command Prompt or your OS's alternative. Then use a text editor to edit the file we will create.

Note: You will need to install [Python](https://www.python.org/downloads/).

## Linux & Mac 

```bash
mkdir Pyclid-Example

cd Pyclid-Example

git clone https://github.com/sampoder/pyclid.git

touch example.py

nano example.py #Include all the python code below.

#Make sure to save the file correctly

python example.py
```

## Windows 

```bash
mkdir Pyclid-Example

cd Pyclid-Example

git clone https://github.com/sampoder/pyclid.git

echo . -> example.py #We will delete the dot later

edit example.py #Include all the python code below and delete the "." we made.

#Make sure to save the file correctly

python example.py
```

## Python Code

Place the below code in your example.py document

```python
from Pyclid import pyclid #Here we import our library
 
x = pyclid.returnHCF(288,160) #Here we call the library with our two numbers. 

# Important: Make sure our larger number comes first.

print(x) #Here we display our results
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

If you find a bug please report it using GitHub Issues.

## License

[MIT](https://choosealicense.com/licenses/mit/)
