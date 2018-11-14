# Flatsplode

Flatten/Explode JSON objects.

## Flatten

Flattening a JSON object squishes nested objects into a flat key-value dict.

Ex.

```python
from flatsplode import flatten

flatten({
  "fizz": {
    "buzz": {
      "jazz": "fuzz"
    }
  }
}, expand=True)

# Returns...
{
  "fizz.buzz.jazz": "fuzz"
}
```

## Explode

Exploding a JSON object yields a number of JSON objects for every list in the original object.

Ex.

```python
from flatsplode import explode

explode({
  "fizz": [
    {"jazz": "fuzz"},
    {"wizz": "bang"}
  ]
}, expand=True)

# Returns...
(
  {"fizz": {"jazz": "fuzz"}},
  {"fizz": {"wizz": "bang"}}
)
```

## Flatsplode

Flatsploding flattens, explodes, and flattens again a JSON object into all possible combinations.

Ex.

```python
from flatsplode import flatsplode

flatsplode({
  "fizz": {
    "buzz": [
      {"jazz": "fuzz"},
      {"wizz": "bang"}
    ]
  }
}, expand=True)

# Returns....
[
  {
    "fizz.buzz": [
      {"jazz": "fuzz"},
      {"wizz": "bang"}
    ]
  }
]
```
