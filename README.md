# LearnSystemWithPython
Simple examples of operating system, distributed system and database system concepts in python

## Two Phase Commit

Demonstration of how two phase commit protocol works in distributed system: TwoPhaseCommit.py

## Multiversion Concurrency Control （MVCC）

MVCC.py

Read only scan on the list is lockless. It use the timestamp to read the latest version.

Other operations acquire lock. Write operations perform Copy-on-Write.

## Journaling File System and CopyOnWrite File System

Oversimplified examples of the common appoaches to solve crash-consistency problem

Journaling a.k.a Write Ahead Logging (WAL) : JournalingFileSystem.py

CopyOnWrite (COW) : CopyOnWriteFileSystem.py

## Monitor and Semaphore Usage

Using monitor and semaphore to solve Bounded Buffer problem, Dining Philosopher problem and ReaderWriter problem

BoundedBufferMonitorSolution.py

BoundedBufferSemaphoreSolution.py

DiningPhilosophersMonitorSolution.py

DiningPhilosophersSemaphoreSolution.py

ReaderWriterSemaphoreSolution.py

## Inter Process Communication 

Using pipe, messagePassing and shared Memory are three common approaches of interprocess communication

pipeIPC.py

messagePassingIPC.py

sharedMemoryIPC.py




