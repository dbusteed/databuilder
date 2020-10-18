# DataBuilder Docs -- Options

<br>

## `correlation`

blurb

The `'correlation'` option, can take the following forms:
* ExplicitCorrelation
* RandomCorrelation

See below for detailed usage examples for each

<br>

### `ExplicitCorrelation`

#### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| columns | List of columns to apply correlation to. The order of this list needs to match the correlation matrix | list of str | yes |
| matrix | Correlation matrix, 1s on the diagonal, etc.  | 2D list of floats | yes |

<br>

#### Example:
```python
# add a correlation between 'age', 'weight', 'height'
#   corr(age, weight) = 0.5
#   corr(age, height) = 0.2
#   corr(weight, height) = 0.9
'correlation': db.ExplicitCorrelation(
    ['age', 'weight', 'height'],
    [[1, .5, .2],
    [.5, 1, .9],
    [.2, .9, 1]]
),
```

<br>

### `RandomCorrelation`

#### Usage:
| Attribute | Description | Type | Required |
|-----------|-------------|------|----------|
| columns | List of columns to apply random correlation to | list of str | yes |

<br>

#### Example:
```python
# add a random correlation between 'age', 'weight', 'height'
'correlation': db.RandomCorrelation(
    ['age', 'weight', 'height']
),
```