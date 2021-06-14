import numpy as np
import time


# Easy for Brute Force
s1 = [[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]

# Hard for Brute Force
s2 = [[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,3,0,8,5],
      [0,0,1,0,2,0,0,0,0],
      [0,0,0,5,0,7,0,0,0],
      [0,0,4,0,0,0,1,0,0],
      [0,9,0,0,0,0,0,0,0],
      [5,0,0,0,0,0,0,7,3],
      [0,0,2,0,1,0,0,0,0],
      [0,0,0,0,4,0,0,0,9]]


def _check_position(sodoku, i, j, number):
    if sodoku[i,j] != 0:
        return False
    if number in sodoku[i,:]:
        return False
    if number in sodoku[:,j]:
        return False

    # Check quadrants
    if i <= 2:
        if j <= 2:
            if number in sodoku[:3,:3]:
                return False
        elif j <= 5:
            if number in sodoku[:3,3:6]:
                return False
        else:
            if number in sodoku[:3,6:]:
                return False
    elif i <= 5:
        if j <= 2:
            if number in sodoku[3:6,:3]:
                return False
        elif j <= 5:
            if number in sodoku[3:6,3:6]:
                return False
        else:
            if number in sodoku[3:6,6:]:
                return False
    else:
        if j <= 2:
            if number in sodoku[6:,:3]:
                return False
        elif j <= 5:
            if number in sodoku[6:,3:6]:
                return False
        else:
            if number in sodoku[6:,6:]:
                return False

    return True

def solver(sodoku):
    while np.sum(sodoku) < 405:
        for i in range(9):
            for j in range(9):
                if sodoku[i,j] == 0:
                    possible = []
                    for n in range(1,10):
                        if _check_position(sodoku, i, j, n):
                            possible.append(n)
                    if len(possible) == 1:
                        sodoku[i,j] = possible[0]
    return sodoku


if __name__ == "__main__":
    t1 = time.time()
    sodoku = np.array(s1)
    print(solver(sodoku))
    print(time.time() - t1)
