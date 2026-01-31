# Mixins Exercises

# Exercise: Mixins
# Create mixins 'Serializable' and 'Loggable'.
# Create a class 'DataHandler' that uses both mixins.

# TODO: Implement mixins and class
class Serializable:
    pass

class Loggable:
    pass

class DataHandler(Serializable, Loggable):
    pass

# Test
# handler = DataHandler([1,2,3])
# handler.save()  # Should print "Logging: Saving data" and "Data saved"
# handler.load()  # Should print "Logging: Loading data" and "Data loaded"