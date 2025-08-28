import datetime

def modify_content(content):
    """
    Modify the content creatively:
    - Reverse each line
    - Capitalize vowels
    - Add a timestamp at the end
    """
    vowels = "aeiou"
    modified_lines = []
    
    for line in content.splitlines():
        reversed_line = line[::-1]
        # Capitalize vowels
        styled_line = ''.join([char.upper() if char.lower() in vowels else char for char in reversed_line])
        
    
    # Add a timestamp
    timestamp = f"\n--- File modified on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ---"
    modified_lines.append(timestamp)
    
    return '\n'.join(modified_lines)

def main():
    print(" Welcome to the File Read & Write Challenge!")
    filename = input("Enter the name of the file to read: ")
    
    try:
        # Read file safely with UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        modified_content = modify_content(content)
        new_filename = "creative_" + filename
        
        # Write modified content to a new file with UTF-8 encoding
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)
        
        print(f" Success! Your file has been creatively modified and saved as '{new_filename}'!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read/write '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
