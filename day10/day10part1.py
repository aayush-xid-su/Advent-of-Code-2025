import re
from functools import lru_cache
from itertools import combinations
import sys

def parse_machine_line(line: str):
    line = line.strip()
    if not line:
        return None
    m = re.search(r'\[([.#]+)\]', line)
    if not m:
        raise ValueError("Bad line, no [..] part: " + line)
    lights_s = m.group(1)
    num_lights = len(lights_s)
    target_mask = 0
    for i, ch in enumerate(lights_s):
        if ch == '#':
            target_mask |= (1 << i)

    buttons = []
    for pm in re.finditer(r'\(([^)]*)\)', line):
        inner = pm.group(1).strip()
        if inner == '':
            buttons.append(0)
            continue
        parts = [p.strip() for p in inner.split(',') if p.strip() != '']
        mask = 0
        for part in parts:
            idx = int(part)
            if idx < 0 or idx >= num_lights:
                raise ValueError(f"button index {idx} out of range for {line}")
            mask |= (1 << idx)
        buttons.append(mask)

    return num_lights, buttons, target_mask

def gaussian_elim_rows(rows, rhs, nvars):
    m = len(rows)
    rows = rows[:]
    rhs = rhs[:]
    pivot_col_for_row = [-1] * m
    where = {}
    row = 0
    for col in range(nvars):
        sel = -1
        for r in range(row, m):
            if (rows[r] >> col) & 1:
                sel = r
                break
        if sel == -1:
            continue
        rows[row], rows[sel] = rows[sel], rows[row]
        rhs[row], rhs[sel] = rhs[sel], rhs[row]
        pivot_col_for_row[row] = col
        where[col] = row
        for r in range(m):
            if r != row and ((rows[r] >> col) & 1):
                rows[r] ^= rows[row]
                rhs[r] ^= rhs[row]
        row += 1
        if row == m:
            break
        
    for r in range(row, m):
        if rows[r] == 0 and rhs[r] == 1:
            return False, row, pivot_col_for_row, where, rows, rhs
    return True, row, pivot_col_for_row, where, rows, rhs

def find_particular_and_nullspace(trans_rows, trans_rhs, where, nvars):
   
    m = len(trans_rows)
    p = 0
    pivot_of_row = {}
    for r, col in enumerate([where_k for where_k in range(nvars) if False]):
        pass
    col2row = {}
    for col, r in where.items():
        col2row[col] = r
    for col, r in where.items():
        if trans_rhs[r] & 1:
            p |= (1 << col)
    free_cols = [c for c in range(nvars) if c not in where]
    basis = []
    for fcol in free_cols:
        vec = 1 << fcol
        for pc, r in where.items():
            if (trans_rows[r] >> fcol) & 1:
                vec |= (1 << pc)
        basis.append(vec)
    return p, basis

def minimal_weight_solution(nvars, rows_mask, rhs_bits):

    solvable, rank, pivot_col_for_row, where, trans_rows, trans_rhs = gaussian_elim_rows(rows_mask, rhs_bits, nvars)
    if not solvable:
        return None
    p, basis = find_particular_and_nullspace(trans_rows, trans_rhs, where, nvars)
    d = len(basis)

    if d == 0:
        return p
    if d <= 24:
        best = None
        best_w = nvars + 1

        for mask in range(1 << d):
            combo = 0

            i = 0
            mm = mask
            while mm:
                lsb = mm & -mm
                idx = (lsb.bit_length() - 1)
                combo ^= basis[idx]
                mm &= mm - 1
            candidate = p ^ combo
            w = candidate.bit_count()
            if w < best_w:
                best_w = w
                best = candidate
        return best
    else:
        if d <= 40:
            d1 = d // 2
            left = basis[:d1]
            right = basis[d1:]
            left_map = {}
            for msk in range(1 << len(left)):
                vec = 0
                mm = msk
                idx = 0
                while mm:
                    lsb = mm & -mm
                    idb = (lsb.bit_length() - 1)
                    vec ^= left[idb]
                    mm &= mm - 1
                left_map.setdefault(vec, 0)
            best = None
            best_w = nvars + 1
            for msk in range(1 << len(right)):
                vecr = 0
                mm = msk
                while mm:
                    lsb = mm & -mm
                    idb = (lsb.bit_length() - 1)
                    vecr ^= right[idb]
                    mm &= mm - 1

                for vecl in left_map.keys():
                    candidate = p ^ vecl ^ vecr
                    w = candidate.bit_count()
                    if w < best_w:
                        best_w = w
                        best = candidate
            return best
        else:

            candidate = p
            improved = True
            iter_count = 0
            while improved and iter_count < 1000:
                improved = False
                iter_count += 1
                for b in basis:
                    newcand = candidate ^ b
                    if newcand.bit_count() < candidate.bit_count():
                        candidate = newcand
                        improved = True

            return candidate

def solve_all_from_file(fname="day10input.txt"):
    total = 0
    with open(fname, "r", encoding="utf-8") as f:
        for li, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parsed = parse_machine_line(line)
            if parsed is None:
                continue
            nlights, buttons, target = parsed
            m = len(buttons)

            rows_mask = []
            rhs_bits = []
            for i in range(nlights):
                rowmask = 0
                for j, bmask in enumerate(buttons):
                    if (bmask >> i) & 1:
                        rowmask |= (1 << j)
                rows_mask.append(rowmask)
                rhs_bits.append((target >> i) & 1)

            sol = minimal_weight_solution(m, rows_mask, rhs_bits)
            if sol is None:
                raise ValueError(f"Machine on line {li} has no solution")
            presses = sol.bit_count()
            total += presses
    return total

if __name__ == "__main__":
    ans = solve_all_from_file("day10input.txt")
    print(ans)
