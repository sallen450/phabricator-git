# phabricator-git

Associate git commit with tasks that appear in the commit message

## Install

```shell
pip install ./
```

## Usage

```shell
pha-g
```

This command will get all commit messages between the current sha to the last version tag. Then get phabricator task_id
from commit message, like `fix(T123): some desc`, and associate the phabricator task with this commit sha.

## Reference

* https://secure.phabricator.com/book/phabricator/article/conduit_edit/
* https://secure.phabricator.com/conduit/
* https://github.com/disqus/python-phabricator
* https://gitpython.readthedocs.io/en/stable/index.html