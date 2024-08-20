import csv
import time

# Klasa przechowująca dane ocen
class RatingData:
    def __init__(self, id, title, rating):
        self.id = id
        self.title = title
        self.rating = rating

MAX_RANKINGS = 1000000

# Funkcja usuwająca puste wpisy w polu ranking
def remove_empty_ratings(arr):
    return [rating for rating in arr if rating.rating > 0]

# Funkcja scalająca dwie posortowane części tablicy w jedną posortowaną tablicę
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Tworzenie tymczasowych list dla lewej i prawej części
    leftArray = arr[left:mid + 1]
    rightArray = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if leftArray[i].rating <= rightArray[j].rating:
            arr[k] = leftArray[i]
            i += 1
        else:
            arr[k] = rightArray[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = leftArray[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = rightArray[j]
        j += 1
        k += 1

# Implementacja algorytmu sortowania przez scalanie
def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        # Sortowanie pierwszej i drugiej połowy
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Scalanie posortowanych połówek
        merge(arr, left, mid, right)

def main():
    # Wczytanie danych z pliku
    filename = 'C:\\Users\\Dell\\Downloads\\Dane.csv'
    ratings = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Pomijanie nagłówka
        for row in csvreader:
            if len(ratings) >= MAX_RANKINGS:
                break
            id = int(row[0])
            title = row[1]
            rating = float(row[2])
            if rating <= 10.0:
                ratings.append(RatingData(id, title, rating))

    ratings = remove_empty_ratings(ratings)

    # Sortowanie i mierzenie czasu dla różnych ilości danych
    for num in [10000, 100000, 500000, 1000000, len(ratings)]:
        start_time = time.time()
        merge_sort(ratings, 0, min(num, len(ratings)) - 1)
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1e6
        print(f"Czas sortowania dla {num} elementów: {elapsed_ms:.2f} mikrosekundy")

if __name__ == "__main__":
    main()
