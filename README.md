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

### How to use it

```python
from jsonstorage import JsonStorage

# Init a new storage.
# The 'path' is where the file will be created after the save() method is called.
storage = JsonStorage(path='/tmp/data.json')

# Put some value. In this case, a list of Ferrari models.
storage.set_value('cars.brands.ferrari', ['360 Modena', 'Enzo', 'F40', 'F50'])

# This method serializes the data to JSON format and then saves it on a file in the given path, chosen when JsonStorage was initiated.
storage.save()

# Get the list of Ferrari models.
ferrari_models = storage.get_value('cars.brands.ferrari')
```
### Development of jsonstorage

If you think that this library can be more fun and do more things as well, feel free to fork and work on it to make things happen. My only request is that you don't forget to share your great work with me, by making a pull request.
