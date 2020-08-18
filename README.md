# DataBuilder

## Installation

```
pip install databuilder
```

<br>

## Basic Usage

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

# create a Pandas DataFrame object with 
# 200 rows and the fields defined in `config`
df = db.create_df(config, n=200)

print(df.head(2))
# Example output:
#       empID first_name last_name department  salary  hire_date
#    0      1      Frank      Ward         IT   69210 2004-05-05
#    1      2    Barbara    George       Mktg   46744 2019-05-20
```

<br>

## MORE COMING SOON

<!-- ## API

### Fields

Quick ref
* see this README for more info
* use the built-in help

### Options -->