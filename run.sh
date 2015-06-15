#!/usr/bin/env bash

# make wc.py file executable 
chmod a+x ./src/wc.py

# Execute my programs, the wc_input directory is searched for in the current directory, 
# wc_output directory (if it doesn't exist) will be created and [wc_result.txt, med_result.txt] files will be created inside it.

python ./src/wc.py --both ./

# usage: python wc.py {--wcount | --rmedian | --both} [path to wc_input dir]

# --wcount:   counts the word frequencies only
# --rmedian:    counts the running median only
# --both:   counts both		



