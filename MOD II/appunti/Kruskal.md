L'algoritmo di Kruskal é uno degli algoritmi fondamentali che serve per trovare il MST di un grafo pesato, connesso e non orientato.

**Input:** 
Un grafo non orientato con pesi:
- $V$ insieme dei vertici
- $E$ insieme degli archi
- $c_{e}$ peso associato a ciascun arco $e$

**Output:**
Un insieme $T \subseteq E$ che rappresenta l'MST.

## PseudoCodice
```Pseudo
algorithm Kruskal (graph G=(V,E,c))
    UnionFind UF
    T = ∅
    ordino gli archi in ordine crescente di costo

    per ogni vertice v:
        UF.makeset(v)

    per ogni arco (x,y) ordinato:
        Tx = UF.find(x)
        Ty = UF.find(y)

        se Tx ≠ Ty allora:
            UF.union(Tx, Ty)
            aggiungi l'arco (x,y) a T

    return T
```

Ordinare gli archi mi costa $O(mlog(m)) = O(mlog(n))$
Operazion Union-Find:
- $n$ makeset
- $n-1$ union
- $2m$ find
$\implies$ $O(mlog(n) + UF(m,n))$ 
Usando QuickFind con union by size il costo é:
	$O(mlog(n) + m + nlog(n) = O(mlog(n))$ 
Usando QuickUnion con union by size il costo é:
	$O(mlog(n) + mlog(n) + n) = O(mlog(n))$ 
