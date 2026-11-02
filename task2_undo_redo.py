document = ""
undo = []
redo = []
while True:
    command = input("type/undo/redo/quit: ")
    if command == "type":
        text = input("Text: ")
        undo.append(document)
        document += text
        redo = []
        print("Document:", document)
    elif command == "undo":
        if undo:
            redo.append(document)
            document = undo.pop()
            print("Document:", document)
        else:
            print("Nothing to undo")
    elif command == "redo":
        if redo:
            undo.append(document)
            document = redo.pop()
            print("Document:", document)
        else:
            print("Nothing to redo")
    elif command == "quit":
        break