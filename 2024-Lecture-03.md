<!--
Cosine simularity: 0.9839793399164405
-->
## Introduction to Lecture Recording and Whisper Technology  

My experiment with recording lectures has been relatively successful, as I could recover what I was speaking. There is an open large language model from OpenAI that can translate audio to text, called Whisper. One of its architectures is known, and there is a C implementation that runs in parallel on Mac. You just download and execute it, and then you have a transcript of your speech.  

::: callout-note
The lecture is recorded for my own use, but it might be converted into a document. If someone volunteers to type the questions and equations and check them, that would be helpful.
:::
I don’t know what to do with the recordings yet, but for fun and to explore the technology, I will keep them. The recordings mostly capture my voice, but don’t hesitate to talk back—this will not appear in the transcript.

<!--
Cosine simularity: 0.9161822247076998
-->
## Recap and Isospin Questions  

We will talk today about structure functions, the structure of hadrons, and their internal composition—how we know about them. Before diving into that, I’d like to start with a recap and leave a few questions on the board.  

**Question 1**: Without looking at the PDG, just from the quark content, determine the isospin of the $\Delta^{++}$, $\Delta^+$, $\Delta^0$, and $\Delta^-$ particles. The quark content here is $uud$, $udd$, etc.  

For $\Delta^{++}$:  

- The state is $3\left(\frac{1}{2} \left( p^\uparrow p^\uparrow p^\uparrow \right)\right)$  
- Isospin calculation:  

$$
I_{\Delta^{++}} = \frac{3}{2} \left\{ \frac{3}{2}, \frac{3}{2} \right\} = \sqrt{\left(\frac{3}{2}\right)^2 - \left(\frac{3}{2}\right)^2}
$$  

For $\Delta^+$:  

- The state is $\frac{3}{2} \left( p^\uparrow p^\uparrow p^\downarrow \right)$  
- Isospin projection: $\left\{\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right\}$  

**Question 2**: What is the dimensionality of the isospin matrix acting on a space of three quarks with two charges (up and down)? If we treat the quarks as wavefunctions in two dimensions—where spin-up corresponds to the $u$-quark and spin-down to the $d$-quark—what is the size of this matrix?  

**Question 3**: What are the irreducible representations of this matrix acting on the quarks? In other words, how does it split into independent blocks that do not mix?  

::: callout-note
When discussing isospin, we focus only on light quarks ($u$, $d$). The $\Delta$ baryons are composed of these light quarks.
:::
I will return shortly to discuss these questions further. For now, think about the quark content and how it relates to isospin symmetry.

<!--
Cosine simularity: 0.8967760072181095
-->
## Meson and Quark Classification  

When discussing isospin, we focus only on light quarks ($u$, $d$). The first meson mentioned does not contain light quarks, so its isospin is zero. If a meson has one light quark, its isospin is $\frac{1}{2}$. For example, a meson like $B \bar{c}$ has no light quarks, so its isospin is zero.  

The notation often distinguishes heavy ($Q$) and light ($q$ or $L$) quarks. For the strange quark ($s$), if we consider it in the context of light quarks, it belongs to the $SU(3)$ classification. However, for isospin, $s$ is not included.  

For the cascade baryon ($\Xi_b$), it contains one light quark, so its isospin is $\frac{1}{2}$. The calculation follows the same logic as before:  

$$
I_{\Xi_b} = \frac{1}{2}
$$  

::: callout-note
Isospin assignments depend strictly on the presence of light quarks ($u$, $d$). Heavy quarks ($c$, $b$, $t$) or strange quarks ($s$) do not contribute to isospin.
:::
<!--
Cosine simularity: 0.9103741679387939
-->
## Pentaquark and Isospin Basics

The pentaquark is a particle observed in the $J/\psi$ proton channel. Generally, pentaquarks contain three light quarks.  

For isospin, we consider the delta group as a reference. The delta group consists of three quarks, similar to certain pentaquark configurations. The delta states include $\Delta^-$, $\Delta^0$, $\Delta^+$, and $\Delta^{++}$, which are combinations of up ($u$) and down ($d$) quarks.  

The isospin of the delta group is not a projection but the length of the vector. For $\Delta$, the isospin is $\frac{3}{2}$.  

When assigning isospin to a particle, we do not yet specify its charge state. For example, stating that the $B$ meson has isospin $\frac{1}{2}$ implies the existence of two charge states: $B^0$ and $B^+$. The $B^+$ meson specifically contains a $u$ quark and an anti-bottom ($\bar{b}$) quark.  

<!--
Cosine simularity: 0.9007396571518567
-->
## Quark Combinations and Charge Calculation

The $B^0$ and $B^+$ mesons can be understood through their quark compositions. The $B^+$ meson is formed by the combination $B \bar{u}$, while the $B^-$ meson is formed by $B \bar{d}$. For antiparticles, you must fully conjugate the quark content. For example, the antiparticle of $B \bar{u}$ is $B^-$, and the antiparticle of $B^0$ is $B^0$ bar.  

The cascade $B$ has isospin $\frac{1}{2}$, which implies a dimensionality of $2J + 1 = 2$, meaning there are two particles of this type.  

To calculate charges, recall the quark charges:  

- Upper row ($u, c, t$): $+\frac{2}{3}$  
- Lower row ($d, s, b$): $-\frac{1}{3}$  

For example:  

- Combining three lower-row quarks ($ddd$) gives a charge of $-1$.  
- Combining three upper-row quarks ($uuu$) gives a charge of $+2$.  

For the $B_s$ meson ($b \bar{s}$), the charge calculation is:  

- The $b$ quark contributes $-\frac{1}{3}$.  
- The $\bar{s}$ antiquark contributes $+\frac{1}{3}$ (since the antiquark flips the sign).  
- The total charge is $0$.  

If you replace the $\bar{s}$ with another lower-row quark, the charge becomes $-1$.  

<!--
Cosine simularity: 0.922436102714166
-->
## Antiparticles and Baryon-Antibaryon Distinction

There will be three bottom parts, and it involves a minus sign. The correct notation is $b^2$, not $B$.  

Now we consider the case with three quarks, which allows for several combinations. The spin of this particle could be either $1/2$ or $3/2$. For the $1/2$ case, we have four particles in the multiplet, similar to the $\Delta^{++}$.  

An important question arises: What is the antiparticle of the $\Xi_c^+$? The antiparticle is not simply $\Xi_c^-$ but rather $\overline{\Xi_c^-}$. This distinction is crucial for baryons and antibaryons, as they have different quark compositions. To denote the antiparticle, we place a bar over the quark components.  

Next, we examine the irreducible representation of the $z$ quarks.  

<!--
Cosine simularity: 0.9234066551017023
-->
## Constructing Quark Flavor Basis Functions  

We now examine the irreducible representation of the $z$ quarks. The dimensionality of the isospin matrix acting on three quarks is determined by the isospin space $I = 3/2$. For $SU(2)$, there are no decuplets or octets — those belong to $SU(3)$. However, the combination rules remain analogous.  

For example, the combination $UUU$ has isospin $I_3 = 3/2$, while $DDD$ has $I_3 = -3/2$. Intermediate states like $UUD$ and $UDD$ correspond to $I_3 = 1/2$ and $I_3 = -1/2$, respectively.  

To construct the quark flavor basis functions, we start with the state of maximum spin or flavor, which is $|3/2, 3/2\rangle$ (using spin or flavor notation equivalently). We then apply the lowering operator $J_-$ to generate the remaining states. The action of the lowering operator is given by:  

$$
J_- |j, m\rangle = \sqrt{j(j+1) - m(m-1)} \ |j, m-1\rangle
$$  

For the case where $j = m = 3/2$, this simplifies to:  

$$
J_- |3/2, 3/2\rangle = \sqrt{3} \ |3/2, 1/2\rangle
$$  

The lowering operator $J_-$ can be decomposed into individual quark operators:  

$$
J_- = J_-^{(1)} \otimes \mathbb{I}^{(2)} \otimes \mathbb{I}^{(3)} + \mathbb{I}^{(1)} \otimes J_-^{(2)} \otimes \mathbb{I}^{(3)} + \mathbb{I}^{(1)} \otimes \mathbb{I}^{(2)} \otimes J_-^{(3)}
$$  

When applied to $UUU$, this yields a superposition of states like $UUD$, ensuring proper normalization. The normalization condition requires that:  

$$
\langle \psi | \psi \rangle = 1
$$  

This is enforced using orthogonality relations: identical quark flavors (e.g., $UU$) are normalized, while different flavors (e.g., $UD$) are orthogonal.  

We can continue applying the lowering operator to generate the full multiplet, including states with $I_3 = -3/2$.  

::: callout-important
The antiparticle of $\Xi_c^+$ is not $\Xi_c^-$ but rather $\overline{\Xi_c^-}$. This distinction is crucial for baryons and antibaryons, as they have different quark compositions.
:::
For three quarks, the spin can be either $1/2$ or $3/2$. The $1/2$ case forms a quadruplet, analogous to the $\Delta^{++}$ multiplet. The irreducible representations must account for these spin-flavor combinations.

<!--
Cosine simularity: 0.9045148504887814
-->
## Combining Spin 1/2 Particles to Achieve Higher Spins  

We can follow through with more lowering operators to construct the wave function. The wave function for this state is a combination like $u^2(3ud + u du + e du)$, and another term like $(dud + d du + u du)$. This is straightforward for the highest spin state.  

Recall that we previously discussed spin $S = 47$, which gives a dimensionality of 95. To build this from spin $1/2$ particles, we need 94 spin $1/2$ particles — essentially 94 "legs." If we want to generate the 95-dimensional space (or 333, referring to the $E_z$ basis), we simply apply the lowering operator 62 times. This process can be automated.  

The situation becomes more complicated when considering intermediate spins, such as 90. Combining 94 spin $1/2$ particles allows for various total spin states. Can we get spin 0? Yes. Can we get spin 1? Yes. All intermediate spins are possible, with different multiplicities.  

The dimensionality of the matrix acting on this space is $2^{94}$, since each spin $1/2$ particle contributes a 2-dimensional representation. This can be written as a tensor product:  

$$
2 \otimes 2 \otimes 2 \otimes \cdots \otimes 2 \quad (\text{94 times})
$$  

This space decomposes into irreducible representations, corresponding to different spin combinations. Last time, we saw that this decomposition involves direct sums of spin states, denoted with plus signs. For example, the case of 94 spin $1/2$ particles follows this pattern.  

::: callout-important
The dimensionality $2^{94}$ is enormous, but the decomposition into irreducible representations simplifies the analysis by breaking it into manageable spin subspaces.
:::
The rules of spin addition apply here: combining multiple spin $1/2$ particles yields a spectrum of possible total spins, each with its own multiplicity. This is a direct consequence of the Clebsch-Gordan decomposition for $SU(2)$.

<!--
Cosine simularity: 0.9274902902019039
-->
## Dimensionality and Basis Construction in Isospin Space

The dimensionality of the isospin matrix acting on the $qqq$ configuration is given by:

$$
(3)(3)(3) \Rightarrow 3^3 = 27
$$

This counts the different combinations of spins with the plus sign. The number 94 is very large, but one of these combinations corresponds to spin 94 with different multiplicities. Constructing 94 or 33 is more challenging, but we will address this shortly.  

For the case of three quarks, we are dealing with the isospin group, which is equivalent to adding three spin-$\frac{1}{2}$ particles. The dimensionality here is determined by the basis vectors in the tensor product space. Each quark contributes a doublet, so the total number of basis vectors is:

$$
2 \otimes 2 \otimes 2 = 8
$$

This means there are eight basis functions in the space of three quarks. Examples include states like $|up, down, up\rangle$ or other combinations of up and down spins.  

::: callout-important
The dimensionality $2^n$ grows exponentially with the number of particles, but decomposing into irreducible representations simplifies the analysis by breaking it into manageable subspaces.
:::
The rules of spin addition apply here, following the Clebsch-Gordan decomposition for $SU(2)$. Combining multiple spin-$\frac{1}{2}$ particles yields a spectrum of possible total spins, each with its own multiplicity. This is a direct consequence of the tensor product structure in isospin space.

<!--
Cosine simularity: 0.9391633078810417
-->
## Combining Spin Halves and Dimensionality Check  

The basis functions include states like $|up, down, up\rangle$, $|up, up, up\rangle$, or $|down, down, up\rangle$, and so on. The total number of these combinations is $2^3 = 8$, since each quark can be in one of two states (up or down).  

The dimensionality of the isospin matrix acting on this space is $8 \times 8$. However, these combinations can be arranged such that they transform under isospin rotations without mixing with other states. This is called splitting into **irreducible representations** — grouping basis functions into multiplets that behave consistently under transformations.  

To answer the question about spin combinations, we apply spin algebra:  

$$
\frac{1}{2} \otimes \frac{1}{2} \otimes \frac{1}{2} = \frac{1}{2} \oplus \frac{1}{2} \oplus 1 \oplus 0
$$  

First, combining two spin-$\frac{1}{2}$ particles gives possible total spins of $0$ or $1$. Then, adding a third spin-$\frac{1}{2}$ can yield further combinations, including another $\frac{1}{2}$.  

::: callout-important
The dimensionality of the tensor product space is $2 \times 2 \times 2 = 8$, matching the number of basis states. This exponential growth in dimensionality with particle count is managed by decomposing into irreducible representations.
:::
The rules follow the Clebsch-Gordan decomposition for $SU(2)$, where combining spins systematically reveals the possible total spins and their multiplicities.

<!--
Cosine simularity: 0.9152561457119857
-->
## Constructing Orthogonal Basis Vectors in Spin Space

Here we have the product $2 \times 2 \times 2$, which represents the dimensionality of the spin space. This should be equal to the sum $2 + 3 + 4$, giving 8 here and 8 there. This means our rotation matrix, which is $8 \times 8$, can be split into blocks of 2 dimensions, 3 dimensions, and 4 dimensions, corresponding to the irreducible representations (irreps).  

It is clear how to construct the reducible basis for the highest isospin state. You start with the known state, such as $|up, up, up\rangle$, and then act with the lowering operator. However, constructing the other basis vectors requires more care.  

For the $1/2$ and $3/2$ isospin states, we have 4-plets and 2-plets. The key principle is that the new vectors we build must be orthogonal to what we've already constructed. We need wavefunctions with the same quark combinations but different coefficients to ensure orthogonality.  

For example, consider the combination:  

$$
\frac{1}{\sqrt{6}} \left( |u d u\rangle + |u u d\rangle - 2 |d u u\rangle \right)
$$

To verify orthogonality, we compute the scalar product with another state. When multiplying, only terms with identical quark content contribute. For normalization, squaring this gives:  

$$
1 + 1 + 4 = 6 \quad \Rightarrow \quad \text{Normalization factor} \ \frac{1}{\sqrt{6}}
$$

To construct the basis function for the $1/2$ state with projection $-1/2$, we act with the lowering operator on the upper state. This yields:  

$$
\frac{1}{\sqrt{6}} \left( |d u d\rangle + |u d d\rangle - 2 |d d u\rangle \right)
$$

The lowering operator acts as follows:  

- On $|u d u\rangle$, it gives $|d d u\rangle + |u d d\rangle$.  
- On $|u u d\rangle$, it gives $|d u d\rangle + |u d d\rangle$.  
- On $|d u u\rangle$, it gives $0$ (since lowering $|d\rangle$ gives zero).  

Combining these terms, we get:  

$$
|d u d\rangle + |u d d\rangle + |u d d\rangle - 2 |d d u\rangle = |d u d\rangle + 2 |u d d\rangle - 2 |d d u\rangle
$$

After normalization, this confirms the orthogonal basis construction.  

The $8 \times 8$ matrix acting on these states decomposes into blocks:  

- A $4 \times 4$ block (for the $3/2$ multiplet).  
- Two $2 \times 2$ blocks (for the $1/2$ multiplets).  
- Another $2 \times 2$ block (for the remaining states).  

This block-diagonal structure reflects the irreducible representations of the spin space.

<!--
Cosine simularity: 0.8770296752217894
-->
## Combining Spins and Constructing Representations

We start with a system of four spins, then reduce it to two. After removing redundant lines, we are left with three cups (states), five, and another one. By examining the representation, we identify two basis vectors: $|1\rangle$ and $|2\rangle$. The third basis vector must be orthogonal to both, such as $|1, -1, 0\rangle$.  

For the first vector, we have $|u t\rangle - |u d u\rangle$. The lower state is obtained by applying the lowering operator. While 94 might seem excessive, it illustrates the process for spin systems.  

Next, we consider spin-2 systems, which are more complicated. The framework applies not only to half-integer spins but also to integer spins. When combining two spin-1 systems, we use spin algebra to determine the possible states, ranging from the lowest (spin-0) to the highest (spin-2).  

We verify the dimensionality by checking:  

$$
3 + 3 = 1 + 3 + 5
$$

This confirms the decomposition into irreducible representations. We begin constructing the basis with the simplest case, using the volume operator. The ladder operator now involves four combinations:  

$$
|0, 0\rangle, \ |+\rangle, \ |-\rangle, \ |+\ +\rangle
$$

For the total spin-2 state, we have:  

$$
\frac{1}{\sqrt{2}} \left( |+\ +\rangle - |-\ -\rangle \right)
$$

To ensure orthogonality, we introduce a minus sign. Care must be taken when applying lowering operators, as Clebsch-Gordan coefficients may vary. For binary systems, these coefficients are identical.  

The normalization factor is $\frac{1}{\sqrt{2}}$, and we proceed by constructing orthogonal vectors in the spin space.

<!--
Cosine simularity: 0.8713288743863498
-->
## Spin Algebra and SU2 Representations

For binary systems, the Clebsch-Gordan coefficients are the same, so the normalization factor is always $\frac{1}{\sqrt{2}}$. Here, we have the Clebsch-Gordan coefficients (or "clefts") — I call them that because they are related. This is the effect of the lowering operator we derived earlier.  

The same decomposition can be checked using the PTG captures. Let's confirm this by cross-checking with the left-hand side. We want to construct $|2\rangle$ for $Y$ and express it as combinations of the following:  

$$
|1\rangle \otimes |1\rangle, \quad |1\rangle \otimes |0\rangle + |1\rangle \otimes |1\rangle, \quad |1\rangle \otimes |{-1}\rangle, \quad |0\rangle \otimes |0\rangle
$$

These coefficients can be found in the third table, and they satisfy the normalization condition $\frac{1}{\sqrt{2}}$.  

::: callout-note
The spin algebra appears in many courses — starting with quantum mechanics, then particle physics, and later in group theory. For $SU(2)$, it is straightforward, but $SU(3)$ is more complicated.
:::
For $SU(2)$, the key is to think in terms of dimensionalities and how spins add together. You need to know a few recipes for constructing these coefficients, which can even be derived without reference books. The method of combining Clebsch-Gordan coefficients will help you in these calculations.  

<!--
Cosine simularity: 0.8948070126539082
-->
## Proton Wave Function and Symmetry Considerations

The proton wave function must be constructed in the product of four spaces: color, space, isospin, and spin. The general form is a sum over components in these spaces, not a simple product:

$$
\Psi = \sum_i \Psi_{\text{space}} \otimes \Psi_{\text{isospin}} \otimes \Psi_{\text{spin}}
$$

However, the color wave function is a singlet (scalar) and can be factored out:

$$
\Psi = \Psi_{\text{color}} \otimes \sum_i \Psi_{\text{isospin}} \otimes \Psi_{\text{spin}}
$$

There is also an argument that the space wave function is a scalar and can be factored out, though this requires justification from the literature. The remaining parts — isospin and spin — are generally not factorizable and must be treated as entangled components.  

To understand the internal structure of hadrons, we need the proton wave function. Similarly, the delta baryon wave function will be addressed in homework, but it may be simpler to start with its symmetries.  

The baryon wave function must be color-neutral, as all hadrons are. It depends on spatial coordinates ($x$, $t$), isospin, and spin. These components are not independent in the general case; the wave function lives in the product of these spaces and can mix them.  

::: callout-note
The color wave function is a singlet, meaning it has no internal dimensionality and can be separated. The space wave function is also argued to be a scalar, though this requires further verification.
:::
For spin and isospin, the Clebsch-Gordan coefficients are essential for combining states. In $SU(2)$, the coefficients follow straightforward rules, but $SU(3)$ is more complex. The method of combining these coefficients (or "clefts") helps derive the wave function structure without reference books.  

The normalization factor for binary systems is always $\frac{1}{\sqrt{2}}$, and the coefficients can be cross-checked using tensor methods. For example, the state $|2\rangle$ can be expressed as combinations of:  

$$
|1\rangle \otimes |1\rangle, \quad |1\rangle \otimes |0\rangle + |1\rangle \otimes |1\rangle, \quad |1\rangle \otimes |{-1}\rangle, \quad |0\rangle \otimes |0\rangle
$$

These satisfy the normalization condition and can be found in standard tables. Spin algebra appears in quantum mechanics, particle physics, and group theory, with $SU(2)$ being simpler than $SU(3)$.
