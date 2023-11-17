# import statements required for the program
import time
from methods import *


# start the timer for the program
start = time.time()


# declare the main method
def main():

    # get a list of documents
    documents = extract_documents(1000)

    # print the number of documents in the list
    print(f"The number of documents: {len(documents)}")

    # plots the year frequency
    plot_year_frequency(documents)

    # uncomment for the reference frequency
    # plot_reference_frequency(documents)

    '''
    # uncomment to find papers that reference each other
    cited_list = reference_of_references(documents)

    # print the number of cited works from the list of documents
    print()
    print(f"Number of cited works from list of documents: {len(cited_list)}")
    print()

    # print the cited list
    pp.pprint(cited_list)
    '''



# magic method to run the main function
if __name__ == "__main__":
    main()

# time of the program
print("\n" + 50 * "#")
print(time.time() - start)
print(50 * "#" + "\n")
