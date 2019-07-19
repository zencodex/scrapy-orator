import os
import yaml
from orator import DatabaseManager, Model
from pathlib import Path

__config = str(Path(os.path.realpath(__file__)).parents[1]) + '/orator.yml'
db = DatabaseManager(yaml.load(open(__config))['databases'])

Model.set_connection_resolver(db)
