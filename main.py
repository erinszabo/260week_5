"""
Chapter 6 in Runestone Exercises:
2, 3 - Do the recursive search without slicing. 5, 6, 7, 15, 16
"""


if __name__ == '__main__':
    print("")
    print("")
    print("2) Use the binary search functions given in the text (recursive and iterative). Generate a random, "
          "ordered list of integers and do a benchmark analysis for each one. What are your results? Can you explain "
          "them?")

    print("")
    print("3) Implement the binary search using recursion without the slice operator. Recall that you will need to "
          "pass the list along with the starting and ending index values for the sublist. Generate a random, "
          "ordered list of integers and do a benchmark analysis.")

    print("")
    print("5) Implement the in method (__contains__) for the hash table Map ADT implementation.")

    print("")
    print("6) How can you delete items from a hash table that uses chaining for collision resolution? How about if "
          "open addressing is used? What are the special circumstances that must be handled? Implement the del method "
          "for the HashTable class.")

    print("")
    print("7) In the hash table map implementation, the hash table size was chosen to be 101. If the table gets full, "
          "this needs to be increased. Re-implement the put method so that the table will automatically resize itself "
          "when the loading factor reaches a predetermined value (you can decide the value based on your assessment "
          "of load versus performance).")

    print("")
    print("15) One way to improve the quick sort is to use an insertion sort on lists that have a small length (call "
          "it the “partition limit”). Why does this make sense? Re-implement the quick sort and use it to sort a "
          "random list of integers. Perform an analysis using different list sizes for the partition limit.")

    print("")
    print("16) Implement the median-of-three method for selecting a pivot value as a modification to quickSort. Run "
          "an experiment to compare the two techniques.")

    print("")
