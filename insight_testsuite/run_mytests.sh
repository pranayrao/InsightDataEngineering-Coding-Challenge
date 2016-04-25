python ./src/average_degree.py './testsuite/tests/test_1/tweet_input/tweets.txt' './testsuite/tests/test_1/tweet_output/output.txt'
python ./src/average_degree.py './testsuite/tests/test_2/tweet_input/tweets.txt' './testsuite/tests/test_2/tweet_output/output.txt'
python ./src/average_degree.py './testsuite/tests/test-2-tweets-all-distinct/tweet_input/tweets.txt' './testsuite/tests/test-2-tweets-all-distinct/tweet_output/output.txt'

cmp testsuite/tests/test_1/tweet_output/output.txt testsuite/tests/test_1/tweet_output/expected_output.txt && echo "The actual output matches the expected output for test_1" || echo "The actual output does not match the expected output for test_1" 
cmp testsuite/tests/test_2/tweet_output/output.txt testsuite/tests/test_2/tweet_output/expected_output.txt && echo "The actual output matches the expected output for test_2" || echo "The actual output does not match the expected output for test_2"
cmp testsuite/tests/test-2-tweets-all-distinct/tweet_output/output.txt testsuite/tests/test-2-tweets-all-distinct/tweet_output/expected_output.txt && echo "The actual output matches the expected output for test-2-tweets-all-distinct" || echo "The actual output does not match the expected output for test-2-tweets-all-distinct" 
