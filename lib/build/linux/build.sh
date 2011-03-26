#!/bin/bash
PYVER=$1
if [ -z "$PYVER" ]; then
  PYMAJ=`python -c "import platform; print(platform.python_version_tuple()[0])"`
  PYMIN=`python -c "import platform; print(platform.python_version_tuple()[1])"`
  PYVER="${PYMAJ}.${PYMIN}"
fi

#SITEPACKAGES=`python${PYVER} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`

make clean

numpyIncludeDirectory=/usr/lib/python${PYVER}/site-packages/numpy/core/include/
if [ ! -d "$numpyIncludeDirectory" ]; then
    numpyIncludeDirectory=/usr/local/lib/python${PYVER}/site-packages/numpy/core/include/
fi

make FLAGS="-I/usr/include/python${PYVER} -I$numpyIncludeDirectory"
if [ $? -eq 0 ] ; then
  mkdir ./py${PYVER}
  cp libmedussa.so ./py${PYVER}
  make clean
else
  echo "Nope!"
fi
