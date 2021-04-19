from No import No
from Adjacente import Adjacente

class Mapa:
    '''Criar todos os No'''
    '''Construtor Mapa'''
    a = No("a")
    b = No("b")
    c = No("c")
    d = No("d")
    e = No("e")
    f = No("f")
    g = No("g")
    h = No("h")
    i = No("i")
    j = No("j")
    k = No("k")
    l = No("l")
    m = No("m")
    n = No("n")
    o = No("o")
    p = No("p")
    q = No("q")
    r = No("r")
    s = No("s")
    t = No("t")
    u = No("u")
    v = No("v")
    w = No("w")
    x = No("x")
    y = No("y")
    z = No("z")
    aa = No("aa")
    bb = No("bb")
    cc = No("cc")
    dd = No("dd")
    ee = No("ee")
    ff = No("ff")
    gg = No("gg")
    hh = No("hh")
    ii = No("ii")
    jj = No("jj")
    kk = No("kk")
    ll = No("ll")
    mm = No("mm")
    nn = No("nn")

    a.addNoAdjacente(Adjacente(b))
    a.addNoAdjacente(Adjacente(f))

    b.addNoAdjacente(Adjacente(a))
    b.addNoAdjacente(Adjacente(c))

    c.addNoAdjacente(Adjacente(b))
    c.addNoAdjacente(Adjacente(d))

    d.addNoAdjacente(Adjacente(c))
    d.addNoAdjacente(Adjacente(e))
    d.addNoAdjacente(Adjacente(i))

    e.addNoAdjacente(Adjacente(d))

    f.addNoAdjacente(Adjacente(a))
    f.addNoAdjacente(Adjacente(k))

    i.addNoAdjacente(Adjacente(d))
    i.addNoAdjacente(Adjacente(n))

    k.addNoAdjacente(Adjacente(f))
    k.addNoAdjacente(Adjacente(p))
    k.addNoAdjacente(Adjacente(l))

    l.addNoAdjacente(Adjacente(k))
    l.addNoAdjacente(Adjacente(m))

    m.addNoAdjacente(Adjacente(l))
    m.addNoAdjacente(Adjacente(n))
    m.addNoAdjacente(Adjacente(r))

    n.addNoAdjacente(Adjacente(m))
    n.addNoAdjacente(Adjacente(o))
    n.addNoAdjacente(Adjacente(s))
    n.addNoAdjacente(Adjacente(i))

    o.addNoAdjacente(Adjacente(n))
    o.addNoAdjacente(Adjacente(t))

    p.addNoAdjacente(Adjacente(k))
    p.addNoAdjacente(Adjacente(u))

    r.addNoAdjacente(Adjacente(m))
    r.addNoAdjacente(Adjacente(s))

    s.addNoAdjacente(Adjacente(r))
    s.addNoAdjacente(Adjacente(n))
    s.addNoAdjacente(Adjacente(x))
    s.addNoAdjacente(Adjacente(t))

    t.addNoAdjacente(Adjacente(o))
    t.addNoAdjacente(Adjacente(s))
    t.addNoAdjacente(Adjacente(y))

    u.addNoAdjacente(Adjacente(p))
    u.addNoAdjacente(Adjacente(z))

    x.addNoAdjacente(Adjacente(s))
    x.addNoAdjacente(Adjacente(bb))
    x.addNoAdjacente(Adjacente(y))

    y.addNoAdjacente(Adjacente(t))
    y.addNoAdjacente(Adjacente(x))

    z.addNoAdjacente(Adjacente(u))
    z.addNoAdjacente(Adjacente(aa))
    z.addNoAdjacente(Adjacente(e))

    aa.addNoAdjacente(Adjacente(z))
    aa.addNoAdjacente(Adjacente(bb))
    aa.addNoAdjacente(Adjacente(ff))

    bb.addNoAdjacente(Adjacente(aa))
    bb.addNoAdjacente(Adjacente(x))
    bb.addNoAdjacente(Adjacente(cc))
    bb.addNoAdjacente(Adjacente(gg))

    ii.addNoAdjacente(Adjacente(nn))

    jj.addNoAdjacente(Adjacente(ee))
    jj.addNoAdjacente(Adjacente(kk))

    kk.addNoAdjacente(Adjacente(ff))
    kk.addNoAdjacente(Adjacente(jj))
    kk.addNoAdjacente(Adjacente(ll))

    ll.addNoAdjacente(Adjacente(gg))
    ll.addNoAdjacente(Adjacente(kk))
    ll.addNoAdjacente(Adjacente(mm))

    mm.addNoAdjacente(Adjacente(ll))
    mm.addNoAdjacente(Adjacente(nn))

    nn.addNoAdjacente(Adjacente(mm))


'''
mapa = Mapa()
print('No Atual ::', mapa.d.nome)
print('No visitado ::', mapa.d.visitado)
for i in range(len(mapa.d.adjacentes)):
    print('No Adjacente ::',  mapa.d.adjacentes[i].no.nome)
'''