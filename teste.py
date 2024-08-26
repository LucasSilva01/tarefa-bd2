import memcache

mc = memcache.Client(['127.0.0.1:11211'])
meu_arquivo = mc.get('meu_arquivo')

if meu_arquivo:
    print(meu_arquivo)
    print("Li do cache")
else:
    filename = './meu_arquivo.txt'
    with open(filename, 'r') as handle:
        content = handle.read()
        mc.set('meu_arquivo', content, time=3600)
        print(content)
        print("Li do arquivo")

