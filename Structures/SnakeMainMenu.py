import curses
import Users


class SnakeMainMenu(object):

#main class builder Menu
    def __init__(self,menu):
        self.menu = menu
        curses.wrapper(self.LoopGame)

#menu with while until the option is to exit
    def LoopGame(self,screenS):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        self.screenS = screenS
        self.screen_height, self.screen_width = self.screenS.getmaxyx()
        selectedRow = 0
        self.PrintAllMenu(selectedRow)

        while 1:
            KeyAtSelect = self.screenS.getch()
            if KeyAtSelect == curses.KEY_UP and selectedRow > 0:
                selectedRow -=1
            elif KeyAtSelect == curses.KEY_DOWN and selectedRow < len(self.menu) - 1:
                selectedRow +=1
            elif KeyAtSelect == curses.KEY_ENTER or KeyAtSelect in [10,13]:
                self.PrintCenter("You selected '{}'".format(self.menu[selectedRow]))
                self.screenS.getch()
                if selectedRow == len(self.menu) - 1:
                    if self.confirm("Are you sure you want to exit?"):
                        break
                if selectedRow == len(self.menu) -2:
                    if self.confirm("Do you want to BulkLoad?"):
                        cicular = Users.UsersList()
                        cicular.BulkLoad()
                if selectedRow == len(self.menu) -3:
                    if self.confirm("Do you Want to see Report?"):
                        cicular.GenerateReportUsers()
                if selectedRow == len(self.menu) -4:
                    data = cicular.first
                    while data.next!=None and KeyAtSelect != ord("q"):
                        if self.confirm("Para Avanzar a la Derecha Seleccione Yes \n Para Avanzar a la Izquierda Seleccione No\n"):
                            data = data.next
                            if self.confirm("El Dato es:"+data.data+"\n Presione Yes Para Seguir Visualizando.. \n Para Salir Presione No"):
                                print("sabe")
                            else:
                                break
                        else:
                            data = data.prev
                            if self.confirm("El Dato es:"+data.data+"\n Presione Yes Para seguir Visualizando.. \n Para Salir Presione No"):
                                print("sabe")
                            else:
                                break
            self.PrintAllMenu(selectedRow)
# here print everythink at the center of the panel
    def PrintCenter(self,Wtext):
        self.screenS.clear()
        x=self.screen_width//2-len(Wtext)// 2
        y=self.screen_height // 2
        self.screenS.addstr(y,x,Wtext)
        self.screenS.refresh()

#PrintAll the Menu when the options selected or move selector
    def PrintAllMenu(self,SelectedRow):
        self.screenS.clear()
        for xC,rowSe in enumerate(self.menu):
            x = self.screen_width // 2-len(rowSe)//2
            y = self.screen_height//2-len(menu)//2 + xC
            if xC == SelectedRow:
                self.ColorPrintPiC(y,x,rowSe,1)
            else:
                self.screenS.addstr(y,x,rowSe)
        self.screenS.refresh()

#The variable take the coordinates of the game
    def ColorPrintPiC(self,y,x,Wtext,num):
        self.screenS.attron(curses.color_pair(num))
        self.screenS.addstr(y,x,Wtext)
        self.screenS.attroff(curses.color_pair(num))

#The variable of the selection of each option
    def confirm(self,TextConfirmation):
        self.PrintCenter(TextConfirmation)
        SelectedOption = "yes"
        self.PrintConfirm(SelectedOption)

        while 1:
            KeyAtSelect = self.screenS.getch()

            if KeyAtSelect == curses.KEY_RIGHT and SelectedOption=="yes":
                SelectedOption="no"
            elif  KeyAtSelect == curses.KEY_LEFT and SelectedOption == "no":
                SelectedOption="yes"
            elif KeyAtSelect == curses.KEY_ENTER or KeyAtSelect in [10, 13]:
                return True if SelectedOption=="yes" else False
            self.PrintConfirm(SelectedOption)

#The option of the confirmation to each option
    def PrintConfirm(self,selected="yes"):
        curses.setsyx(self.screen_height//2+1,0)
        self.screenS.clrtoeol()
        y=self.screen_height//2+1
        WidthOption = 10
        Option="yes"
        x=self.screen_width//2-WidthOption//2+len(Option)
        if selected== Option:
            self.ColorPrintPiC(y,x,Option,1)
        else:
            self.screenS.addstr(y,x,Option)
        Option="no"
        x=self.screen_width//2+WidthOption//2-len(Option)
        if selected==Option:
            self.ColorPrintPiC(y,x,Option,1)
        else:
            self.screenS.addstr(y,x,Option)
        self.screenS.refresh()
    pass


menu = ['Play','Scoreboard', 'User Selection', 'Reports','Bulk Loading', 'Exit']
SnakeMainMenu(menu)
