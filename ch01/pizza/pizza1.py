import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

# -----------------------------
# 가격/옵션 설정
# -----------------------------
PIZZA_TYPES = {
    "치즈": 3000,
    "페퍼로니": 3900,
    "콤비네이션": 4200,
    "하와이안": 4200,
    "베지": 3800,
}

SLICE_SIZE = {
    "레귤러 조각": 0,      # 기본가
    " 라지(큰) 조각": 800,  # +800원
}

CRUST = {
    "오리지널": 0,
    "씬": 0,
}

TOPPINGS = {
    "엑스트라 치즈": 700,
    "양송이": 500,
    "올리브": 500,
    "할라피뇨": 500,
    "베이컨": 900,
}

PICKUP_METHOD = {
    "매장 식사": 0,
    "포장": 0,
    "배달": 3000,
}

VAT_RATE = 0.10  # 10% 부가세
BULK_DISCOUNT_THRESHOLD = 5  # 총 조각 5조각 이상
BULK_DISCOUNT_RATE = 0.05    # 5% 할인


def krw(n):
    return f"{int(n):,}원"


class PizzaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("조각 피자 주문 프로그램")
        self.geometry("980x650")
        self.resizable(False, False)

        # 상태 데이터
        self.cart = []  # 각 아이템: dict
        self.delivery_fee = 0

        self._build_ui()

    # -----------------------------
    # UI 구성
    # -----------------------------
    def _build_ui(self):
        main = ttk.Frame(self, padding=10)
        main.pack(fill="both", expand=True)

        # 좌: 옵션/추가/요약, 우: 장바구니
        left = ttk.Frame(main)
        right = ttk.Frame(main)
        left.pack(side="left", fill="y")
        right.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # ---- (좌상) 피자 옵션
        opt = ttk.LabelFrame(left, text="1) 피자 옵션")
        opt.pack(fill="x", pady=(0, 8))

        # 피자 종류
        ttk.Label(opt, text="피자 종류").grid(row=0, column=0, sticky="w", padx=8, pady=6)
        self.var_type = tk.StringVar(value="치즈")
        cmb_type = ttk.Combobox(opt, textvariable=self.var_type, values=list(PIZZA_TYPES.keys()), state="readonly", width=18)
        cmb_type.grid(row=0, column=1, padx=8, pady=6)

        # 크기
        ttk.Label(opt, text="크기").grid(row=1, column=0, sticky="w", padx=8, pady=6)
        self.var_size = tk.StringVar(value="레귤러 조각")
        cmb_size = ttk.Combobox(opt, textvariable=self.var_size, values=list(SLICE_SIZE.keys()), state="readonly", width=18)
        cmb_size.grid(row=1, column=1, padx=8, pady=6)

        # 도우
        ttk.Label(opt, text="도우").grid(row=2, column=0, sticky="w", padx=8, pady=6)
        self.var_crust = tk.StringVar(value="오리지널")
        frm_crust = ttk.Frame(opt)
        frm_crust.grid(row=2, column=1, padx=8, pady=6, sticky="w")
        for c in CRUST.keys():
            ttk.Radiobutton(frm_crust, text=c, value=c, variable=self.var_crust).pack(side="left", padx=(0, 8))

        # 수량
        ttk.Label(opt, text="수량(조각)").grid(row=3, column=0, sticky="w", padx=8, pady=6)
        self.var_qty = tk.IntVar(value=1)
        spn_qty = tk.Spinbox(opt, from_=1, to=50, textvariable=self.var_qty, width=6)
        spn_qty.grid(row=3, column=1, padx=8, pady=6, sticky="w")

        # ---- (좌중) 토핑
        tpf = ttk.LabelFrame(left, text="2) 추가 토핑 (개당 추가요금)")
        tpf.pack(fill="x", pady=(0, 8))
        self.vars_toppings = {}
        col = 0
        row = 0
        for name, price in TOPPINGS.items():
            v = tk.BooleanVar(value=False)
            self.vars_toppings[name] = v
            chk = ttk.Checkbutton(tpf, text=f"{name} ({krw(price)})", variable=v, command=self._update_preview_price)
            chk.grid(row=row, column=col, sticky="w", padx=8, pady=4)
            col += 1
            if col == 2:
                col = 0
                row += 1

        # ---- (좌하) 수령 방법
        puf = ttk.LabelFrame(left, text="3) 수령 방법")
        puf.pack(fill="x", pady=(0, 8))
        self.var_pick = tk.StringVar(value="포장")
        for i, (k, fee) in enumerate(PICKUP_METHOD.items()):
            ttk.Radiobutton(puf, text=f"{k}" + (f" (+{krw(fee)})" if fee else ""), value=k, variable=self.var_pick, command=self._on_pick_change)\
                .grid(row=0, column=i, sticky="w", padx=8, pady=6)

        self.addr_label = ttk.Label(puf, text="배달 주소")
        self.addr_entry = ttk.Entry(puf, width=36)
        # 초기에는 배달 아님
        self.addr_label.grid(row=1, column=0, padx=8, pady=4, sticky="w")
        self.addr_entry.grid(row=1, column=1, padx=8, pady=4, sticky="w", columnspan=2)
        self._toggle_address()

        # ---- (좌하단) 미리보기 & 버튼
        pvf = ttk.LabelFrame(left, text="가격 미리보기")
        pvf.pack(fill="x", pady=(0, 8))

        self.lbl_preview = ttk.Label(pvf, text="", font=("맑은 고딕", 10, "bold"))
        self.lbl_preview.pack(anchor="w", padx=8, pady=6)

        btns = ttk.Frame(left)
        btns.pack(fill="x")
        ttk.Button(btns, text="장바구니 담기", command=self.add_to_cart).pack(side="left", padx=4, pady=4)
        ttk.Button(btns, text="현재 선택 초기화", command=self.reset_current_selection).pack(side="left", padx=4, pady=4)

        # 최초 미리보기 업데이트
        self._update_preview_price()

        # ---- (우) 장바구니 & 합계
        cartf = ttk.LabelFrame(right, text="장바구니")
        cartf.pack(fill="both", expand=True)

        cols = ("품목", "옵션", "토핑", "수량", "단가", "합계")
        self.tree = ttk.Treeview(cartf, columns=cols, show="headings", height=14)
        for c in cols:
            self.tree.heading(c, text=c)
        self.tree.column("품목", width=110, anchor="center")
        self.tree.column("옵션", width=160, anchor="w")
        self.tree.column("토핑", width=220, anchor="w")
        self.tree.column("수량", width=60, anchor="e")
        self.tree.column("단가", width=90, anchor="e")
        self.tree.column("합계", width=100, anchor="e")
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)

        cartbtn = ttk.Frame(cartf)
        cartbtn.pack(fill="x", padx=8, pady=(0, 8))
        ttk.Button(cartbtn, text="선택 항목 삭제", command=self.remove_selected).pack(side="left", padx=4)
        ttk.Button(cartbtn, text="장바구니 비우기", command=self.clear_cart).pack(side="left", padx=4)

        # 합계 영역
        totalf = ttk.LabelFrame(right, text="결제 요약")
        totalf.pack(fill="x")

        self.var_subtotal = tk.StringVar(value="0원")
        self.var_discount = tk.StringVar(value="0원")
        self.var_vat = tk.StringVar(value="0원")
        self.var_delivery = tk.StringVar(value="0원")
        self.var_total = tk.StringVar(value="0원")
        self.var_total_slices = tk.StringVar(value="0 조각")

        rows = [
            ("총 조각 수", self.var_total_slices),
            ("상품 소계", self.var_subtotal),
            (f"대량할인({BULK_DISCOUNT_THRESHOLD}조각↑ {int(BULK_DISCOUNT_RATE*100)}%)", self.var_discount),
            ("부가세(10%)", self.var_vat),
            ("배달요금", self.var_delivery),
            ("결제 금액", self.var_total),
        ]

        for i, (label, var) in enumerate(rows):
            ttk.Label(totalf, text=label).grid(row=i, column=0, sticky="w", padx=8, pady=4)
            ttk.Label(totalf, textvariable=var, font=("맑은 고딕", 10, "bold") if label == "결제 금액" else None)\
                .grid(row=i, column=1, sticky="e", padx=8, pady=4)

        finalbtn = ttk.Frame(right)
        finalbtn.pack(fill="x", pady=8)
        ttk.Button(finalbtn, text="영수증 저장", command=self.save_receipt).pack(side="left", padx=4)
        ttk.Button(finalbtn, text="결제(요약 보기)", command=self.checkout).pack(side="right", padx=4)

        self._recalc_totals()

    # -----------------------------
    # 이벤트/로직
    # -----------------------------
    def _on_pick_change(self):
        self._toggle_address()
        self._recalc_totals()

    def _toggle_address(self):
        is_delivery = (self.var_pick.get() == "배달")
        state = "normal" if is_delivery else "disabled"
        self.addr_entry.configure(state=state)
        # 라벨은 항상 보이되, 안내 텍스트 변경
        self.addr_label.configure(text="배달 주소" + (" (필수)" if is_delivery else " (배달 선택 시 입력)"))

    def _update_preview_price(self, *_):
        ptype = self.var_type.get()
        size = self.var_size.get()
        qty = max(1, self.var_qty.get())
        base = PIZZA_TYPES.get(ptype, 0)
        size_add = SLICE_SIZE.get(size, 0)
        topping_cost = sum(price for name, price in TOPPINGS.items() if self.vars_toppings.get(name, tk.BooleanVar()).get())
        unit = base + size_add + topping_cost
        preview = f"[미리보기] {ptype} / {size} / 도우:{self.var_crust.get()} / 수량:{qty}조각\n" \
                  f"  - 기본 {krw(base)} + 크기 {krw(size_add)} + 토핑 {krw(topping_cost)} = 1조각 단가 {krw(unit)}\n" \
                  f"  - 소계(단가×수량): {krw(unit * qty)}"
        self.lbl_preview.config(text=preview)

    def reset_current_selection(self):
        self.var_type.set("치즈")
        self.var_size.set("레귤러 조각")
        self.var_crust.set("오리지널")
        self.var_qty.set(1)
        for v in self.vars_toppings.values():
            v.set(False)
        self.var_pick.set("포장")
        self._toggle_address()
        self._update_preview_price()

    def add_to_cart(self):
        qty = self.var_qty.get()
        if qty < 1:
            messagebox.showwarning("안내", "수량은 1 이상이어야 합니다.")
            return

        # 배달 선택 시 주소 확인은 결제 시점에서 최종 검사

        ptype = self.var_type.get()
        size = self.var_size.get()
        crust = self.var_crust.get()
        toppings = [name for name, v in self.vars_toppings.items() if v.get()]

        # 단가 계산
        unit = PIZZA_TYPES[ptype] + SLICE_SIZE[size] + sum(TOPPINGS[t] for t in toppings)

        item = {
            "type": ptype,
            "size": size,
            "crust": crust,
            "toppings": toppings,
            "qty": qty,
            "unit": unit,
            "subtotal": unit * qty
        }
        self.cart.append(item)

        # 트리뷰에 추가
        opt_text = f"{size}, 도우:{crust}"
        tps = ", ".join(toppings) if toppings else "-"
        self.tree.insert("", "end", values=(ptype, opt_text, tps, qty, krw(unit), krw(unit * qty)))

        self._recalc_totals()
        self._update_preview_price()

    def remove_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("안내", "삭제할 항목을 선택하세요.")
            return
        # 선택된 항목의 인덱스를 역순으로 제거
        indices = []
        for iid in selected:
            idx = self.tree.index(iid)
            indices.append(idx)
        for iid in selected:
            self.tree.delete(iid)
        for idx in sorted(indices, reverse=True):
            if 0 <= idx < len(self.cart):
                self.cart.pop(idx)
        self._recalc_totals()

    def clear_cart(self):
        if not self.cart:
            return
        if messagebox.askyesno("확인", "장바구니를 모두 비우시겠습니까?"):
            self.cart.clear()
            for iid in self.tree.get_children():
                self.tree.delete(iid)
            self._recalc_totals()

    def _recalc_totals(self):
        subtotal = sum(item["subtotal"] for item in self.cart)
        total_slices = sum(item["qty"] for item in self.cart)

        # 대량할인
        discount = 0
        if total_slices >= BULK_DISCOUNT_THRESHOLD:
            discount = int(subtotal * BULK_DISCOUNT_RATE)

        # 배달료
        delivery = PICKUP_METHOD.get(self.var_pick.get(), 0)

        # 부가세(상품 - 할인)에 대해서만
        taxable = max(0, subtotal - discount)
        vat = int(taxable * VAT_RATE)

        total = taxable + vat + delivery

        # 상태 반영
        self.var_total_slices.set(f"{total_slices} 조각")
        self.var_subtotal.set(krw(subtotal))
        self.var_discount.set("-" + krw(discount) if discount else krw(0))
        self.var_vat.set(krw(vat))
        self.var_delivery.set(krw(delivery))
        self.var_total.set(krw(total))

    def _build_receipt_text(self):
        lines = []
        lines.append("=== 조각 피자 영수증 ===")
        lines.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        lines.append("")
        if self.cart:
            for i, it in enumerate(self.cart, 1):
                lines.append(f"[{i}] {it['type']} × {it['qty']}조각  (단가 {krw(it['unit'])}, 합계 {krw(it['subtotal'])})")
                lines.append(f"    옵션: {it['size']}, 도우:{it['crust']}")
                lines.append(f"    토핑: {', '.join(it['toppings']) if it['toppings'] else '-'}")
        else:
            lines.append("(장바구니 비어 있음)")

        lines.append("")
        lines.append(f"총 조각 수: {self.var_total_slices.get()}")
        lines.append(f"상품 소계: {self.var_subtotal.get()}")
        lines.append(f"대량할인: {self.var_discount.get()}")
        lines.append(f"부가세(10%): {self.var_vat.get()}")
        lines.append(f"배달요금: {self.var_delivery.get()}")
        lines.append(f"결제 금액: {self.var_total.get()}")

        lines.append("")    
        lines.append(f"수령 방법: {self.var_pick.get()}")
        if self.var_pick.get() == "배달":
            addr = self.addr_entry.get().strip()
            lines.append(f"배달 주소: {addr if addr else '(미입력)'}")

        lines.append("========================")
        return "\n".join(lines)

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("안내", "장바구니가 비어 있습니다.")
            return
        if self.var_pick.get() == "배달":
            addr = self.addr_entry.get().strip()
            if not addr:
                messagebox.showwarning("확인", "배달 주소를 입력해주세요.")
                return
        receipt = self._build_receipt_text()
        messagebox.showinfo("결제 요약", receipt)

    def save_receipt(self):
        if not self.cart:
            messagebox.showwarning("안내", "장바구니가 비어 있어 영수증을 저장할 수 없습니다.")
            return
        if self.var_pick.get() == "배달":
            addr = self.addr_entry.get().strip()
            if not addr:
                messagebox.showwarning("확인", "배달 주소를 입력해주세요.")
                return

        default_name = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = filedialog.asksaveasfilename(
            title="영수증 저장",
            defaultextension=".txt",
            initialfile=default_name,
            filetypes=[("텍스트 파일", "*.txt")]
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self._build_receipt_text())
            messagebox.showinfo("완료", "영수증이 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"파일 저장 중 오류가 발생했습니다.\n{e}")


if __name__ == "__main__":
    # Tk 테마 약간 정리
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    app = PizzaApp()
    style = ttk.Style()
    if "clam" in style.theme_names():
        style.theme_use("clam")
    app.mainloop()

