# jsonstorage

JSON Storage is a simple lightweight data storage using JSON format in Python.

The focus of this library is to allow simple storage of data by serializing the data stored in the Python data structures to a json file.

Some key features of this library are:

1. Built on top of Python default API, that means, no third party library dependencies.

2. Simple navigation to get and put values. Dot notation: `'give.me.this.value'`, `'put.this.value'`.

3. It encapsulates the operations that deal with files and JSON serialization as well.

4. The data is serialized in UTF-8.

This library best fits for:

1. Create configuration files;
2. Storage of temporary and structured information that doesn't need complex search.

### How to install

`pip install jsonstorage`

### Usage

```python
from jsonstorage import JsonStorage

# Init a new storage. 
# The 'path' is where the file will be created after save() is called.
storage = JsonStorage(path='/tmp/data.json')

# Put some value. In this case, a list of Ferrari models.
storage.set_value('cars.brands.ferrari', ['360 Modena', 'Enzo', 'F40', 'F50'])

# Serialize the data into a JSON file.
storage.save()

models = storage.get_value('cars.brands.ferrari')
```