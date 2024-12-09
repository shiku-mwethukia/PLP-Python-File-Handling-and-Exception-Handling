def read_and_modify_file():
    try:
        input_file = input("Enter the name of the file to read from: ")
        
        # Read the content of the input file
        with open(input_file, "r") as file:
            content = file.readlines()
        
        # 1. Add line numbers to each line
        numbered_content = [f"{idx + 1}. {line}" for idx, line in enumerate(content)]
        with open("output_numbered.txt", "w") as file:
            file.writelines(numbered_content)
        print("Numbered content written to output_numbered.txt.")
        
        # 2. Remove blank lines
        non_blank_lines = [line for line in content if line.strip()]
        with open("output_non_blank.txt", "w") as file:
            file.writelines(non_blank_lines)
        print("Non-blank lines written to output_non_blank.txt.")
        
        # 3. Convert content to uppercase
        uppercase_content = [line.upper() for line in content]
        with open("output_uppercase.txt", "w") as file:
            file.writelines(uppercase_content)
        print("Uppercase content written to output_uppercase.txt.")
        
        # 4. Sort lines alphabetically
        sorted_content = sorted(content)
        with open("output_sorted.txt", "w") as file:
            file.writelines(sorted_content)
        print("Sorted content written to output_sorted.txt.")
        
        # 5. Limit each line to 100 characters
        truncated_content = [line[:100] + '\n' for line in content]
        with open("output_truncated.txt", "w") as file:
            file.writelines(truncated_content)
        print("Truncated content written to output_truncated.txt.")
        
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the file name and try again.")
    except PermissionError:
        print("Error: You don't have the required permissions to read or write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
