class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book: 'Book', date: str, royalties: int):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    pass


class Book:
    all = []
    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    pass


class Contract:
    all = []
    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        self.author: Author = author
        self.book: Book = book
        self.date: str = date
        self.royalties: int = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    pass