def longest_common_substrs(a,b):
    """
    >>> longest_common_substrs('ABABC', 'BABCA')
    ['BABC']
    >>> longest_common_substrs('ABABC', 'ABCBA')
    ['ABC']
    >>> longest_common_substrs('FROODHOOPY', 'HOOPYFROOD')
    ['FROOD', 'HOOPY']
    """
    tbl = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    longest_len = 0
    longest_substrs = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                tbl[i+1][j+1] = tbl[i][j] + 1
                if tbl[i+1][j+1] > longest_len:
                    longest_len = tbl[i+1][j+1]
                    longest_substrs = [a[i-longest_len+1:i+1]]
                elif tbl[i+1][j+1] == longest_len:
                    longest_substrs.append(a[i-longest_len+1:i+1])
            else:
                tbl[i+1][j+1] = 0
    return longest_substrs
