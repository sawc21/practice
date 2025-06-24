def store_highscore(dictionary, fn="file.txt", top_n=0):
    with open(fn, "w") as f:
        for idx, (name, pts) in enumerate(sorted(dictionary.items())):
            f.write(f'{name}:{pts}')
            if top_n and idx == top_n - 1:
                break

def load_highscore(fn ="file.txt"):
    hs = {}
    try:
        with open(fn, "r") as f:
            for line in f:
                name, _, points = line.partition(":")
                if name and points:
                    hs[name] = int(points)
    except FileNotFoundError:
        return {}
    return hs

k = load_highscore()

k["p"]=10
k["a"]=110
k["k"]=1110
k["l"]=1022
print(k)
store_highscore(k, top_n=3)

# load back into new dict
kk = load_highscore()
print(kk)