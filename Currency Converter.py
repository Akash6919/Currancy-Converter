def main():

    print("This Program converts Indian Rupee to US Dollars")
    print()

    rupee = eval(input("Enter amount in Rupee: "))

    dollars = convert_to_dollars(rupee)

    print("That is" , dollars, "dollars. ")

convert_to_dollars = lambda rupee: rupee * 0.012

main()