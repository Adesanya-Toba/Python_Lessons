import datetime

# Store the next available id for all new notes
last_id = 0

# Creating the notes class
class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    def __init__(self, memo, tags='') -> None:
        '''Initialize note with memo and optional space-separated tags
        Automatically set the note's creation date and unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        # Using the global variable
        global last_id
        last_id +=1
        self.id = last_id

    
    def match(self, filter:str) -> bool:
        '''Determine if this note matches the filter text. 
        Return True if it matches, False otherwise
        
        Search is case sensitive and matches both text and tags'''
        return filter in self.memo or filter in self.tags
    

# Creating the notebook class
class Notebook:
    '''Represents a collection of notes that can be tagged,
    modified and searched'''
    def __init__(self) -> None:
        '''Initialize a new notebook with an empty list'''
        self.notes:Note = []

    
    def new_note(self, memo:str, tags=''):
        '''Create a new note and add it to the list'''
        self.notes.append(Note(memo, tags))

    
    def modify_memo(self, note_id:int, new_memo:str):
        '''Find a note with the given id and change its memo
        to a new one'''
        self._find_note(note_id).memo = new_memo

    def search(self, filter:str):
        '''Find all notes that match the given filter string'''
        return [note for note in self.notes if note.match(filter)]
    
    def _find_note(self, note_id:int):
        '''Locate the note with the given id'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None


def main() ->None:
    n1 = Note('hello first')
    n2 = Note('hello again')

    print(n1.id)
    print(n2.id)

    print(n1.match('hello'))
    print(n2.match('ell '))

    # Create a new notebook
    n = Notebook()

    n.new_note("hello world")
    n.new_note('hello girl')
    
    for p in n.notes:
        print(p.memo)

    print(n.modify_memo(0, 'my helper'))

    print(n.notes[0].memo)
    # n.search('hello')

if __name__ == "__main__":
    main()