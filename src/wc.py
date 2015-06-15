import sys 
import os 
import shutil
import re
import math
import collections
from heapq import heappush as push, heappop as pop


def concat_files(dir_in, to_dir):    
  """ For all files in dir_in directory, in alphabetical order, cleans from [',`,-],
  concatenates files to a temporary file concat.tex and places it inside /to_dir/Temp directory.
  Returns a link to this concatenated file. """
  temp = os.path.join(to_dir, 'Temp')
  if not os.path.exists(temp):
          os.mkdir(temp)
  concat_file_path = os.path.join(temp, 'concat.txt')
  file_list = sorted(os.listdir(dir_in), key=str.lower)
  with open(concat_file_path, 'w') as outfile:
      for file in file_list:  
        try:  
          # if file.endswith(".txt"):
              fpath = os.path.join(dir_in, file)
              with open(fpath) as infile:
                  for line in infile:
                      line = re.sub("'|`|-", '', line)
                      outfile.write(line)    
        except Exception, e:
          print "File {} has problem {}".format(file, e)                  
  return concat_file_path
  
                                                                    
def word_count(filename):
    """ Given a text file returns the word count list. """
    with open(filename) as fh:
        text = fh.read().lower()
    wordList = re.compile('\w+').findall(text)   
    counter=collections.Counter(wordList)
    return sorted(counter.items())

def write_wc(inFile, outFile):
    """ Performs word counting on an input file and saves the result into an output file.""" 
    with open(outFile, 'w') as gh:
        wc = word_count(inFile)
        for c in wc:
            gh.write(c[0]+'\t'+str(c[1])+'\n')
      

def wc_lines(filepath):
    """ Reading text file at location filepath, counts number of words on each line and returns a list.""" 
    wc_lines = []
    with open(filepath) as fh:
        text = fh.readlines()
    for line in text:
        wc_lines.append(len(re.compile('\w+').findall(line)))   
    return wc_lines 

def run_medians(numlist):
    """ Given a list of integers, returns a generator of running medians.
    The method uses 2 heaps (max heap/min heap) and places streaming numbers in either of the 
    heap depending on their values. The way median is found depends if the heaps are balanced or not. """
    itnum = iter(numlist)
    less, more = [], []   
    first = next(itnum)
    yield first
    second = next(itnum)
    push(less, - min(first, second))
    push(more, max(first, second))
    while True:
        curr = ( more[0] if len(less) < len(more)
                    else - less[0] if len(less) > len(more)
                    else (more[0] - less[0]) / 2.0 )
        yield curr
        it = next(itnum)
        if it <= curr: push(less, - it)
        else: push(more, it)
        small, big = ( (less, more) if len(less) <= len(more)
                       else (more, less) )
        if len(big) - len(small) > 1: push(small, - pop(big))


def write_rm(inFile, outFile):
    """ Takes a text file, creates a list of word counts on each line, 
    generates streaming medians and writes the result into an outFile."""
    wc_ls = wc_lines(inFile) 
    med_list = [float(it) for it in run_medians(wc_ls)]
    with open(outFile, 'w') as gh:
        for c in med_list:
            gh.write(str(math.floor(c*10)/10)+'\n')
  

def main():    
  # List of command line arguments, omitting the [0] element - script itself
  args = sys.argv[1:]  
  
  if len(args) != 2:   # we expect entry like:  [script --option PATH]
    print 'usage: python wc.py {--wcount | --rmedian | --both} [path to wc_input dir]'
    sys.exit(1)
   
  option = args[0]
  path = os.path.abspath(args[1])
  dir_in = os.path.join(path, 'wc_input')  
  to_dir = os.path.join(path, 'wc_output')  
   
  # dir_in is a path where wc_input directory is (not path to wc_input itself)
  if not os.path.exists(args[1]):
    print 'Not a valid path: ' + args[1]
    sys.exit(1)
  if not os.path.exists(dir_in):
    print 'Not a path where directory wc_input is located.'    
    sys.exit(1)
      
  # concatenate all tex files in dir_in into one concat.tex file inside to_dir/Temp directory  
  # after the execution the file will be deleted
  concat_file_path = concat_files(dir_in, to_dir)   
  
  # create to_dir directory (wc_output in this case) if it doesn't exist
  if not os.path.exists(to_dir):
          os.mkdir(to_dir)
  
  result1_path = os.path.join(to_dir, 'wc_result.txt')
  result2_path = os.path.join(to_dir, 'med_result.txt') 
  
  if option == '--wcount':     
      write_wc(concat_file_path, result1_path)
      shutil.rmtree(os.path.join(to_dir, 'Temp'))   
  elif option == '--rmedian':      
      write_rm(concat_file_path, result2_path)
      shutil.rmtree(os.path.join(to_dir, 'Temp'))      
  elif option == '--both':
      write_wc(concat_file_path, result1_path)
      write_rm(concat_file_path, result2_path)
      shutil.rmtree(os.path.join(to_dir, 'Temp'))     
  else:
      print 'unknown option {}, should be [--wcount, --rmedian, --both]'.format(option)
      sys.exit(1)



if __name__ == "__main__":
      main()


