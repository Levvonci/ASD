Si utilizzano per esprimere la complessitá computazionale di un algoritmo ricorsivo
*Esempi:*
- $T(n) = T(n/3) + 2T(n/4) + O(nlog(n))$
- $T(n) = T(n-1) + O(1)$
- $T(n) = T(n/3) + T(2n/3) + n

**Caso base:**
- $T(1) = 1$

## Metodo dell'iterazione
L'idea é quella di **"Srotolare"** la ricorsione, ottendendo una sommatoria dipendente solo dalla dimensione $n$ del problema iniziale
*Esempi:*
- $T(n) = c + T(n/2)$
	- $T(n/2) = 2c + T(n/4)$
		- $T(n/4) = 3c + T(n/8)$
			- $T(n/8) = 4c + T(n/16)$
				- $\dots$ 
					- $T(n) = ic + T(n/2^i)$
**Quindi:**
Per $i = log_2(n)$:
$T(n) = c\cdot log_2(n) + T(1) = \Theta(log(n))$
---
- $T(n) = T(n-1) + 1$
	- $T(n-1) = T(n-2) + 1 + 1$
		- $T(n-2) = T(n-3) + 1 + 1 + 1$
			- $T(n-3) = T(n-4) + 1 + 1 + 1 + 1$
				- $\dots$
					- $T(n) = T(n-i) + i$
**Quindi:**
Per $i = n-1$:
$T(n) = T(1)+n-1 = \Theta(n)$ 

**Esercizio ![[cap2_equazioni_ricorrenza_2024.pdf]]**
**Esercizio 1:**
$T(n) = T(n-1) + n$
- $T(n-1) = T(n-2) + n-1$ 
	- $T(n-2) = T(n-3) + n-2$ 
