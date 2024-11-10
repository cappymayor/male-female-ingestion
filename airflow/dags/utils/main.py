import logging

import pandas as pd
import requests


def fetch_users(total_users):
    """
    This function fetches a specified number of user profiles from an API,
    splits them into separate male and female profiles.

    Args:
        total_users: The total number of user profiles to retrieve.

    Returns:
        pd.DataFrame: DataFrame containing detailed user profile data,
        male and female profiles

    Note:
        - The API request is limited to 5000 profiles per call,
        and multiple requests are made if needed to reach total_users.
    """
    max_users_per_request = 5000
    all_users = []
    num_full_requests = total_users // max_users_per_request
    remainder = total_users % max_users_per_request
    url = "https://randomuser.me/api/"

    logging.info("Starting to fetch user profiles...")

    try:
        for _ in range(num_full_requests):
            response = requests.get(f"{url}?results={max_users_per_request}")
            response.raise_for_status()
            all_users.extend(response.json()['results'])
            logging.info(f"Fetched {max_users_per_request} profiles.")

        if remainder > 0:
            response = requests.get(f"{url}?results={remainder}")
            response.raise_for_status()
            all_users.extend(response.json()['results'])
            logging.info(f"Fetched remainder {remainder} profiles.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching user profiles: {e}")

    df = pd.json_normalize(all_users)
    return df
