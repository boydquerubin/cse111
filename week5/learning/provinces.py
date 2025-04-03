def main():
    text_list, num_of_ab = read_list("provinces.txt")
    print(text_list)
    print(f"Alberta occurs {num_of_ab} times in the modified list")

def read_list(filename):
    text_list = []
    with open(filename, mode="rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    if len(text_list) > 1:
        text_list.pop(0)
        text_list.pop()           

    updated_list = replace_element_in_list(text_list, "AB", "Alberta")

    num_of_ab = 0
    for i in updated_list:
        if i == "Alberta":
            num_of_ab += 1
   
    return updated_list, num_of_ab

def replace_element_in_list(original_list, element_to_replace, new_element):  
    for i in range(len(original_list)):
        if original_list[i] == element_to_replace:
            original_list[i] = new_element
    return original_list

if __name__ == "__main__":
    main()