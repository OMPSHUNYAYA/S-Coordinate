import hashlib
import matplotlib.pyplot as plt

# ----------------------------------------
# Structural Coordinate Definition
# ----------------------------------------

C = {
    "x": 1,
    "y": 1,
    "z": 0,
    "S": "RESOLVED",   # Change to: INCOMPLETE / CONFLICT
    "tau": "VALID",
    "frame": "LOCAL-STRUCTURAL-FRAME"
}

# ----------------------------------------
# Structural Certificate (sigma)
# ----------------------------------------

def cert(C):
    raw = f'{C["x"]}|{C["y"]}|{C["z"]}|{C["S"]}|{C["tau"]}|{C["frame"]}'
    return hashlib.sha256(raw.encode()).hexdigest()[:16]

# ----------------------------------------
# Structural Visibility Resolver
# ----------------------------------------

def visible(C):
    sigma = cert(C)
    if C["S"] == "RESOLVED" and C["tau"] == "VALID" and sigma:
        return "VISIBLE", sigma
    return "NOT_VISIBLE", sigma

# ----------------------------------------
# Resolve State
# ----------------------------------------

state, sigma = visible(C)

print(state)
print("certificate:", sigma)

# ----------------------------------------
# Visual Rendering (Structure -> View)
# ----------------------------------------

fig, ax = plt.subplots()

# Plot coordinate
if state == "VISIBLE":
    ax.plot(C["x"], C["y"], marker="o", markersize=14)
    ax.text(
        C["x"] + 0.05,
        C["y"] + 0.10,
        "VISIBLE",
        ha="left",
        fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3")
    )
else:
    ax.plot(C["x"], C["y"], marker="x", markersize=14)
    ax.text(
        C["x"] + 0.05,
        C["y"] + 0.10,
        "NOT VISIBLE",
        ha="left",
        fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3")
    )

# Structural metadata block
ax.text(
    C["x"],
    C["y"] - 0.30,
    "S: " + C["S"] + "\n"
    "tau: " + C["tau"] + "\n"
    "sigma: " + sigma,
    ha="center",
    fontsize=10
)

# Plot settings
ax.set_title("Structural Coordinate Resolution")
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_aspect("equal")
ax.grid(True)

plt.show()