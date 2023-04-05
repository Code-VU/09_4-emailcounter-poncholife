def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    sender_collection = dict()
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            line_split = line.split()
            sender = line_split[1]
            sender_collection[sender] = sender_collection.get(sender, 0) + 1
   
    largest = 0
    for item in sender_collection:
        if sender_collection[item] > largest:
            largest = sender_collection[item]
            max_key = item
    
    print(max_key, sender_collection[max_key])

    handle.close()
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
