import tomllib
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content)
        project_data = data["project"]
        name = project_data["name"]
        description = project_data["description"]
        license = project_data["license"]
        authors = [author["name"] for author in project_data["authors"]]
        dependencies = project_data["dependencies"]
        dev_dependencies = data["dependency-groups"]["dev"]
        dependencies = [dependency.split(">=")[0] for dependency in dependencies]
        dev_dependencies = [dependency.split(">=")[0] for dependency in dev_dependencies]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
