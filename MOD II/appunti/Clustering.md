# Clustering
Dato un insieme di punti $p_{1}, p_{2}, \dots, p_{n}$ con una funzione di distanza, vogliamo raggrupparli in k cluster coerenti, cioé:
- Punti vicini nello stesso cluster
- Cluster lontani tra loro

# K-Clustering di massima separazione
Definizione:
- La distanza tra cluster = distanza minima tra due punti appartenenti a cluster diversi
<u>Obiettivo:</u> trovare una divisione in $k$ cluster che massimizzi questa distanza

# Algoritmo Single-Linkage
1. Inizia con ogni punto come cluster separato.
2. Unisci i due cluster piú vicini
3. Ripeti fino a rimanere con $k$ cluster

>[!Osservazione]
>Sembra **Kruskal** ma fermato quando rimangono $k$ componenti connesse

## TH:
Il clustering $C^{*}$ ottenuto cosí é di massima separazione.

**Dimostrazione:**
- La separazione $d^{*}$ é il peso del ($k-1$)-esimo arco rimosso.
- Se esistesse un clustering migliore, ci sarebbero punti collegati da un arco <= $d^{*}$ in cluster diversi $\rightarrow$ Contraddizione