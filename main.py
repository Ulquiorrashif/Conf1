import zipfile
import sys

def main():
    name = "Arxive.zip"
    Away = "/root"
    pWay=""

    z = zipfile.ZipFile(name, 'r')
    allFiles=(z.namelist())
    cmd = input("~# ")
    while cmd != "exit":
        cmd=cmd.split(" ")
        if cmd[0] == "pwd":
            if pWay == "":
                print("/root")
            else:
                print("/root/" + pWay + "/")
        elif cmd[0] == "cat":
            if(pWay+"/"+cmd[1] in allFiles):
                with zipfile.ZipFile(name) as myzip:
                    myfile= myzip.open(pWay+"/"+cmd[1])
                    print(myfile.read())
            else:
                print("Невозможно открыть файл")
        elif cmd[0] == "ls":
            a=pWay
            counter = pWay.count('/')
            a += '/'

            for i in allFiles:
                if a == '/':
                    if a in i and i != a:
                        if counter == (i.count('/') - 1) and (i[len(i) - 1] == '/'):
                            b = i[:i.rfind("/")]
                            print(b, end="    ")
                else:
                    if a in i and i != a:
                        if counter == (i.count('/') - 2) and (i[len(i) - 1] == '/'):#Вывод папки
                            b = i[:i.rfind("/")]
                            print(b[b.rfind("/") + 1:], end="    ")
                        if counter == (i.count('/') - 1): #вывод обычного файла
                            b = i[i.rfind("/") + 1:]
                            print(b, end="    ")
            print()
        elif cmd[0] == "cd":
            if (len(cmd)==1):
                if (pWay.count("/")!=0):
                    pWay=(pWay[:pWay.rfind("/")])
                else:
                    pWay =""


            elif (cmd[1]==".."):
                    pWay=""
                    Wway=""
            else:
                pWay1=pWay

                if(pWay=="" ):
                    pWay += cmd[1]
                    if ((pWay+"/" in allFiles)==False):
                        pWay=pWay1
                        print(cmd[1] + " not found")
                else:
                    pWay +="/"
                    pWay += cmd[1]
                    if ((pWay+"/" in allFiles)==False):
                        pWay=pWay1
                        print(cmd[1] + " not found")

        else:
            print(cmd[0]+ " not found")
        cmd = input("~"+pWay+"# ")


main()