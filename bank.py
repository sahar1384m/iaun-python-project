# باز کردن حساب
account=[]
n = int(input("چند حساب بانکی میخواهید ایجاد کنید؟ "))
for i in range(n):
    print(f"\n--- حساب #{i+1} ---")
    name=input("نام صاحب حساب راوارد کنید:")
    balance=float(input("موجودی اولیه را وارد کنید:"))
    account.append({"نام": name, "موجودی": balance})

# منوی تکرار شونده
while True:
    print("\n*** منوی بانک ***")
    print("1. نمایش موجودی همه ی حساب ها")
    print("2. سپرده گذاری")
    print("3. برداشت")
    print("4. نمایش حساب هایی با موجودی بیشتر از میانگین")
    print("5. خروج")
    options = input("گزینه ی مورد نظر را انتخاب کنید:")

    # نمایش
    if options == "1":
        print("\n  حساب ها:")
        for acc in account:
            print(f" {acc['نام']} →  {acc['موجودی']}")
    elif options == "2":
        name = input("نام حساب را وارد کنید: ")
        amount = float(input("مبلغ سپرده را وارد کنید: "))
        found = False
        for acc in account:
            if acc["نام"] == name:
                acc["موجودی"] += amount
                print(f"{amount}  اضافه شد به حساب{name}")
                found = True
                break
        if not found:
            print("این حساب وجود ندارد")

    elif options == "3":
        name = input("نام حساب را وارد کنید:")
        amount = float(input("چقدر میخواهید برداشت کنید؟"))
        found = False
        for acc in account:
            if acc["نام"]==name:
                if acc["موجودی"]>=amount:
                    acc["موجودی"]-=amount
                    print(f" {amount}برادشت شد از حساب{name}")
                else:
                    print("موجودی کافی نیست")
                found = True
                break
        if not found:
            print("این حساب وجود ندارد")

    elif options == "4":
        if not account:
            print(" این حساب وجود ندارد")
        else:
            avg = sum(acc["موجودی"] for acc in account) / len(account)
            print(f"\n میانگین موجودی: {avg}")
            print(" حساب هایی که موجودی بالاتر از میانگین دارند:")
            for acc in account:
                if acc["موجودی"] > avg:
                    print(f" {acc['نام']} →  {acc['موجودی']}")

    elif options == "5":
        print("باتشکر")
        break

    else:
        print("***خطا***")