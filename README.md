# DiemBFT V4

Platform:
For our implementation, we used pyDistAlgo version 1.1.0b15 and CPython version 3.7. The operating systems used are macOS _____ and Windows 10. This program is hosted on a laptop.


Workload generation.  describe your design for client workload generation, and mention which file(s) contain the implementation.


Timeouts.  discuss your choice of timeout formulas and timeout values for clients and servers (e.g., in function get_round_timer).


Bugs and Limitations.  a list of all known bugs in and limitations of your code.


Main files:
diembftv4\Client.da contains the code to initialize the client as well as functions which allow the client to send and receive requests to its validators.
diembftv4\Validator.da contains the code to intialize replicas as well as the corresponding code for the Main module in the DiemBFT v4 paper's pseudocode.  


Code size:
LOC for algorithm:
We estimate that _____% of this code is for the algorithm itself and _____% of this code is for other functionality interleaved with it.
LOC for other:
Total LOC:
To count the number of lines of code, we used CLOC as suggested in the assignment document.


Language feature usage:
List Comprehensions: 0
Dictionary Comprehensions: 0
Set Comprehensions: 0
Aggregations: 0
Quantifications: 5
Await Statements: 7
Receive Handlers: 7


Contributions:
Nasratullah:
Sudipto:
Stella: PaceMaker.da, LeaderElection.da, logging functionality, config functionality, README.md, Test Report.txt, User Manual.txt



