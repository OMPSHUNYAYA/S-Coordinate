import hashlib

C = {
    "x": 1,
    "y": 1,
    "z": 0,
    "S": "RESOLVED",
    "tau": "VALID",
    "frame": "LOCAL-STRUCTURAL-FRAME"
}

def cert(C):
    raw = f'{C["x"]}|{C["y"]}|{C["z"]}|{C["S"]}|{C["tau"]}|{C["frame"]}'
    return hashlib.sha256(raw.encode()).hexdigest()[:16]

def visible(C):
    sigma = cert(C)
    if C["S"] == "RESOLVED" and C["tau"] == "VALID" and sigma:
        return "VISIBLE", sigma
    return "NOT_VISIBLE", sigma

state, sigma = visible(C)

print(state)
print("certificate:", sigma)