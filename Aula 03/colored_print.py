class colored_print:
    def __init__(self):
        self.colors = {
            "HEADER": '\033[95m',
            "OKBLUE": '\033[94m',
            "OKCYAN": '\033[96m',
            "OKGREEN": '\033[92m',
            "WARNING": '\033[93m',
            "FAIL": '\033[91m',
            "ENDC": '\033[0m',
            "BOLD": '\033[1m',
            "UNDERLINE": '\033[4m'
        }

    def get_color(self, color):
        color_selected = None
        if color == "red":
            color_selected = self.colors.get("FAIL")
        elif color == "yellow":
            color_selected = self.colors.get("WARNING")
        elif color == "green":
            color_selected = self.colors.get("OKGREEN")
        elif color == "cyan":
            color_selected = self.colors.get("OKCYAN")
        elif color == "blue":
            color_selected = self.colors.get("OKBLUE")
        elif color == "pink":
            color_selected = self.colors.get("HEADER")
        return color_selected

    def string(self, text=None, color=None, bold:bool=False, underline:bool=False):
        self.colorSelected = self.get_color(color)
        if bold:
            print(self.colors.get("BOLD"), end="")
        if underline:
            print(self.colors.get("UNDERLINE"), end="")
        print(self.colorSelected + str(text) + self.colors.get("ENDC"))

    def array_for_each(self, array, color, bold:bool=False, underline:bool=False):
        self.colorSelected = self.get_color(color)
        if bold:
            print(self.colors.get("BOLD"), end="")
        if underline:
            print(self.colors.get("UNDERLINE"), end="")
        print(self.colorSelected, end="")
        for value in array:
            print(str(value))
        print(self.colors.get("ENDC"))