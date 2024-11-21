import os

def read_and_write_file():
    print("📁 Welcome to the File Modifier Program!")
    input_file = input("Enter the name of the file you want to read (with extension): ").strip()
    
    try:
        if not os.path.isfile(input_file):
            raise FileNotFoundError("The file does not exist. Please check the filename and try again.")
        
        
        with open(input_file, 'r') as file:
            content = file.readlines()
   
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
   
        output_file = input("Enter the name of the file to save the modified content (with extension): ").strip()
        

        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"✅ Success! Modified content has been saved to '{output_file}'.")
    
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except PermissionError:
        print("❌ Error: Permission denied. Please check your file permissions and try again.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


read_and_write_file()
