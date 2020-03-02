class WrongFolderLength(Exception):
    def __init__(self, length):
        self.message = f"There should be only one file inside the 'Spreadsheet' folder instead of {length}."
        super().__init__(self.message)


class WrongFileFormat(Exception):
    def __init__(self):
        self.message = 'Only .csv or .xlsx files are supported'
        super().__init__(self.message)
