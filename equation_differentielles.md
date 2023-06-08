---
title: "Équations différentielles"
author: Corentin GUIGOT
date: 28 mars 2023
geometry: margin=2cm
output: pdf_document
---

Une équation différentielle est une relation mathématique liant des fonction incconnues et leurs dérivées.

L'ordre d'une équation différentielle correspond au degré maximal de dérivation auquel l'une des fonction a été soumise.

<div style='color:green'>

### Exemple :

$y' + y =  0$, $y'$ est dérivé 1 fois -> ordre 1

</div>

# I. Équation de premier ordre

## Définition

Elle sont de la forme : $ay'(x) + by(x) = h(x)$

Où $h(x)$ fonction :

- polynome,
- $e^{\lambda x} x$ polynome,
- $[\alpha \sin + \beta \cos]$.

Et $(a, b) \in \mathbb{R}^2$

<div style='color:green'>

### Exemple :

- <u>Électricité :</u> Décharge d'un condensateur à travers une résistance.

  La tension $u(t)$ est solution de l'équation.

  $$u(t) + \frac{1}{RC}u(t) = 0$$

- <u>Physique nucléaire :</u> Désintégration d’un corps radioactif.

  Le nombre de noyaux cassés $N(t)$ est solution de l’équation $N' t = - \lambda N(t)$, où $\lambda$ désigne la constante radioactive du corps

</div>

## Méthode de résolution

Soit l'équation $(E) : ay'(x) + by(x) = h(x)$

1. On résoud l'équation homogène $(E_0) : ay'(x) + by(x) = 0$ de la façon suivante :
   - On associe à $(E_0)$ l'équation caractéristique $ar + b = 0$ dont la solution est $r_0 = - \frac{b}{a}$.
   - Les solutions de $(E_0)$ sont alors $y_0 = K e^{r_0 x}\ \text{où}\ K \in \mathbb{R}$
2. On cherche une solution particulière $y_1$ de $(E)$.
3. Les solutions de $(E)$ sont les fonctions $y = y_0 + y_1$.
4. La connaissance d'une condition particulière est nécessaire pour déterminer la constante K.

## Résolution d’équations homogènes :

<div style='color:green'>

### Exemples :

- $y'(x) - 2y(x) = 0\ E_0$

  L'équation associée : $r - 2 = 0$ a pour solution $r_0 = 2$.

  Donc, les solutions de $(E_0)$ sont $y_0(x) = Ke^{2x} où $K \in \mathbb{R}$

- $y'(x) + y(x) = 0\ E_0$

  L'équation associée : $r + 1 = 0$ a pour solution $r_0 = -1$.

  Donc, les solutions de $(E_0)$ sont $y_0(x) = Ke^{-x}$ où $K \in \mathbb{R}$

- $2y'(x) - y(x) = 0\ (E_0)$

  L'équation associée : $2r - 1 = 0$ a pour solution $r_0 = \frac{1}{2}$

  Donc, les solutions de $(E_0)$ sont $y_0(x) = Ke^{\frac{x}{2}}$ où $K \in \mathbb{R}$

</div>

## Recherche d'une solution particulière

Soit l'équation $(E) : ay'(x) + by(x) = h(x)$

La forme de l a solution particulière $y_1(x)$ de $(E)$ dépend de la forme de $h(x)$.

Nous développons les trois cas les plus courant $(P_n(x)\ \text{et}\ \Psi_n(x))$ désignant des polynômes de degré $n$.

- Premier cas : $h(x) = P_n(x)$
  - Si $b \neq 0$, alors $y_1(x) = \Psi_n(x)$
  - Si $b = 0$, alors $y_1(x) = x\Psi_n(x)$
- Deuxième cas : $h(x) = P_n(x) e^{\lambda x}$
  - Si $\lambda \neq 0$, alors $y_1(x) = \Psi_n(x) e^{\lambda x}$
  - Si $\lambda = 0$, alors $y_1(x) = x\Psi_n(x) e^{\lambda x}$
- Troisième cas : $h(x) = A \cos(px) + B \sin(px)$, où $(A, B) \in \mathbb{R}^2$
  - Alors y_1(x) = $C \cos(px) + D \sin(px)$, où $(C, D) \in \mathbb{R}^2$

<div style='color:green'>

### Exemple :

- Premier cas : $y'(x) - 2y(x) = 2x$

  $h(x) = P_1(x) = 2x$ et $b = -2\neq 0$, donc $y_1(x) = cx + d\ \in \mathbb{R}$.

  Par identification, on obtient : $c - 2cx - 2d = 2x$. Soit $\left\{ \begin{array}{c} -2c = 2 \\c - 2d = 0 \end{array} \right. \Leftrightarrow \left\{ \begin{array}{c} c = -1 \\ d = - \frac{1}{2} \end{array} \right.$

  Donc $y_1(x) = -x - \frac{1}{2}$

- Deuxième cas : $y'(x) + y(x) = 2xe^{-x}$

  $h(x) = P_1(x) e^{\lambda x} = 2xe^{-x}$ et $\lambda = -1 = r_0$, donc $y_1(x) = x (cx +d) e^{-x}$ où $(c,d) \in \mathbb{R}^2$.

  Par identification on obtient : $(2cx + d) e^{-x} - (cx^2 + dx) e^{-x} + (cx^2 + dx) e^{-x} = 2x e^{-x}$

  C'est à dire $(2cx +d)e^{-x} = 2x e^{-x}$, soit $\left\{ \begin{array}{c} 2c = 2 \\ d = 0\end{array}\right. \Leftrightarrow \left\{ \begin{array}{c} c = 1 \\ d = 0 \end{array} \right.$

  Donc $y_1(x) = x^2 e^{-x}$

- Troisième cas : $2y'(x) - y(x) = \sin(x)$

  $h(x)$ est de la forme $A \cos(px) + B \sin(px)$, où $A = 0$, $B = 1$ et $p = 1$.

  Donc $y_1(x) = C \cos(px) + D \sin(px)$, où $(C, D) \in \mathbb{R}^2$.

  Par identification, on obtient : $-2C \sin(x) +2D\cos(x) -C \cos(x) - D \sin(x) = \sin(x)$

  Soit $\left\{ \begin{array}{c} -2C - D= 1 \\ 2D - C = 0 \end{array} \right. \Leftrightarrow \left\{ \begin{array}{c} C = 2D \\ -5D = 1 \end{array} \right. \Leftrightarrow \left\{ \begin{array}{c} C = - \frac{2}{5} \\[10pt] D = - \frac{1}{5} \end{array} \right.$
  </div>

## Solution générale

Soit l'équation $(E) : ay'(x) + by(x) = h(x)$

La solution générale de l'équation $(E)$ s'obtient en additionnant la solution de l'équation homogène $(E_0)$ et la solution particulière de $(E)$.

$$y(x) = y_0(x) + y_1(x)$$

<div style='color:green'>

### Exemple : $y'(x) - 2y(x) = 2x$

Les solutions de $(E_0)$ sont $y_0(x) = Ke^{2x}$ où $K \in \mathbb{R}$

La solution particulière de $(E)$ est $y_1(x) = -x - \frac{1}{2}$

La solution générale de $(E)$ est donc $y(x) = Ke^{2x} - x - \frac{1}{2}$ où $K \in \mathbb{R}$

</div>

## Détermination de la constante

Soit l'équation $(E) : ay'(x) + by(x) = h(x)$

La connaissace de la valeur de $y(x_0)$ permet de déterminer la constante $K$ de la solution de l'équation $(E_0)$.

<div style='color:green'>

### Exemple : Trouver la solution $(E) : y'(x) + y(x) = 2xe^{-x}$ Vérifiant $y(0) = 1$.

Les solution de $(E_0)$ sont $y_0(x) = K e^{-x}$ où $K \in \mathbb{R}$

Une solution particulière de $(E)$ est $y_1(x) = x^2 e^{-x}$

La solution générale de $(E)$ est donc $y(x) = K e^{-x} + x^2 e^{-x}$

Or, $y(0) = 1$, donc $K = 1$.

L'unique solution vérifiant $y(0) = 1$ est donc $y(x) = (x^2 + 1) e^{-x}$

</div>

# II. Équations différentielles du deuxième ordre

## Définition

Elles sont de la forme : $ay''(x) + by'(x) + cy(x) = h(x)$ où $a \in \mathbb{R}^*$, $(b,c) \in \mathbb{R}^2$.

<div style='color:green'>

### Exemple :

- Mécanique : Ellongation d'un ressort
- Électricité : Décharge d’un condensateur dans une résistance et une bobine
</div>

## Méthode de résolution

Soit l'équation différentielle du deuxième ordre $(E) : ay''(x) + by'(x) + cy(x) = h(x)$

1. On résout l'équation homogène $(E_0)$ : $ay''(x) + by'(x) + cy(x) = 0$ de la façon suivante :
   - On associe à $(E_0)$ l'équation caractéristique $ar^2 + br + c = 0\ (E_C)$
   - On calcule $\Delta = b^2 - 4ac$

Si $\Delta > 0$, $(E_C)$ admet deux racines réelles $r_1 = \frac{-b - \sqrt{\Delta}}{2a}$ et $r_2 = \frac{-b + \sqrt{\Delta}}{2a}$

Si $\Delta = 0$, $(E_C)$ admet une racine double $r_0 = \frac{-b}{2a}$

Les solutions de $(E_0)$ sont $y_0(x) = (Ax + B) e^{rx}$ avec $(A,B) \in \mathbb{R}^2$.

Si $\Delta < 0$, $(E_C)$ admet deux racines complexes $r_1 = \alpha + i \beta$ et $r_2 = \alpha - i \beta$

Les solutions de $(E_0)$ sont $y_0(x) = e^{\alpha x} (A \cos(\beta x) + B \sin(\beta x))$

2. On cherhce la solution particulière $y_1$ de $(E)$.
3. Les solutions de $(E)$ sont les fonctions $y = y_0 + y_1$
4. La connaissance de $y(x_0)$ et $y'(x_0)$ est nécessaire pour déterminer les constantes $A$ et $B$.

## Recherche d'une solution particulière

Soit l'équation différentielle du deuxième ordre $(E) : ay''(x) + by'(x) + cy(x) = h(x)$

LA forme de la solution particulière $y_1$ de $(E)$ dépend de celle de $h(x)$.

Nous développons les trois cas les plus courrant ($P_n(x)$, $\Psi_n(x)$ et $\Phi_n(x)$ désignent les polynômes de degré $n$).

- Premier cas : $h(x) = P_n(x)$

  Si $b \neq 0$ et $c \neq 0$, alors $y_1(x) = \Psi_n(x)$

  Si $b \neq 0$ et $c = 0$, alors $y_1(x) = x \Psi_n(x)$

  Si $b = 0$ et $c = 0$, alors $y_1(x) = x^2 \Psi_n(x)$

- Deuxième cas : $h(x) = P_n(x) e^{\lambda x}$

  Si $b \neq 0$ et $c \neq 0$, alors $y_1(x) = \Psi_n(x) e^{\lambda x}$

  Si $b \neq 0$ et $c = 0$, alors $y_1(x) = x \Psi_n(x) e^{\lambda x}$

  Si $b = 0$ et $c = 0$, alors $y_1(x) = x^2 \Psi_n(x) e^{\lambda x}$

- Troisième cas : $h(x) = P_n(x) \cos(px)$ ou $P_n(x) \sin(px)$

  Si $ip$ n'est pas solution de $(E_C)$, alors $y_1(x) = \Psi_n(x) \cos(px) + \Phi_n(x) \sin(px)$

  Si $ip$ est solution de $(E_C)$, alors $y_1(x) = x (\Psi_n(x) \cos(px) + \Phi_n(x) \sin(px))$

## Solution générale

La solution générale de l'équation de $(E)$ s'obtient en additionnant la solution d'équation homogène $(E_0)$ et la solution particulière $(E)$.
$$y(x) = y_0(x) + y_1(x)$$
