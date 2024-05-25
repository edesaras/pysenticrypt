import requests

class SentiCryptAPI:
    """
    A simple wrapper for the SentiCrypt API.

    Attributes:
        base_url (str): The base URL for the SentiCrypt API.
    """

    def __init__(self):
        self.base_url = "https://api.senticrypt.com/v2/"

    def get_all_data(self):
        """
        Get the entire history of sentiment analysis data.

        Returns:
            list: A list of dictionaries containing sentiment analysis data.
        """
        response = requests.get(f"{self.base_url}all.json")
        response.raise_for_status()
        return response.json()

    def get_pretty_all_data(self):
        """
        Get the entire history of sentiment analysis data in a pretty format.

        Returns:
            list: A list of dictionaries containing sentiment analysis data.
        """
        response = requests.get(f"{self.base_url}all-pretty.json")
        response.raise_for_status()
        return response.json()

    def get_index(self):
        """
        Get a list of all available endpoints in v2.

        Returns:
            list: A list of available endpoints.
        """
        response = requests.get(f"{self.base_url}index.json")
        response.raise_for_status()
        return response.json()

    def get_data_by_date(self, date):
        """
        Get sentiment analysis data for a specific date.

        Args:
            date (str): The date in the format YYYY-MM-DD.

        Returns:
            dict: A dictionary containing sentiment analysis data for the specified date.
        """
        response = requests.get(f"{self.base_url}history/{date}.json")
        response.raise_for_status()
        return response.json()
