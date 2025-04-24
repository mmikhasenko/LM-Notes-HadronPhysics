<!--
Cosine simularity: 0.9169510955556898
-->
## Introduction and Homework Discussion

Do you expect anyone else to find the problems difficult? At some point, I think yes. He found last week's problems too easy, so we should increase the difficulty.  

How was the homework problem level? Have you seen them before? In particle physics, some problems appear multiple times across different courses — first in nuclear physics, then in particle physics or quantum field theory.  

> [!NOTE]  
> Clebsch-Gordan coefficients are so important that you encounter them four times.  

They will be part of this week's homework, and I hope you won't have trouble with them.

<!--
Cosine simularity: 0.9445375076924339
-->
## Estimating Hadronic Cross Sections

Today's lecture will focus more on symmetries in hadron physics. We will start with QCD as discussed before, particularly the SU group, and then move to the phenomenology of the SU flavor group. We will discuss isospin and then explore the SU flavor group by interchanging up (u) and down (d) quarks. This will be connected to the Lorentz group, which has SU(2) as a subgroup responsible for rotations.  

You will see how the addition of spins relates to the addition of quarks inside hadrons. Much of this material will be a reminder of quantum mechanics concepts you’ve already encountered, and I hope it will be easy to follow. I particularly enjoy this part because it’s something you can derive once you isolate yourself from books and the internet — it’s a nice exercise in spin algebra.  

Before diving in, let’s briefly recap the previous lecture. One key question from last time was: **How would you estimate the typical cross section of hadronic reactions?** Not an exact calculation, but just an order of magnitude.  

The precise method involves integrating over all possible configurations of the squared matrix element $|\mathcal{M}_{if}|^2$, summing over final states, and accounting for flux and initial-state averaging. The formula is:  

$$
\sigma = \frac{1}{4\sqrt{(p_1 \cdot p_2)^2 - m_1^2 m_2^2}} \frac{1}{N_i} \sum_f |\mathcal{M}_{if}|^2 d\Phi_n
$$

- $\mathcal{M}_{if}$: Transition matrix element (initial $\to$ final).  
- $N_i$: Initial state averaging factor (spins, colors, etc.).  
- $d\Phi_n$: $n$-body phase space element.  

This gives the cross section in units of inverse GeV, which can then be converted to centimeters squared.  

But for a rough estimate, think of the cross section as an effective interaction area. Imagine a proton as a target fixed in space, and another proton colliding with it. The cross section represents the area where the reaction occurs — if the projectile misses this area, no interaction happens.  

The characteristic size of a proton is about 1 fermi ($1 \ \text{fm} = 10^{-13} \ \text{cm}$). The cross section is then roughly the geometric area:  

$$
\sigma \sim \pi r^2 \approx 10 \ \text{mb}
$$

where $1 \ \text{b} = 10^{-24} \ \text{cm}^2$.  

For hadrons, the total cross section is determined by their overlapping densities. If they are too far apart, they don’t interact — the strong interaction is very strong but short-ranged.  

> [!NOTE]  
> The typical hadronic cross section scale is around 10 millibarns, derived from the proton’s size.  

Now, let’s transition to symmetries in hadron physics, starting with QCD and the SU group. This will lead us to isospin and the SU flavor group, where we’ll explore how quark interchange relates to spin addition and the Lorentz group.  

This part of the discussion is particularly elegant because it relies on fundamental spin algebra, something you can work out independently with just pen and paper.  

Let me begin by reminding you of the last lecture’s key points and addressing any questions before moving forward.  

> [!IMPORTANT]  
> The cross-section estimation hinges on the proton’s size ($\sim 1 \ \text{fm}$), translating to an interaction area of $\sim 10 \ \text{mb}$.  

We’ll now proceed to discuss symmetries, starting with QCD and the SU group, and then connecting it to the phenomenology of the SU flavor group.  

The addition of spins inside hadrons mirrors the addition of quark states, and this will be a recurring theme as we link it to the Lorentz group’s rotational subgroup, SU(2).  

This material should feel familiar from quantum mechanics, and I hope it will be straightforward to follow.  

Let’s start by reviewing the last lecture’s content and addressing any lingering questions before diving deeper into symmetries.  

<!--
Cosine simularity: 0.9175687607416603
-->
## Defining Charge in QED and QCD

In QED, the charge is simply the electrical charge. The charge operator is defined as:

$$
Q = e\int d^3x \, \Psi^\dagger \gamma^0 \Psi = e\int d^3x \, j^0(x)
$$

where $j^\mu(x)$ is the electromagnetic current density. The charge can be probed using photons.  

In QCD, the charge is the color charge, associated with the $SU(3)$ gauge group. The charge operator in QCD is given by:

$$
Q^a_{QCD} = g_s\int d^3x \, \Psi_i^\dagger(x) \gamma^0 T^a \Psi_j(x)
$$

where $T^a$ are the generators of $SU(3)$.  

Now, suppose we are given a field $\Psi$. How do we determine its charge? The charge is a conserved quantity, meaning that for a freely moving field, the charge does not change. This conservation arises from a symmetry, as stated by Noether's theorem, which guarantees a conserved current. The charge is then defined as the integral of the zero-component of this conserved current.  

For the Dirac field, the charge density is $\Psi^\dagger \Psi$, which is a positive quantity for physical solutions. If $\Psi$ represents an electron, this would imply a positive charge. At first glance, this seems contradictory, but the sign of the charge is a matter of convention. We define the observed charge $Q$ to match our physical conventions, such as assigning $-e$ to the electron. The overall normalization is arbitrary; what matters is the conservation law.  

> [!NOTE]  
> The sign of the charge in QED is a convention. The conserved quantity is the key feature, not the specific value assigned to particles like the electron.  

The strong interaction is very strong but operates only at short distances. Hadrons interact when their densities overlap; if they are too far apart, they do not interact at all. This is why the typical hadronic cross section is determined by the proton's size, roughly $1 \ \text{fm}$, leading to an interaction area of about $10 \ \text{mb}$.  

The charge definitions in QED and QCD are fundamentally linked to their respective gauge symmetries—$U(1)$ for QED and $SU(3)$ for QCD—and the associated conserved currents. The distinction between observed charge and the mathematical definition is important, especially when matching theoretical predictions to experimental observations.

<!--
Cosine simularity: 0.916595410118432
-->
## Current and Charge in QCD

The constant in front of the charge operator does not matter — what's important is that this quantity is conserved in field theory. How we match this to our expectations is up to us.  

The current in QCD can be written as $j^\mu$ or sometimes as a lowercase $j$, where:  

$$
j^\mu = -e \bar{\Psi} \gamma^\mu \Psi
$$

Here, the minus sign in $-e$ is a convention to match our usual definition of charge. We could have defined electrons as positively charged particles, though that would be unconventional.  

To define the charge in QCD, we follow a similar approach as in QED. The quark field is still a fermion, so we retain the Dirac spinor structure, but now we must account for color indices. The charge operator in QCD is:  

$$
Q^a_{QCD} = g_s \int d^3x \, \Psi_i^\dagger(x) \gamma^0 T^a \Psi_j(x)
$$

Here, $\gamma^0$ is the Dirac matrix, and $T^a$ are the generators of $SU(3)$, representing the color charge. When we compute this for a quark field, we find that the charge is not simply red, green, or blue — it corresponds to one of the 8 possible color charges in QCD.  

The strong interaction is very strong but operates only at short distances. Hadrons interact when their densities overlap; if they are too far apart, they do not interact at all. This is why the typical hadronic cross section is determined by the proton's size, roughly $1 \ \text{fm}$, leading to an interaction area of about $10 \ \text{mb}$.  

The charge definitions in QED and QCD are fundamentally linked to their respective gauge symmetries — $U(1)$ for QED and $SU(3)$ for QCD — and the associated conserved currents. The distinction between observed charge and the mathematical definition is important, especially when matching theoretical predictions to experimental observations.  

<!--
Cosine simularity: 0.9089833123346178
-->
## Introduction to SU2 Group and Its Properties

The quark field $\psi$ in QCD carries a color index (1, 2, or 3), representing red, green, or blue. QCD has 8 charges, corresponding to the 8 gluons. For example, if $\psi$ has color indices $i=1,2,3$, its charge is an 8-component vector, where each component depends on which gluon probes it. These charges are computed using group theory, specifically the generators of $SU(3)$.  

Today, we focus on the $SU(2)$ group, which is fundamental in particle physics. A group must satisfy three properties:  
1. For every element $g \in G$, there exists an inverse $g^{-1} \in G$.  
2. For any $g_1, g_2 \in G$, their composition $g_1 \circ g_2 \in G$.  
3. There exists an identity element $e \in G$.  

$SU(2)$ is the special unitary group of $2 \times 2$ matrices with determinant 1. An element $g \in SU(2)$ satisfies:  

$$
g^\dagger g = 1, \quad \det g = 1
$$

This group is unitary (preserving inner products) and special (determinant 1). The generators of $SU(2)$ are the Pauli matrices, which we will discuss further.

<!--
Cosine simularity: 0.9362335009413588
-->
## Properties and Representations of SU2 Group

The group $SU(2)$ consists of unitary matrices with determinant 1. For any $U \in SU(2)$, the following holds:

$$
UU^\dagger = U^\dagger U = 1, \quad \det U = 1
$$

Here, $U^\dagger$ is the Hermitian conjugate of $U$, and the condition $UU^\dagger = 1$ ensures unitarity. The determinant condition $\det U = 1$ is what makes the group "special."  

This is the fundamental representation of $SU(2)$, where $U$ is a $2 \times 2$ matrix. While it is impossible to list all elements of $SU(2)$ explicitly due to its infinite size, the group composition rules are well-defined.  

To construct other representations, we map each element of $SU(2)$ to matrices of larger dimensions (e.g., $3 \times 3$ or $4 \times 4$) while preserving the group properties. $SU(2)$ is particularly nice because it allows a systematic way to build all possible representations.

<!--
Cosine simularity: 0.9188034298081221
-->
## Introduction to SU2 Group and Pauli Matrices

The $SU(2)$ group is a nice group because it provides a straightforward way of constructing any dimensional representation.  

From group theory, another key concept is the algebra. All group elements have a nice structure, where the generators $\sigma_1, \sigma_2, \sigma_3$ are the Pauli matrices.  

Any group element of $SU(2)$ can be represented in exponential form:  

$$
U = e^{i \theta \vec{J} \cdot \hat{n}}
$$

Here, $J^a = \frac{1}{2} \sigma^a$ are the generators, and $\sigma^a$ are the Pauli matrices.  

<!--
Cosine simularity: 0.9011745675344695
-->
## Matrix Exponentiation and Taylor Series  

The exponential of a matrix is well-defined through its Taylor expansion. For a matrix $A$, the exponential is given by:  

$$
e^A = I + A + \frac{1}{2}A^2 + \frac{1}{6}A^3 + \cdots
$$  

If the matrix is nilpotent (e.g., $A^2 = 0$), the series simplifies to just the first two terms:  

$$
e^A = I + A
$$  

This happens because higher powers of $A$ vanish after the first multiplication. For example, if $A$ is a $2 \times 2$ zero matrix, $A^2 = 0$, so the exponential reduces to $I + A$.  

The Taylor series is a powerful tool for computing matrix exponentials, especially when the matrix has special properties like nilpotency.

<!--
Cosine simularity: 0.9021596562838852
-->
## SU(2) Group and Spin Applications

The exponential of a matrix can be expressed as the sum of the identity matrix plus the matrix itself, plus higher-order terms. For example:

$$
e^A = I + A + \frac{1}{2}A^2 + \cdots
$$

When you multiply and observe how quickly the series converges, some terms may die out. For instance, if the matrix squared ($A^2$) equals the identity matrix $E$, the series does not vanish quickly, and one of the elements remains.  

This group is important in two key applications. First, **spin** arises due to the conservation associated with SU(2) symmetry, which acts on the Lorentz components of vectors. For a three-vector, rotations are described by rotation matrices, but for a spinor, rotations are given by the Pauli matrices $\sigma_i$.  

The second application is **flavor symmetry**. In mesons and baryons, transformations between up ($u$) and down ($d$) quarks can be performed continuously, similar to how spinor wave functions are characterized. This allows for a "flavor rotation" analogous to spin rotations in quantum mechanics.  

> [!NOTE]  
> The Pauli matrices ($\sigma_i$) are fundamental in describing spin rotations, while flavor symmetry extends similar principles to quark states.  

The algebraic structure of SU(2) is crucial in both spin and flavor symmetry, as seen in quantum mechanics and particle physics.

<!--
Cosine simularity: 0.8996625627682487
-->
## Introduction to Charges and Group Theory

Before moving on, let’s revisit these questions. We will now consider two new groups: the first is **allotations**, and the second is **flavor**.  

What is the charge of these groups? For QED, the charge is the electric charge. The physical quantity corresponding to the charge depends on the group.  

> [!NOTE]  
> The charge in a group theory context often corresponds to a conserved quantity, such as electric charge in QED or flavor charge in quark systems.  

<!--
Cosine simularity: 0.9355056374451567
-->
## Spin, Helicity, and Charge Computation

The physical quantity corresponding to the charge depends on the group. For QED, it is electric charge, while for $SU(3)$ in QCD, it is color charge.  

Consider a spinner with values 1, 4, 9, 14. Using the Pauli matrices ($\sigma_i$) as the linear generators of the group, we can compute a charge. The equation involves substituting the $t$ matrices with the Pauli matrices:  

$$
Q = \int \psi^\dagger \sigma_i \psi \, d^3x
$$

This charge corresponds to a parameter — specifically, the orientation of the spin. For a particle in motion, these values characterize the projection of the spin onto the direction of motion, which defines its helicity.  

> [!NOTE]  
> The computed charge in this context gives the three-dimensional direction of the spin, directly related to helicity.

<!--
Cosine simularity: 0.914945279586125
-->
## Introduction to Isospin and Generators

For the spin, we can consider the three-dimensional direction with components $s_1$, $s_2$, and $s_3$, corresponding to the $x$, $y$, and $z$ projections. The charge can be computed similarly using the wave functions $\psi$ that relate to the quark composition.  

In this case, the resulting quantity is called **isospin**, which satisfies:  

$$
I = 2 S_c
$$  

Here, $S_c$ represents the spin algebra. The charge computation depends on the group structure, analogous to how electric charge arises in QED or color charge in QCD.  

> [!NOTE]  
> The isospin operator is derived from the spin algebra, and its value is directly tied to the quark composition of the system.  

<!--
Cosine simularity: 0.9167933374846267
-->
## Commutator Relations and Pauli Matrices

This is called isospin, and it is related to the $SU(2)$ algebra recap. I assume you've seen these formulas before, so this will be a repetition for most of you.  

The commutator relation between the generators $J_i$ is given by:  

$$
[J_i, J_j] = i \epsilon_{ijk} J_k \quad \text{(cyclic: } i,j,k=1,2,3\text{)}
$$

Here, $\epsilon_{ijk}$ is the Levi-Civita symbol, and $J_i$ are the generators of the algebra. You can think of these as operators or matrices — it holds for any representation. For the fundamental representation, these are the Pauli matrices:  

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

The commutator relation implies that $[J_1, J_2] = i J_3$, and similarly for cyclic permutations. The Pauli matrices satisfy the same commutation relations, confirming their role as generators of $SU(2)$.  

> [!NOTE]  
> Fortunately, there is no ambiguity in conventions for Pauli matrices — they are universally defined as above.  

<!--
Cosine simularity: 0.9595549765594683
-->
## Diagonal Matrices and Rank in Group Theory

Fortunately, there is no different convention for this — we all use the same definition, and it's extremely important.  

The key question is: *How many of the generators of the group have diagonal form?* This is fundamental in group theory. All generators must be traceless because the condition $\det(M) = 1$ implies a relation between the determinant and trace of the matrix. Specifically, the determinant equals the exponential of the trace:  

$$
\det(M) = e^{\text{tr}(M)}
$$

Since $\det(M) = 1$, this enforces $\text{tr}(M) = 0$. However, the number of diagonal generators is crucial because it determines the eigenvalues and eigenvectors you work with.  

In our case, there is only one diagonal matrix among the generators, which is why the group is called **rank one**. For example, $SU(2)$ has rank 1 because only one generator (typically $\sigma_3$) is diagonal.  

> [!NOTE]  
> The rank of a group is deeply connected to its classification in group theory. Higher-rank groups have more diagonal generators, leading to richer structure.  

<!--
Cosine simularity: 0.9595630929488866
-->
## Spin States and Matrix Representations

There is only one diagonal matrix, and this matrix will be used to determine the physical quantity from the states. We will now act with these matrices on the states.  

We use the ket notation $|j, m\rangle$ for the states, where $|j, m\rangle$ represents a unit vector with only one non-zero component at the position corresponding to $m$. The dimension of this vector space is determined by $j$, where each component corresponds to a possible value of the spin projection.  

For a given $j$, there are $2j + 1$ possible projections: $-j, -j+1, \dots, j$. For example, when $j = 1/2$, we have a two-dimensional representation with states:  

$$
|1/2, 1/2\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1/2, -1/2\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

These matrices act as generators for the fundamental representation, operating on the vector space spanned by these two states. Any other vector in this space can be expressed as a linear combination of these basis states.  

The spin quantization axis defines the possible projections of the spin vector. For $j = 1/2$, the two projections correspond to spin-up ($m = +1/2$) and spin-down ($m = -1/2$). This is the simplest non-trivial case and serves as the foundation for understanding higher-dimensional representations.  

The matrices acting on these states are traceless, as required by the condition $\det(M) = 1$, which implies $\text{tr}(M) = 0$. In $SU(2)$, only one generator (typically $J_3$ or $\sigma_3$) is diagonal, making it a rank-one group.

<!--
Cosine simularity: 0.9312634352032335
-->
## Vector Space Notations and Lowering/Raising Operators

We can represent vectors in this space, such as $32 - i \ 9$ or $14^2$. Here, the notation $3$ simply refers to the vector space conventions. Any element acting on this space can be constructed using the operators we define.  

Now, let's quickly examine the lowering and raising operators. We define $G_+ = G_1 + i G_2$ and $G_- = G_1 - i G_2$, which are the lowering and raising operators. Their action on states changes the projection component—either increasing or decreasing it. For example, $G_+$ acting on a lower state moves the vector to a higher state.  

To demonstrate this, we compute the commutator:  

$$
G_+ G_- = J_1^2 + J_2^2 - i [J_1, J_2]
$$

This simplifies to $J^2 - J_3^2 \pm J_3$, where $J^2$ is the total angular momentum operator and $J_3$ is the projection operator. The exact form depends on the algebra of the generators.  

> [!NOTE]  
> The raising and lowering operators shift the $m$ eigenvalue of the state $|j, m\rangle$ by $\pm 1$, as seen in the earlier relations for $J_\pm$.  

The full expression involves additional terms, but the key idea is that these operators modify the state's projection while preserving the total angular momentum $j$.

<!--
Cosine simularity: 0.9182581262782797
-->
## Angular Momentum Operators and Their Actions

What I haven't yet given is how the operator $J^2$ acts on the state $|j, m\rangle$. We know that $J_3$ acting on $|j, m\rangle_\text{max}$ gives just one component, while $J^2$ acting on $|j, m\rangle$ yields $\hbar^2 j(j+1)$.  

Both $J^2$ and $J_3$ commute with the Hamiltonian in quantum mechanics. In our case, these operators commute with the action and Lagrangian, meaning they represent conserved quantities.  

Now, consider the action of $J_+$ and $J_-$ on the state $|j, m\rangle$. The lowering operator $J_-$ acts as:  

$$
J_- |j, m\rangle = \sqrt{(j+m)(j-m+1)} |j, m-1\rangle
$$

This gives a factor of $\sqrt{j(j+1) - m(m-1)}$, which adjusts the projection quantum number $m$ by $-1$. Similarly, $J_+$ raises $m$ by $+1$ with the corresponding coefficient.  

The commutator relations for these operators are:  

$$
[J_+, J_-] = 2J_3, \quad [J_3, J_\pm] = \pm J_\pm
$$

These relations are fundamental to the algebra of angular momentum operators.

<!--
Cosine simularity: 0.8628699798775729
-->
## Construction of Arbitrary Representations in SU(2)

The square root of $g - 1 - n^2$ plus $m(dm - n)$ arises from adding another $|j, m\rangle$ state. If we contract from the other side with the conjugate state $\langle j, m|$, using the normalization of $|j, m\rangle$, we obtain this coefficient.  

This is closely related to what we will see later in the lecture. The coefficient for lowering the state is given by:

$$
J_- |j, m\rangle = \sqrt{(j + m)(j - m + 1)} |j, m - 1\rangle
$$

Here, the term $\sqrt{j(j+1) - m(m-1)}$ adjusts the projection quantum number $m$ by $-1$. The corresponding raising operator $J_+$ acts similarly but with a $+1$ shift in $m$.  

The commutator relations for these operators are fundamental:

$$
[J_+, J_-] = 2J_3, \quad [J_3, J_\pm] = \pm J_\pm
$$

These relations define the algebra of angular momentum operators in SU(2). The action of $J^2$ on $|j, m\rangle$ yields $\hbar^2 j(j+1)$, while $J_3$ extracts the projection $m$. Both operators commute with the Hamiltonian, indicating conserved quantities in quantum mechanics.

<!--
Cosine simularity: 0.9208392081155281
-->
## Constructing Representations in Four Dimensions

The coefficient discussed here is associated with lowering operators, but it's important not to restrict its interpretation to just this algebra. Instead, it serves as a way to determine these coefficients.  

There is a connection to cleft coordinates, and we can extend this to other representations. To construct arbitrary representations in four dimensions, we use a method involving matrices analogous to the Pauli matrices ($\sigma$).  

For example, in the case of $D$, we define $G_+$ as the operator that raises the projection of a state. Its matrix elements in a four-dimensional basis (e.g., $|0\rangle, |1\rangle, |3\rangle, |7\rangle$) are non-zero only at specific positions, say $x_1, x_2, x_3$, with the rest being zero.  

The action of $G_+$ on a state corresponds to a four-dimensional representation with spin $\frac{3}{2}$, since the number of components is $2j + 1$. This implies $j = \frac{3}{2}$.  

> [!NOTE]  
> The raising and lowering operators in higher dimensions generalize the SU(2) ladder operators, with matrix elements determined by the representation's dimension and spin.  

<!--
Cosine simularity: 0.8871944117249053
-->
## Constructing J Matrices and Spin Representations

For a state with $j = 3$, the coefficient is given by $g + 2j + 1$. The matrix elements for $J_-$ can be constructed as follows:  

$$
J_- = \begin{pmatrix}
0 & \sqrt{3} & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
\end{pmatrix}
$$

Here, the non-zero element $\sqrt{3}$ corresponds to the transition between states $|3/2\rangle$ and $|1/2\rangle$.  

The operators $G_1$ and $G_2$ are defined in terms of the ladder operators $G_+$ and $G_-$:  

$$
G_1 = \frac{G_+ + G_-}{2}, \quad G_2 = \frac{G_+ - G_-}{2i}
$$

Meanwhile, $G_3$ (or $J_3$) is the diagonal matrix containing the eigenvalues of the spin projection.  

> [!NOTE]  
> The dimension of the representation determines the spin $j$. For example, a 95-dimensional representation corresponds to $j = 47$, since $2j + 1 = 95$.  

The diagonal entries of $J_3$ in this representation would be:  

$$
47/2, \ 45/2, \ \ldots, \ -47/2
$$

These values correspond to the possible projections of spin $j = 47/2$.  

To construct the full representation, one first builds $J_+$ and $J_-$ using the standard ladder operator formulas, then combines them to obtain $G_1$ and $G_2$.  

<!--
Cosine simularity: 0.9381459498385765
-->
## Constructing Arbitrary Representations of the SC2 Group

We have the generators $G_1$ and $G_2$. The key step is to assign the exponents for arbitrary rotations, since the group element is given by $e^{-i \alpha G}$.  

> [!NOTE]  
> This construction is typically done computationally rather than manually.  

The discussion so far covers how to construct arbitrary representations of the SC2 group. The group $SU(2)$ plays a central role in this process.

<!--
Cosine simularity: 0.9007720100667088
-->
## Introduction to Xi and Xic Particles

The quark content in the Particle Data Group (PDG) for one of these particles is $|ssu\rangle$ or $|ssd\rangle$. The particle is called the $\Xi$ (xi), named after the Greek letter. In the PDG, it has two strange quarks ($s$) and either an up ($u$) or down ($d$) quark.  

The charged state is $\Xi^-$ ($|ssd\rangle$) and the neutral state is $\Xi^0$ ($|ssu\rangle$). These two particles have very similar properties, with close masses and identical behavior except for their charge.  

Another example is the $\Xi_c$ (xic) particle. The quark content here involves a charm quark ($c$). The charge assignments are:  
- The upper state has a charge of $+1$ ($\Xi_c^+$), with quark content like $|usc\rangle$.  
- The lower state is neutral ($\Xi_c^0$), with quark content like $|dsc\rangle$.  

These particles, $\Xi_c^+$ and $\Xi_c^0$, are well-known experimentally. They have very similar masses and lifetimes, just like the $\Xi^-$ and $\Xi^0$ states.  

<!--
Cosine simularity: 0.9370039322332746
-->
## Discovery and Controversy of the 6 ICC Particle

The particles discussed here have very similar masses and lifetimes, making them appear identical. The third particle is tentatively named **6 ICC**, while the upper state has a double charge ($++$) and the lower state is singly charged ($+5cc$).  

One experiment reported observing a signal resembling this particle, appearing as a "bump" in the data. However, the LHCb experiment did not confirm its presence at the expected mass. Instead, LHCb discovered another state, but its mass conflicted with previous measurements by about 40 MeV.  

> [!IMPORTANT]  
> The discrepancy in mass measurements between experiments suggests unresolved systematic effects or a possible misidentification of the state.  

This inconsistency has made the 6 ICC particle a frequent topic of discussion at conferences.

<!--
Cosine simularity: 0.9345095919128487
-->
## Symmetry and Mass Properties of U and D Quarks

There is a 40 MeV difference in mass compared to what was seen before. This is scandalous because, so far, we've observed that replacing the U and D quarks with each other barely changes the mass or properties. For this case, it would be impossible. We know from strong interactions that these two particles must have the same properties, yet they exhibit significantly different masses.  

The strong interaction is blind to the flavor of light quarks, so their properties should remain consistent. The approximate masses are:  

$$
m_u, m_d \approx 3 \text{ MeV}, \quad m_s \approx 100 \text{ MeV}
$$  

The discrepancy suggests a conflict with our understanding of how these quarks behave under strong interactions.

<!--
Cosine simularity: 0.9019675771575024
-->
## Introduction to Blind Analysis in Particle Physics

Strong interactions conserve properties, meaning the interaction is blind to quark flavor. Whether a quark is present or not, the outcome is determined by strong interaction dynamics.  

If you analyze data and discover a new particle, it could make you a prominent figure in particle physics, as such findings often lead to multiple PhD projects. However, blind analysis complicates this process. Researchers define their study parameters—such as the reactions and mass window—but avoid looking at the target region until all selection criteria and procedures are optimized.  

Only after finalizing all analysis steps—fixing cuts, writing programs—do they "unblind" the mass range. Sometimes, despite extensive work, the unblinding reveals no signal, leaving PhD students disappointed.  

> [!NOTE]  
> Blind analysis prevents bias by delaying access to the signal region until the full analysis is finalized.  

The approximate quark masses are:  

$$
m_u, m_d \approx 3 \text{ MeV}, \quad m_s \approx 100 \text{ MeV}
$$  

This suggests a discrepancy, as strong interactions should preserve quark properties, yet observed mass differences challenge this expectation.

<!--
Cosine simularity: 0.8927716577164105
-->
## Understanding Quark Decay Channels and Symmetry in QCD

In our analysis, we pressed the button to unblind the data, but unfortunately, no signal was observed. This suggests we may not have picked the right configuration yet. The particle in question decays into many different channels, and our current statistical limitations prevent us from observing it in rare decay modes.  

Strong interactions are flavor-blind—they do not distinguish between a $u$ quark, $d$ quark, or any other flavor. If you examine the particle data group (PDG) listings, you'll find that the mass difference between the $u$ and $d$ quarks is around $3 \ \text{MeV}$.  

> [!NOTE]  
> These are the current quark masses—the values you input into the Lagrangian before gluon condensation and dynamical mass generation.  

For strong interactions, what matters is that these quarks have nearly identical masses. This leads to an approximate symmetry in QCD, where the group permuting $u$ and $d$ quarks is almost exact.

<!--
Cosine simularity: 0.9270547622741692
-->
## Symmetry Breaking and Mass Terms in QCD Lagrangian

The symmetries of the QCD Lagrangian include a term for the gluons and a term for the quarks. The quark term, the Dirac term, contains a mass parameter. If the quark masses are not identical, this mass term breaks the symmetry. For the $u$ and $d$ quarks, the masses are nearly the same, so the symmetry is not broken by the mass term, making it a good symmetry.  

The mass of the $s$ quark, however, is around $100 \ \text{MeV}$, which breaks the symmetry. This leads to an approximate $SU(3)$ flavor symmetry, corresponding to the $u$, $d$, and $s$ quarks.  

> [!NOTE]  
> The $u$ and $d$ quark mass difference is about $3 \ \text{MeV}$, which is negligible for strong interactions, preserving the approximate symmetry.  

The symmetry breaking due to mass differences is a key feature of the QCD Lagrangian.

<!--
Cosine simularity: 0.9106136576470412
-->
## Introduction to Isospin and Cascade Particle

We can approximate the $SU(2)$ flavor group, where $u$ and $d$ quarks are treated as the same particle in the isospin wave function. A rotation in this space is a good symmetry.  

The cascade particle (historically named due to its decay pattern) is represented as a single particle in our consideration with respect to the strong interaction.  

> [!NOTE]  
> The correct pronunciation is difficult for non-Greek speakers, so it is commonly referred to as "cascade."  

In this framework, the cascade particle is treated as a state within the isospin symmetry, where $u$ and $d$ quarks are indistinguishable under strong interactions.

<!--
Cosine simularity: 0.9343637484193199
-->
## Combining Spin and Isospin Representations

Now we consider a single particle with respect to the strong interaction, which has an isospin wave function. This is very similar to spin—we again have a two-dimensional vector space where group elements act. The unitary transformation is given by:

$$
U = e^{-i \alpha G}
$$

Here, $G$ represents the generator of the group.  

> [!NOTE]  
> The charge of the group can be determined by applying the equation for the charge, which clarifies the role of isospin.  

Isospin behaves analogously to spin:  
- A doublet (two-component representation) corresponds to isospin $1/2$.  
- A multiplet of four dimensions would correspond to isospin $3/2$.  
- For 95 dimensions, the isospin would be 47.  

You might wonder how we obtain higher-dimensional representations if we only have two quarks ($u$ and $d$). The key is that when considering multiple quarks, the group structure changes. Here, we stick with $SU(2)$, where we only permute the two quarks.  

Higher-dimensional representations appear when combining particles—such as multiple quarks—into a single system. This introduces a tensor product structure, where the total isospin (or spin) of the combined system must be considered.  

For example, if we have two systems, each with isospin $1/2$, their combined state can form:  
- A **triplet** ($J = 1$):  
  $$
  \frac{uu + dd}{\sqrt{2}}, \quad ud, \quad du
  $$
- A **singlet** ($J = 0$):  
  $$
  \frac{ud - du}{\sqrt{2}}
  $$

This is analogous to combining spins in quantum mechanics. The total isospin of the system is determined by the Clebsch-Gordan decomposition of the constituent representations.

<!--
Cosine simularity: 0.9325707728087054
-->
## Combining Spin Vectors and Total Spin

For the case of $SU(2)$, we are still dealing with the $SU(2)$ group. You can think of the system as two vectors—one in each hand—with spins $j_1$ and $j_2$. The total spin $J$ of the system can take values from $|j_1 - j_2|$ to $j_1 + j_2$.  

This is analogous to combining vectors in regular vector space: you take one vector and attach the other to it. The resulting vector can have different lengths depending on the angle between them. However, there are minimal and maximal possible lengths, and all intermediate values are allowed.  

The general rule for angular momentum addition is:  

$$
j_1 \otimes j_2 = |j_1 - j_2| \oplus \cdots \oplus (j_1 + j_2)
$$

The dimensions of the resulting representations follow the sequence:  

$$
\text{Dim: } 1 + 3 + 5 + \cdots + (2(j_1 + j_2) + 1)
$$

For example, combining spins $3$ and $2$ gives:  

$$
3 \otimes 2 = 1 \oplus 2 \oplus 3 \oplus 4 \oplus 5
$$

The minimal total spin occurs when the vectors are antiparallel, and the maximal when they are parallel. All intermediate alignments correspond to the allowed values in between.

<!--
Cosine simularity: 0.9369996903947596
-->
## Combining Spin Vectors and Representation Theory

Let's consider the combination of spin vectors and how they relate to representation theory. The general rule for angular momentum addition is:

$$
j_1 \otimes j_2 = |j_1 - j_2| \oplus \cdots \oplus (j_1 + j_2)
$$

Here, $j_1$ and $j_2$ are the spins of the two systems being combined, and the resulting total spin $J$ can take any value from $|j_1 - j_2|$ up to $j_1 + j_2$.  

For example, combining spin $\frac{1}{2}$ with another spin $\frac{1}{2}$ gives possible total spins of $0$ and $1$. Similarly, if we combine spin $3$ and spin $2$, the possible total spins are:

$$
3 \otimes 2 = 1 \oplus 2 \oplus 3 \oplus 4 \oplus 5
$$

The dimensions of these representations follow the sequence:

$$
\text{Dim: } 3 + 5 + 7 + 9 + 11
$$

> [!IMPORTANT]  
> The dimensions on the left and right must match. For spin $3$ (dimension $7$) and spin $2$ (dimension $5$), the total dimension is $7 \times 5 = 35$. On the right, the sum of dimensions is $3 + 5 + 7 + 9 + 11 = 35$. This consistency is a crucial check when combining spins.  

The basis in this space can be thought of as unit vectors in each dimension. For example, a $35$-dimensional vector has blocks corresponding to the different spin sectors: $3, 5, 7, 9, 11$.  

> [!NOTE]  
> Group theory tells us that these blocks do not mix under rotations. A matrix acting on this $35$-dimensional space will only rotate components within each block, not between them. This is the essence of irreducible representations.  

If a system has a total spin of $3$, no rotation can change it to $4$. This is a fundamental property: under rotations, the total spin is preserved. Mathematically, this means the interaction matrix is block-diagonal, with no mixing between different spin sectors.  

Now that we understand how to combine spins, we can apply this to practical examples. The key takeaway is that the dimensions must align, and the resulting representations decompose into independent blocks corresponding to each possible total spin.

<!--
Cosine simularity: 0.9605135048931919
-->
## Introduction to Isospin and Spin in Particle Physics

Before doing a few practical combinations, let's quickly introduce charge conjugation. It should be clear that what we discussed about spin applies equally to isospin. In particle physics, you often deal with both, and one shouldn't mix them up.  

We use isospin when constructing the quark wave function, while spin is used when combining particles to understand angular dependence. The rotational group has the same algebra and methods for both—just remember whether you're working with flavor $SU(2)$ (isospin) or the Lorentz part (spin).  

> [!IMPORTANT]  
> The key distinction is the context: isospin deals with flavor symmetry, while spin describes angular momentum. The mathematical framework is identical, but their physical interpretations differ.

<!--
Cosine simularity: 0.934302020469882
-->
## Parity and Charge Conjugation Operators in Particle States

What we're discussing here is either flavor $SU(2)$ or the Lorentz part of the Lorentz group (rotational $SU(2)$). Parity and charge conjugation are operators that act on states.  

The parity operator $\hat{P}$ performs a space inversion with respect to the origin. It answers the question: how does the wave function of a particle change when you flip it through the origin? This is intuitive—for a vector, flipping all spatial components through the origin reverses its direction.  

For any particle, you can determine its parity. When $\hat{P}$ acts on a state $|\psi\rangle$, the eigenvalue must be $\pm 1$ because applying it twice returns the original state:  

$$
\hat{P} | \psi \rangle = \pm | \psi \rangle
$$

Charge conjugation $\hat{C}$ flips all charges in the system. It is well-defined only for neutral particles or particle-antiparticle systems. Like parity, its action on a state yields eigenvalues $\pm 1$:  

$$
\hat{C} | \psi \rangle = \pm | \psi \rangle
$$

> [!IMPORTANT]  
> The key distinction between spin and isospin lies in their physical interpretation—spin describes angular momentum, while isospin deals with flavor symmetry. The mathematical framework (rotational $SU(2)$) is identical for both.  

<!--
Cosine simularity: 0.8916620059184868
-->
## Charge Conjugation and Particle States

By convention, we define the charge conjugation eigenvalue as either $+1$ or $-1$. When the charge conjugation operator $\hat{C}$ acts on a state, it returns the same state if the particle is neutral. For charged particles, $\hat{C}$ transforms the state into its antiparticle counterpart (indicated by the prime notation).  

For any particle, you can look up its charge conjugation eigenvalue. However, not all particles are eigenstates of $\hat{C}$. For example, the $\pi^0$ meson has:  

$$
\hat{C} | \pi^0 \rangle = + | \pi^0 \rangle
$$  

Its quantum numbers are $J^{PC} = 0^{-+}$ and isospin $I = 1$. The Particle Data Group provides comprehensive listings of these quantum numbers.  

For charged pions ($\pi^+$, $\pi^-$), charge conjugation is still assigned as positive, even though they are not eigenstates of $\hat{C}$ — acting with $\hat{C}$ on $\pi^+$ yields $\pi^-$. The convention is derived from the neutral member of the multiplet.  

> [!IMPORTANT]  
> The charge conjugation operator is well-defined only for neutral particles or particle-antiparticle systems. For charged particles, it maps the state to its antiparticle, not an eigenstate.  

<!--
Cosine simularity: 0.9471541205068776
-->
## Spin and Parity Combinations for Particle States

When applying charge conjugation ($\hat{C}$) to $\pi^+$, you get $\pi^-$, but we still assign a charge conjugation value for convenience in applications. The charge conjugation of a neutral particle multiplet determines this assignment.  

To find the total spin ($J$), parity ($P$), and charge conjugation ($C$) for a combination of particles, follow these steps:  
1. **Total spin $J$**: Compute it using spin algebra (vector addition of spins).  
2. **Parity $P$**: It is multiplicative, given by $(-1)^L$, where $L$ is the orbital angular momentum.  
3. **Charge conjugation $C$**: Also multiplicative, derived from the product of individual $C$ eigenvalues.  

> [!IMPORTANT]  
> The factor $(-1)^L$ arises from the parity transformation of the spatial wavefunction under coordinate inversion.  

For example, combining two particles with $L = 1$ yields a parity of $-1$. This is a crucial skill for determining possible spin-parity combinations in particle systems.  

<!--
Cosine simularity: 0.9423803255151243
-->
## Charge Conjugation and Spin Combinations for Fermions  

For unequivocal fermions, charge conjugation does not apply, so we consider only spin ($j$) and parity ($p$). When combining two particles, we start with orbital angular momentum $L = 0$ and focus on spin and charge combinations.  

> [!IMPORTANT]  
> The total spin $J$ is determined by vector addition of individual spins, while parity $P$ is multiplicative and given by $(-1)^L$.  

For example, combining two particles with $L = 0$ simplifies the analysis to pure spin combinations.

<!--
Cosine simularity: 0.9185823663422268
-->
## Excitation Spectrum and Quark Model in Lambda Baryons

When the orbital angular momentum $L = 0$, we combine spin and charge multiplicatively. Starting with spin $1/2$ and adding 0, the result remains $1/2$.  

> [!IMPORTANT]  
> The charge part is multiplicative, not additive.  

For the first row, we add 1 unit of angular momentum ($\Delta L = 1$), resulting in states with $J = 1/2$ and $J = 3/2$. The second row follows by adding 2 units, with the parent state determined by the rule $1N + 1$.  

For example, starting from $L = 0$, the excitation spectrum for $\Lambda_c^+$ includes states with negative parity, such as $J^P = 1/2^-$ and $3/2^-$.  

This framework applies to the quark model description of $\Lambda$ baryons.

<!--
Cosine simularity: 0.9590870865610963
-->
## Quark Model and Isospin Symmetry in Heavy Quarks

In the quark model, we consider heavy quarks where gluons have all condensed. The quarks are heavy, and among them is the charm quark, which is not part of our symmetry.  

From the flavor considerations of the group, the quarks can be in isospin $I = 1$ or $I = 0$. This is how we combine the isospin, which is the flavor part of the group. There is a symmetry that holds for variance, but since the quarks are the same particle, they must be in a symmetric combination.  

If they are in isospin $I = 0$, they are arranged antisymmetrically. For example, isospin zero introduces a minus sign, so the spin combination must also be in spin $S = 0$ to ensure overall antisymmetry.  

> [!IMPORTANT]  
> The overall wave function for the baryon must be antisymmetric.  

The color wave function contributes a minus sign, and the spin wave functions must correspond to spin $S = 0$ for the $u$ and $d$ quarks. For the $S$-wave, the spatial part is symmetric, but a minus sign is still missing in the overall antisymmetry condition.  

The isospin wave function is determined, and the spin wave functions must align with the spin-zero state of the $u$ and $d$ quarks.

<!--
Cosine simularity: 0.9414475513716338
-->
## Excitation Spectrum of Baryons and Lambda Particles

The spin wave functions correspond to the spin-zero state of the $u$ and $d$ quarks. Now we can consider how this baryon is excited. We discussed already that one way of making different particles is to interchange $u$ and $d$ quarks. However, since it is isospin zero, there are no other particles in this multiplet — it is only one $\Lambda_c$.  

The other way to make different particles is to excite the system. You can excite it radially, like the hydrogen atom, to make the object larger. Recall the hydrogen atom, where the principal quantum number $n$ determines the size of the system, essentially describing the electron's orbitals. The same applies to $\Lambda_c$: you can have $1s$, $2s$, and so on. The ground state is $\Lambda_c$, and the next excited state would be a larger $\Lambda_c$, which we might call $\Lambda_c^{**}$.  

> [!NOTE]  
> The $\Lambda_c^{**}$ state has been observed experimentally and is relatively broad.  

You can also excite the system orbitally by introducing angular momentum between, for example, the $u$-$d$ quark pair and the heavy quark (the charm quark in $\Lambda_c$). This corresponds to $P$-wave states, labeled as $P_{1/2}$ and $P_{3/2}$. The quantum numbers of these states have been experimentally determined.  

> [!IMPORTANT]  
> When we excite the system, we obtain different particles. The Particle Data Group (PDG) lists around seven different $\Lambda_c$ states discovered in experiments: the ground state, two radial excitations, two orbital excitations, and one higher-energy state whose multiplet assignment is still uncertain.  

These states, although listed as distinct particles, are essentially excitations of the ground-state $\Lambda_c$. Understanding how to construct this spectrum is crucial.  

<!--
Cosine simularity: 0.936360389967747
-->
## Spin Algebra and Angular Momentum in Particle Decays

The state $\lambda$ is super important. Learn how to construct the spin algebra table. Constructing the $S$-wave ($L = 0$) with Condon-Shortley phase conventions is straightforward. Adding one unit of angular momentum is also straightforward, but one must avoid mixing up the procedure.  

When combining states with orbital angular momentum zero, they must be considered separately. For example, in the decay of particle $A$ into particles $B$ and $C$, suppose:  
- Particle $A$ has quantum numbers $0^+$.  
- Particle $B$ is a vector meson with $1^-$.  
- Particle $C$ has $2^-$.  

The decay occurs in the rest frame of $A$, with particles $B$ and $C$ emitted in opposite directions at an angle. The question is: *What is the orbital angular momentum in this decay?*  

> [!NOTE]  
> If the decay proceeds via an $S$-wave ($L = 0$), the possible $J^P$ is only $1^-$. In a $P$-wave, the parity would be positive, and a $D$-wave is required to reach $2^-$.  

Thus, in this decay, the partial wave must be a $D$-wave due to the quantum number constraints.  

> [!IMPORTANT]  
> Mastering this table construction is a crucial skill for analyzing particle decays. We will practice this further to solidify understanding.  

<!--
Cosine simularity: 0.92744607720623
-->
## Hydrogen Atom Excitation Spectrum in a Magnetic Field

Let's consider a hydrogen atom placed in a strong magnetic field. The problem is to determine the excitation spectrum for states with principal quantum number $n < 3$. Specifically, we examine the $1s$, $2s$, $2p$, $3s$, and $3d$ levels, but neglect the $f$-wave ($L \geq 3$) since $L$ must be less than $n$ in a hydrogen atom.  

> [!NOTE]  
> For a hydrogen atom, the orbital angular momentum quantum number $L$ satisfies $L < n$, where $n$ is the principal quantum number. This restricts the possible states, such as excluding $f$-waves for $n < 4$.  

We also neglect the spin of both the proton and the electron for simplicity. The task is to draw the energy spectrum of these states under the influence of the magnetic field.  

> [!IMPORTANT]  
> The Zeeman effect splits the energy levels in a magnetic field. For states with $L \geq 1$, the degeneracy is lifted, and each level splits into $2L + 1$ sublevels.  

This problem serves as a good exercise to understand how quantum states behave in external fields. We will focus on the $s$, $p$, and $d$ orbitals up to $n = 3$, ensuring no $f$-waves are included.  

<!--
Cosine simularity: 0.877894458468116
-->
## Lecture Closing Remarks and Student Interaction

The wave not including the $f$-wave presents beautiful puzzles. You may have seen this problem somewhere already.  

Thanks a lot for coming, and I hope to see you next time. As always, if you have any questions or suggestions, I'm open to discussion. You can also whisper them to me.  

<!--
Cosine simularity: 0.9233675677468438
-->
## Attendance Check and Student Interaction

If you have any suggestions, I'm open to them. You can also whisper them anonymously to Ilya and R.  
Did anyone notice if other students from the class didn't show up today? I would then give a reminder.  

> [!NOTE]  
> Anonymous feedback can be shared with Ilya or R for discretion.  

Okay, let’s proceed. Hi, John. Is everything all right? Yes.  

<!--
Cosine simularity: 0.8926993883024781
-->
## Introduction and Homework Discussion

Do you expect anyone else to find the problems difficult? At some point, I think yes. He found last week's problems too easy, so we should increase the difficulty.  

How was the homework problem level? Have you seen these problems before? In particle physics, some problems appear multiple times across different courses — first in nuclear physics, then in particle physics, and later in quantum field theory.  

For example, Clebsch-Gordan coefficients are encountered repeatedly because they are essential.  

> [!NOTE]  
> Clebsch-Gordan coefficients ($C^{j_1 j_2 j}_{m_1 m_2 m}$) describe the coupling of angular momenta in quantum mechanics.  

They will be part of this week's homework, and I hope you won't have trouble with them.  
