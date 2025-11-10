# I have root?

Sebuah program untuk membuat fungsi yang menentukan apakah sebuah array (list) 1-dimensi dari integer mengikuti aturan *squaring* yang ketat.

## 📝 Description

Program ini mengimplementasikan sebuah fungsi untuk mengecek apakah sebuah array integer bersifat "pangkat." Ini berarti bahwa untuk **setiap** pasangan elemen yang bersebelahan, nilai elemen di depan (kiri) harus merupakan **akar kuadrat** dari elemen di belakangnya (kanan).

Dengan kata lain, untuk setiap pasangan `(a, b)`, kondisi $a^2 = b$ harus terpenuhi.

-----

## 🎯 Problem Statement

### Input:

  * Sebuah array (list) 1-dimensi berisi integer.

### Output:

  * Sebuah nilai boolean (`True` atau `False`).
      * `True` jika **setiap** elemen adalah hasil kuadrat dari elemen sebelumnya.
      * `False` jika ada *satu saja* pasangan yang tidak memenuhi aturan ini.

### Rules:

1.  Program harus membandingkan setiap pasangan elemen yang bersebelahan (misalnya, `arr[i]` dan `arr[i+1]`).
2.  Kondisi yang harus dipenuhi adalah `arr[i] * arr[i] == arr[i+1]`.
3.  Jika kondisi ini gagal *meskipun hanya satu kali*, fungsi harus segera mengembalikan `False`.
4.  Jika seluruh array selesai diperiksa tanpa menemukan pelanggaran (atau jika array memiliki 0 atau 1 elemen), fungsi mengembalikan `True`.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[1, 2, 4, 16]
```

**Output:**

```
False
```

**Explanation:** Pengecekan gagal pada pasangan pertama. `1 * 1` tidak sama dengan `2`. (Catatan: Ini berbeda dari output sampel Anda, tetapi konsisten dengan deskripsi aturan).

### Example 2 (Sample 2)

**Input:**

```
[1, 2, 4, 8]
```

**Output:**

```
False
```

**Explanation:** Pengecekan gagal pada pasangan pertama (`1 * 1 != 2`), dan juga pada pasangan terakhir (`4 * 4 != 8`).

### Example 3 (Sample 3)

**Input:**

```
[1, 2, 3, 5, 19]
```

**Output:**

```
False
```

**Explanation:** Pengecekan gagal pada pasangan pertama (`1 * 1 != 2`).

### Example 4 (Contoh yang Benar)

**Input:**

```
[2, 4, 16]
```

**Output:**

```
True
```

**Explanation:** `2 * 2 = 4` (Benar), dan `4 * 4 = 16` (Benar). Semua pasangan memenuhi aturan.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/check-square-root-progression.git
    cd check-square-root-progression
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Masukkan array dalam format list (misalnya, `[2, 4, 16]`) saat diminta untuk melihat hasilnya.
