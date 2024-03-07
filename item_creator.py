try:
    import pyperclip
except ImportError:
    print("Could not import pyperclip. Please install it using 'pip install pyperclip' and run the program again.")
    quit()

print("Welcome to Infinite Craft Item Creator! MIT License (c) MesonProgrammer")
print("WARNING: This program won't work if there is a (') in the text.")

def end_program():
    input("[PROGRAM TERMINATED]")
    quit()

while True:
    try:
        data = input("Data: ")
        data = data.replace('false', 'False').replace('true', 'True')
        data = eval(data)
    except KeyError:
        print("Error processing data. Try again.")
    except KeyboardInterrupt:
        end_program()
    else:
        break

item_to_add_text = input("Item to add (text): ")
item_to_add_emoji = input("Item to add (emoji): ")

item = {"text":item_to_add_text,"emoji":item_to_add_emoji,"discovered":False}

elements = data.get('elements')
if elements and type(elements) == list:
    elements.append(item)
else:
    print("Elements must be a list.")
    end_program()

input("Successful. Please enter to copy it to your clipboard.")
pyperclip.copy(str(data).replace('False', 'false').replace('True', 'true').replace('\'', '"').replace(': ', ':'))
