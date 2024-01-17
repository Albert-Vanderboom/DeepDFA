conda activate deepdfa

rootdir="$PWD"
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
export PYTHONPATH="$rootdir:$PYTHONPATH"
export PATH="$rootdir/storage/external/joern/joern-cli:$PATH"

export JAVA_HOME="/usr/lib/jvm/jdk-19.0.1"
export PATH="$JAVA_HOME/bin:$PATH"