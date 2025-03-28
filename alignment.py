from unrestricted import unrest
from banded import banded
import math

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
    if banded_width== -1:
        score, al1,al2 = unrest(seq1,seq2,match_award,indel_penalty,sub_penalty,gap)
    else:

        if abs(len(seq1) - len(seq2)) > banded_width:
            return math.inf, None, None

        score, al1,al2 = banded(seq1,seq2,match_award,indel_penalty,banded_width,sub_penalty,gap)
    return score, al1,al2



if __name__ == "__main__":
    seq1 = 'GGGGTTTTAAAACCCCTTTT'
    seq2 = 'TTTTAAAACCCCTTTTGGGG'
    cost, alignment1, alignment2 = banded(seq1, seq2, banded_width=2)
    print(cost)
    print(alignment1)
    print(alignment2)


