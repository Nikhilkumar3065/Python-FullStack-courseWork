notes={}
name=input("enter your name: ")

while True:
    print(f"Hey {name},welcome to the notes")
    if notes:
        for i in notes:
            print(i.ljust(15,' '),':',notes[i])
        else:
            print("Empty Notes")
    print('[A]dd Note')
    print('[E]dit Note')
    print('[D]elete Note')
    print('[B]ack')

    ch=input("enter your choice :").upper()
    if ch=='A':
        note_name=input("enter the note name:").title()
        content=input("write your thoughts.....:")
        notes[note_name]=content

    elif ch=='E':
        note_name=input("enter the note name to edit:").title()
        if note_name in notes:
            new_content=input("write your thoughts.....:")
            notes[note_name]+=new_content
        else:
            print(f'{note_name} is not available')
        

    elif ch=='D':
        note_name=input("enter the note name to delete:").title()
        notes.pop(note_name)
        print(f"{note_name} is deleted successfully!!!")

    elif ch=='B':
        print(f"Thank You,{name}!")
