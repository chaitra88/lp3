{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0750e5b6-447f-4620-bd86-ae9ed1308e34",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_board(board,n):\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            print(board[i][j],end=\" \")\n",
    "        print()\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "623ce30f-7a23-42d5-80e1-d575e1bc5ec3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def isSafe(board,row,col,n):\n",
    "    for i in range(n):\n",
    "        if board[i][col]==1 and i!=row:\n",
    "            return False\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            if board[i][j]==1 and (abs(row-i))==abs(col-j):\n",
    "                return False\n",
    "    return True\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "acbdc7e0-9a03-419b-845f-921615520d65",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solve(board,row,n):\n",
    "    if row==n:\n",
    "        print_board(board,n)\n",
    "        return\n",
    "    if 1 in board[row]:\n",
    "        solve(board,row+1,n)\n",
    "        return\n",
    "    for col in range(n):\n",
    "        if isSafe(board,row,col,n):\n",
    "            board[row][col]=1\n",
    "            solve(board,row+1,n)\n",
    "            board[row][col]=0\n",
    "    return board"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "895d012b-56e5-4cb3-a594-77214bb7fbf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def n_queens(f_row,f_col,n):\n",
    "    board=[[0 for _ in range(n)]for _ in range(n)]\n",
    "    board[f_row][f_col]=1\n",
    "    solve(board,0,n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c4e9bcf8-1b8a-4146-acf6-10b7fc8d4e86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "entrer board size:  4\n",
      "enter first row (0--->n-1) 1\n",
      "enter first col (0--->n-1) 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 0 0 \n",
      "0 0 0 1 \n",
      "1 0 0 0 \n",
      "0 0 1 0 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"entrer board size: \"))\n",
    "fr=int(input(\"enter first row (0--->n-1)\"))\n",
    "fc=int(input(\"enter first col (0--->n-1)\"))\n",
    "n_queens(fr,fc,n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3fa3c0b-4469-46c7-b21c-4eaa50f9d90f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
