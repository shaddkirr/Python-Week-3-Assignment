def modify_content(content):
    """Modify the content before writing to a new file (e.g., convert to uppercase)."""
    return content.upper()

def read_and_write_file():
    """Reads a file, modifies its content, and writes it to a new file with error handling."""
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
        
        # Modify content (e.g., convert text to uppercase)
        modified_content = modify_content(content)

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been saved in {new_filename} ✅")

    except FileNotFoundError:
        print("Error: The file does not exist. ❌")
    except IOError:
        print("Error: The file could not be read. ❌")

# Run the program
read_and_write_file()
