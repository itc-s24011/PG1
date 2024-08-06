# グローバルスコープ
def scope_test():
    # ネステッドスコープ(scope_testのローカルスコープ)
    def do_local():
        # ローカルスコープ
        s1 = "local     "
    def do_nonlocal():
        # ローカルからネステッドへスコープを移す
        nonlocal s2
        # ネステッドスコープ
        s2 = "nonlocal"
    def do_global():
        # ローカルからグローバルへスコープを移す
        global s3
        # グローバルスコープ
        s3 = "global    "
    # ネステッドスコープ(scope_testのローカルスコープ)
    s0 = s1 = s2 = s3 = "test       "
    do_local()
    print("After local      :", s0, s1, s2, s3)
    do_nonlocal()
    print("After nonlocal   :", s0, s1, s2, s3)
    do_global()
    print("After global     :", s0, s1, s2, s3)

# グローバルスコープ
s0 = s1 = s2 = s3 = "initial "
print("In the global    :", s0, s1, s2, s3)
scope_test()
print("After func call  :", s0, s1, s2, s3)
