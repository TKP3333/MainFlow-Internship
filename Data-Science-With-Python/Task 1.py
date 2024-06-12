"""Description:
This task involves understanding the basic data
types in Python such as lists, dictionaries, and
sets.
Responsibility:
Write a Python program to create a list, a
dictionary, and a set. Perform basic operations
like adding, removing, and modifying
elements."""
# Name:- Krishna Tilwane


# 1. List
# operations

fruits_list = ["Apple", "Banana", "Orange"]
print("Original list ", fruits_list)
# Adding an element to the list
fruits_list.append("Grapes")
print("List after adding Grapes:", fruits_list)
# Removing an element from the list
fruits_list.remove("Banana")
print("List after removing Banana:", fruits_list)
# Modifying an element in the list
fruits_list[1] = "Pineapple"
print("List after modifying Orange to Pineapple:", fruits_list)

# Dictionary operations
fruit_quantities = {"Apple": 50, "Banana": 100, "Orange": 80}
print("\nOriginal dictionary of fruit quantities:", fruit_quantities)
# Adding new fruit to the dictionary
fruit_quantities["Grape"] = 40
print("Dictionary after adding Grapes:", fruit_quantities)
# Removing a key-value pair from the dictionary
del fruit_quantities["Banana"]
print("Dictionary after removing Banana:", fruit_quantities)
# Modifying a value in the dictionary
fruit_quantities["Apple"] = 60
print("after modifying quantity of Apple to 60:", fruit_quantities)

# Set operations
fruit= {"Apple", "MAngo", "Papaya"}
print("\nOriginal set of fruit :", fruit)
# Adding an element to the set
fruit.add("SweetLemon")
print("Set after adding sweetLemon':", fruit)
# Removing an element from the set
fruit.remove("Apple")
print("Set after removing 'Apple':", fruit)

#
