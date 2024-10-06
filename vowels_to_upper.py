class VowelTransformer:
    def __init__(self, text):
        self.text = text
        self.vowels = 'aeiou'

    def vowels_to_upper(self):
        return ''.join([char.upper() if char in self.vowels else char for char in self.text])

# Sample usage
transformer1 = VowelTransformer("Hello, world!")
print(transformer1.vowels_to_upper())  # Output: "HEllO, wOrld!"

transformer2 = VowelTransformer("hello hi bye")
print(transformer2.vowels_to_upper())  # Output: "hEllO hI byE"

transformer3 = VowelTransformer("")
print(transformer3.vowels_to_upper())  # Output: ""
