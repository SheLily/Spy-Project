import time
import tqdm
import vk_spy
import file_ops
from settings import User, Token, V, Request_time


def main():
    user = vk_spy.get_id_by_name()

    usr_groups = vk_spy.get_groups(user)

    set_usr_group = vk_spy.get_groups_set(usr_groups)

    usr_friends = vk_spy.get_friends(user)

    pbar = tqdm.tqdm(usr_friends)
    for i in pbar:
        start = time.time()
        frnd_groups = vk_spy.get_groups(i['id'])

        if frnd_groups:
            set_usr_group -= vk_spy.get_groups_set(frnd_groups[:1000])
        sleep_time = Request_time - (time.time() - start)
        if sleep_time > 0:
            time.sleep(sleep_time)

    usr_groups = [i for i in usr_groups if i['id'] in set_usr_group]
    for i in usr_groups:
        if 'members_count' not in i:
            i['members_count'] = 0
    usr_groups = [
            {
                'name': i['name'],
                'gid': i['id'],
                'members_count': i['members_count']}
            for i in usr_groups
        ]

    file_ops.save_results(usr_groups, 'groups.json')


if __name__ == '__main__':
    main()
