books = [
    {"cim": "1984", "szerzo": "George Orwell", "megjelenes": 1949, "kiado": "Secker & Warburg", "oldalszam": 328, "isbn": "978-0451524935"},
    {"cim": "A kis herceg", "szerzo": "Antoine de Saint-Exupéry", "megjelenes": 1943, "kiado": "Reynal & Hitchcock", "oldalszam": 96, "isbn": "978-0156012195"},
    {"cim": "A Mester és Margarita", "szerzo": "Mihail Bulgakov", "megjelenes": 1967, "kiado": "Azbuka", "oldalszam": 384, "isbn": "978-0141184524"},
    {"cim": "Száz év magány", "szerzo": "Gabriel García Márquez", "megjelenes": 1967, "kiado": "Harper & Row", "oldalszam": 417, "isbn": "978-0060883287"},
    {"cim": "A nagy Gatsby", "szerzo": "F. Scott Fitzgerald", "megjelenes": 1925, "kiado": "Charles Scribner's Sons", "oldalszam": 180, "isbn": "978-0743273565"},
    {"cim": "Az utolsó vacsora", "szerzo": "Agatha Christie", "megjelenes": 1943, "kiado": "Collins Crime Club", "oldalszam": 244, "isbn": "978-0007287564"},
    {"cim": "A Gyűrűk Ura", "szerzo": "J.R.R. Tolkien", "megjelenes": "1954–1955", "kiado": "Allen & Unwin", "oldalszam": 1200, "isbn": "978-0261102385"},
    {"cim": "Harry Potter és a Bölcsek Köve", "szerzo": "J.K. Rowling", "megjelenes": 1997, "kiado": "Bloomsbury", "oldalszam": 223, "isbn": "978-0747532699"},
    {"cim": "Vörös és fekete", "szerzo": "Stendhal", "megjelenes": 1830, "kiado": "Olivier & Co", "oldalszam": 464, "isbn": "978-1857150313"},
    {"cim": "A Párizsi Istenek", "szerzo": "Hilary Mantel", "megjelenes": 1992, "kiado": "HarperCollins", "oldalszam": 400, "isbn": "978-0006547237"},
    {"cim": "A francia forradalom története", "szerzo": "Thomas Carlyle", "megjelenes": 1837, "kiado": "Chapman & Hall", "oldalszam": 608, "isbn": "978-1605209899"},
    {"cim": "Bűn és bűnhődés", "szerzo": "Fjodor Mihajlovics Dosztojevszkij", "megjelenes": 1866, "kiado": "The Russian Messenger", "oldalszam": 430, "isbn": "978-0143058195"},
    {"cim": "Anna Karenina", "szerzo": "Lev Tolsztoj", "megjelenes": 1877, "kiado": "The Russian Messenger", "oldalszam": 864, "isbn": "978-0143035004"},
    {"cim": "Frankenstein", "szerzo": "Mary Shelley", "megjelenes": 1818, "kiado": "Lackington, Hughes, Harding, Mavor & Jones", "oldalszam": 280, "isbn": "978-0486282114"},
    {"cim": "Drága bárányok", "szerzo": "Thomas Harris", "megjelenes": 1988, "kiado": "Doubleday", "oldalszam": 338, "isbn": "978-0452274173"},
    {"cim": "A háború és béke", "szerzo": "Lev Tolsztoj", "megjelenes": 1869, "kiado": "The Russian Messenger", "oldalszam": 1225, "isbn": "978-1400079988"},
    {"cim": "Szentivánéji álom", "szerzo": "William Shakespeare", "megjelenes": 1595, "kiado": "John Healy", "oldalszam": 160, "isbn": "978-0743482884"},
    {"cim": "A kis csillag", "szerzo": "Vavyan Fable", "megjelenes": 2004, "kiado": "Jaffa Kiadó", "oldalszam": 320, "isbn": "978-9638263683"},
    {"cim": "Huckleberry Finn kalandjai", "szerzo": "Mark Twain", "megjelenes": 1884, "kiado": "Chatto & Windus", "oldalszam": 366, "isbn": "978-1503215129"},
    {"cim": "A lovak szempillája", "szerzo": "Szécsi Noémi", "megjelenes": 2014, "kiado": "Libri", "oldalszam": 504, "isbn": "978-9637994401"},
    {"cim": "Közöny", "szerzo": "Albert Camus", "megjelenes": 1942, "kiado": "Gallimard", "oldalszam": 160, "isbn": "978-0679733942"},
    {"cim": "Az emberi méltóság", "szerzo": "Kertész Imre", "megjelenes": 2004, "kiado": "Jelenkor", "oldalszam": 212, "isbn": "978-9636761782"},
    {"cim": "Dűne", "szerzo": "Frank Herbert", "megjelenes": 1965, "kiado": "Chilton Books", "oldalszam": 412, "isbn": "978-0441013593"},
    {"cim": "A kutya, aki megmentette a karácsonyt", "szerzo": "David Rosenfelt", "megjelenes": 2005, "kiado": "Minotaur Books", "oldalszam": 320, "isbn": "978-0312990677"},
    {"cim": "Tíz kicsi néger", "szerzo": "Agatha Christie", "megjelenes": 1939, "kiado": "Collins Crime Club", "oldalszam": 272, "isbn": "978-0062073488"},
    {"cim": "Tigris tánca", "szerzo": "Tomi Ungerer", "megjelenes": 1999, "kiado": "Harcourt Brace", "oldalszam": 32, "isbn": "978-0151001977"},
    {"cim": "A három testőr", "szerzo": "Alexandre Dumas", "megjelenes": 1844, "kiado": "P. W. Ziegler", "oldalszam": 624, "isbn": "978-0451528513"},
    {"cim": "A Zöld lovag", "szerzo": "Pearl S. Buck", "megjelenes": 1943, "kiado": "John Day Company", "oldalszam": 384, "isbn": "978-0451531025"},
    {"cim": "A remény rabjai", "szerzo": "Stephen King", "megjelenes": 1982, "kiado": "Viking Penguin", "oldalszam": 576, "isbn": "978-0451166767"},
    {"cim": "Szent Ágota", "szerzo": "Márai Sándor", "megjelenes": 1939, "kiado": "Jelenkor Kiadó", "oldalszam": 544, "isbn": "978-9636761805"},
    {"cim": "A természetes", "szerzo": "Bernard Malamud", "megjelenes": 1952, "kiado": "Harper & Row", "oldalszam": 256, "isbn": "978-0375701189"},
    {"cim": "Elvont művészet", "szerzo": "Wassily Kandinsky", "megjelenes": 1910, "kiado": "Bauhaus Books", "oldalszam": 108, "isbn": "978-0486221500"},
    {"cim": "A csodálatos hónapok", "szerzo": "Karel Čapek", "megjelenes": 1933, "kiado": "Knižní klub", "oldalszam": 320, "isbn": "978-8087912121"},
    {"cim": "Öröm és bánat", "szerzo": "Virginia Woolf", "megjelenes": 1922, "kiado": "Hogarth Press", "oldalszam": 266, "isbn": "978-0156787845"},
    {"cim": "Az álomfejtő", "szerzo": "Sigmund Freud", "megjelenes": 1900, "kiado": "Macmillan", "oldalszam": 616, "isbn": "978-0393003055"},
    {"cim": "Fahrenheit 451", "szerzo": "Ray Bradbury", "megjelenes": 1953, "kiado": "Ballantine Books", "oldalszam": 158, "isbn": "978-1451673319"},
    {"cim": "A harcosok klubja", "szerzo": "Chuck Palahniuk", "megjelenes": 1996, "kiado": "W.W. Norton & Company", "oldalszam": 208, "isbn": "978-0393311746"},
    {"cim": "A bűnözés titkai", "szerzo": "John Grisham", "megjelenes": 1991, "kiado": "Doubleday", "oldalszam": 368, "isbn": "978-0385418889"},
    {"cim": "A Lord of the Rings – Két torony", "szerzo": "J.R.R. Tolkien", "megjelenes": 1954, "kiado": "Allen & Unwin", "oldalszam": 352, "isbn": "978-0261102323"},
    {"cim": "A sziget", "szerzo": "Albert Sánchez Piñol", "megjelenes": 2002, "kiado": "Duomo", "oldalszam": 592, "isbn": "978-8435069634"},
    {"cim": "A sötét torony: A pusztító", "szerzo": "Stephen King", "megjelenes": 2004, "kiado": "Scribner", "oldalszam": 352, "isbn": "978-0743235097"},
    {"cim": "A másik bolygó", "szerzo": "Ursula K. Le Guin", "megjelenes": 1972, "kiado": "HarperCollins", "oldalszam": 400, "isbn": "978-0060854255"},
    {"cim": "A mágikus világ", "szerzo": "C.S. Lewis", "megjelenes": 1950, "kiado": "HarperCollins", "oldalszam": 208, "isbn": "978-0064471190"},
    {"cim": "A titok", "szerzo": "Rhonda Byrne", "megjelenes": 2006, "kiado": "Atria Books", "oldalszam": 198, "isbn": "978-1582701707"},
    {"cim": "Március", "szerzo": "Geraldine Brooks", "megjelenes": 2005, "kiado": "Viking", "oldalszam": 432, "isbn": "978-0143036667"},
    {"cim": "Vihar a szívben", "szerzo": "John Boyne", "megjelenes": 2008, "kiado": "Doubleday", "oldalszam": 368, "isbn": "978-0385527244"},
    {"cim": "A szél neve", "szerzo": "Patrick Rothfuss", "megjelenes": 2007, "kiado": "DAW Books", "oldalszam": 662, "isbn": "978-0756404741"},
    {"cim": "A világ vége", "szerzo": "Cormac McCarthy", "megjelenes": 2006, "kiado": "Alfred A. Knopf", "oldalszam": 287, "isbn": "978-0307387139"},
    {"cim": "A hosszú eső", "szerzo": "Joe Hill", "megjelenes": 2007, "kiado": "St. Martin's Press", "oldalszam": 320, "isbn": "978-0312991216"},
    {"cim": "A vadon szívében", "szerzo": "Jon Krakauer", "megjelenes": 1996, "kiado": "Villard", "oldalszam": 224, "isbn": "978-0385483492"}
]
