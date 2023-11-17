# import statements required for the program
import glob
import json
import re
import pprint as pp
import pandas as pd
from Document import Document
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import textwrap

# method to extract the files
def extract_documents(file_number):

    # declare the root folder
    root = r"/Users/martinhanna/Desktop/document_parses"

    # use glob to get to the files from pmc
    json_files = glob.glob(f'{root}//pmc_json/*.json')

    # list to hold the documents
    document_list = []

    # variable to hold the individual text within an article
    article_text = ""

    # for the first file within the folder
    for file_path in json_files[:file_number]:

        # open the file
        with open(file_path) as file:

            # create document object
            document = Document()

            # get the article
            article = json.load(file)

            # assign the title from the metadata
            document.title = article['metadata']['title']

            # if the article has an author section -- needed to add this in to cleanse return
            if article['metadata']['authors']:

                # if the article has both a first name and last name author
                if article['metadata']['authors'][0]['first'] and article['metadata']['authors'][0]['last']:

                    # assign the lead author first name by using 0 index
                    document.author_first_name = article['metadata']['authors'][0]['first']

                    # assign the lead author last name by using 0 index
                    document.author_last_name = article['metadata']['authors'][0]['last']

            # if the article has body text
            if article['body_text']:

                # for each instance of text in the article
                for text_index in range(len(article['body_text'])):

                    # assign the text
                    text = article['body_text'][text_index]['text']

                    # add this to the overall text
                    article_text += text

                # assign the body text of the document to the article text
                document.body_text = article_text

            # get the length of the references in the paper
            references_length = len(article['bib_entries'])

            # for each of the references in the range
            for reference in range(references_length):

                # if the title isnt empty
                if article['bib_entries'][f'BIBREF{reference}']['title']:

                    # append the reference title - work around for the key issue
                    document.reference_titles.append(article['bib_entries'][f'BIBREF{reference}']['title'])

                # if the year is not empty
                if article['bib_entries'][f'BIBREF{reference}']['year']:

                    # appenf the reference year - work around for the key issue
                    document.reference_years.append(article['bib_entries'][f'BIBREF{reference}']['year'])

            # append this document to the document list
            document_list.append(document)

    # return the document_list with all of the documents
    return document_list


# helper method to create frequency dicitonary
def create_frequency_dictionary(list):

    # dictionary to hold the year and a count
    item_frequency = {}

    # loop over the years in the list
    for item in list:

        # if year is in the dictionary
        if item in item_frequency:

            # increment the year frequency count
            item_frequency[item] += 1

        # otherise
        else:

            # initialise the year frequency count
            item_frequency[item] = 1

    # return the dictionary
    return item_frequency


# method to see if any references cite each other
def reference_of_references(documents):

    # get a list of all the titles
    title_list = []

    # a list to hold the papers that have cited each other
    cited_list = []

    # for each document
    for document in documents:

        # append the title
        title_list.append(document.title)

    # for each document
    for document in documents:

        # for every title in the title list
        for title in title_list:

            # if the title is in the reference titles for a document
            if title in document.reference_titles:

                # append the title
                cited_list.append(title)

    # return the cited list to the main method
    return cited_list


# method to plot the top reference frequency
def plot_reference_frequency(documents):

    # declare a list to hold the references
    reference_list = []

    # for each document in the documents list
    for document in documents:

        # for every reference title in the reference titles list
        for reference_title in document.reference_titles:

            # append the reference_title to the list
            reference_list.append(reference_title)

    # create a dictionary with the reference frequency
    reference_frequency = create_frequency_dictionary(reference_list)

    # change the dicitonary to a sorted list
    x = sorted(list(reference_frequency.values()), reverse = True)[:20]

    # change the dicitonary to a sorted list
    y_name = sorted(list(reference_frequency.keys()), reverse = True)[:20]

    # shorten the names of the papers
    short_y_names = [textwrap.shorten(name, 40, placeholder = "") for name in y_name]

    # get the number of names in the y axis
    y = np.arange(len(y_name))

    # set the colour palette for the bars
    palette = sns.hls_palette(len(set(y)), l = .4, s = .9)

    # give the plot a title and x axis label
    plt.title("Top 20 frequency")
    plt.xlabel("Frequency")

    # create a horizontal bar chart
    plt.barh(y_name, x, color = palette)

    # set the y ticks
    plt.yticks(y, short_y_names, fontsize = 6)

    # create the legend
    plt.legend(y_name, bbox_to_anchor = (1.04, 1), loc = "upper right")

    # display the plot
    plt.show()


# method to plot the year frequency
def plot_year_frequency(documents):

    # list to hold the years in the references
    year_list = []

    # for each document in the documents list
    for document in documents:

        # for every year in the reference years list
        for year in document.reference_years:

            # append the year to the year list
            year_list.append(year)

    # dictionary to hold the year and a count
    year_frequency = create_frequency_dictionary(year_list)

    # change the dicitonary to a sorted list
    y = sorted(list(year_frequency.values()))

    # change the dicitonary to a sorted list
    x = sorted(list(year_frequency.keys()))

    # get unique values for the x axis
    x_axis = list(set(x))

    # create a figure and axes
    fig, ax = plt.subplots()

    # create the graph
    ax.set_title('Frequency per year of publication')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Year')
    ax.set_xlim(x_axis[0], x_axis[-1]+20)

    # function to plot and show graph
    ax.plot(x, y)
    plt.show()
