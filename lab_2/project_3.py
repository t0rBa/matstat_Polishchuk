import matplotlib.pyplot as plt

vowels = "аеєиіїоуюя"

freq = {v: 0 for v in vowels}

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

for char in text:
    if char in vowels:
        freq[char] += 1

letters = list(freq.keys())
counts = list(freq.values())

plt.bar(letters, counts, color="skyblue")
plt.xlabel("Голосні літери")
plt.ylabel("Кількість появ")
plt.title("Гістограма частоти голосних літер")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("vowels_histogram.png")
plt.show()
