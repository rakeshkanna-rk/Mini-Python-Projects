def flames_checker(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Count unique characters in each name
    count1 = {char: name1.count(char) for char in set(name1)}
    count2 = {char: name2.count(char) for char in set(name2)}
    
    # Remove common characters
    for char in count1:
        if char in count2:
            min_count = min(count1[char], count2[char])
            count1[char] -= min_count
            count2[char] -= min_count
    
    # Combine remaining characters
    remaining_chars = ''.join([char * count for char, count in count1.items()]) + \
                      ''.join([char * count for char, count in count2.items()])
    
    # FLAMES categories
    categories = ["Friends", "Lovers", "Attraction", "Marriage", "Enemies", "Siblings"]
    
    # FLAMES algorithm
    index = 0
    while len(categories) > 1:
        length = len(remaining_chars)
        index = (index + length - 1) % len(categories)
        categories.pop(index)
    
    return categories[0]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = flames_checker(name1, name2)
print("Relationship status:", result)