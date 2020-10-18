# DataBuilder Docs -- Fields

## Quick Reference
* [UniformDist](#UniformDist)
* [NormalDist](#NormalDist)
* [Name](#Name)
* [Group](#Group)
* [Custom](#Custom)
* [Constant](#Constant)
* [Date](#Date)
* [DateTime](#DateTime)
* [Time](#Time)
* [ID](#ID)
* [GUID](#GUID)

<br>

---

## `UniformDist`

Returns a series of data with a uniform distribution.

<br>

### Usage:
| Attribute | Description | Type | Required | Default |
|-----------|-------------|------|----------|---------|
| low | Lower bound of uniform distribution | int | yes ||
| high | Upper bound of uniform distribution | int | yes ||
| precision | Number of decimal places | int | no | `None` |

<br>

### Example:
```python
'work_experience': db.UniformDist(1, 10, precision=1) 
```

<br>

---

## `NormalDist`

Returns a series of data with a normal distribution.

<br>

### Usage:
| Attribute | Description | Type | Required | Default |
|-----------|-------------|------|----------|---------|
| mean | Mean of the normal distribution | int/float | yes | |
| sd | Standard deviation of the normal distribution | int/float | yes | |
| precision | Number of decimal places | int | no | `None` |
| bounds | Low and high end limits for the data points | tuple | no | `None` |

<br>

### Examples:
```python
# basic usage
'height': db.NormalDist(68, 5, precision=2)

# use `bounds` to ensure the data points are realistic
'age': db.NormalDist(40, 20, bounds=(1, 110))
```

<br>

---

## `Name`

Returns a first name, last name, or both.

<br>

### Usage:
| Attribute | Description | Type | Required | Default |
|-----------|-------------|------|----------|---------|
| first_only | returns a first name only | `bool` | no | `False` |
| last_only | returns a last name only | `bool` | no | `False` |
| brule | returns a [Steve Brule-esque name](https://www.youtube.com/watch?v=02iIN4n4y0A) | `bool` | no | `False` |
| depends_on | Points to a gender field (if available), so that names and genders are consistent | `str` | no | `None` |

<br>

### Examples:
```python
# first and last names in separate columns
'first_name': db.Name(first_only=True),
'last_name': db.Name(last_only=True)

# full name consistent with a "gender" column
'gender': db.Group( [('M', .5), ('F', .5)] ),
'name': db.Name(depends_on='gender')
```

<br>

---

## `Group`

Returns different groups, or classes. Can also provide probabilities associated with each group. When probabilities are specified, a uniform distribution is used.

<br>

### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| groups | List of groups (with optional discrete probability) | `list`, `tuple` | yes |

<br>

### Examples:
```python
# generate groups with an even split between all four classes
'department': db.Group(["Sales", "Acct", "Mktg", "IT"]),

# generate groups so that ~30% are 'Y', and ~70% are 'N'
'purchased': db.Group( [('Y', .3), ('N', .7)] )
```

<br>

---

## `Custom`

Returns customized value based on other columns.

**NOTE**: `Custom` columns need to be listed *after* the columns they're based on (see example).

<br>

### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| base | Column name which `func` will be applied to | `str` | yes |
| func | Function which takes the column value of `base`, and returns a transformed value | `function` | yes |

<br>

### Example:
```python
# create the column `email` based
# using the values from the `name` column
'name': db.Name(),
'email': db.Custom(
    'name',
    lambda x: x.replace(' ', '.').lower() + '@mail.com'
),
```

<br>

---

## `Constant`

Returns a constant value for every row.

<br>

### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| value | Literal value to be returned | `str` | yes |

<br>

### Example:
```python
# create a column with a constant value of 'Yes'
'is_customer': db.Constant('Yes')
```

<br>

---






## `Date`

Returns a series of dates, within a predefined range.

<br>

### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| start | start of datetime range | `datetime.date`, or `str` | yes |
| end | end of datetime range | `datetime.date`, or `str` | yes |

<br>

### Examples:
```python
# you can either pass a `datetime.date`
from datetime import date
'hire_date': db.Date(date(1980, 1, 1), date(2020, 12, 31))

# or use strings (YYYY-MM-DD)
'hire_date': db.Date("1980-01-01", "2020-12-31")
```

<br>

---

## `DateTime`

Returns a series of dates and times, within a predefined range.

<br>

### Usage:
| Attribute | Description | Type | Required | Default |
|-----------|-------------|------|----------|---------|
| start | start of datetime range | `datetime.datetime` or `str` | yes | |
| end | end of datetime range | `datetime.datetime` or `str` | yes | |
| unix | returns datetime as UNIX timestamp if `True` | `bool` | no | `False` |

<br>

### Examples:
```python
# you can either pass a `datetime.datetime`
from datetime import datetime
'order_timestamp': db.DateTime(datetime(2019, 1, 1, 6, 0), datetime(2019, 12, 31, 22, 0), unix=True)

# or use strings (YYYY-MM-DD HH:MM:SS)
'order_timestamp': db.DateTime("2019-01-01 6:00", "2019-12-31 22:00", unix=True)
```

<br>

---

## `Time`

Returns a series of times, within a predefined range. TODO

<br>

### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| start | start of time range | `datetime.time`, or `str` | yes |
| end | end of time range | `datetime.time`, or `str` | yes |

<br>

### Examples:
```python
# you can either pass a `datetime.time`
from datetime import time
'clock_in': db.Time(time(7, 0), time(9, 30))

# or use strings (HH:MM:[SS])
'clock_out': db.Time("16:45", "18:00")
```

<br>

---

## `ID`

Returns a series of integer IDs, each one incremented from the previous one.

<br>

### Usage:
| Attribute | Description | Type | Required | Default |
|-----------|-------------|------|----------|---------|
| start | Starting value for the ID | `int` | no | `1` |

<br>

### Example:
```python
'customerID': db.ID(start=100) 
```

<br>

---

## `GUID`

Returns a series of GUID/UUIDs.

<br>

### Usage:
| Attribute | Description | Type | Required | Default |
|-----------|-------------|------|----------|---------|
| format | Format of the GUID | `"str"`, `"hex"`, or `"int"` | no | `"str"` |

<br>

### Example:
```python
'deviceID': db.GUID(format="hex") 
```
