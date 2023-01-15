
from SudokuTools import SudokuSolver as st
import zipfile
import io
import csv
import os
import time
from tqdm import tqdm

max=100000
total_solve_time=0
errors=0


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(os.getcwd())

with zipfile.ZipFile("sudoku_archive.zip") as zipf:
    with zipf.open("sudoku.csv", "r") as f:
        reader = csv.reader(
            io.TextIOWrapper(f, newline='')
        )
        for index, row in enumerate(tqdm(reader, total=max)):
            if index == max:
                break
            elif index == 0:
                pass
            else:
                start_time = time.time()
                puzz=st.Puzzle(row[0])
                puzz.solve()
                solved=puzz.check(row[1])
                if not solved:
                    errors+=1
                total_solve_time+=time.time()-start_time

print(f'Errors: {errors}, total time: {total_solve_time/60} minutes, average time {total_solve_time/max} seconds.')
