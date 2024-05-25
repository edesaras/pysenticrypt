# pysenticrypt

A simple Python wrapper for the SentiCrypt API, providing access to cryptocurrency sentiment analysis data.

[SentiCrypt](https://senticrypt.com/)
## Installation

```bash
pip install pysenticrypt
```


## Usage

```python
from pysenticrypt import SentiCryptAPI

# Initialize the API client
api_client = SentiCryptAPI()

# Get the entire history of sentiment analysis data
all_data = api_client.get_all_data()
print(all_data)

# Get the entire history of sentiment analysis data in a pretty format
pretty_data = api_client.get_pretty_all_data()
print(pretty_data)

# Get a list of all available endpoints
index_data = api_client.get_index()
print(index_data)

# Get sentiment analysis data for a specific date
date_data = api_client.get_data_by_date("2023-04-17")
print(date_data)
```
