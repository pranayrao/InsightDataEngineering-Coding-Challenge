#Insight Data Engineering - Coding Challenge

#Challenge Summary
Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

I have used Python 2.7.11 for the solution to this challenge. List and Dictionaries are the data structures of choice. User defined functions have been employed

#Additional Packages Required

Please install the following:

networkx 1.10

you can use 'pip install networkx'

numpy 1.10.1

you can use 'pip install numpy'

#Other Modules/ Libraries

sys

json

itertools

datetime

decimal

time


#Steps to run the code:

1) Place the tweets.txt file in the tweet_input folder. Note that the tweets.txt file should contain a single tweet on each line.

2) Ensure that average_degree.py is present in the src folder

2) Open a LINUX terminal and type the following command in the home directory directory and press enter:

./run.sh

3) The output will be written to tweet_output/output.txt

#Implementation Summary:

The Python code does the following:

1) Reads the input file line by line

2) Calls a function is made that converts each line passed as an argument to it into a JSON object and returns the created_at and hashtags fields

3) Creates a data dictionary with the timestamp as keys and hashtags as a list for values

4) Appends the hashtags contained in the new tweet to an edge list and this edge list is also maintained with the help of another function that
   ensures that any edges formed by a tweet that is behind the max processed timestamp by 60 seconds or more is removed from the edgelist
   
5) Updates the data dictionary created earlier as it maintains the 60 second window

6) Passes this updated edge list as an argument to a function that generates combinations of edges formed by hashtags present in the hashtag list in each tweet. The resulting list of tuples are then added as edges to the graph and the degree of each node is calculated using the methods available in the networkx module. The average_degree is returned by this function which is written to the output file.


#Testing:

1) The test case descriptions are present in :

insight_testsuite/tests/test_1/

insight_testsuite/tests/test_2/

2) The test input files are present in :

insight_testsuite/tests/test_1/tweet_input

insight_testsuite/tests/test_2/tweet_input

insight_testsuite/tests/test-2-tweets-all-distinct/tweet_input


3) Download the expected_output.txt files and store them in the respective tweet_output folder corresponding to the test (test_1 , test_2 etc.)

4) Run the following commands in a terminal:

./insight_testsuite/run_mytests.sh


5) The test output files will be written to :

insight_testsuite/tests/test_1/tweet_output

insight_testsuite/tests/test_2/tweet_output

insight_testsuite/tests/test-2-tweets-all-distinct/tweet_output
