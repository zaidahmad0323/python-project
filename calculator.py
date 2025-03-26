def calculator():
    operators = ['+','-','*','/']
    firstNumber = float(input("Enter first number : "))
    selectedOperator = input("Select an operator : ")
    secondNumber = float(input("Enter the second number : "))
    
    if selectedOperator == '+':
        addition = firstNumber + secondNumber
        return addition
    elif selectedOperator == '-' :
        subtraction = firstNumber - secondNumber    
        return subtraction
    elif selectedOperator == '*' :
        multiplication = firstNumber * secondNumber    
        return multiplication
    elif selectedOperator == '/' :
        division = firstNumber / secondNumber    
        return division   
    else :
        print("The operator is not correct please select the correct operator ")
        reSelection = input("would you want to select the correct operator : \n") 
        result = calculator()     
        if reSelection == "yes" or reSelection == "Yes":
            morecalculation(result=result)
    result = calculator()
    print(f"{firstNumber} {selectedOperator} {secondNumber} = {result}")
        

def morecalculation(result):
    operators = ['+','-','*','/']
    selectedOperator = input("Select an operator for the given : ")
    secondNumber = float(input("Enter the second number : "))

    #result = calculator()
    print(f"{result} {selectedOperator} {secondNumber} = {result}")

    if selectedOperator == '+':
        addition = result + secondNumber
        return addition
    elif selectedOperator == '-' :
        subtraction = result - secondNumber    
        return subtraction
    elif selectedOperator == '*' :
        multiplication = result * secondNumber    
        return multiplication
    elif selectedOperator == '/' :
        division = result / secondNumber    
        return division
    else :
        print("The operator is not correct please select the correct operator ")
        reSelection = input("would you want to select the correct operator : \n") 
        if reSelection == "yes" or reSelection == "Yes":
            morecalculation(result=result)
    print(f"{result} {selectedOperator} {secondNumber} = {result}")        

result = calculator()
operateMore = True
while operateMore:
    moreOpOnResult = input(f"Would you want to operate more on the {result} enter(yes), restart enter(res) or exit enter(exit)")
    if moreOpOnResult == "yes" or moreOpOnResult == "Yes":
        morecalculation(result=result)