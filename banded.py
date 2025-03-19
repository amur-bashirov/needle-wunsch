def banded(
        seq1: str,
        seq2: str,
        match_award=-3,
        indel_penalty=5,
        banded_width=-1,
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
    arr = [[0] * (col + 2) for _ in range(row + 2)]

    letters1 = list(seq2)
    letters2 = list(seq1)

    arr[0][1] = " "
    arr[1][0] = " "


    for i in range(2, col + 2):
        arr[0][i] = letters1[i - 2] + " "

    for i in range(2, row + 2):
        arr[i][0] = letters2[i - 2] + " "

    for i in range(row + 2):
        string = "|"
        for j in range(col + 2):
            string += f" {arr[i][j]} |"
        print(string)







def retrace(arr, alignment1, alignment2, col, row,
            match_award=-3,
            indel_penalty=5,
            sub_penalty=1,
            gap='-'):
    current = (row + 1, col + 1)

    while current[0] != 0 and current[1] != 0:
        i = current[0]
        j = current[1]
        print(arr[i][j])
        if j < 2:
            letter2 = alignment2[0]
            delete = float('inf')
            substitution = float('inf')
        else:
            letter2 = alignment2[j - 2]
            delete = arr[i][j - 1] + indel_penalty
        if i < 2:
            letter1 = alignment1[0]
            insert = float('inf')
            substitution = float('inf')
        else:
            letter1 = alignment1[i - 2]
            insert = arr[i - 1][j] + indel_penalty
        if j >= 2 and i >= 2:
            substitution = arr[i - 1][j - 1] + (match_award if letter1 == letter2 else sub_penalty)

        if substitution <= delete and substitution <= insert:
            current = (i - 1, j - 1)

        elif delete <= insert:
            current = (i, j - 1)
            if i - 2 < 0:
                temp = alignment1[0]
                alignment1[0] = gap
                alignment1.insert(1, temp)

            else:
                temp = alignment1[i - 2]
                alignment1[i - 2] = gap
                alignment1.insert(i - 2, temp)



        else:
            current = (i - 1, j)
            if j - 2 < 0:
                temp = alignment2[0]
                alignment2[0] = gap
                alignment2.insert(1, temp)

            else:
                temp = alignment2[j - 2]
                alignment2[j - 2] = gap
                alignment2.insert(j - 2, temp)


if __name__ == "__main__":
    seq1 = 'ATGCATGC'
    seq2 = 'ATGGTGC'
    banded(seq1, seq2)
