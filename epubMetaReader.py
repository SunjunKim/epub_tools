import ebooklib
from ebooklib import epub

book = epub.read_epub('2036004611 - 밀애의 법칙.epub')

print(book.get_metadata('DC', 'title'))
print(book.get_metadata('DC', 'creator'))
print(book.get_metadata('DC', 'description'))

print(book.get_metadata('OPF', 'cover'))
