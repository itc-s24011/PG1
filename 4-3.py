def show_args(*args):
    '''与えられた複数の位置引数をタプルのまとめて受け取りそのタプルを表示して返す'''
    print('positional arguments:', args)
    return args

def show_kwargs(**kwargs):
    '''与えられた複数のキーワード引数を辞書にまとめて受け取りその辞書を表示して返す'''
    print('leyword arguments:', kwargs)
    return kwargs

positional_args = [4, 5, 6, 'ya']
show_args(*positional_args)

keyword_args = {'pasta': 'ペンネ', 'drink': '赤ワイン', 'main_dish': '肉料理', 'n_customers': 3}
show_kwargs(**keyword_args)
