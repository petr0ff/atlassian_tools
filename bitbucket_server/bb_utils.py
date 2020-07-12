from commons import utils

import stashy

bitbucket = stashy.connect(utils.BASE_BITBUCKET_URL, utils.LOGIN, utils.PASSWORD)


def get_repos(project=utils.BITBUCKET_PROJECT):
    print(bitbucket.projects.list())
    repos = bitbucket.projects[project].repos.list()
    print(repos)
    return repos
