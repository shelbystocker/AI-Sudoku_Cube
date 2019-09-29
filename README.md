# AI-Sudoku_Cube
CS 463, Fall 2019, Program 1

Consider the Sudoku Cube. (Links to an external site.)  (Links to an external site.You will, in the next assignment, be asked to program a particular style of solver (A*) for it. For this assignment, you have some programming and some problem solving.

 

Programming

Design and implement data structures for the puzzle itself, produce some (possibly crude) GUI for sanity checks, and write a program to randomize the puzzle.

The GUI could be very simple, perhaps with the cube unfolded into a cross, indicating which numerical value is where. Plain text is fine.  (It might be helpful to indicate the orientation of the number, perhaps with one of ^, >, <, v.)  If you use someone else's code (just for the GUI---the rest must be your own code!), CITE YOUR SOURCE: Name, if it's from someone you know, else URL, author, title of link, and dates posted (if known) and read, if found online.

The randomizer function should take as input the number of moves. To make a move, you should specify the face that is rotated and the direction of rotation.

Note that there are solvers available online, like this one (Links to an external site.).  You will be implementing a different algorithm than this.

Problem Solving

Come up with at least one heuristic for the puzzle, and explain both the heuristic and why you believe that that heuristic is ​admissible (Links to an external site.)​. ​A heuristic, in this context, is NOT an algorithm.​ It is an approximation of the number of steps to the solved state.  An admissible heuristic is guaranteed to not be greater than the actual number of steps.   Read the book, about and before the discussion of the A* algorithm. If you don't have the book then read about the A* algorithm somewhere else.

 

To hand in:

A description in English of your data structure;
Code for the data structures, along with instructions on how to run it;

An example of the GUI output;

A description of the randomizer;

Code for the randomizer, along with instructions on how to run it;

Your heuristic, clearly described and justified, including an argument that it is admissible;

A statement of what you learned from this assignment.
