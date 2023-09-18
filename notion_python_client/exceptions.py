class APIException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f"APIException: {self.status_code} - {self.message}"


class PropertyTypeException(Exception):
    def __init__(self, excpected_type, actual_type):
        self.excpected_type = excpected_type
        self.actual_type = actual_type

    def __str__(self):
        return f"PropertyException: Expected type {self.excpected_type} but got {self.actual_type}"


class PageValidationException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"PageValidationException: {self.message}"


class PropertyNotIncludedException(Exception):
    def __init__(self, property_name):
        self.property_name = property_name

    def __str__(self):
        return f"PropertyNotIncludedException: Property {self.property_name} is not included in the properties of the page"
