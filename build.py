import sys
import os

cmake_cmd = "$HOME_BREW/bin/cmake"
commands = [cmake_cmd]
commands.append("..")
commands.append("-DCPU_ONLY=ON")
commands.append("-DUSE_libstdcpp=OFF")
commands.append("-DBUILD_python=ON")
commands.append("-DBUILD_matlab=ON")
commands.append("-DUSE_HDF5=ON")

#commands.append("-DBoost_INCLUDE_DIR=/usr/local/brew/Cellar/boost/1.67.0_1/include")
commands.append("-DGFLAGS_INCLUDE_DIR=/usr/local/brew/Cellar/gflags/2.2.1/include")
commands.append("-DGFLAGS_LIBRARY=/usr/local/brew/Cellar/gflags/2.2.1/lib/libgflags.dylib")
commands.append("-DGLOG_INCLUDE_DIR=/usr/local/brew/Cellar/glog/0.3.5_3/include")
commands.append("-DGLOG_LIBRARY=/usr/local/brew/Cellar/glog/0.3.5_3/lib/libglog.dylib")
commands.append("-DProtobuf_LIBRARIES=/usr/local/brew/opt/protobuf/lib/libprotobuf.dylib")
commands.append("-DProtobuf_INCLUDE_DIR=/usr/local/brew/opt/protobuf/include")
commands.append("-DLMDB_INCLUDE_DIR=/usr/local/brew/Cellar/lmdb/0.9.22/include")
commands.append("-DLMDB_LIBRARIES=/usr/local/brew/Cellar/lmdb/0.9.22/lib/liblmdb.dylib")
commands.append("-DLevelDB_INCLUDE=/usr/local/brew/Cellar/leveldb/1.20_2/include")
commands.append("-DLevelDB_LIBRARY=/usr/local/brew/Cellar/leveldb/1.20_2/lib/libleveldb.dylib")
commands.append("-DSnappy_INCLUDE_DIR=/usr/local/brew/Cellar/snappy/1.1.7_1/include")
commands.append("-DSnappy_LIBRARIES=/usr/local/brew/Cellar/snappy/1.1.7_1/lib/libsnappy.dylib")

#commands.append('-G"Xcode"')
  
cmdline = " ".join(commands)
print(cmdline)
os.chdir("build")
os.remove("CMakeCache.txt")
os.system(cmdline)

#buildcmd = cmake_cmd + " --build . --config Release -- -j4"
#print(buildcmd)
#os.system(buildcmd)
