#!/bin/bash
cd ~/neuroforge_node || exit 1
python3 ~/forge_watcher.py
python3 ~/forge_dashboard.py
