def count_carbons(smiles):
    cnt = 0
    cnt += smiles.count("C")
    cnt += smiles.count("c")
    return cnt


def wrong_count_nitorgens(smiles):
    cnt = 0
    cnt = smiles.count("N")
    cnt = smiles.count("n")
    return cnt

