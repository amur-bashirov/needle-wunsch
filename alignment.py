def align(
        seq1: str,
        seq2: str,
        match_award=-3,
        indel_penalty=5,
        sub_penalty=1,
        banded_width=-1,
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
    col = len(seq1)
    row = len(seq2)

    # Initialize matrix with correct dimensions
    arr = [[0] * (col + 2) for _ in range(row + 2)]

    # Convert sequences to list of characters
    letters1 = list(seq1)
    letters2 = list(seq2)

    # Fill the first row with seq2 characters and the first column with seq1 characters
    arr[0][1] = " "
    arr[1][0] = " "

    for i in range(2, col + 2):
        arr[0][i] = letters1[i - 2]  # Assign letters of seq1 in the first row

    for i in range(2, row + 2):
        arr[i][0] = letters2[i - 2]  # Assign letters of seq2 in the first column

    # Print the matrix
    for i in range(row + 2):
        string = "|"
        for j in range(col + 2):
            string += f" {arr[i][j]} |"
        print(string)


# Main function to test the alignment matrix
if __name__ == "__main__":
    seq1 = "OTHER"
    seq2 = "THARS"
    align(seq1, seq2)


