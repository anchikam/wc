Insight Data Engineering - Coding Challenge
===========================================================

One of the first problems you’ll encounter in data engineering is Word Count, which takes in a text file or set of text files from a directory and outputs the number of occurrences for each word.  For example, Word Count on a file containing the following passage:

> So call a big meeting,  
Get everyone out out,  
Make every Who holler,  
Make every Who shout shout.  

would return:

	a			1
	big			1  
	call		1  
	every		2  
	everyone	1  
	get			1  
	holler		1  
	make		2  
	meeting		1  
	out			2  
	shout		2  
	so			1  
	who			2  

The first part of the coding challenge is to implement your own version of Word Count that counts all the words from the text files contained in a directory named `wc_input` and outputs the counts (in alphabetical order) to a file named `wc_result.txt`, which is placed in a directory named `wc_output`.

Another common problem is the Running Median - which keeps track of the median for a stream of numbers, updating the median for each new number.  The second part of the coding challenge is to implement a running median for the number of words per line of text.  Consider each line in a text file as a new stream of words, and find the median number of words per line, up to that point (i.e. the median for that line and all the previous lines).  For example, the first line of the passage

> So call a big meeting,  
Get everyone out out,  
Make every Who holler,  
Make every Who shout shout.  

has 5 words so the running median for the first line is simply 5.  Since the second line has 4 words, the running median for the first two lines is the median of {4, 5} = 4.5 (since the median of an even set of numbers is defined as the mean of the middle two elements after sorting).  After three lines, the running median would be the median of {4, 4, 5} = 4, and after all four lines the running median is the median of {4, 4, 5, 5} = 4.5.  Thus, the correct output for the running median program for the above passage is:

	5.0  
	4.5  
	4.0  
	4.5  

We'd like you to implement your own version of this running median that calculates the median number of words per line, for each line of the text files in the `wc_input` directory.  If there are multiple files in that directory, the files should be combined into a single stream and processed by your running median program in alphabetical order, so a file named `hello.txt` should be processed before a file named `world.txt`.  The resulting running median for each line should then be outputted to a text file named `med_result.txt` in the `wc_output` directory.

You may write your solution in any one of the following programming languages: C, C++, Clojure, Java, Python, Ruby, or Scala - then submit a link to a Github repo with your source code.  In addition to the source code, the top-most directory of your repo must include `wc_input` and `wc_output` directories, and a shell script named `run.sh` that compiles and runs the Word Count and Running Median programs.  If your solution requires additional libraries or dependencies, the shell script should load them first so that your programs can be run on any system just by running `run.sh`.  See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

![Example Repo Structure](images/directory-pic.png)

As a data engineer, it’s important that you write clean, well-documented code that scales for large amounts of data.  For this reason, it’s important to ensure that your solution works well for small and large text files, rather than just the simple examples above.  For example, your solution should be able to process large files like the text of the book "War and Peace" without taking much longer than processing the small files.


## FAQ

Here are some common questions we've received.  If you have additional questions, feel free fork this repo, add them to the README.md, then issue a pull request.  Alternatively, you can email info@insightdataengineering.com and we'll add the answers.

* *Which Github link should I submit?*  
You should submit the URL for the top-level root of your repository.  For example, this repo would be submitted by copying the URL `https://github.com/InsightDataScience/cc-example` into the appropriate field on the application.  Please do NOT try to submit your coding challenge using a pull request, which will make your source code publicly available.  

* *Do I need to account for punctuation in the word count?*  
Yes, punctuation should be removed so `shout` and `shout.` should both be counted together.

* *Should I count capitalization differently in the word count?*  
No, both `Who` and `who` should be counted together.  For simplicity, the word count should return an alphabetical list of lowercase words (e.g. `who	2`).

* *What should the format of the word count be?*  
Please try to match the above example, by listing the words in **alphabetical** order, with a tab between the word and count, and each word separated by a newline.

* *How should hyphens be handled?*  
For simplicity, please remove hyphens so that `hi-lite` is counted as `hilite`.

* *Should words that are split onto two lines using hyphenation be counted as one word (or two separate words) for the word-counting program?*  
For simplicity, you may assume that all text files do not have any hyphens for splitting words across two different lines.  

* *How should conjunctions like `we're` or `haven't` be handled?*  
For simplicity, please remove apostrophes so that `we're` and `haven't` are counted as `were` and `havent`.

* *Do I need to account for digits (e.g 0-9)?*  
No, for simplicity you may assume that the text files do not contain any digits.  

* *Do I need to account for complicated Unicode characters?*  
No, you may assume that all of the characters are conventional, ASCII characters.

* *Should I check if the files in the input directory are text files or non text files(binary)?*
No, for simplicity you may assume that all of the files in the input directory are standard text files.  

* *Will our program need to look for text files in any subdirectories of the `wc_input` directory?*  
No, for simplicity you may assume that the `wc_input` directory only contains text files, with no subdirectories.  

* *What if I need to load a library or dependency for my program to run?*  
Make sure that your `run.sh` script loads all the dependencies for your program.  These dependencies should also be well documented in your Markdown README.

* *Do I need separate programs for WordCount and Running Median?*  
No, you may use a single combined program or several programs, as long as they are all executed by the `run.sh` script.

* *Does the `run.sh` script need to be a Bash script (i.e. on Linux or Mac OSX)?*  
Yes - Unix based systems like Linux and MacOSX are the standard in the field of Data Engineering - and the system needs to be compiled and tested on a Unix based system.  With that said, you can use emulators like [Cygwin](https://www.cygwin.com/) if you only have access to a Windows system.

* *Can I use an IDE like Eclipse to write my program?*  
Yes, you can use what ever tools you want -  as long as your `run.sh` script correctly runs the relevant target files and creates the `wc_result.txt` and `med_result.txt` files in the `wc_output` directory.

* *What should be in the `wc_input` directory?*  
You can put any text file you want in the directory.  In fact, this could be quite helpful for testing your solutions.

* *What should the output of the running median be?*  
For simplicity, please output the running median as a double with only 1 digit after the decimal (i.e. 2.0 instead of 2).  In the event that you need to round, simply truncate the answer (i.e. 2/3 should be 0.6).  The running median for each line of text should be separated by newlines as shown in the example above.

* *How should blank lines be handled in the running median?*  
Blank lines should be considered as lines with 0 words, so the runnning set for

> Hello world  
> 		  
> Brave new world  

should be {2, 0, 3} with a corresponding result of

	2  
	1  
	2

* *How does the running median work for multiple files?*  
All of the files should be processed as if they come from a single stream, ordered in alphabetical order as given by the ASCII code.  For example, if you had a file name `a.txt` with the following lines

> Hello world  
Hello brave new world

and another file named `b.txt` with the following

> Foo  
Bar

then the running median should process `a.txt` first, then `b.txt`.  As each line is read the running set will be

	{2}  
	{2, 4}  
	{1, 2, 4}  
	{1, 1, 2, 4}

to give a resulting running median of

	2.0
	3.0
	2.0  
	1.5  

This would continue in alphabetical order until the all the files in `wc_input` have been processed.  For simiplicity, you may assume that all the text files are lowercase.

* *Do I need to use MapReduce or Hadoop?*  
No, while you should make sure the algorithms you use scale for larger text files, you do not need to use Hadoop or the MapReduce programming paradigm.  






