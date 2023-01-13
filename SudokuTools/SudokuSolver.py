def get_column_id(index:int):
    return index%9
def get_row_id(index:int):
    return index//9
def get_box_id(index:int):
    return get_column_id(index)//3+(get_row_id(index)//3)*3

class Column:
    def __init__(self,id:int):
        self.id= id
        self.values=set()

    def __str__(self):
        return f'Column {self.id} with values {self.values}.'

    def possible_values(self):
        return set(range(1,10)) - self.values

    def add_value(self, value:int):
        self.values.add(value)

class Row:
    def __init__(self,id:int):
        self.id= id
        self.values=set()

    def __str__(self):
        return f'Row {self.id} with values {self.values}.'

    def possible_values(self):
        return set(range(1,10)) - self.values

    def add_value(self, value:int):
        self.values.add(value)
        
class Box:
    def __init__(self,id:int):
        self.id=id
        self.values=set()

    def __str__(self):
        return f'Box {self.id} with values {self.values}.'

    def possible_values(self):
        return set(range(1,10)) - self.values

    def add_value(self, value:int):
        self.values.add(value)

class Cell:
    def __init__(self, row:Row, column:Column, box:Box, value=0):
        self.row=row
        self.column=column
        self.box=box
        if value!= 0:
            self.update_puzzle(value)
        else:
            self.value=value
    
    def __str__(self):
        return f'[value:{self.value}, column:{self.column}, row:{self.row}, box:{self.box}]'

    def __int__(self):
        return self.value
    
    def update(self):
        possible_values = set(range(1,10)) - self.column.values - self.row.values - self.box.values

        if len(possible_values)==1:
            self.update_puzzle(list(possible_values)[0])
            return self.value
        else:
            return 0


    def update_puzzle(self, value:int):
        self.column.add_value(value)
        self.row.add_value(value)
        self.box.add_value(value)
        self.value=value

class Puzzle:
    def __init__(self, numbers:str):
        '''
        numbers: A 81 digit integer that's used to denote a sudoku puzzle read left to right starting at the top going down to the bottom.
        '''
        self.rows = [Row(x) for x in range(0,9)]
        self.columns = [Column(x) for x in range(0,9)]
        self.boxes = [Box(x) for x in range(0,9)]
        self.cells = []
    
        for index, num in enumerate(str(numbers)):
            self.cells.append(Cell(self.rows[get_row_id(index)], self.columns[get_column_id(index)], self.boxes[get_box_id(index)], int(num)))


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
