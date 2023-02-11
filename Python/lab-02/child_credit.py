from child import Child
import pprint

def produceReport(children):
    """
    Loop over the array of children
    if the array has a value greater than 0,

    Return an equally sized array of tax credit per child
    """
    credit = []    
    for i in range(len(children)):
        if children[i].age < 18 and sum(credit) == 0:
            credit.append(1000)
        elif children[i].age < 18:
            credit.append(500)
        else:
            credit.append(0)
    print("-Name-----------Return-")        
    for i in range(len(children)):
        print(f"{children[i].name} ({children[i].age})     ${credit[i]}")
    print(f"\nTotal Tax Credit Received: ${sum(credit)}")
    return sum(credit)
        

def main():

    tom = Child("Tommy", 14)
    dick = Child("Richard", 12)
    harry = Child("Harold", 21)
    pete = Child("Peter", 17)

    children = [tom, dick, harry, pete]

    produceReport(children)

if __name__ == "__main__":
    main()