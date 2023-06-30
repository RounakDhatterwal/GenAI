file = open("input.txt", "r")
content = file.read()
wordCount = len(content)

newFile = open("output.txt", "w")
newContent = newFile.write(f"Number of words : {wordCount}")


