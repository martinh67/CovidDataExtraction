class Document():

    # magic method for the initialisation of the class
    def __init__(self):

        # set class attributes
        self.title = ""
        self.author_first_name = ""
        self.author_last_name = ""
        self.body = ""
        self.reference_titles = []
        self.reference_years = []


    # magic method for directory
    def __dir__(self):

        # return parameters and outputs of the Document class
        return ['title', 'author_first_name', 'author_last_name',
        'body', 'reference_titles', 'reference_years']


    # magic method for call
    def __call__(self, title, author_first_name,
    author_last_name, body, reference_titles, reference_years):

        # return that the Document instance has been called
        return("Document instance called")


    # method to produce machine readable representation of a type
    def __repr__(self):

        # return a formatted string of the data
        return(f'{self.title}, {self.author_first_name}, \
        {self.author_last_name}, {self.body}, \
        {self.reference_titles}, {self.reference_years}')


    # method to format the class as a string
    def __str__(self):

        # return a string
        return(f'title is {self.title}, author first name is \
        {self.author_first_name}, author last name is \
        {self.author_last_name}, body is {self.body}, \
        number of references is {len(self.reference_titles)}')
