import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

### Apps Definition ###
app_package = 'geoids_traveltimepolygons'
release_package = 'tethysapp-' + app_package
app_class = 'geoids_traveltimepolygons.app:GeoidsTraveltimepolygons'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='',
    description='This app shows the distance that can be travelled within a certain amount of time, as well as the population that lives within the area.',
    long_description='',
    keywords='',
    author='Joseph Browning, Luke Newey, and Tyler Mickelson',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
