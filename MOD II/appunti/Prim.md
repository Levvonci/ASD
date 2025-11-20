Come Kruskal, anche l'algoritmo di Prim si utilizza per trovare il MST in un grafo pesato, non orientato e connesso.
**La differenza** tra i due sta nella costruzione dell'MST.
- Kruskal parte dagli archi piú economici (Bottom-Up)
- Prim parte da un vertice e cresce l'albero espandendolo un nodo alla volta (Top-Down)

**Input:**
- Grafo non orientato pesato $G = (V, E, c)$

**Output:**
- Insieme degli archi $T \subseteq E$ che formano un MST

```Pseudo
Prim(G, s) {
	per ogni (v in V) a[v] <- infinito
	a[s] <- 0
	
	Inizializza una coda con prioritá Q vuota
	
	per ogni (v in V) inserisci v dentro Q con prioritá a[v]
	
	Inizializza un set di nodi esplorati S <- 0
	Inizializza T come albero contenente solo s.
	
	while (Q non é vuota) {
		u <- cancella l'elemento minimo di Q
		S <- S unito { u }
	
	per ogni (arco e = (u, v) incident to u)
		se ((v non appartiene S) e (c_e < a[v]))
			make u padre di v in T
			decrementa la prioritá a[v] to c_e
	return T
}
```

