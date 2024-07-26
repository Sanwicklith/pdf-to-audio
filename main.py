import PyPDF2
import pyttsx3

# Instantiate the obj
speaker = pyttsx3.init()

# getting the pdf and reading its content in binary
book = open("Benford's Law.pdf", 'rb')
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)
print(pages)

# Now lets read a specific page
page = reader.pages[1]

# now we extract the binary to text
text = page.extract_text()

# pass string to be read to instance using .say() method
speaker.say(text)

# Read out the string now using .runAndWait()
speaker.runAndWait()
