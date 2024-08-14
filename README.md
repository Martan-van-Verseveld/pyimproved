# Basic Usage
Quick example printing a string inside of a box
```
import pyimproved

dictionary = {
    "name": "Martan van Verseveld",
    "library": "pyimproved"
}

# print_=False makes it return instead of printing it.
prettified_string = pyimproved.dprint(dictionary, print_=False)
pyimproved.boxed(prettified_string)


# OUTPUT:
# ╭──────────────────────────────────╮
# │ name....:   Martan van Verseveld │
# │ library.:   pyimproved           │
# ╰──────────────────────────────────╯
```

# Installation
## Fast
```
git clone https://github.com/Martan-van-Verseveld/pyimproved && cd ./pyimproved && pip install . -y
```

## Step by step
### Step 1
```
git clone https://github.com/Martan-van-Verseveld/pyimproved
```
### Step 2
```
cd ./pyimproved
```
### Step 3
```
pip install .
```