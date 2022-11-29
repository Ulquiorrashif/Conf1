import json
from sly import Lexer, Parser

# with open('output.json', 'r') as f:
#     for line in f:
#         print(line.rstrip())
"""
files ::= file files | empty
file ::=  group student subject 
group ::= "(" "^" name names  ")"
subject ::= "(" title ")"
student ::= "(" "@" info infooo ")"
title ::= name
"""
class CalcLexer(Lexer):
    tokens = {FIRST_SKOBKA, LAST_SKOBKA, NAMEGROUP, STUDENTS,  GROUP, STUDENT}

    # Tokens
    FIRST_SKOBKA = r'\('
    LAST_SKOBKA = r'\)'
    ignore = r' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'\#.*'
    STUDENT = r'stud'
    GROUP = r'spisokgr'
    NAMEGROUP=r'[^ \t\#();\'\@\^]+'
    STUDENTS =r"'[^\:\)\()\t\']*'"






class CalcParser(Parser):
    debugfile = 'parser.out'
    tokens = CalcLexer.tokens

    @_('group student subject')
    def file(self, p):
        return dict(groups=p.group, students=p.student, subject=p.subject)

    @_("FIRST_SKOBKA title LAST_SKOBKA")
    def subject(self, p):
        return (p.title[1:-1]).replace('\n', 'h')

    @_("FIRST_SKOBKA STUDENT info infooo  LAST_SKOBKA")
    def student(self, p):
        print(p.info)
        return [dict(age=int(p.info[0:2]),
                     group=(p.info[2:12]),
                     name=(p.info[13:]))] + p.infooo

    @_("FIRST_SKOBKA GROUP name names  LAST_SKOBKA")
    def group(self, p):
        # print(p.value)
        return [p.name] + p.names

    @_('info infooo')
    def infooo(self, p):
        print(p.info)
        return [dict(age=int(p.info[0:2]),
                     group=(p.info[2:12]),
                     name=(p.info[13:]))] + p.infooo

    @_('STUDENTS')
    def info(self, p):
        return p[0][1:-1]

    @_('name')
    def title(self, p):
        return '"' + p.name + "'"

    @_('name names')# Название группы + новое изначально names вернуло пустоту
    def names(self, p):
        return [p.name] + p.names

    @_('empty')
    def infooo(self, p):
        print("kak1")
        return []

    @_('empty')
    def names(self, p):
        print("kak")
        return []

    @_('NAMEGROUP')
    def name(self, p):

        return p[0]

    @_('STUDENTS')
    def name(self, p):
        return p[0][1:-1]

    @_('')
    def empty(self, p):
        pass

if __name__ == '__main__':
    a = 'check.txt'
    f = open(a, 'r', encoding='utf-8')
    text = f.read()
    f.close()


    lexer = CalcLexer()
    parser = CalcParser()



    data = (parser.parse(lexer.tokenize(text)))
    # for tok in lexer.tokenize(text):
    #     print('type=%r, value=%r' % (tok.type, tok.value))
    with open('output.json', 'w') as f:
        f.write(json.dumps(data, indent=3, ensure_ascii=False))
