import sys

def print_operation(operation_name):
    print("operation name:" + operation_name)

if __name__ == "__main__":
    operation_name = "default"
    # print( len(sys.argv))
    if len(sys.argv) > 1: 
        operation_name = sys.argv[1]
    print_operation(operation_name)