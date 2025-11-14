Dato un grafo connesso e non diretto G=(V,E) con pesi reali $c_{e}$ associati ad ogni arco, l'MST é un sottoinsieme di archi $T \subseteq E$ tale che $T$ é lo spannin tree con somma dei pesi degli archi minima
![[MST.png | center | 600]]

## Brute forcing
Per il teorema di **Cayley's**, in un grafo completo esistono al piú $n^{n-2}$ spannin tree. Quindi questa proprietá rende impossibile brute forzare la ricerca dello spannin tree minimo.

## Unicitá
Se gli archi del grafo hanno tutti pesi distinti, allora l'MST é unico.

## Cicli e Tagli
**Ciclo:** 
Percorso che partendo da un nodo iniziale, passa attraverso una sequenza di nodi distinti per poi tornare al nodo iniziale - {1-2, 2-3, 3-4,....., 10-1}

**Taglio:** 
Partizione del grafo in due insiemi non vuoti di vertici:
- **S**
- **V\S** (Tutto ció che non é in **S**)
Gli archi che collegano un nodo in **S** ad un nodo in **V\S** si chiamano **archi che attraversano il taglio**

**CutSet:**
Dato un taglio del grafo, il cutset é l'insieme di tutti gli archi che hanno un estremo in S e un estremo in V\S
>$\delta(S) = \{(u,v) \in E \ |\  u \in S, \ v\in V ∖ S\}$     

## Cycle Property
**Enunciato:**
>Sia $C$ un qualsiasi ciclo nel grafo $G$.
>Sia $f$ un arco di $C$ che ha peso massimo $\implies$ Esiste un MST $T*$ che non contiene $f$

Se dentro un ciclo prendi l'arco piú pesante, puoi sempre rimuoverlo e trovare un altro percorso che collega gli stessi nodi con costo minore o uguale

### Dimostrazione
1. Partiamo da un MST $T*$ e supponiamo che contiene $f$
2. Cancelliamo $f$ da $T*$, questo crea un cut S in $T*$
3. Poiché $f$ apparteneva al ciclo $C$, $C$ va da un lato del taglio all'altro: quindi nel cutset $\delta(S)$ c'é almeno l'arco $f$. Ma essendo un ciclo che attraversa un taglio, deve esistere un altro arco $e$ che appartiene sia a $C$ sia a $\delta(S)$
4. Per ipotesi $f$ é un arco di peso massimo nel ciclo $C$. Quindi il peso di $e$ soddisfa $c_{e} \leq c_{f}$
5. Costruiamo $T' = T* \cup \ \{e\} ∖ \{f\}$
	- Aggiungendo $e$ e togliendo $f$ otteniamo nuovamente uno spannin tree.
	- Quindi $T'$ é ancora uno spannin tree
6. Poiché $c_{e} \leq {c_{f}}$, il costo totale soddisfa $cost(T') \leq cost(T*)$

Ma $T*$ é un MST, quindi non puó esistere uno spannin tree con costo strettamente minore: dunque $T'$ é anch'esso un MST.
E $T'$ non contiene $f$
Quindi abbiamo costruito un MST che non contiene $f$.

## Cut Property
**Enunciato:**
>Sia S un qualsiasi sottoinsieme di nodi del grafo.
 Sia $e$ l'arco piú economico fra quelli che attraversano il taglio (S, V\S)$\implies$ Esiste un MST $T*$ che contiene l'arco $e$.

**Enunciato breve:**
>L'arco di peso minimo $e$ di un cutset D appartiene ad un MST $T*$ 

Se devi collegare due insiemi scollegati del grafo, l’arco più leggero che li connette è sempre la scelta ottimale.  
Non esiste un modo più economico per "saltare" da un lato all’altro del taglio.

### Dimostrazione
1. Supponiamo per assurdo che l'arco $e$ non appartiene all'MST $T*$
2. Aggiungiamo l'arco $e$ all'MST $T*$. Dato che l'albero ricoprente ha $n-1$ archi, aggiungendo l'arco $e$ si creerebbe un ciclo che chiameremo $C$
3. L'arco $e$ é sia nel ciclo $C$ che nel cutset $D$. Questo perché:
	- Il ciclo $C$ attraversa il taglio (perché $e$ lo attraversa)
	- Ogni ciclo che attraversa il taglio deve avere almeno un altro arco che attraversa quel taglio.
	 Quindi esiste un altro arco $f$ che:
	 - Appartiene al ciclo $C$
	 - Attraversa lo stesso taglio del taglio di $S$
4. L'arco $f$ ha peso $\geq$ di $e$, questo perché $e$ é l'arco di peso minimo che attraversa il taglio data l'ipotesi iniziale.
5. Costruiamo un nuovo albero:
	 - $T' = T* \cup \ \{e\} ∖ \{f\}$ 
	 - Aggiungiamo l'arco $e$, rimuoviamo l'arco $f$ che stava nel ciclo
	 - Rimane comunque uno spannin tree (Abbiamo rotto il ciclo)
6. Poiché $c_{e} \leq c_{f}$ $\implies$ $cost(T') \leq cost(T*)$ "Contraddizione!"

Quindi $T'$ non é piú costoso di $T*$.
Ma $T*$ é un MST -> nessun albero puó essere piú economico.
Quindi $T'$ é anche un MST che contiene l'arco $e$ 

