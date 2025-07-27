from sympy import nthroot_mod, mod_inverse

p = 2**256 - 2**32 - 977          # secp256k1.p
y = 31282165107190493695021426851743201686364630648138188080113774344851451653480 % p      # 例として適当な y

k = (y*y - 7) % p

# ① 立方剰余テスト
if pow(k, (p-1)//3, p) != 1:
    raise ValueError("この y では点を作れません")

# ② キューブ根（x 候補を 3 個まとめて取得）
x_candidates = nthroot_mod(k, 3, p, all_roots=True)

for x in x_candidates:
    assert (x**3 + 7) % p == (y*y) % p     # 必ず一致
print(x_candidates)  # 3 つの x が得られる
