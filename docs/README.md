# DataBuilder Docs

## 1. Basics

The primary use of DataBuilder module is the `create_df` method

To generate data with `create_df`, simply provide a **configuration dictionary** and the **number of desired rows**:

```python
# see project README.md for installation
import databuilder as db

# a configuration dictionary specifying
# fields and other DataBuilder options
my_config = {
    'fields': {
        # ...
    },
    'options': {
        # ...
    }
}

# create a Pandas DataFrame with 200 rows
df = db.create_df(config=my_config, n=200)
```

That's it! The basics of creating a data frame with DataBuilder is pretty simple, but the flexibility and power comes by specifying the different fields and options that work for your situation

**NOTE:** Both parameters for the `create_df` method are ***REQUIRED***. It's also important to define the configuration dictionary as shown above, albeit the `options` entry is optional

<br>

## 2. Fields

Fields are how you can define the different columns or features of your data frame. The name and type of the field is specified in the configuration dictionary that is passed to `create_df`

```python
import databuilder as db

my_config = {
    'fields': {
        
        # create a column called "StudentID" which
        # uses the databuilder.ID field type
        'StudentID': db.ID(),

        # ... more fields here
    
    }
}

df = db.create_df(config=my_config, n=50)
```

A *very* basic description of the available DataBuilder fields can be found below

Click on the **docs** link for each field, or use Python's `help()` function within an interactive shell

| Field | Description | Docs | 
|-------|-------------|-----------|
| UniformDist | uniform distribution | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#UniformDist) |
| NormalDist | normal distribution | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#NormalDist) |
| Name | first, last, or full name | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#Name) |
| Group | group, class, or category | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#Group) |
| Custom | custom field | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#Custom) |
| Constant | constant value | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#Constant) |
| Date | date | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#Date) |
| DateTime | date and time | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#DateTime) |
| Time | time | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#Time) |
| ID | integer id | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#ID) |
| GUID | guid / uuid | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/fields.md#GUID) |

<br> 

## 3. Options

Options are specified in the configuration dictionary that is passed to `create_df`, and as you might assume, they are optional

Specifying these options is a little different than defining the fields. A general example would look like this:

```python
import databuilder as db

my_config = {
    'fields': {
        # ...
    },

    'options': {
        # OPTION_NAME: OPTION_VALUE(...params)
        'option_name': db.ExampleOption(x='example')
    }
}

df = db.create_df(config=my_config, n=50)
```

The table below lists the available options:

| Name | Value(s) | Description | Docs |
|------|----------|-------------|------|
| correlation | ExplicitCorrelation | artificially correlate certain fields provided a correlation matrix | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/options.md#ExplicitCorrelation) |
| | RandomCorrelation | artificially correlate certain fields randomly | [docs](https://github.com/dbusteed/databuilder/blob/master/docs/options.md#RandomCorrelation) |