import requests
from settings import User, Token, V


BASE_PARAMS = {
        'access_token': Token,
        'v': V
    }


def get_request_params(base_params=BASE_PARAMS, **kwargs):
    base_params.update(kwargs)
    return base_params


def get_request(method, params):
    url = f'https://api.vk.com/method/{method}'
    return requests.get(url, params).json()


def get_id_by_name():
    response = get_request('users.get', get_request_params(user_ids=User))
    return response['response'][0]['id']


def get_groups(user_id):
    response = get_request(
            'groups.get',
            get_request_params(
                    user_id=int(user_id),
                    extended=1,
                    fields='members_count',
                )
            )
    if 'error' not in response:
        return response['response']['items']


def get_friends(user_id):
    response = get_request(
            'friends.get',
            get_request_params(user_id=int(user_id)),
        )
    if 'error' not in response:
        return response['response']['items']


def get_groups_set(group_list):
    return {i['id'] for i in group_list}
