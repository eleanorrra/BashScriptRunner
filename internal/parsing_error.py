class ParsingError(RuntimeError):
    def __init__(self, line, message):
        formatted_message = f"Parsing error on line {line}: {message}"
        super(ParsingError, self).__init__(formatted_message)
