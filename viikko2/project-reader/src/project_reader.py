from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        x = toml.loads(content)
        name = x["tool"]["poetry"]["name"]
        tdes = x["tool"]["poetry"]["description"]
        dep = x["tool"]["poetry"]["dependencies"].keys()
        dev_dep = x["tool"]["poetry"]["dev-dependencies"].keys()
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, tdes, dep, dev_dep)
