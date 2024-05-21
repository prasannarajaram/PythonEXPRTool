# output = "output_file.txt"

# def IsOutput():
#     try:
#         with open(output, 'w') as file:
#             return True
#     except Exception as e:
#         print("An error occurred:", e)
#         sys.exit(1)  # Exit the program with an error code

def write_to_output_file(content, output_file):
    with open(output_file, 'a') as file:
        file.writelines(content)