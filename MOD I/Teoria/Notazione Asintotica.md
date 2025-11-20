# $O \ Grande$ 
Si utilizza per descrivere il caso peggiore di un algoritmo
**"L'algoritmo ci mette al massimo cosí tanto in funzione di $n$"**
*Ex:* se un algoritmo é $O(n^2)$, vuol dire che al crescere di $n$, il tempo di esecuzione aumenta al massimo come $n^2$ 

Se:
$$lim_{n\rightarrow \infty} \frac {f(n)}{g(n)} = 0 \ \implies \ f(n) = O(g(n))  
$$

# $o \ Piccolo$
L'algoritmo cresce piú lentamente di una certa funzione
Con $O \ Grande$ possiamo crescere fino a quella funzione, invece con $o \ piccolo$ siamo strettamente piú piccoli, non arriviamo a crescere come quella funzione
*Ex:* se un algoritmo é $o(n^2)$  significa che cresce meno velocemente di $n^2$, ma non come $n^2$ o peggio

# $\Omega \ Grande$
**L'algoritmo ci mette almeno "cosí tanto"**
Si utilizza per descrivere il caso migliore dell'algoritmo
*Ex:* se un algoritmo é $\Omega(nlog(n)$ significa che non potrá mai essere piú veloce di  $nlog(n)$ su input grandi

Se:$$lim_{n\rightarrow \infty} \frac {f(n)}{g(n)} = \infty \ \implies \ f(n) = \Omega(g(n))  
$$

# $\Theta$
**L'algoritmo cresce esattamente come quella funzione: né piú e né meno**
Si usa per dire che un algoritmo ha sia $O$ e $\Omega$ uguali alla stessa funzione, allora é l'ordine di crescita preciso
*Ex:* se un algoritmo é $\Theta(n)$ significa che cresce linearmente 

**Notare che:**
$$
f(n) = \Theta(g(n)) \implies f(n) = O(g(n))
$$
**Ma:**
$$
f(n) = O(g(n)) \centernot\implies f(n) = \Theta(g(n)) 
$$
**E:**
$$
f(n) = \Theta(g(n)) \implies f(n) = \Omega(g(n))
$$
**Ma:**
$$
f(n) = \Omega(g(n)) \centernot\implies f(n) = \Theta(g(n)) 
$$
>[!IMPORTANTE]
>$$
>\boxed{f(n) = \Theta(g(n)) \iff f(n) = \Omega(g(n)) \ e \ f(n) = O(g(n))}  
>$$ 

