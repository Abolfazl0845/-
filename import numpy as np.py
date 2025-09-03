import numpy as np

# --- مرحله ۱: ساخت بردار بدون تکرار ---
digits = list("0372280481")
unique_digits = sorted(set(digits))  # حذف تکرار
unique_digits = list(map(int, unique_digits))  # تبدیل به عدد صحیح

print(f"بردار بدون تکرار: {unique_digits}")

# --- مرحله ۲: ساخت ماتریس ۱۰x۱۰ ---
# تعداد لازم = 100 عدد
needed = 10 * 10
repeats = (needed // len(unique_digits)) + 1  # چند بار تکرار لازم داریم؟

full_list = (unique_digits * repeats)[:needed]  # تکرار و بریدن
matrix = np.array(full_list).reshape((10, 10))

print("\nماتریس ۱۰x۱۰ ساخته شده:")
print(matrix)

# --- مرحله ۳: عملیات ضرب و جمع روی ماتریس ---
product = np.prod(matrix)  # ضرب همه عناصر
summation = np.sum(matrix)  # جمع همه عناصر

print(f"\nحاصل ضرب همه عناصر ماتریس: {product}")
print(f"حاصل جمع همه عناصر ماتریس: {summation}")