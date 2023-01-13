class Cell:
    def __init__(self, value=0):
        self.in_column=[]
        self.in_row=[]
        self.in_box=[]
        self.value=value
    
    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)
    
    def update(self):
        possible_values = self.possible_values()
        if len(possible_values)==1:
            self.value=list(possible_values)[0]
            return self.value
        else:
            return 0
    
    def possible_values(self):
        column_values=set([int(cell) for cell in self.in_column])
        row_values=set([int(cell) for cell in self.in_row])
        box_values=set([int(cell) for cell in self.in_box])
        return set(range(1,10)) - column_values - row_values - box_values

    def set_column(self, column:list):
        self.in_column=column

    def set_row(self, row:list):
        self.in_row=row

    def set_box(self, box:list):
        self.in_box=box

class Puzzle:
    def __init__(self, numbers:str):
        '''
        numbers: A 81 digit integer that's used to denote a sudoku puzzle read left to right starting at the top going down to the bottom.
        '''
        self.cells = []
        self.solutions=set()


        columns = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]
        boxes=[[] for _ in range(9)]
        for index, num in enumerate(str(numbers)):
            cell=Cell(num)
            self.cells.append(cell)
            column_num=index//9
            row_num=index%9
            columns[column_num].append(cell)
            rows[row_num].append(cell)
            boxes[column_num//3+(row_num//3)*3].append(cell)
        
        for x in range(9):
            for cell in columns[x]:
                cell.set_column(columns[x])

            for cell in rows[x]:
                cell.set_row(rows[x])

            for cell in boxes[x]:
                cell.set_box(boxes[x])

    def __int__(self) -> int:
        return int(''.join(str(int(x)) for x in self.cells))
    
    def __str__(self) -> str:
        num=str(int(self))
        if len(num) < 81:
            num='0'+num
        out=""
        for x in range(0,9):
            out+=f'{num[0+x*9:9+x*9]}\n'
        return out
    
    def solve(self):
        updated = True
        while updated:
            updated = False
            for cell in self.cells:
                if int(cell) == 0:
                    if cell.update() != 0:
                        updated = True
        
        #If there are still 0s after reducing the puzzle then solve the remaining recursively.
        if '0' in str(self):
            print('solve more')
