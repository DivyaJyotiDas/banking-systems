
def validate_customer(func):
    def inner(*args, **kwargs):
        """ Validation of Inputs can be done here.
            Leaving as of now.
        """
        #
        #
        #
        func(*args, **kwargs)
    return inner