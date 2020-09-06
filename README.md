# DataBuilder

Have you ever needed some dummy data to demonstrate some basic data analysis / machine learning topics?

DataBuilder can save you time by creating custom data sets within minutes.

<br>

## Installation

```
pip install databuilder
```

<br>

## Quick Example

```python
import databuilder as db

# make a dummy dataset about "our employees"
config = {
    'fields': {
        'empID':        db.ID(),
        'first_name':   db.Name(first_only=True),
        'last_name':    db.Name(last_only=True),
        'department':   db.Group(["Sales", "Acct", "Mktg", "IT"]),
        'salary':       db.NormalDist(50000, 10000),
        'hire_date':    db.Date("1990-01-01", "2020-12-31")
    }
}

# create a Pandas DataFrame with 
# the fields defined in `config`
df = db.create_df(config, n=200)

print(df.head(2))
#
#   Example output:
#         empID first_name last_name department  salary  hire_date
#      0      1      Frank      Ward         IT   69210 2004-05-05
#      1      2    Barbara    George       Mktg   46744 2019-05-20
```

<br>

## Complete Usage Guide

Coming Soon!

<!-- Detailed docs on how to use DataBuilder can be found in the `docs/` folder of this repo (or [click here](https://github.com/dbusteed/databuilder/blob/master/docs/README.md)) -->