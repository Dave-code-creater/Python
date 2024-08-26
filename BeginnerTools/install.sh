#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        ./installation/linux.sh
elif [[ "$OSTYPE" == "darwin"* ]]; then
        ./installation/mac.sh
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
elif [[ "$OSTYPE" == "win32" ]]; then
        # I'm not sure this can happen.
elif [[ "$OSTYPE" == "freebsd"* ]]; then