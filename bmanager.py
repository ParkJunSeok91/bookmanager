__author__ = 'user'

import sys
import time

class BookManager:
    def __init__(self):
        self.dic = [
            {
                "book_title": "",
                "book_author": "",
                "book_price": ""
            }
        ]
        self.inManager = 0
        self.number = ''

    def mainscreen(self):
        self.number = ''
        print('도서 매니저 프로그램입니다')
        print('0: 도서목록 추가')
        print('1: 도서목록 검색')
        print('2: 도서목록 삭제')
        print('3: 도서목록 출력')
        print('4: 도서 매니저 프로그램 종료')

        self.number = input('원하시는 메뉴를 입력해주세요> ')
        if self.number is '0':
            self.addBook()
        elif self.number is '1':
            self.findBook()
        elif self.number is '2':
            self.delBook()
        elif self.number is '3':
            self.printBook()
        elif self.number is '4':
            self.exitBook()

    def addBook(self):
        btitle = input('책 제목을 입력해주세요> ')
        bauthor = input('책 저자를 입력해주세요> ')
        bprice = input('책 가격을 입력해주세요> ')

        for x in range(len(self.dic)):
            if btitle in self.dic[x]["book_title"]:
                print('이 도서는 이미 추가되었습니다')
                break
            else:
                self.dic.append(
                    {
                        "book_title": btitle,
                        "book_author": bauthor,
                        "book_price": bprice
                    }
                )
                with open("book_list.txt", "w+") as f:
                    f.write(str(self.dic[1:]))

    def findBook(self):
        choice = input('책 제목으로 검색하려면 1번, 책 저자로 검색하려면 2번을 눌러주세요> ')
        bookfind = 0

        if choice is '1':
            bookfind = 0
            btitle = input('책 제목을 입력해주세요> ')

            for x in range(len(self.dic)):
                if btitle in self.dic[x]["book_title"]:
                    print("책 제목: '{0}', 책 저자: '{1}', 책 가격: '{2}'".format(self.dic[x]["book_title"], self.dic[x]["book_author"], self.dic[x]["book_price"]))
                    bookfind = 1
                    break
                else:
                    pass

            if bookfind is 0:
                print('도서 목록에 해당 책 제목이 등록되어 있지 않습니다')

        elif choice is '2':
            bookfind = 0
            btitle = input('책 저자를 입력해주세요> ')

            for x in range(len(self.dic)):
                if btitle in self.dic[x]["book_author"]:
                    print("책 제목: '{0}', 책 저자: '{1}', 책 가격: '{2}'".format(self.dic[x]["book_title"], self.dic[x]["book_author"], self.dic[x]["book_price"]))
                    bookfind = 1
                    break
                else:
                    pass

            if bookfind is 0:
                print('도서 목록에 해당 책 제목이 등록되어 있지 않습니다')
        else:
            print('잘못된 숫자를 입력하셨습니다\n')

    def delBook(self):
        btitle = input('삭제하려는 책 제목을 입력해 주세요> ')
        for x in range(len(self.dic)):
                if btitle in self.dic[x]["book_title"]:
                    self.dic.pop(x)
                    break
        print('삭제되었습니다')

    def printBook(self):
        if 1 == len(self.dic):
            print("저장된 도서 목록이 없습니다")
        else:
            for x in range(1,len(self.dic)):
                print("책 제목: '{0}', 책 저자: '{1}', 책 가격: '{2}'".format(self.dic[x]["book_title"], self.dic[x]["book_author"], self.dic[x]["book_price"]))

    def exitBook(self):
        sys.exit()

b = BookManager()

while True:
    b.mainscreen()