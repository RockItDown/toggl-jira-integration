
import requests
from base64 import b64encode


def get_from_me_api(entity: str, api_token: str, query_params: dict[str, str] = None) -> dict:
    # the official documentation states, that "<api_token>:api_token"
    # can be used with BasicAuth instead of "user:pw"
    auth_string = f"{api_token}:api_token"
    data = requests.get(
        url=f'https://api.track.toggl.com/api/v9/me/{entity}',
        params=query_params,
        headers={
            'content-type': 'application/json',
            'Authorization': 'Basic %s' % b64encode(auth_string.encode("utf-8")).decode("ascii")})
    return data.json()


def get_projects(api_token) -> dict:
    return get_from_me_api("projects", api_token)


def get_time_entries(api_token, start_date, end_date) -> dict:
    query_params = {"start_date": str(start_date),
                    "end_date": str(end_date)}
    return get_from_me_api("time_entries", api_token, query_params)
