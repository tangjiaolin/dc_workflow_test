import sys

def printOperator(operatorName):
    print(f'operation name:{operatorName}')


if __name__ == "__main__":
    operatorName = sys.argv[1]
    printOperator(operatorName)