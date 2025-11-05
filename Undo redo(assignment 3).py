# lab assignment 3
# Implement an Undo/Redo system using Stack.

undo_stack = []
redo_stack = []
document = ""

def make_change(change):
    global document
    undo_stack.append(document)
    document += change
    print("Document:", document)

def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
        print("Undo performed. Document:", document)
    else:
        print("Nothing to undo.")

def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
        print("Redo performed. Document:", document)
    else:
        print("Nothing to redo.")

# Main Program
make_change("Hello ")
make_change("World")
undo()
redo()
