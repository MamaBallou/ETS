---
title: "Transformée de Laplace"
author: Corentin GUIGOT
date: 29 mars 2023
geometry: margin=2cm
output: pdf_document
---

# SAM - Transformée de Laplace

## **Définition :**

Soit $f(t)$ une fonction réelle définie $\forall t>0$ (fonction causale) et soit $p \in \mathbb{C}$.

La **transformée de Laplace** de $f$, notée $\mathcal{L} \left[f\right]$ est définie par :
$$F(p) = \mathcal{L} \left[ f(t)\right] = \int_0^{+\infty} f(t)e^{-tp} dt$$
(à condition que l'intégrale soit définie)

L’ensemble des $p$ tels que l’intégrale généralisée $\int_0^{+\infty} f(t)e^{-tp} dt$ converge est le **domaine de définition** de la transformée de Laplace de $f$.

On peut définir **la transformée de Laplace inverse** : $\mathcal{L}^{-1} \left[ F(p)\right] = f(t)$

<div style="color:lightblue">

<ins>**_Remarque :_**</ins>

$F(p)$ est appelée image de $f(t)$ et $f(t)$ est appelé original de $F(p)$.

</div>

<div style="color:green">

## **Exemples :**

</div>

- Soit $H(t)$ une fonction d'Heaviside définie par :
  $$
  \left\{
  \begin{aligned}
  H(t) =0 \text{ si } t <0 \\
  H(t) =1 \text{ si } t \geq 0
  \end{aligned} \right.
  $$

La **transformée de Laplace** de $H$ est définie par :

$$
H(P) = \int_0^{+\infty} H(t)e^{-tp} dt = \int_0^{+\infty} e^{-tp} dt = \left[-\frac{1}{p}e^{-tp} \right]_0^{+\infty}  = \boxed{\pmb{\frac{1}{p}}}
$$

La **transformée de Laplace** de $H$ n'est pas définie pour $p = 0$

<p align="center">
<img src="./img/TLaplce_H_graph.png">
</p>

- Soit $f(t)$ la fonction définie par $f(t) = H(t)e^{at}$, $a \in \mathbb{C}$.
  La **transformée de Laplace** de $f$ est définie par :
  $$
  F(p) = \int_0^{+\infty} H(t)e^{(a-p)t} dt = \int_0^{+\infty} e^{(a-p)t} dt = \left[\frac{1}{a-p}e^{(a-p)t} \right]_0^{+\infty}  = \frac{1}{a-p}(0-1)= \boxed{\pmb{\frac{1}{p-a}}}
  $$
  La transformée de Laplace de $f$ n'est pas définie pour $p = a$
  <p align="center">
  <img src="./img/TLaplce_f_graph.png" width=200>
  </p>

<div style="color:blue">

## **Propriétés :**

</div>

### **Opérations algébriques**

- Soit $f(t)$ et $g(t)$ deux fonctions réelles transformables au sens de Laplace. On note $F(p)$ et $G(p)$ les transformées de Laplace de $f$ et $g$ respectivement.

<ins>**_Linéarité_**</ins> : $\forall a,b \in \mathbb{R}, \mathcal{L}\left[ af(t) + bg(t)\right] = aF(p) + bG(p)$

<ins>**_Changement d'échelle :_**</ins> $\forall a \in \mathbb{R}, \mathcal{L}\left[ \frac{1}{a}f\left(\frac{t}{a}\right)\right] = F(ap)$

<ins>**_Translation :_**</ins> $\forall a \in \mathbb{R}, \mathcal{L}\left[ e^{at}f(t)\right] = F(p-a)$

### **Opérations analytiques**

Soit $f(t)$ une fonction réelle transformable au sens de Laplace. On note $F(p)$ la transformée de Laplace de $f$.

- Transformée de la dérivée : $\mathcal{L}\left[ f'(t)\right] = pF(p) - f(0)$
- Transformée de l'intégrale : $\mathcal{L}\left[ \int_0^t f(\tau)d\tau\right] = \frac{1}{p}F(p)$

- Dérivée de la transformée : $F'(p) = - \mathcal{L}\left[ tf(t)\right]$
- Intégrale de la transformée : $\int_p^{+\infty} F(\tau)d\tau = \mathcal{L}\left[ \frac{f(t)}{t}\right]$

<div style="color:blue">

## **Théorèmes :**

</div>

Soit $f(t)$ une fonction réelle transformable au sens de Laplace. On note $F(p)$ la transformée de Laplace de $f$.

<ins>**_Théorème de la valeur initiale :_**</ins>
$$\lim\limits_{t \rightarrow 0}f(t)= \lim\limits_{p \rightarrow +\infty} pF(p)$$

<ins>**_Théorème de la valeur finale :_**</ins>
$$\lim\limits_{t \rightarrow +\infty}f(t)= \lim\limits_{p \rightarrow 0^+} pF(p)$$

<div style="color:blue">

## **Calcul des Originaux :**

</div>

Soit $F(p)$ une fonction réelle transformable au sens de Laplace. On note $f(t)$ la transformée de Laplace inverse de $F$.
**$f(t)$ est appelé original de F(p) et, si l'on suppose $f(t)$ continue sur $\left[0,+\infty\right[$, cet original est unique.**

De très nombreuses transformées de Laplace sont des fractions rationnelles.
**La décomposition d’une fraction rationnelle en éléments simples est donc une
méthode très importante pour calculer l’original d’une transformée de Laplace.**

### **Décomposition en éléments simples**

Dans le domaine $\mathbb{C}$, il y a n racines $bn$
$$\Rightarrow (x-bn)(x-bn-1)(x-bn-2) \cdots (x-b_1)$$
Dans le domaine $\mathbb{R}$, il y a 2 racines $b_1$ et $b_2$.

$$
\Rightarrow (a_1x^2+a_2x+a_3)(a_4x^2+a_5x+a_6) \cdots (x-b_1)(x-b_2) \\
((x^2 - 4x +2)=0) \Rightarrow ((x-b_1)(x-b_2))=0
$$

$\pagebreak$

|                           Nature du pôle                            |                            Forme de la décomposition                            |
| :-----------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
|        Pôle simple $\newline \cdots \times \frac{1}{(p-b)}$         |                           $\cdots + \frac{A}{(p-b)}$                            |
|      Pôle multiple $\newline \cdots \times \frac{1}{(p-b)^n}$       | $\cdots + \frac{A_n}{(p-b)^n}+\frac{A_{n-1}}{(p-a)^n}+ \frac{A_{n-2}}{(p-a)^n}$ |
| Pôle complexe d'ordre 2 $\newline \cdots \times \frac{1}{p^2+cp+d}$ |                        $\cdots + \frac{Ap+B}{p^2+cp+d}$                         |

<div style="color:green">

### **Exemples :**

</div>

**Exemple 1:**

Soit $F(p) = \frac{1}{(p-a)^2(p-b)}$. On cherche l'original de $F$.
$$\frac{1}{(p-a)^2(p-b)} = \frac{A}{(p-a)^2} + \frac{B}{(p-a)} + \frac{C}{(p-b)}$$

Pour trouver $A$,on multiplie par $(p-a)^2$ et on pose $p = a$
$$\frac{1}{(p-b)} |_{p=a} = A = \frac{1}{a-bs}$$

Pour trouver $C$,on multiplie par $(p-b)$ et on pose $p = b$
$$\frac{1}{(p-a)^2} |_{p=b} = C = \frac{1}{(b-a)^2}$$

Pour trouver $B$,on multiplie par $p$ et on fait tendre $p$ vers $+\infty$.
On trouve B = -C

**Exemple 2:**

Décomposer la fraction $F(p) = \frac{3p^2-5p+3}{(p-2)(p^2-2p+5)}$ puis calculer F(p)

Le polynome $p^2-2p+5$ n'admet pas de racines réelles ($\Delta = -16 <0$).
La décomposition de $F(p)$ est donc :
$$F(p)=\frac{A}{p-2}+\frac{B}{p^2-2p+5}$$

Pour calculer $A$, on multiplie par $(p-2)$ et on pose $p=2$.
$$\frac{3p^2-5p+3}{(p^2-2p+5)}|_{p=2} = A = 1$$

Pour calculer $B$,$C$ on multiplie par $(p-2)(p^2-2p+5)$ puis on identifie terme à terme selon les degrés de $dp$.
$$3p^2-5p+3 = A(p^2-2p+5)+(Bp+C)(p-2)$$
Or $A = 1$, donc
$$2p^2-3p-2 = Bp^2+(C-2B)p+2C$$

Soit

$$
\left\{\begin{aligned}
B=2\\
C-2B=-3\\
-2C=-2 \end{aligned}\right. \Leftrightarrow \left\{\begin{aligned}
B=2\\
C=1 \end{aligned}\right.
$$

Finalement, $F(p)=\frac{1}{p-2}+\frac{2p+1}{p^2-2p+5}$

Néanmoins, on cherche $f(t)$ et non $F(p)$. L'original de $F(p)$ est la somme des originaux de chaque élément simple.

L'original de $\frac{1}{p-2}$ est $e^{2t}$
Puis, on peut réécrire le deuxième terme tel que :
$$ \frac{2p+1}{p^2-2p+5} = \frac{2p+1}{(p-1)^2+4} = \frac{2p+1}{(p-1)^2+2^2} = 2\frac{p-1}{(p-1)^2+2^2} + 3 \frac{1}{(p-1)^2+2^2}$$

- L'original de $\frac{p-1}{(p-1)^2+2^2}$ est $e^{t} \cos(2t)$
- L'original de $\frac{1}{(p-1)^2+2^2}$ est $\frac{1}{2}e^{t} \sin(2t)$
- L'original de $F(p) = \frac{1}{p-2}+\frac{2p+1}{p^2-2p+5}$ est donc:
  $$f(t) = e^{2t} + e^{t} \left( 2\cos(2t) + \frac{3}{2}\sin(2t) \right)$$

<div style="color:blue">

### **Résolution d'équation différentielle :**

</div>

La transformée de Laplace permet de résoudre les équations différentielles.

<div style="color:green">

### **Exemple :**

</div>

Résoudre l'équation différentielle $f''(t) + 5f'(t) + 4f(t) = 2H(t)$ avec $H(t)$ l'échelon de Heaviside et $f''(0)=f'(0)=f(0)=0$

#### **Résolution en 2 étapes :**

1. Appliquer la transformée de Laplace de 2 cotés ($f(t) \rightarrow F(p)$)
   - On sait que $\mathcal{L} \left[ f(t) \right] = F(p); \mathcal{L} \left[f'(t)\right] = pF(p) - f(0)$
   - On a également $\mathcal{L} \left[ H(t) \right] = \frac{1}{p}$
   - On obtient donc alors l'équation dans p
     $$p^2F(p) + 5pF(p) + 4F(p) = \frac{2}{p} \Leftrightarrow (p^2+ 5p+4)F(p) = \frac{2}{p}$$
   - Soit si on isole F(p) :
     $$F(p) = \frac{2}{p(p^2+ 5p+4)}$$
2. Simplifier et ramener l'équation à une somme d'éléments simple
   $$F(p)= \frac{2}{p(p^2+ 5p+4)}$$
   - On note que qu'il est possible de factoriser le dénominateur de $F(p)$ car $p^2+ 5p+4$ possède des racines réelles, $-4$ et $1$
   - On en déduit donc la simplification en éléments simple suivante :
     $$F(p)= \frac{2}{p(p-4)(p-1)} = \frac{A}{p} + \frac{B}{p+4} + \frac{C}{p+1}$$
   - On peut alors calculer $A$, en multipliant par $p$ et en prenant $p=0$ :
     $$A = \frac{2}{(p+4)(p+1)} = \frac{2}{4\times 1} = \boxed{\frac{1}{2}}$$
   - Pour $B$, on multiplie par $(p+4)$ et on prend $p=-4$ :
     $$B = \frac{2}{p(p+1)} = \frac{2}{(-4)\times -3} = \boxed{\frac{1}{6}}$$
   - Pour $C$, on multiplie par $(p+1)$ et on prend $p=-1$ :
     $$C = \frac{2}{p(p+4)} = \frac{2}{(-1)\times (-1+4)} = \boxed{-\frac{2}{3}}$$

On obtient donc finalement la réponse :
$$F(p) = \frac{1}{2p} + \frac{1}{6(p+4)} - \frac{2}{3(p+1)}$$

3. Appliquer la transformée de Laplace inverse ($F(p) \rightarrow f(t)$)

On regarde les tables des transformées de Laplace et on identifie membre à membre. On a :
$$ \mathcal{L}^{-1} \left[ \frac{1}{2p} \right] = \frac{1}{2}; \mathcal{L}^{-1} \left[ \frac{1}{6(p+4)} \right] = \frac{1}{6}e^{-4t}; \mathcal{L}^{-1} \left[ \frac{-2}{3(p+1)} \right] = -\frac{2}{3}e^{t}$$
