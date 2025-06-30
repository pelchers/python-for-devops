print("Q1")

print("a list is mutable collection of things") 



print("Q2")

print("create a list with brackets and a tuple with parentheses")

Q2_List = [1, 2, 3, 4, 5]
Q2_Tuple = (1, 2, 3, 4, 5)

print(Q2_List)
print(Q2_Tuple)

# Alternative approach using dictionary
print("\nAlternative approach with dictionary:")
data = {
    "Q2 List": [1, 2, 3, 4, 5],
    "Q2 Tuple": (1, 2, 3, 4, 5)
}

print(data["Q2 List"])
print(data["Q2 Tuple"])
print("Accessing specific elements:")
print(f"First element from list: {data['Q2 List'][0]}")
print(f"Third element from tuple: {data['Q2 Tuple'][2]}")

print("Q3")

print("a list is mutable and a tuple is immutable")

print("Q4")

print("to access elements in a list, we use brackets and the index of the element we want to access.")

servers = ["server1", "server2", "server3", "server4", "server5"]

print(servers[0])
print(servers[1])
print(servers[2])
print(servers[3])
print(servers[4])

print("Q5")

servers.append("server6")
print(servers[5])

print("Q6")

servers.remove("server1")
print(servers)



