# Reference
import datetime

class BoxedResp:
    def __init__(self, name, code, expected):
        self.name = name
        self.code = code
        self.expected = expected

class MetadResp(BoxedResp):
    date = datetime.date.today()

code_hours = {
    "66": "Execution",
    "58": "Continue",
    "26": "Checking",
    "20": "Termination",
}

red = BoxedResp(name = "Danger", code = "20", expected = False)
black = MetadResp("Black", "26", False)
green = BoxedResp("Green", "58", False)
orange = BoxedResp("Orange", "66", True)

def main():
    for i in [red, black, green, orange]:
        print(f"Status of {i.name} from {i.code}:")
        signal = code_hours[i.code]
        print("\t", signal)
        print(f"Expected is {'valid.' if i.expected else 'unknown.'}")
        # Checking the signal instead of the code
        if signal == "Checking":
            if i.expected:
                print(f"Hello {i.name}!!")
            else:
                print(f"Insert message about {i.name} from {i.code}")

main()
