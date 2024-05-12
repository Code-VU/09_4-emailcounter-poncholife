def countEmail():
    # This first line is provided for you
    
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    fhand = open(name)

    try: 
        fhand = open(name)
    except:
        print(f'Error, unable to open {name}')
        quit()

    from_email_address = dict()

    for line in fhand:
        if line.startswith('From '):
            words = line.split()
            from_email_address[words[1]] = from_email_address.get(words[1],0) + 1

    highest_count = 0
    highest_sender = None
    for key,value in from_email_address.items():
        if value > highest_count:
            highest_count = value
            highest_sender = key

    print(highest_sender, highest_count)

    fhand.close()


## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()