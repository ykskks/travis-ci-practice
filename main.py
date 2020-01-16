def count_carbons(smiles):
    cnt = 0
    cnt += smiles.count("C")
    cnt += smiles.count("c")
    return cnt