def banded(
        seq1: str,
        seq2: str,
        match_award=-3,
        indel_penalty=5,
        banded_width=7,
        sub_penalty=1,
        gap='-'
) -> tuple[float, str | None, str | None]:

    col = len(seq1)
    arr = [[0]]
    d = (banded_width - 1) // 2


    alignment1 = list(seq1)
    alignment2 = list(seq2)

    for i in range(col + 1):
        if i != 0:
            arr.append([])
        for j in range(d+i+1):

            if j < 1:
                letter2 = alignment2[0]
                delete = float('inf')
                substitution = float('inf')
            else:
                letter2 = alignment2[j - 1]
                delete = arr[i][j - 1] + indel_penalty
            if i < 1:
                letter1 = alignment1[0]
                insert = float('inf')
                substitution = float('inf')
            # try to check if previous len(list) smaller than j:
                letter1 = alignment1[i - 1]
                insert = arr[i - 1][j] + indel_penalty
            if j >= 1 and i >= 1:
                substitution = arr[i - 1][j - 1] + (match_award if letter1 == letter2 else sub_penalty)
            if i == 0 and j == 0:
                continue


            if substitution <= delete and substitution <= insert:
                arr[i].append(substitution)


            elif delete <= insert:
                arr[i].append(delete)

            else:
                arr[i].append(insert)


    cost = arr[col][d]

    return cost, alignment1, alignment2





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
    seq1 = 'THARS'
    seq2 = 'OTHER'
    banded(seq1, seq2)
