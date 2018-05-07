a_list = []

a_list_numbers = [1,2,3,4,5]

a_list_string = ["hello","world","to","everybody"]

a_list_mix = ["hello", [1,2,3], 2, False]


print a_list_mix
print "\n"
print a_list_mix[1]
print "\n"
print a_list_mix[1][1]


print a_list_string[-1]


print "\n\n\n\n\n"

a_list.append("x")
print a_list

a_list.extend(a_list_numbers)
print a_list

a_list.insert(0, "a")
print a_list

a_list.remove(1)
print a_list

print a_list.count("a")

a_list.sort()
print a_list

a_list.reverse()
print a_list