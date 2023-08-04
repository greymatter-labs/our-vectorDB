
# GZIP Vector Database

`VectorDatabase` is a class for storing and searching text documents in a high-dimensional vector space. It uses the Annoy library for approximate nearest neighbor search, which allows for efficient querying of large databases.

## Class Initialization

The `VectorDatabase` class can be initialized with the following parameters:

- `n_trees` (optional): The number of trees for the Annoy index. The default value is 10. Increasing this value will increase indexing time while decreasing query time.

## Methods

The `VectorDatabase` class has the following methods:

### `add_entries(entries)`

Adds a list of text entries to the database.

- `entries`: A list of strings to be added to the database.

### `search(query, n)`

Searches the database for the `n` entries that are most similar to the query.

- `query`: A string to be searched for in the database.
- `n`: The number of similar entries to return.

## Example Usage

Here is an example of how to use the `VectorDatabase` class:

```python
from sklearn.feature_extraction.text import CountVectorizer

db = VectorDatabase()

# Add entries to the database
db.add_entries(["Hello, world!", "Goodbye, world!", "Hello, goodbye!"])

# Search the database
print(db.search("Hello, world!", 2))
```

This will print the two entries that are most similar to "Hello, world!".

## Dependencies

This class requires the following libraries:

- `gzip`
- `pickle`
- `sklearn`
- `Annoy`
