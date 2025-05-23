def solve_n_queens(n):
    def backtrack(row=0, cols=set(), diagonals1=set(), diagonals2=set(), board=[]):
        if row == n:
            
            for r in board:
                print("".join(r))
            exit()
        for col in range(n):
            if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            cols.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            board.append(["Q" if c == col else "." for c in range(n)])
            backtrack(row + 1, cols, diagonals1, diagonals2, board)
            board.pop()
            cols.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    backtrack()

solve_n_queens(8)
