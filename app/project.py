import os
import json

from git import Repo


class ScmGit:
    def __init__(self, path):
        self.path = path
        self.repo = Repo(path)

    # get sha of the tag
    def get_sha_from_tag(self, tag):
        return self.repo.tags[tag].commit

    # get tag via package.json version field
    def get_tag_from_package_json(self):
        package_json_file = os.path.join(self.path, "package.json")
        f = open(package_json_file)
        data = json.load(f)
        f.close()
        return "v{version}".format(version=data["version"])