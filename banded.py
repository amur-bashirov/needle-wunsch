def banded(
        seq1: str,
        seq2: str,
        match_award=-3,
        indel_penalty=5,
        banded_width=-1,
        sub_penalty=1,
        gap='-'
) -> tuple[float, str | None, str | None]:

    col = len(seq1)
    arr = [[0]]
    d = banded_width


    alignment1 = list(seq1)
    alignment2 = list(seq2)

    shift_count = 0
    for i in range(col + 1):
        shift = False
        if i != 0:
            arr.append([])
        if i >= d+1:
            shift = True
            shift_count += 1
        for j in range(d+i+1):
            if j > len(alignment2) or (shift and j >= (2*d+1)):
                break
            if shift and j + shift_count > len(alignment2):
                break
            if i == 0 and j == 0: continue

            insert, letter1 = calc_insert(i,j,arr,alignment1, indel_penalty,shift)
            delete, letter2 = calc_delete(i,j,arr,alignment2, indel_penalty,shift, shift_count)
            substitution = calc_substitution(i,j,arr,letter1,letter2,match_award,sub_penalty,shift)



            if substitution <= delete and substitution <= insert:
                arr[i].append(substitution)


            elif delete <= insert:
                arr[i].append(delete)

            else:
                arr[i].append(insert)


    last_col = arr[col]
    cost = arr[col][len(last_col)-1]

    og_alignment1 = alignment1.copy()
    og_alignment2 = alignment2.copy()

    retrace(og_alignment1,og_alignment2, arr, alignment1, alignment2, col, d, match_award,
            indel_penalty,
            sub_penalty,
            gap,)
    alignment1 = "".join(alignment1)
    alignment2 = "".join(alignment2)

    return cost, alignment1, alignment2




def calc_insert(i,j,arr,alignment1, indel_penalty=5,shift=False):
    if shift:
        if i < 1:
            letter1 = alignment1[0]
            insert = float('inf')
        elif j >= len(arr[i - 1])-1:
            letter1 = alignment1[i - 1]
            insert = float('inf')
        else:
            letter1 = alignment1[i - 1]
            insert = arr[i - 1][j+1] + indel_penalty

        return insert, letter1
    else:
        if i < 1 :
            letter1 = alignment1[0]
            insert = float('inf')
        elif j >=len(arr[i - 1])-1:
            letter1 = alignment1[i - 1]
            insert = float('inf')
        else:
            letter1 = alignment1[i - 1]
            insert = arr[i - 1][j] + indel_penalty


        return insert,letter1



def calc_delete(i,j,arr,alignment2, indel_penalty=5,shift=False, shift_count=0):
    if shift:
        if j<1:
            letter2 = alignment2[shift_count-1]
            delete = float('inf')
        else:
            letter2 = alignment2[j - 1 + shift_count]
            delete = arr[i][j - 1] + indel_penalty
        return delete, letter2
    else:
        if j < 1:
            letter2 = alignment2[0]
            delete = float('inf')
        else:
            letter2 = alignment2[j - 1]
            delete = arr[i][j - 1] + indel_penalty

        return delete,letter2



def calc_substitution(i,j,arr,letter1,letter2,match_award=-3,sub_penalty=1,shift=False):
    if shift:
        substitution = arr[i - 1][j ] + (match_award if letter1 == letter2 else sub_penalty)
        return substitution
    else:
        if j >= 1 and i >= 1:
            substitution = arr[i - 1][j - 1] + (match_award if letter1 == letter2 else sub_penalty)
        else:
            substitution = float('inf')
        return substitution



def retrace(og_alignment1,og_alignment2,arr, alignment1, alignment2, col, d,
            match_award=-3,
            indel_penalty=5,
            sub_penalty=1,
            gap='-',):
    last_col = arr[col]
    current = [ col, len(last_col) - 1]


    shift_count = len(arr) - d-1
    while not (current[0] == 0 and current[1] == 0):
        i = current[0]
        j = current[1]
        print(arr[i][j])



        stop_shift = False
        shift = False
        if i < d+1:
            stop_shift = True
        if stop_shift!= True:
            shift = True



        insert, letter1 = calc_insert(i, j, arr, alignment1, indel_penalty, shift)
        delete, letter2 = calc_delete(i, j, arr, alignment2, indel_penalty, shift, shift_count)
        if shift:
            letter1_corr = og_alignment1[i - 1]
            letter2_corr = og_alignment2[j-1 + shift_count]
        else:
            letter1_corr = og_alignment1[i - 1]
            letter2_corr = og_alignment2[j - 1]
        substitution = calc_substitution(i, j, arr, letter1_corr, letter2_corr, match_award, sub_penalty, shift)




        if shift:


            if substitution <= delete and substitution <= insert:
                current = [i - 1, j]
                shift_count -= 1

            elif delete <= insert:
                current = [i, j - 1]
                if i - 1 < 0:
                    temp = alignment1[0]
                    alignment1[0] = gap
                    alignment1.insert(1, temp)

                else:
                    temp = alignment1[i - 1]
                    alignment1[i - 1] = gap
                    alignment1.insert(i - 1, temp)



            else:
                current = [i - 1, j+1]
                shift_count -= 1
                if j - 1 < 0:
                    temp =alignment2[shift_count-1]
                    alignment2[shift_count-1] = gap
                    alignment2.insert(shift_count, temp)

                else:
                    temp = alignment2[j - 1 + shift_count]
                    alignment2[j - 1 + shift_count] = gap
                    alignment2.insert(j - 1 + shift_count, temp)



        else:



            if substitution <= delete and substitution <= insert:
                current = [i - 1, j - 1]

            elif delete <= insert:
                current = [i, j - 1]
                if i - 1 < 0:
                    temp = alignment1[0]
                    alignment1[0] = gap
                    alignment1.insert(1, temp)

                else:
                    temp = alignment1[i - 1]
                    alignment1[i - 1] = gap
                    alignment1.insert(i - 1, temp)



            else:
                current = [i - 1, j]
                if j - 1 < 0:
                    temp = alignment2[0]
                    alignment2[0] = gap
                    alignment2.insert(1, temp)

                else:
                    temp = alignment2[j ]
                    alignment2[j] = gap
                    alignment2.insert(j+1, temp)





if __name__ == "__main__":
    seq1 = 'GGGGTTTTAAAACCCCTTTT'
    seq2 = 'TTTTAAAACCCCTTTTGGGG'
    cost, alignment1, alignment2 = banded(seq1, seq2, banded_width=2)
    print(cost)
    print(alignment1)
    print(alignment2)
