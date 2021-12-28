from setuptools import find_packages, setup
from core import __version__


setup(name="datalib",
      keywords="datalib",
      packages=find_packages(include=["core", "core.*"]),
      install_requires=["psycopg2-binary==2.9.1", "pandas","SQLAlchemy","loguru","typer","typer-cli"],
      version=__version__,
      description="A data utility",
      author="Aritra Biswas",
      author_email='pandalearnstocode@gmail.com',
      platforms=["any"],
      license="BSD",
      url="http://github.com/pandalearnstocode/datalib"
)
