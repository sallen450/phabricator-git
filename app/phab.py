import re

import click
from phabricator import Phabricator

phab = Phabricator()  # This will use your ~/.arcrc file
phab.update_interfaces()


# get phid by git commit sha
def get_phid_from_git_sha(sha):
    r = phab.phid.lookup(names=[sha])

    if len(r) == 0:
        return ''

    phid = r[sha]["phid"]
    return phid


# update some task if it associates this git commit sha
def update_if_has_task(git_message, git_sha):
    # find all task_id in commit message
    pattern = re.compile(r"\(T(\d+)\)")
    task_ids = pattern.findall(git_message)
    task_ids = map(int, task_ids)

    click.echo("sha: {sha}".format(sha=git_sha))

    # associate commit sha with task
    for task_id in task_ids:
        phid = get_phid_from_git_sha(git_sha)

        if phid == '':
            continue

        transaction = [{
            "type": "commits.add",
            "value": [phid],
        }]
        click.echo("Associate task T{task_id} with {sha}".format(task_id=task_id, sha=git_sha))
        phab.maniphest.edit(objectIdentifier=task_id, transactions=transaction)
