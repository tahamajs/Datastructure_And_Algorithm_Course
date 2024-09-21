
# Data Structure and Algorithm Course 

This repository contains lecture notes, homework assignments, and additional resources for the **Data Structures and Algorithms** course at the University of Tehran (1402 Fall Semester).

## Repository Structure

- **CAc/**: Contains class assignments (CA) that include a variety of problems on data structures such as arrays, graphs, stacks, queues, and more. Each CA is labeled with a corresponding number, for example, `CA1`, `CA2`, etc.
- **Extra/**: Additional resources, practice problems, or reference material not covered in the regular assignments or lecture notes.
- **HWs/**: Homework assignments provided throughout the semester. These assignments focus on the practical implementation of various data structures like linked lists, trees, heaps, graphs, and more.
- **Notes/**: Lecture notes and theoretical explanations on topics covered in the course. Topics include stacks, queues, trees, graphs, sorting algorithms, and time complexity analysis.
- **Slides/**: Slides from the lectures that cover key concepts and examples related to data structures and algorithms.
- **ref/**: Reference materials that can include textbooks, research papers, and links to online documentation that were used or recommended during the course.

## Getting Started

To get started with the course materials:

1. Navigate to the appropriate folder for the assignment or topic you're interested in.
2. Review the lecture notes and slides to understand the theoretical concepts.
3. Work on the assignments in the **CAc/** or **HWs/** folder and practice using the examples provided.
4. Refer to **ref/** for additional reading or to clarify difficult concepts.

---

# CAs:

The **CAs** (Class Assignments) are sets of practical problems designed to test and enhance students' understanding of various data structure concepts covered in the course. Here's a breakdown of the CAs based on the files you uploaded:

### **CA1: Data Structures Basics & String Manipulation**

This assignment focuses on problems involving basic data structures such as arrays and string manipulation. The challenges often require implementing efficient algorithms to manipulate and process data in various forms. Example problems include:

- **Palindrome Detection**: Implement algorithms to identify substrings that form palindromes.
- **AM/PM Time Manipulation**: A problem that deals with converting and manipulating time in 12-hour format.
- **Array Input/Output Operations**: Basic operations on arrays, such as retrieving, inserting, or reversing data in an array.

Key skills tested:

- String manipulation techniques.
- Array traversal and modification.
- Basic problem-solving using loops and conditionals.

### **CA2: Linked Lists, Queues, and Stacks**

In this CA, you are tasked with implementing core data structures from scratch, such as:

- **Queues**: Creating a queue with functions like `enqueue`, `dequeue`, and checking if it's empty.
- **Stacks**: Implementing stacks with standard operations such as `push`, `pop`, and `peek`.
- **Linked Lists**: Inserting elements at both the front and end, as well as reversing a linked list.

This CA is essential for understanding how to work with dynamic data structures where elements are connected via pointers or references, and it provides an opportunity to implement abstract data types (ADTs) from the ground up.

Key skills tested:

- Understanding of dynamic memory allocation.
- Manipulating pointers/references.
- Implementing stack, queue, and linked list data structures.

### **CA3: Min-Heap, Huffman Tree, and Binary Search Trees (BST)**

This CA focuses on more advanced data structures such as:

- **Min-Heap**: You are required to implement heap operations like inserting an element and maintaining the heap property.
- **Huffman Tree**: A tree structure used in compression algorithms, where you implement tree-building and encoding operations.
- **Binary Search Trees**: Implementing BST operations like insertion and inorder traversal.

These problems are designed to give students a deeper understanding of tree structures and their applications in searching, sorting, and compression algorithms.

Key skills tested:

- Recursive tree traversal techniques.
- Binary heap operations for priority queues.
- Constructing and using Huffman trees for efficient encoding.

### **CA4: Graph Theory and Special Algorithms**

This assignment involves more complex problems, primarily focusing on graph algorithms and special cases:

- **Graph Coloring / Bipartitioning**: A problem where you have to split nodes into two teams while avoiding certain conflicts (edges in the graph representing "enemies").
- **Tree Traversal and Manipulation**: Several problems are based on trees where you must traverse or manipulate nodes under specific constraints.
- **Advanced Sorting and Rearranging**: Some problems focus on rearranging elements (like a bookshelf of dictionaries) using unconventional methods (like reversing subarrays).

These problems are aimed at developing your skills in graph theory, including understanding graph traversal (BFS, DFS), as well as learning advanced sorting and optimization techniques.

Key skills tested:

- Understanding graph representations (adjacency list/matrix).
- Traversal techniques like DFS and BFS.
- Tree operations and pathfinding.


---

# HWs:

### **HW1: Recursive Algorithms and Time Complexity Analysis**

This assignment introduces problems focused on understanding the time complexity of recursive algorithms and basic problem-solving with recursive functions. The problems involve:

- **Time Complexity Analysis**: Calculating time complexity for different recursive relations.
- **Proof and Disproof**: Addressing questions on Big-O notation.
- **Recursive Function Solutions**: Solving given recursive functions and calculating their time complexity.
- **Algorithm Design**: Designing algorithms with time complexities like O(n) and solving sum-related problems.

Key skills tested:

- Understanding of recursion.
- Time complexity analysis of algorithms.

---

### **HW2: Stack, Queue, and Linked List Operations**

This assignment focuses on implementing data structures such as stacks, queues, and linked lists. Some tasks include:

- **Min Stack**: Implementing a version of the stack that supports push, pop, and retrieving the minimum element in constant time.
- **Multi-stack with Fixed Array**: Managing multiple stacks in a fixed array while maintaining efficient time complexity.
- **Depth-First Search (DFS)**: Implementing DFS on a multi-level linked list and converting it to a flat structure.

Key skills tested:

- Working with dynamic memory.
- Linked list traversal and manipulation.
- Efficient data structure implementation using limited memory.

---

### **HW3: Trees and Binary Search Trees (BST)**

In this CA, you work with tree data structures such as AVL trees, Huffman trees, Red-Black trees, and B-trees. The tasks include:

- **AVL Trees**: Understanding AVL tree operations and proving properties related to height and rotation balance.
- **Huffman Trees**: Constructing Huffman trees based on character frequencies and understanding its application in data compression.
- **Red-Black Trees**: Inserting nodes into Red-Black trees and proving height and balancing properties.

Key skills tested:

- Tree traversal algorithms.
- Balanced tree operations.
- Understanding self-balancing trees.

---

### **HW4: Graph Theory and Special Algorithms**

This assignment focuses on graph theory problems and graph traversal algorithms. Some of the problems include:

- **BFS and DFS Traversal**: Implementing and analyzing both BFS and DFS, marking specific edges like back-edges and cross-edges.
- **Graph Bipartitioning**: Solving problems based on bipartite graphs and connectivity.
- **Maze and Pathfinding**: Algorithms for navigating through a maze and identifying possible escape routes.

Key skills tested:

- Graph traversal techniques.
- Graph partitioning algorithms.
- Pathfinding and shortest path problems.

---

### **HW5: Hashing and Sorting Algorithms**

This CA delves into advanced sorting algorithms and hashing techniques, including:

- **Designing O(n) Sorting Algorithms**: Creating an efficient sorting algorithm where each element satisfies specific constraints.
- **Advanced Hashing Techniques**: Improving the efficiency of hash table operations like search, insert, and delete.
- **QuickSort Optimization**: Implementing an optimized version of QuickSort using tail recursion.

Key skills tested:

- Sorting large datasets.
- Hash table implementation and optimization.
- Efficient recursive algorithms.

---

### **HW6: Amortized Analysis and Aggregate Methods**

In this CA, the focus shifts to amortized analysis and aggregate methods for analyzing the performance of algorithms over time. Problems include:

- **Stack Operations**: Performing operations on a k-sized stack, ensuring that no more than k elements are ever copied.
- **Amortized Cost Analysis**: Using amortized techniques to calculate the cost of operations such as incrementing a counter or performing deletions in a dynamic array.
- **Aggregate Analysis of Data Structures**: Applying aggregate methods to calculate the total cost of operations over a sequence.

Key skills tested:

- Amortized cost analysis.
- Aggregate method applications.
- Efficient implementation of dynamic data structures.

---

This summary provides an ordered overview of the assignments, with each focusing on critical concepts within data structures and algorithms. Let me know if you'd like to explore or modify any specific assignment in more detail!

## Running Code (for practical implementations)

Some of the assignments and practice problems may require Python or C++ for implementation. Below is a simple guide on how to run Python programs:

1. Make sure you have Python 3 installed. You can download it from [here](https://www.python.org/).
2. Navigate to the directory containing the code using a terminal.
3. Run the program using:
   ```
   python3 your_script.py
   ```
4. Follow the instructions in the program or solve the given problems.

## Contributing

This repository is primarily for use in the course. However, if you'd like to contribute:

1. Fork the repository.
2. Make your changes (bug fixes, additional material, etc.).
3. Submit a pull request with a description of the changes made.

## License

This repository is for educational purposes only.

---
