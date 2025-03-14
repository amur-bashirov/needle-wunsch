def unrest(
        seq1: str,
        seq2: str,
        match_award=-3,
        indel_penalty=5,
        sub_penalty=1,
        gap='-'
) -> tuple[float, str | None, str | None]:
    """
        Align seq1 against seq2 using Needleman-Wunsch
        Put seq1 on left (j) and seq2 on top (i)
        => matrix[i][j]
        :param seq1: the first sequence to align; should be on the "left" of the matrix
        :param seq2: the second sequence to align; should be on the "top" of the matrix
        :param match_award: how many points to award a match
        :param indel_penalty: how many points to award a gap in either sequence
        :param sub_penalty: how many points to award a substitution
        :param banded_width: banded_width * 2 + 1 is the width of the banded alignment; -1 indicates full alignment
        :param gap: the character to use to represent gaps in the alignment strings
        :return: alignment cost, alignment 1, alignment 2
    """
    col = len(seq2)
    row = len(seq1)
    alignment2 = list(seq1)


    arr = [[0] * (col + 2) for _ in range(row + 2)]


    letters1 = list(seq2)
    letters2 = list(seq1)


    arr[0][1] = " "
    arr[1][0] = " "

    for i in range(2, col + 2):
        arr[0][i] = letters1[i - 2] + " "

    for i in range(2, row + 2):
        arr[i][0] = letters2[i - 2] + " "




    for i in range(1, col+2):
        if arr[1][i-1]== " ": arr[1][i] = 0
        else:arr[1][i] = arr[1][i-1] + indel_penalty
    for j in range(1, row+2):
        if arr[j-1][ 1] == " ": arr[j][1] = 0
        else: arr[j][1] = arr[j-1][ 1] + indel_penalty


    for i in range(2, row+2):
        for j in range(2, col+2):
            delete = arr[i][j-1] + indel_penalty
            insert = arr[i-1][j] + indel_penalty
            substitution = arr[i-1][j-1] + (match_award if letters1[j-2] == letters2[i-2] else sub_penalty)


            if substitution <= delete and substitution <= insert:
                arr[i][j] = substitution

            elif delete <= insert:
                arr[i][j] = delete

            else:
                arr[i][j] = insert



    cost = arr[row + 1][col + 1]
    print(" ".join(alignment2))
    print(cost)


    for i in range(row + 2):
        string = "|"
        for j in range(col + 2):
            string += f" {arr[i][j]} |"
        print(string)


    return cost,seq2,seq1

if __name__ == "__main__":
    seq1 =  "AGTCGA"
    seq2 = "ATCGT"
    cost = unrest(seq1, seq2)
