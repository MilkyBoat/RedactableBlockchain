#!/bin/bash

# 进入当前脚本目录
cd $(dirname $0)

# 如果没有eth数据库则通过创世区块初始化区块链
if [ ! -d "../RDBlockchain" ]; then
  bash chainInit.sh
fi

# 新终端中启动节点1
gnome-terminal -x bash -c "bash node1.sh;exec bash;"

# 新终端中启动节点2
gnome-terminal -x bash -c "bash node2.sh;exec bash;"
