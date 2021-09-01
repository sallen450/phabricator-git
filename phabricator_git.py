import os

import click

from app import phab
from app.project import ScmGit


# update task from shas between current to last version tag
@click.command()
def main():
    project = ScmGit(path=os.getcwd())
    tag = project.get_tag_from_package_json()

    if tag == '':
        return

    latest_tag_commit = project.get_sha_from_tag(tag)

    for c in project.repo.iter_commits():
        if c.hexsha == latest_tag_commit.hexsha:
            break

        phab.update_if_has_task(c.message, c.hexsha)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
