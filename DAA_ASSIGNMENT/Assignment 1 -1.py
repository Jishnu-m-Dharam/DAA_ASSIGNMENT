try:
    with open('test.txt', 'r') as file:
        content = file.read()
        print(content)      
except FileNotFoundError:
    print("Error: The file was not found.")     
except Exception as e:
    print(f"An unexpected error occurred: {e}") 
