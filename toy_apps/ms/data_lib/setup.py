from setuptools import find_packages, setup


setup(name="datalib",
      keywords="datalib",
      packages=find_packages(),
      install_requires=["psycopg2-binary==2.9.1", "pandas","SQLAlchemy","loguru","typer","typer-cli"],
      version="0.0.1",
      description="A data utility",
      author="Aritra Biswas",
      author_email='pandalearnstocode@gmail.com',
      platforms=["any"],
      license="BSD",
      py_modules=["datalib"],
      package_dir={'':'quicksample/src'},
      url="http://github.com/pandalearnstocode/datalib"
)
