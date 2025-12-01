# This is a database management application that will involve viewing, adding, editing, and deleting the data

books = [
    {
        'title': 'The Outsiders',
        'author': 'S.E. Hinton',
        'page_count': 192
    },
    {
        'title': 'Holes',
        'author': 'Louis Sachar',
        'page_count': 233
    },
    {
        'title': 'The Giver',
        'author': 'Lois Lowry',
        'page_count': 240
    },
    {
        'title': 'The House on Mango Street',
        'author': 'Sandra Cisneros',
        'page_count': 110
    },
    {
        'title': 'A Long Walk to Water: Based on a True Story',
        'author': 'Linda Sue Park',
        'page_count': 128
    },
    {
        'title': 'Freak the Mighty',
        'author': 'Rodman Philbrick',
        'page_count': 160
    },
    {
        'title': 'Wonder',
        'author': 'R.J. Palacio',
        'page_count': 320
    },
    {
        'title': 'The Witch of Blackbird Pond',
        'author': 'Elizabeth George Speare',
        'page_count': 288
    },
    {
        'title': 'Roll of Thunder, Hear My Cry',
        'author': 'Mildred D. Taylor',
        'page_count': 276
    },
    {
        'title': 'Hatchet',
        'author': 'Gary Paulsen',
        'page_count': 208
    },
    {
        'title': 'A Wrinkle in Time',
        'author': 'Madeleine L\'Engle',
        'page_count': 256
    },
    {
        'title': 'Ender\'s Game',
        'author': 'Orson Scott Card',
        'page_count': 324
    },
    {
        'title': 'The Lightning Thief',
        'author': 'Rick Riordan',
        'page_count': 377
    },
    {
        'title': 'The Book Thief',
        'author': 'Markus Zusak',
        'page_count': 552
    },
    {
        'title': 'A Christmas Carol',
        'author': 'Charles Dickens',
        'page_count': 128
    },
    {
        'title': 'The Adventures of Tom Sawyer',
        'author': 'Mark Twain',
        'page_count': 366
    },
    {
        'title': 'The Diary of Anne Frank',
        'author': 'Anne Frank',
        'page_count': 336
    },
    {
        'title': 'Hidden Figures',
        'author': 'Margot Lee Shetterly',
        'page_count': 240
    },
    {
        'title': 'The Boy in the Striped Pajamas',
        'author': 'John Boyne',
        'page_count': 240
    },
    {
        'title': 'Fish in a Tree',
        'author': 'Lynda Mullaly Hunt',
        'page_count': 288
    },
    {
        'title': 'Ghost',
        'author': 'Jason Reynolds',
        'page_count': 192
    },
    {
        'title': 'Long Way Down',
        'author': 'Jason Reynolds',
        'page_count': 320
    },
    {
        'title': 'Brown Girl Dreaming',
        'author': 'Jacqueline Woodson',
        'page_count': 336
    },
    {
        'title': 'Refugee',
        'author': 'Alan Gratz',
        'page_count': 338
    },
    {
        'title': 'Ground Zero',
        'author': 'Alan Gratz',
        'page_count': 336
    },
    {
        'title': 'Allies',
        'author': 'Alan Gratz',
        'page_count': 272
    },
    {
        'title': 'Stella by Starlight',
        'author': 'Sharon M. Draper',
        'page_count': 304
    },
    {
        'title': 'Out of My Mind',
        'author': 'Sharon M. Draper',
        'page_count': 320
    },
    {
        'title': 'The Girl Who Drank the Moon',
        'author': 'Kelly Barnhill',
        'page_count': 384
    },
    {
        'title': 'Scythe',
        'author': 'Neal Shusterman',
        'page_count': 435
    },
    {
        'title': 'Dry',
        'author': 'Neal Shusterman',
        'page_count': 400
    },
    {
        'title': 'The War That Saved My Life',
        'author': 'Kimberly Brubaker Bradley',
        'page_count': 320
    },
    {
        'title': 'The Evolution of Calpurnia Tate',
        'author': 'Jacqueline Kelly',
        'page_count': 368
    },
    {
        'title': 'Insignificant Events in the Life of a Cactus',
        'author': 'Dusti Bowling',
        'page_count': 304
    },
    {
        'title': 'Where the Mountain Meets the Moon',
        'author': 'Grace Lin',
        'page_count': 288
    },
    {
        'title': 'City of Ember',
        'author': 'Jeanne DuPrau',
        'page_count': 336
    },
    {
        'title': 'The Mysterious Benedict Society',
        'author': 'Trenton Lee Stewart',
        'page_count': 496
    },
    {
        'title': 'Howl\'s Moving Castle',
        'author': 'Diana Wynne Jones',
        'page_count': 336
    },
    {
        'title': 'Fablehaven',
        'author': 'Brandon Mull',
        'page_count': 352
    },
    {
        'title': 'Eragon',
        'author': 'Christopher Paolini',
        'page_count': 500
    },
    {
        'title': 'Percy Jackson & the Olympians: The Sea of Monsters',
        'author': 'Rick Riordan',
        'page_count': 279
    },
    {
        'title': 'Amari and the Night Brothers',
        'author': 'B. B. Alston',
        'page_count': 416
    },
    {
        'title': 'The Girl in the Blue Coat',
        'author': 'Monica Hesse',
        'page_count': 288
    },
    {
        'title': 'They Went Left',
        'author': 'Monica Hesse',
        'page_count': 352
    },
    {
        'title': 'The Selection',
        'author': 'Kiera Cass',
        'page_count': 336
    },
    {
        'title': 'Miss Peregrine\'s Home for Peculiar Children',
        'author': 'Ransom Riggs',
        'page_count': 352
    },
    {
        'title': 'Divergent',
        'author': 'Veronica Roth',
        'page_count': 487
    },
    {
        'title': 'The Maze Runner',
        'author': 'James Dashner',
        'page_count': 375
    },
    {
        'title': 'Uglies',
        'author': 'Scott Westerfeld',
        'page_count': 425
    },
    {
        'title': 'Every Body Shines',
        'author': 'Various authors',
        'page_count': 300
    },
    {
        'title': 'The Hitchhiker\'s Guide to the Galaxy',
        'author': 'Douglas Adams',
        'page_count': 216
    },
    {
        'title': 'Salt to the Sea',
        'author': 'Ruta Sepetys',
        'page_count': 400
    },
    {
        'title': 'Chains',
        'author': 'Laurie Halse Anderson',
        'page_count': 336
    },
    {
        'title': 'Code Name Verity',
        'author': 'Elizabeth Wein',
        'page_count': 352
    },
    {
        'title': 'Serafina and the Black Cloak',
        'author': 'Robert Beatty',
        'page_count': 320
    },
    {
        'title': 'Anya\'s Ghost',
        'author': 'Vera Brosgol',
        'page_count': 224
    },
    {
        'title': 'The Crossover',
        'author': 'Kwame Alexander',
        'page_count': 240
    },
    {
        'title': 'Rebound',
        'author': 'Kwame Alexander',
        'page_count': 400
    },
    {
        'title': 'Long Way Down',
        'author': 'Jason Reynolds',
        'page_count': 320
    },
    {
        'title': 'The Girl Who Fell from the Sky',
        'author': 'Heidi W. Durrow',
        'page_count': 256
    },
    {
        'title': 'Theodore Boone: Kid Lawyer',
        'author': 'John Grisham',
        'page_count': 272
    },
    {
        'title': 'Artemis Fowl',
        'author': 'Eoin Colfer',
        'page_count': 396
    },
    {
        'title': 'The House of Dies Drear',
        'author': 'Virginia Hamilton',
        'page_count': 256
    },
    {
        'title': 'My Side of the Mountain',
        'author': 'Jean Craighead George',
        'page_count': 192
    },
    {
        'title': 'Where the Red Fern Grows',
        'author': 'Wilson Rawls',
        'page_count': 256
    },
    {
        'title': 'Black Beauty',
        'author': 'Anna Sewell',
        'page_count': 256
    },
    {
        'title': 'The Secret Garden',
        'author': 'Frances Hodgson Burnett',
        'page_count': 368
    },
    {
        'title': 'The Cay',
        'author': 'Theodore Taylor',
        'page_count': 144
    },
    {
        'title': 'Hoot',
        'author': 'Carl Hiaasen',
        'page_count': 304
    },
    {
        'title': 'Rules of the Road',
        'author': 'Joan Bauer',
        'page_count': 208
    },
    {
        'title': 'Walk Two Moons',
        'author': 'Sharon Creech',
        'page_count': 288
    },
    {
        'title': 'A Mango-Shaped Space',
        'author': 'Wendy Mass',
        'page_count': 272
    },
    {
        'title': 'Does My Head Look Big in This?',
        'author': 'Randa Abdel-Fattah',
        'page_count': 352
    },
    {
        'title': 'The Mysterious Island',
        'author': 'Jules Verne',
        'page_count': 491
    },
    {
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'page_count': 374
    },
    {
        'title': 'Theodore Boone: Kid Lawyer',
        'author': 'John Grisham',
        'page_count': 272
    },
    {
        'title': 'Artemis Fowl',
        'author': 'Eoin Colfer',
        'page_count': 396
    },
    {
        'title': 'The House of Dies Drear',
        'author': 'Virginia Hamilton',
        'page_count': 256
    },
    {
        'title': 'My Side of the Mountain',
        'author': 'Jean Craighead George',
        'page_count': 192
    },
    {
        'title': 'Where the Red Fern Grows',
        'author': 'Wilson Rawls',
        'page_count': 256
    },
    {
        'title': 'Black Beauty',
        'author': 'Anna Sewell',
        'page_count': 256
    },
    {
        'title': 'The Secret Garden',
        'author': 'Frances Hodgson Burnett',
        'page_count': 368
    },
    {
        'title': 'The Cay',
        'author': 'Theodore Taylor',
        'page_count': 144
    },
    {
        'title': 'Hoot',
        'author': 'Carl Hiaasen',
        'page_count': 304
    },
    {
        'title': 'Rules of the Road',
        'author': 'Joan Bauer',
        'page_count': 208
    },
    {
        'title': 'Walk Two Moons',
        'author': 'Sharon Creech',
        'page_count': 288
    }
]

def edit_book():
    view_books()
    wanted_title = input("What is the title of the book you want to edit?")
    for book in books:
        if book['title'] == wanted_title:
           wanted_change = input("What would you like to change (title, author, or page_count)?")
           if wanted_change == "title":
              new_title = input("What is your new title?")
              book['title'] = new_title
              print("done!")
              return
           elif wanted_change == "author":
                new_author = input("What is your new author?")
                book['author'] = new_author
                print('Done!')
                return
           elif wanted_change == "page_count":
                new_page_count = input("what is your new page count?")
                book['page_count'] = int(new_page_count)
                print("Done!")
                return
           else :
                print("please input the word title, author, or page_count exactly")
                return
    print(f"Sorry, '{wanted_title}' was not found in the list.")
def view_books():
  for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}, Page_count: {book['page_count']}")
def add_book():
  new_title = input("What is your title? ")
  new_author = input("What is your author? ")
  new_page_count = input("what is your page count? ")
  new_book = {'title': new_title,
              'author': new_author,
              'page_count': int(new_page_count)
             }
  books.append(new_book)
def delete_book():
  global books
  view_books()
  unwanted_book_title = input("What is the exact title of the unwanted book?")
  books = [book for book in books if book['title'] != unwanted_book_title]
  print(f"Succesfully deleted {unwanted_book_title}!")
while True:
    print("Menu: [1] Add Book, [2] View Books, [3] Delete Book, [4] Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("please type 1, 2, 3, or 4")
