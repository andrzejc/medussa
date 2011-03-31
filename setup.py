# -*- coding: utf-8 -*-
from distutils.core import setup
import platform
from distutils.sysconfig import get_python_lib
import os

pyver = "%s.%s" % (platform.python_version_tuple()[0], platform.python_version_tuple()[1])
import shutil
shutil.copy(os.path.join('src','docs.py'), '.')
import docs
os.remove('docs.py')
if os.path.isfile('docs.pyc'):
    os.remove('docs.pyc')
medussa_package = [docs.package_name]
medussa_package_dir = 'src'
medussa_package_data = ['*.py']
medussa_data_files = []
medussa_data_files_path = ''
medussa_requires = ['numpy (>=1.2)',]

if platform.system() == "Windows":
	medussa_data_files.append('lib/build/win/py%s/medussa.dll' % pyver)
	medussa_data_files.append('lib/build/win/portaudio_x86.dll')
	medussa_data_files.append('lib/build/win/libsndfile-1.dll')
	medussa_data_files_path = os.path.join(get_python_lib(prefix=''), 'medussa')
else:
	medussa_data_files.append('lib/build/linux/py%s/libmedussa.so' % pyver)
	medussa_data_files_path = os.path.join(get_python_lib(prefix='/usr/local'), 'medussa')

#TODO: Pull version, author, etc., from imported medussa
setup(name=docs.package_name,
	version=docs.version,
	description=docs.short_description,
	author=docs.author,
	author_email=docs.author_email,
	maintainer = docs.maintainer,
	maintainer_email = docs.maintainer_email,
	url=docs.url,
	packages = medussa_package,
	requires = medussa_requires,
	package_dir={docs.package_name: medussa_package_dir},
	package_data={docs.package_name: medussa_package_data},
	data_files=[(medussa_data_files_path, medussa_data_files)],
	keywords = docs.keywords,
	license = docs.license,
	platforms = docs.platforms,
	long_description = "%s%s" % (docs.long_description, docs.url),
	classifiers=[
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python",
		"Operating System :: Microsoft :: Windows",
		"Operating System :: POSIX",
		#"Operating System :: MacOS :: MacOS X",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3.1",
		"Programming Language :: Python :: 3.2",
		"Environment :: Console",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"Topic :: Multimedia :: Sound/Audio",
		"Topic :: Scientific/Engineering",
	],
)
