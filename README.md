# Flatsplode

Flatten/Explode JSON objects.

## Flatten

Flattening a JSON object squishes nested objects into a flat key-value dict.

Ex.

```python
{
  "fizz": {
    "buzz": {
      "jazz": "fuzz"
    }
  }
}
```

Becomes:

```python
{
  "fizz.buzz.jazz": "fuzz"
}
```

## Explode

Exploding a JSON object yields a number of JSON objects for every list in the original object.

Ex.

```python
{
  "fizz": [
    {
      "jazz": "fuzz"
    },
    {
      "wizz": "bang"
    }
  ]
}
```

Becomes:

```python
[
  {
    'fizz': {
      'jazz': 'fuzz'
    }
  },
  {
    'fizz': {
      'wizz': 'bang'
    }
  }
]
```

## Flatsplode

Flatsploding explodes the JSON object and flattens it.

Ex.

```python
{
  "fizz": {
    "buzz": [
      {
        "jazz": "fuzz"
      },
      {
        "wizz": "bang"
      }
    ]
  }
}
```

Becomes:

```python
[
  {
    'fizz.buzz': [
      {
        'jazz': 'fuzz'
      },
      {
        'wizz': 'bang'
      }
    ]
  }
]
```
