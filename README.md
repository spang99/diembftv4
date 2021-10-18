# DiemBFT V4

Platform:
For our implementation, we used pyDistAlgo version 1.1.0b15 and CPython version 3.7. The operating systems used are macOS OS 10.14 and Windows 10. This program is hosted on a laptop.

Workload generation. Workload generation consists of a simple Workload class, contained within diembftv4/src/Client.da. The class maintains num_requests, delay, and retransmit attributes. Num_requests simply tells the client how many requests it should send over the course of its lifetime. Delay is how long it should wait between requests (only 1 pending request at a time is allowed), and retransmit is a boolean that tells the client to retransmit a request for which it has already verified committment. These 3 parameters allow us to test a variety of cases and behaviors, ranging from message loss, validator caching, and dry spells in the validator MemPools.

Timeouts. Timeout formulas were not given much attention in this implementation. It was mainly used to allow for real time debugging of the algorithm by choosing timeouts on the order of seconds. Once we move onto a real distributed network, we can adjust timeout parameters based on real-world network delay measurements.

Bugs and Limitations. Known bugs and limitations include: Clients do not verify if they receive 2f+1 replies from unique validators. If one validator sends multiple replies, the client will consider them as multiple validators having committed the request. Also, in some cases when timeouts are being tested through the faulty_leader argument in diembftv4/src/config.csv, the validators have a possibility of getting caught in an endless cycle of proposing and committing empty blocks. This has to do with a bug in how we implemented the mechanism for validators to not timeout nor propose a series of empty blocks when there are no pending requests to process.

Main files:
diembftv4\Client.da contains the code to initialize the client as well as functions which allow the client to send and receive requests to its validators.
diembftv4\Validator.da contains the code to intialize replicas as well as the corresponding code for the Main module in the DiemBFT v4 paper's pseudocode.

Code size:
LOC for algorithm: 1131
We estimate that about 80% of this code is for the algorithm itself and 20% of this code is for other functionality interleaved with it.
LOC for other: 229
Total LOC: 1360
To count the number of lines of code, we used CLOC as suggested in the assignment document.

Language feature usage:
List Comprehensions: 5
Dictionary Comprehensions: 2
Set Comprehensions: 0
Aggregations: 0
Quantifications: 5
Await Statements: 7
Receive Handlers: 7

Contributions:
Nasratullah: Validator.da, Safety.da, MemPool.da, client, config functionality, signature verification, README.md, Test Report, extended psuedocode
Sudipto: BlockTree.da, Ledger.da, signature verification, extended psuedocode
Stella: PaceMaker.da, LeaderElection.da, logging functionality, config functionality, README.md, Test Report.txt, User Manual.txt
