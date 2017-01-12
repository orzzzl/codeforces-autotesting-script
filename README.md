# codeforces-autotesting-script
A script which can get sample case and do auto-testing for each problem.

##How to use it??

1. edit the config file with the link to the contest your are parsing.
2. run
<pre>
python init.py
</pre>
-- this will automatically download all the sample input and output.
3. write your solution for the problems, but notice that you have to name "a.cpp" for problem A, and "b.cpp" for problem B, and so on.
4. run 
<pre>
./test.sh a
</pre>
This will automatically compile a.cpp and run tests for the code you wrote. The same case for Problem B, C, etc.
5. After the contest is over, you can run 
<pre>
python end.py
</pre>
to delete all the inputs and outputs which have been downloaded.
