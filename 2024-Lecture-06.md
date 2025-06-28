<!--
Cosine simularity: 0.9267377551237035
-->
## Introduction to Lambda Decay and Interaction Type

Let's start with the physics reaction where the lambda baryon decays into a proton and a pion:  

$$
\Lambda \rightarrow p + \pi^-
$$

To analyze this, we follow a standard checklist:  

1.**Identify the interaction type** responsible for the decay.  
2. Determine the variables describing the process.  
3. Write the matrix element for the process.  
4. Calculate the polarized decay width.  

::: callout-important
The decay involves a **flavor change** (strangeness violation), so it must be mediated by the **weak interaction**. Strong interactions preserve flavor, while weak interactions allow transitions like $s \rightarrow u$.
:::
The initial state ($\Lambda$) has strangeness $S = -1$, while the final state ($p + \pi^-$) has $S = 0$. Since parity is not conserved in weak interactions, this decay violates parity.  

Here’s a simplified diagrammatic representation (not a Feynman diagram):  

-**Initial state**: $\Lambda$  
- **Final state**: $p + \pi^-$  
- **Interaction vertex**: Weak decay (flavor-changing).  

The matrix element $\mathcal{M}$ for this process would involve weak coupling constants and quark-level transitions like $u \bar{d}$ for the pion.

<!--
Cosine simularity: 0.9107277263055694
-->
## Kinematics and Variables in Lambda Decay  

We are analyzing the decay $\Lambda \rightarrow p + \pi^-$. This is a one-to-two transition, and the kinematics are simplest when working in the center-of-mass frame. Here, the initial $\Lambda$ is at rest, and the final-state proton and pion carry momenta of fixed magnitude determined by their masses:  

$$
|\vec{p}_p| = |\vec{p}_\pi| = \sqrt{\frac{(m_\Lambda^2 - (m_p + m_\pi)^2)(m_\Lambda^2 - (m_p - m_\pi)^2)}{4m_\Lambda^2}}
$$

Since there is no preferred spatial orientation in this system, no angular variables are needed to describe the process. The momenta of the particles define the only directions, and we can align the $z$-axis arbitrarily (e.g., along the proton momentum for convenience).  

::: callout-note
The kinematics of a two-body decay in the center-of-mass frame are fully constrained by energy-momentum conservation, leaving no free variables. The momenta magnitudes are fixed by the particle masses.
:::
<!--
Cosine simularity: 0.9372389708310774
-->
## Spin Projection and Matrix Elements in Lambda Decay

We can choose the $Z$-axis along the direction of the particle momenta. The amplitude describing this process is denoted by $H$. The dependencies of $H$ are limited to discrete indices of spin projection, as there are no free kinematic variables in this decay.  

The particles involved in the interaction have the following spin and parity assignments:  

-$\Lambda$: $J^P = \frac{1}{2}^+$  
- Proton: $J^P = \frac{1}{2}^+$  
- Pion: $J^P = 0^-$  

Since this is a weak interaction, parity is not conserved in the decay. The initial state $\Lambda$ has a definite parity, but the final state does not preserve it.  

The key constraint comes from spin projection conservation. The spin projection of the initial $\Lambda$ must match the helicity of the proton in the final state. The transition amplitude is given by the matrix element:  

$$
H_\lambda = \langle \text{final} | T | \text{initial} \rangle
$$  

By convention, the initial state is written on the right and the final state on the left. The final state consists of:  

-A proton with momentum $P_Z$ and spin projection $\lambda$ (helicity).  
- A pion with momentum $-P_Z$ (opposite direction) and spin projection $0$ (since it is spinless).  

The initial state is simply $|\Lambda, \lambda \rangle$, where $\lambda$ is the spin projection of the $\Lambda$.  

The matrix element $H_\lambda$ is constrained by angular momentum conservation, requiring:  

$$
\lambda_\Lambda = \lambda_p
$$  

This means there is only one independent matrix element, indexed by $\lambda$. Since $\Lambda$ has spin $\frac{1}{2}$, there are two possible spin projections ($\lambda = \pm \frac{1}{2}$), leading to two distinct matrix elements.

<!--
Cosine simularity: 0.9138632735039812
-->
## Unpolarized Decay Widths and Lambda Lifetime

The decay width $\Gamma_\Lambda$ is given by:

$$
\Gamma_\Lambda = \frac{1}{2m_\Lambda} \sum_{\text{final}} \int \frac{d^3p}{(2\pi)^3 2E} |\mathcal{M}|^2
$$

Here, $\mathcal{M}$ is the matrix element squared, averaged over initial spin states and summed over final states. Since the momenta are aligned (no angular dependence), the phase space integral simplifies. The angular integration $\int \frac{d\Omega}{4\pi}$ reduces to 1, leaving only the momentum factor:

$$
\frac{p}{8\pi m_\Lambda^2}
$$

The matrix element is constrained by spin conservation, so $\lambda_\Lambda = \lambda_p$, meaning only two independent helicity configurations exist ($\lambda = \pm \frac{1}{2}$).  

The lifetime of the $\Lambda$ baryon is determined by its dominant decay channel ($\Lambda \to p \pi^-$). Its lifetime is relatively long at $10^{-9}$ seconds, allowing it to travel measurable distances (meters) in detectors before decaying. This makes it identifiable through secondary vertices from its decay products (charged proton and pion tracks).  

::: callout-note
The unpolarized decay width calculation includes averaging over initial spin states and summing over final helicities, with no angular dependence due to alignment.
:::
The final expression for the width combines the phase space factor and the squared matrix element, providing the decay rate observable in experiments.  

<!--
Cosine simularity: 0.9185847034418799
-->
## Helicity Frame and Particle Spin Quantization

The relation $J^P = \frac{1}{2}^+$ holds because two of the four terms vanish, leaving only two remaining terms with a factor of $\frac{1}{2}$.  

When there is a preferred direction in space, such as the direction of a flying $\Lambda$ particle with non-zero momentum, this defines an axis. By boosting along the momentum direction and aligning the $Z$-axis with this direction, you can measure angles relative to it. This is called the **helicity frame**.  

The $|JM\rangle$ states are the basis states for a particle with spin $J$, where $M$ represents the projection onto the $Z$-axis. Acting with the $J_Z$ operator confirms that these are eigenstates with eigenvalue $M$. For a spin-$J$ particle, there are $2J + 1$ possible projections.  

::: callout-note
When the $Z$-axis is used for quantization, the state is called **canonical**.
:::
All transformations discussed here are **active transformations**, meaning they are applied to the particle rather than the coordinate system. For example:  

-Boosting the particle in the $Z$-direction increases its velocity along that axis.  
- Rotating the particle about the $Y$-axis is a nontrivial transformation.  

Consider a coordinate system with $X$ and $Y$ axes. A rotation about the $Y$-axis corresponds to rotating the particle itself, not the coordinate frame. This is the most common transformation we will use.

<!--
Cosine simularity: 0.9054347361350654
-->
## Wigner D Functions and Spin Rotation Matrices

When rotating a particle (rather than the coordinate system) about the $Y$-axis, the spin projection along the $Z$-axis is no longer well-defined. Instead, it becomes a superposition of states with coefficients $C_{J' M'}$. These coefficients are given by the **Wigner D functions**, which are tabulated and can be found alongside Clebsch-Gordan coefficients.  

For computational purposes, the Wigner D functions can be obtained via matrix exponentiation:  

$$
D(\theta) = e^{-i \theta J_Y}
$$

Here, $J_Y$ is the generator of rotations about the $Y$-axis, and its matrix form depends on the particle's spin.  

::: callout-note
For spin-$\frac{1}{2}$ particles, the rotation matrix is particularly simple. It involves the Pauli matrices $\sigma_i$ and a half-angle factor:
:::
$$
D_{1/2}(\theta) = e^{-i \frac{\theta}{2} \sigma_Y}
$$

The half-angle arises because spin-$\frac{1}{2}$ particles transform under a double cover of the rotation group. For spin-1 particles, the rotation matrix is more complex, involving full-angle trigonometric functions:  

$$
D_{1}(\theta) = 
\begin{pmatrix}
\frac{1 + \cos \theta}{2} & -\frac{\sin \theta}{\sqrt{2}} & \frac{1 - \cos \theta}{2} \\
\frac{\sin \theta}{\sqrt{2}} & \cos \theta & -\frac{\sin \theta}{\sqrt{2}} \\
\frac{1 - \cos \theta}{2} & \frac{\sin \theta}{\sqrt{2}} & \frac{1 + \cos \theta}{2}
\end{pmatrix}
$$

This matrix acts in the basis of $|J M\rangle$ states. Alternatively, working in the basis of ladder operators ($J_+, J_-$) simplifies the form, but the $|J M\rangle$ basis is more commonly used in practical calculations.  

::: callout-important
The Wigner D functions describe how quantum states transform under rotation, and their explicit form depends on the spin representation. For higher spins (e.g., $J = \frac{3}{2}, 2$), the matrices become larger but can still be computed using the same principles.
:::
The key insight is that rotations of quantum states are governed by the generators of the rotation group, and the Wigner D functions encode these transformations explicitly. Whether you look them up or compute them numerically, they are essential for describing spin dynamics in quantum systems.  

<!--
Cosine simularity: 0.9306259565055195
-->
## Helicity States and Spin Quantization

When dealing with helicity states, we can either look up the Wigner D functions or compute them using matrix exponentiation. Let's perform some algebra to understand how states transform when boosted and rotated.  

The simplest approach is to define spin quantization for a moving particle. Consider the coordinate axes: $X$, $Y$, and $Z$, with the particle moving in the $XZ$ direction. There are two ways to quantize spin in this scenario:  

1. **Helicity basis**: Quantize spin along the direction of motion.  
2. **Canonical basis**: Quantize spin along the $Z$-axis.  

These two bases are not equivalent but are related. If a state has a definite spin projection along the direction of motion (helicity state), it will be a superposition of states in the canonical basis. Conversely, if a state has a definite projection along the $Z$-axis, it will be a combination of helicity states.  

To construct the helicity state $|P \lambda\rangle$, we apply a sequence of transformations starting from the particle's rest frame:  

1. Begin with a particle at rest, having spin projection $\lambda$ along the $Z$-axis.  
2. Boost the particle forward—this increases its momentum without altering the spin projection.  
3. Rotate the entire system to align with the desired configuration.  

The resulting state $|P j \lambda\rangle$ is a helicity state.  

::: callout-note
The Wigner D functions describe how quantum states transform under rotation. For a spin-$\frac{1}{2}$ particle, the rotation matrix is:
:::
$$
D_{1/2}(\theta) = e^{-i \frac{\theta}{2} \sigma_Y}
$$

For spin-1 particles, the rotation matrix is more complex:  

$$
D_{1}(\theta) = 
\begin{pmatrix}
\frac{1 + \cos \theta}{2} & -\frac{\sin \theta}{\sqrt{2}} & \frac{1 - \cos \theta}{2} \\
\frac{\sin \theta}{\sqrt{2}} & \cos \theta & -\frac{\sin \theta}{\sqrt{2}} \\
\frac{1 - \cos \theta}{2} & \frac{\sin \theta}{\sqrt{2}} & \frac{1 + \cos \theta}{2}
\end{pmatrix}
$$

These transformations are essential for describing spin dynamics in quantum systems, particularly when dealing with moving particles and different quantization axes.

<!--
Cosine simularity: 0.9234466052038162
-->
## Properties and Rotation of Helicity States  

When you see $|P j \lambda\rangle$, it's a helicity state. Immediately think of it as the combination of boost and rotation operators acting on the canonical states in the rest frame.  

There are many properties we can derive for helicity states. One worth mentioning is that when you rotate a helicity state, only the momentum rotates—the helicity stays the same. If you apply further rotations, the momentum continues to rotate, but the spin remains quantized along the direction of motion, preserving the helicity value. This is evident from how the state is constructed.  

If you introduce a rotation here (multiplying by a rotation operator), you can combine the rotations into a single one, affecting only the momentum during the boost. Boosting is trickier because when you boost this state, you insert a boost operator $B$ (here, $B_z$). For any combination of boosts and rotations ($B R B^{-1}$), you can find equivalent pure rotations.  

When you evaluate this and rotate the canonical state (using the inverse operation), you obtain a combination of coefficients $C_{\lambda'}$, yielding the helicity state. Applying boosts and rotations to this gives you back a helicity state.  

The most demanding part of this exercise is finding the relation between the boosted/rotated states and the original helicity basis.  

::: callout-note
The Wigner D functions describe how states transform under rotation. For example, for spin-$\frac{1}{2}$ particles, the rotation matrix is:
:::
$$
D_{1/2}(\theta) = e^{-i \frac{\theta}{2} \sigma_Y}
$$  

For spin-1 particles, the matrix becomes more complex:  

$$
D_{1}(\theta) = 
\begin{pmatrix}
\frac{1 + \cos \theta}{2} & -\frac{\sin \theta}{\sqrt{2}} & \frac{1 - \cos \theta}{2} \\
\frac{\sin \theta}{\sqrt{2}} & \cos \theta & -\frac{\sin \theta}{\sqrt{2}} \\
\frac{1 - \cos \theta}{2} & \frac{\sin \theta}{\sqrt{2}} & \frac{1 + \cos \theta}{2}
\end{pmatrix}
$$  

These transformations are crucial for describing spin dynamics in quantum systems, especially when dealing with moving particles and different quantization axes.

<!--
Cosine simularity: 0.9199212060031491
-->
## Composition of Spin Projection and Directional Motion  

The most demanding part of this exercise is to find the relation between boost-rotation-boost and rotation-boost-rotation. We know what happens with the momentum when you boost—we know how Lorentz transformations act on the vectors. The boost matrix for the 4-momentum $P^\mu$ is a $4 \times 4$ matrix in $SO(1,3)$, with components involving $\gamma$ (Lorentz factor) and $\beta$ (velocity fraction).  

When you apply a boost, the 4-vector $P^\mu$ transforms into a different vector $P'^\mu$. The key remaining task is to understand the composition of spin projection and directional motion. Clearly, we have a linear combination of different projections—not just a single one.  

Intuitively, if you start with a vector and boost it, the vector becomes more inclined forward. Instead of boosting twice, you can boost only once to achieve the same final momentum magnitude. This is captured in the relation between boost and rotation operations.  

For example, applying a boost $B_z$ to a particle at rest directly produces the desired momentum. Then, the only remaining step is to rotate it to the correct orientation. This equivalence is what simplifies the problem—instead of multiple boosts, a single boost followed by a rotation suffices.  

::: callout-note
The Wigner rotation matrices describe how spin states transform under rotations. For spin-$\frac{1}{2}$ particles, the rotation matrix is:
:::
$$
D_{1/2}(\theta) = e^{-i \frac{\theta}{2} \sigma_Y}
$$  

For spin-1 particles, the matrix is more complex:  

$$
D_{1}(\theta) = 
\begin{pmatrix}
\frac{1 + \cos \theta}{2} & -\frac{\sin \theta}{\sqrt{2}} & \frac{1 - \cos \theta}{2} \\
\frac{\sin \theta}{\sqrt{2}} & \cos \theta & -\frac{\sin \theta}{\sqrt{2}} \\
\frac{1 - \cos \theta}{2} & \frac{\sin \theta}{\sqrt{2}} & \frac{1 + \cos \theta}{2}
\end{pmatrix}
$$  

These transformations are essential for describing how spin states evolve under combined boosts and rotations.

<!--
Cosine simularity: 0.9072459857344257
-->
## Transformation of Canonical States  

The canonical spin state is represented as:  

$$
|j m\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}_{m}
$$  

To understand the canonical state, consider the combination of boost and rotation operations. The canonical state is defined by first rotating the system back in the rest frame of the particle, ensuring the combination has a certain projection onto the $z$-axis. After this rotation, the state may have a slight downward projection due to the inverse rotation $R^{-1}$.  

Next, we apply a boost along the momentum direction. This transforms the state into a moving frame. Finally, we perform another rotation to align the system into the desired configuration.  

::: callout-note
Notation clarity is crucial. When encountering $|p, j, m\rangle$, it is ambiguous whether the state is canonical or helicity. To avoid confusion, explicitly label the state as $|p, j, m\rangle_{\text{canonical}}$ or $|p, j, \lambda\rangle_{\text{helicity}}$, where $m$ refers to the $z$-axis projection and $\lambda$ to helicity.
:::
The transformation of canonical states under rotation is given by:  

$$
R |j m\rangle = D^{(j)}(R) |j m\rangle
$$  

Here, $D^{(j)}(R)$ is the Wigner rotation matrix for spin-$j$. For spin-$\frac{1}{2}$, this matrix is:  

$$
D_{1/2}(\theta) = e^{-i \frac{\theta}{2} \sigma_Y}
$$  

For spin-1, the rotation matrix becomes:  

$$
D_{1}(\theta) = 
\begin{pmatrix}
\frac{1 + \cos \theta}{2} & -\frac{\sin \theta}{\sqrt{2}} & \frac{1 - \cos \theta}{2} \\
\frac{\sin \theta}{\sqrt{2}} & \cos \theta & -\frac{\sin \theta}{\sqrt{2}} \\
\frac{1 - \cos \theta}{2} & \frac{\sin \theta}{\sqrt{2}} & \frac{1 + \cos \theta}{2}
\end{pmatrix}
$$  

These transformations are essential for describing how spin states evolve under combined boosts and rotations. The key insight is that instead of applying multiple boosts, a single boost followed by a rotation suffices to achieve the desired momentum and orientation.  

The relation between boost-rotation-boost and rotation-boost-rotation simplifies the problem. For example, applying a boost $B_z$ to a particle at rest directly produces the desired momentum, and only a final rotation is needed to align the state correctly. This equivalence captures the composition of spin projection and directional motion, where the final state is a linear combination of different projections.

<!--
Cosine simularity: 0.8930631880606437
-->
## Introduction to Helicity Frame and Angle

This is equal to what I have on the right side, where I replace the two canonical $R$ operations. I inserted $R'^{-1} R'$ here, combined these matrices, and now this gives me the canonical state when applied to the state at rest. The remaining step is to apply the rotation accelerator to the state at rest, which is described by the $D$ functions acting on this state. Therefore, the result is a sum over coefficients $C$. After applying $R$, I obtain a linear combination with coefficients $C$, and for each state, I act with the inverse boost rotation to get a canonical state. Now, this is a projection labeled with $\lambda'$, and I have a linear combination of them.  

The momentum $P$ also changes because the angle is rotated. The rotated momentum is $P' = R' R P_z$, where $P_z$ is the momentum after boosting along the $z$-axis. After the boost, the momentum becomes non-zero, and applying the rotation $R'$ gives $P'$.  

Now, let’s discuss the relation between the helicity state and the canonical state. The helicity state $|p, j, \lambda\rangle$ can be expressed as a linear combination of canonical states $|p, j, m\rangle_{\text{canonical}}$. The coefficients for this transformation are determined by applying the inverse rotation $R^{-1}$ to the state. The key operation is $R B R^{-1}$, which converts the state into a canonical form, and then applying $R$ to this state gives the desired linear combination.  

::: callout-note
The helicity state is defined by boosting to the rest frame and then rotating. The angle of decay in this frame, measured relative to the direction of motion, is called the **helicity angle**.
:::
Returning to the example of $\Lambda$ decay, consider a $\Lambda$ moving in the lab frame. To define the $z$-axis in the helicity frame, we boost to the rest frame of the $\Lambda$ and use its direction of motion in the lab frame. This defines the helicity frame for $\Lambda$. The helicity angle is then the angle of decay measured relative to this $z$-axis.  

::: callout-important
The helicity frame depends on the reference frame from which the boost is performed. Different frames will result in different rest-frame orientations of the particle.
:::
The helicity frame is always defined as the rest frame of the particle obtained by boosting from the frame where it was moving. The helicity angle is a standard term in hadron physics, referring to the angle measured in this boosted rest frame.  

<!--
Cosine simularity: 0.9435942757436995
-->
## Recap of Lambda Decay Plane and Boost Inversion

We took the particles as the reference and measured the angle from there. All of the motion remains in the same plane as before. The boost and the two-part complement are now exactly opposite. Here, the boost inversion ( $-1$ ) occurred.  

We start with a $\Lambda$ flying in the $z$-direction with a certain velocity. It decays into a proton and a pion in some plane. After inverting the boost, the proton and pion still lie in the same plane with exactly the same direction.  

The plane is defined by three vectors:  

1.The original direction of motion of the $\Lambda$ (defining the axis).  
2. The angle measured with respect to this axis.  
3. The decay products forming the plane.  

Without the original direction of the $\Lambda$, the plane is no longer defined. The angle and the plane are constructed from these three vectors.

<!--
Cosine simularity: 0.9443906373930285
-->
## Transition Operator and Rotation in Lambda Decay

The matrix element for the transition is given by:

$$
H = \langle f \uparrow | H | i \rangle
$$

We can measure the angle and define a plane. This is our recap exercise. Initially, we started with only one axis, but now we have a plane with an additional variable on which the amplitude depends, in addition to the two discrete variables. This variable is the scattering angle or the helicity angle.  

The final state here will be frozen binary. On the right side, we have configurations of $\Lambda$ sitting in its rest frame with the proton in $\Lambda$. On the left side, we have this configuration of the pion-proton system. The way to proceed is to apply rotation to this configuration and align it back.  

The answer for this is:

$$
H_{\lambda p} = T_{\Lambda \lambda}
$$

This equation describes the matrix element for the sequence of decays. To derive it, we apply the transition operator $T$ on the final state. The goal is to simplify this expression. Here, $T$ acts on the proton state.  

We want to evaluate the application of the transition operator that takes the pion-proton system and transforms it into $\Lambda$. This is the meaning of our operator. When this operator acts on the pion-proton state with momentum $\vec{P} = (0, 0, P_z)$, we notice that it is rotated about the $y$-axis by an angle $\theta$.  

We want to align this to the left state, which has aligned combinations. Thus, we perform a rotation, pull out the outer rotation, and obtain the same combination along the $z$-axis. The proton moves forward, time goes backward, and the rotation is made explicit.  

Since these operators commute and strong interactions conserve spin, we can compute the transition operator and rotation separately. We first apply the transition operator and then the rotation. Essentially, the transition operator transforms the pion-proton system into $\Lambda$, and we explicitly perform this operation.  

The plane is defined by three vectors:  

1.The original direction of motion of $\Lambda$ (defining the axis).  
2. The angle measured with respect to this axis.  
3. The decay products forming the plane.  

Without the original direction of $\Lambda$, the plane is no longer defined. The angle and the plane are constructed from these three vectors.

<!--
Cosine simularity: 0.9511209829799391
-->
## Parity Violation in Polarized Lambda Decay

The transition operator transforms the pion-proton problem to the lambda system. We explicitly do this by inserting the identity state here. Here, we have a lambda state for the light statement. This part is a path lambda problem, and it gives us just the state of the lambda with the same speed.  

The matrix element we just evaluated is simply the lambda coupling. If we insert the identity, it should account for all possible combinations. Therefore, that would be a sum over lambda states. This will give us delta functions for the lambda lambda problem, allowing us to isolate a single state.  

The final step is to apply rotation to the system. It's good to see this once, but once you understand the idea, it becomes clear that in the case of the cascade reaction, each transition involves the product of the block helicity amplitude (the transition matrix element for the aligned transition) and the rotation.  

Now, the differential cross section depends on the angle as a function of the scattering angle. The equation involves cosine and sine matrices:  

$$
\begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix}
$$

For the spin matrix, we have an explicit numerical form, and we have two coupling constants measured in experiments. These can be used to compute the angular distribution.  

The result is the same as before because:  

$$
\sin^2 \theta + \cos^2 \theta = 1
$$

This term appears in front of the first component, while the second component has:  

$$
-\sin^2 \theta + \cos^2 \theta
$$

This simplifies to another trivial result.  

From this exercise, we learn that if we start with an unpolarized particle, we will not observe any interesting angular distribution. We sum over final states and initial states, and no non-trivial angle distributions remain for the $2\pi DDK$ system before integrating over the full phase space.  

The phase space integral is:  

$$
\int \frac{d\Omega}{4\pi} = \int \frac{d\cos \theta}{2} \int \frac{d\phi}{2\pi}
$$

This is a standard phase space measure.  

Now, let’s consider the case of polarized decay. Here, we obtain non-trivial distributions if the particle is polarized. Suppose the lambda particle is flying with a definite spin projection along its momentum direction, say $+1/2$. When it decays, we find that the proton is more likely to travel forward than backward.  

This angle dependence of the proton’s momentum violates parity. Applying parity to the initial and final states flips the momentum but not the spin. The final configuration under parity would require the proton to be more likely backward, which contradicts the original observation.  

This confirms that parity is violated in this decay process. This is consistent with the fact that weak interactions, which govern this decay, do not conserve parity. The asymmetry in the angular distribution directly demonstrates this violation.  

<!--
Cosine simularity: 0.9301531663064168
-->
## Polarization and Analyzing Power in Lambda Decay

We consider the decay width for the $\Lambda$ particle:

$$
\Gamma_{\Lambda} = \frac{1}{2 m_{\Lambda}} \sum_{i} |H_{i}|^2 \frac{2p}{8 \pi m_{\Lambda}}
$$

The parity validation appears when the two amplitudes are not equal to each other. If they were equal, the sum $\sin^2 \theta + \cos^2 \theta$ would give 1 with no angle dependence. The fact that they are not equal reflects parity violation.  

In the case of a fully polarized $\Lambda$ with $\lambda = 1/2$, it is a pure state with 100% polarization. However, realistic scenarios involve mixed states, such as the $\Lambda$ being produced with 60% polarization in the BD case. This reduces the observed asymmetry.  

The differential decay width can be written as:

$$
d\Gamma = \Gamma_0 (1 + \alpha P \cos \theta)
$$

Here, $\alpha$ is the **analyzing power**, which quantifies how well the decay reflects the initial polarization. If the couplings are equal, $\alpha = 0$, and the decay is insensitive to polarization. However, for most weak decays, $\alpha \neq 0$, allowing the angular distribution to reveal parity violation.  

The asymmetry in the proton emission angle confirms parity violation. If the $\Lambda$ is polarized along its momentum direction ($+1/2$), the proton is more likely to be emitted forward than backward. Under parity transformation, this configuration would reverse, contradicting the observation. This is consistent with weak interactions, which do not conserve parity.  

The phase space integral is given by:

$$
\int \frac{d\Omega}{4\pi} = \int \frac{d\cos \theta}{2} \int \frac{d\phi}{2\pi}
$$

This is the standard measure for integrating over the full angular distribution.  

::: callout-important
The analyzing power $\alpha$ determines the sensitivity of the decay to the initial polarization. If $\alpha = 0$, no asymmetry is observed, even if parity is violated.
:::
The angular distribution asymmetry directly demonstrates parity violation in $\Lambda$ decay.

<!--
Cosine simularity: 0.936053571621552
-->
## Polarimetry Technique and Initial Polarization Measurement  

The decay width $\Gamma_{\Lambda}$ is non-zero, and by examining the angular distribution, you observe parity violation. You can also measure the initial polarization using the **polarimetry technique**, which is actively employed.  

By analyzing the angle distributions, you can determine the polarization since all particles have known spin and couplings (though these must be measured in advance). The initial polarization is a powerful observable.  

For particles like the $\Lambda$, which carry spin, the polarization at the interaction point contains valuable information. How the $\Lambda$ is produced—its momentum and polarization—reveals details about the internal dynamics of the interaction.  

For example, if the $\Lambda$ is produced in a carbon equilibrium or a plasma, its polarization can be linked to the properties of the medium.  

::: callout-important
The polarimetry technique allows extraction of initial polarization, providing insights into production mechanisms and interaction physics.
:::
<!--
Cosine simularity: 0.9555648141427531
-->
## Polarization and Particle Decay in Quaternion Interaction

The polarization of the particle can be related to its properties, making it a free carrier of information from the quaternion interaction. Polarization plays a crucial role, often more significant than other observables.  

This particle not only carries information but also provides a way to measure polarization through its decay.  

::: callout-important
The ability to measure polarization via decay is essential for understanding the underlying dynamics of quaternion interactions.
:::
If I were to explain the material, you would already know it, but since I haven’t, I’ll pose a question instead: Can you determine the relationship between polarization and decay properties without prior lecture content?  

Meanwhile, let me know if you have any questions.  

<!--
Cosine simularity: 0.9220048021589232
-->
## Introduction to Analytic Functions and Cauchy Integrals

Next lecture, we will move on to discussing analytic functions and properties of amplitudes in the complex plane. This requires some background in complex analysis, so we’ll review key concepts, including the complex plane and complex algebra.  

The discussion arises from evaluating a circle integral. Consider a function $F(X)$ in the complex $X$-plane. If $F(X)$ is analytic and there are no singularities inside the integration contour, the integral over a closed circle is zero:  

$$
\oint F(X') \, dX' = 0
$$

However, if we introduce a pole at $X$ inside the contour, the integral is no longer zero. The Cauchy integral formula states:  

$$
\oint \frac{F(X')}{X' - X} \, dX' = 2\pi i \, F(X)
$$

Here, the integral evaluates to the function at the pole $F(X)$. This principle is central to extending the contour and handling singularities in analytic functions.  

::: callout-note
The Cauchy integral formula allows us to explicitly account for singularities inside the contour, transforming the integral into the function's value at the pole.
:::
The same idea applies to more general cases, where we start with a small circle and stretch it while preserving analyticity.  

<!--
Cosine simularity: 0.8955305173789901
-->
## Contour Integration and Imaginary Part Analysis

I started with a small contour and stretched it to infinity. The part of the contour at infinity drops out, leaving only the integral from 1 to 7. The question is whether the equation can be satisfied when integrating the imaginary part of $F(x)$ from 1 to 7.  

The second question concerns the analytic structure: what do we mean by branch cuts and poles? This is common in physics, where integrals like this arise. The leftover contour from 1 to 7 integrates $F(x)$, but since contributions from both sides of the contour have opposite signs, the real parts cancel, leaving only the imaginary part.  

For example, if $F(x) = 3$, the imaginary part vanishes, and the equation holds trivially. The real question is whether non-trivial (non-constant) solutions exist where the imaginary part does not vanish.  

::: callout-note
When integrating over a contour where $F(x)$ is analytic, contributions from opposite sides cancel the real part, leaving only the imaginary part in the final result.
:::
The Cauchy integral formula is central here. If $F(X)$ is analytic and has no singularities inside the contour, the integral over a closed path is zero:  

$$
\oint F(X') \, dX' = 0
$$

However, if there is a pole at $X$ inside the contour, the integral becomes:  

$$
\oint \frac{F(X')}{X' - X} \, dX' = 2\pi i \, F(X)
$$

This principle allows us to handle singularities and extend contours while preserving analyticity.

<!--
Cosine simularity: 0.9165438281195135
-->
## Constructing Special Functions with Branch Points  

If we remove the constant term, the imaginary part vanishes entirely. The question is whether non-trivial solutions exist where the imaginary part is non-zero. The answer is yes—any function can be inserted here, and the integral will converge. For example, take $\sqrt{X}$ and place it in the expression. This constructs a special function $F(X)$ whose imaginary part equals $\sqrt{X}$ in the region from $-1$ to $7$. Outside this interval, the function is non-zero but has no singularities.  

The construction introduces non-trivial analytic structures. Three candidates for these structures are:  

1.A continuous stretch of poles,  
2. A branch cut,  
3. A combination of both.  

::: callout-note
A branch cut is a non-analytic structure where the function differs on either side. For example, $\sqrt{-1 + i0^+}$ equals $+i$, while $\sqrt{-1 - i0^+}$ equals $-i$. Unlike poles, branch cuts do not involve divergences—just a discontinuity in function values.
:::
Poles introduce divergences, whereas branch cuts do not. The distinction lies in whether the function diverges (poles) or simply changes value discontinuously (cuts). In this case, the structure is more akin to a branch cut because the function remains finite but takes different values on opposite sides of the cut.  

The Cauchy integral formula governs such constructions. For an analytic function $F(X)$ with no singularities inside a contour:  

$$
\oint F(X') \, dX' = 0
$$

If a pole exists at $X$, the integral becomes:  

$$
\oint \frac{F(X')}{X' - X} \, dX' = 2\pi i \, F(X)
$$

This principle allows extending contours while preserving analyticity, even when introducing branch cuts or other singular structures.

<!--
Cosine simularity: 0.9076568097224533
-->
## Understanding Branch Points and Cuts in Complex Analysis  

The integrand has poles at zero and $X$. These are not branch points. To analyze the function, you must analytically continue it—perhaps above and below the real line—to see different branches.  

A branch point is where a branch starts or ends. For example, if you consider the analytic structure of a function in the $X$-plane, it might have branch points at $1$ and $7$, connected by a branch cut. The function itself has no poles.  

The distinction between poles and branch cuts is important. Poles introduce divergences, while branch cuts represent discontinuities in function values. For instance, $\sqrt{-1 + i0^+} = +i$ and $\sqrt{-1 - i0^+} = -i$—this is a branch cut, not a pole.  

The Cauchy integral formula governs these cases. For an analytic function $F(X)$ with no singularities inside a contour:  

$$
\oint F(X') \, dX' = 0
$$

If a pole exists at $X$, the integral becomes:  

$$
\oint \frac{F(X')}{X' - X} \, dX' = 2\pi i \, F(X)
$$

This principle allows extending contours while preserving analyticity, even with branch cuts or other singular structures.

<!--
Cosine simularity: 0.8939392133556964
-->
## Exploring Multisheeted Complex Planes and Singularities

There are no poles. The function doesn't have any poles. That's the way we construct the function here — by introducing a "gate" in the complex plane. It's interesting to think about where this structure comes from or where it leads.  

When you examine this plane, you can take a walk on it without encountering any poles or singularities. However, if you "dive under" the plane, you enter a different world — another sheet — accessible through this gate. On this new sheet, the function has poles, including at zero, and a branch cut associated with $\sqrt{X}$.  

The function has a complex structure: on the regular complex plane, it has no singularities except for the gate. But through the gate, you reach another sheet where the behavior changes dramatically, with poles and branch cuts appearing.  

::: callout-note
The gate here acts as a transition point between sheets of a multisheeted Riemann surface, allowing the function to exhibit different analytic properties on each sheet.
:::
This is how you get used to working with multisheeted complex planes — by recognizing that singularities may exist on other sheets even if they are absent on the principal sheet.  

<!--
Cosine simularity: 0.8912046881280075
-->
## Understanding Branch Points and Poles in Complex Analysis

The integral converges from 1 to 7, and we are evaluating the logarithm function. Consider the expression:

$$
\log(1 - 8) - \log(17 - 8)
$$

When evaluating at $8 \pm i\epsilon$, we observe:
- $\log(1) = 0$
- $\log(-1 \mp i\epsilon) = \log(1) \pm i\pi$  

This leads to a discontinuity (jump) in the imaginary part, confirming the presence of a branch cut. The real part of $X$ cannot lie between 1 and 7 because the function's structure loops around these points.  

::: callout-note
The branch points at $X = 1$ and $X = 7$ are explicitly identified by the integral's behavior. The branch cut connects these points, restricting the domain of $X$.
:::
The function has singularities at these branch points, but they are not poles. A branch point can have a divergence (e.g., $\log(X)$ diverges at $X = 0$), but it is distinct from a pole. For example:
- $1/(X - C)^3$ has a third-order pole at $X = C$.
- $\log(X - C)$ has a logarithmic branch point at $X = C$, not a pole.  

A pole is a singularity that can be resolved by adding an infinitesimal shift in the complex plane (e.g., $1/(X \pm i\epsilon)$). In contrast, branch points persist and require branch cuts to define the function's behavior.  

The function here has no poles on the principal sheet, but the branch points at 1 and 7 introduce a multivalued structure. The branch cut enforces a discontinuity, preventing $X$ from taking values between 1 and 7 on the principal branch.  

::: callout-important
Branch points and poles are both singularities, but they differ in how they affect the function's analyticity. Poles are isolated and removable with $i\epsilon$ prescriptions, while branch points necessitate cuts and multisheeted surfaces.
:::
<!--
Cosine simularity: 0.8512935455454501
-->
## Lecture Style and Student Feedback on Rigor vs. Conceptual Learning  

The unique complex plane has an infinitesimal value in the other direction, but it would stay at infinity. This is an isolated singularity. The branch point is a concept you might have encountered in mathematics, particularly in relation to the residual theorem or theoretical minimum.  

For example, the square root function has a branch point, though you may know it by other terminology. The exponential function $e^X$ also exhibits branch points.  

::: callout-note
Branch points and isolated singularities are distinct concepts in complex analysis. A branch point introduces multivaluedness, while an isolated singularity (like a pole) is a single-point discontinuity.
:::
Regarding lecture style, some students find the approach unstructured, with sketches and intuitive explanations rather than rigorous proofs. However, this makes the material more engaging for advanced learners. For first-semester students, a more structured approach might be necessary to avoid confusion.  

The branch point for $\sqrt{X}$ or $\log(X)$ is a key example where the function becomes multivalued. In contrast, poles (like those in $1/(X - C)^3$) are isolated singularities resolvable with an infinitesimal shift in the complex plane.  

::: callout-important
Teaching advanced students allows for a more conceptual approach, but foundational courses require clearer structure to build rigorous understanding.
:::
The distinction between branch points and poles is critical: branch points require branch cuts, while poles are removable with $i\epsilon$ prescriptions.

<!--
Cosine simularity: 0.8461662585382317
-->
## Exploring Infinite Worlds and Gates in a Virtual Environment

We go through the gate, but outside the gate, the function is continuous. Here, it's another gate. This is the first world, and the second world is entered by walking around the gate. Then, it goes through the gate and ends up in another world. This is because of how we choose the first road. You can go through the gate and appear in that world, which has many more gates. You can go around and enter on the other side, emerging elsewhere.  

This creates an infinite number of worlds due to the nature of the construction. For example, you can go to the forest world, which is another world with its own gate. Appearing here, you can go around and emerge elsewhere. This works because the structure is a square, while another configuration might be logarithmic.  

Imagine using VR glasses and walking through these gates—it would be quite fun. You could suggest this as an 80th Matrix Netflix concept, making it an escape room where you only exit by finding the first gate.  

The function's behavior appears in the amplitudes, which are structured this way.  

::: callout-note
Branch points and isolated singularities are distinct in complex analysis. A branch point introduces multivaluedness (e.g., $\sqrt{X}$ or $\log(X)$), while an isolated singularity (like a pole in $1/(X - C)^3$) is a single-point discontinuity resolvable with an infinitesimal shift in the complex plane.
:::
The unique complex plane has an infinitesimal value in the other direction but remains at infinity for an isolated singularity. The branch point is a concept encountered in mathematics, particularly with the residual theorem or theoretical minimum.  

::: callout-important
Teaching advanced students allows for a conceptual approach, but foundational courses require clearer structure to build rigorous understanding.
:::
<!--
Cosine simularity: 0.8968583727372633
-->
## The Role of Rigorous Proofs in Learning

The scattering amplitudes are functions of Mandelstam variables, which describe energies and momentum transfers in particle interactions. For this lecture, it would be nice to have a more rigorous proof, but I quite like that we don't always rely on them. However, some background knowledge is necessary to follow the reasoning. Without foundational proofs, it would be difficult to understand the concepts.  

When I was a student, I disliked when instructors expected prior knowledge that hadn't been taught. This feeling is more extreme in courses that focus solely on rigorous proofs. For example, Dr. Creeps' lectures consist entirely of long proofs, which become tedious and disconnected from conceptual understanding. It’s better to introduce the ideas first and then provide proofs later.  

::: callout-note
Branch points and isolated singularities are distinct in complex analysis. A branch point introduces multivaluedness (e.g., $\sqrt{X}$ or $\log(X)$), while an isolated singularity (like a pole in $1/(X - C)^3$) is a single-point discontinuity resolvable with an infinitesimal shift in the complex plane.
:::
The unique structure of the complex plane means an isolated singularity remains at infinity, while branch points are tied to multivalued functions. This distinction is crucial in advanced mathematics, particularly when applying the residue theorem or theoretical minimum principles.  

::: callout-important
Teaching advanced students allows for a conceptual approach, but foundational courses require clearer structure to build rigorous understanding.
:::
<!--
Cosine simularity: 0.8648794575125085
-->
## Compensation for Lack of Rigor in Seminars and Exercises

I think our seminars and exercise classes compensate for the absence of rigor. That’s why we spend so much time on them. I feel bad that polarization has not been covered properly — we didn’t have time to introduce the polarization matrix to explain where this $P$ comes from.  

::: callout-note
The polarization matrix ( $P$ ) describes how the polarization state of light or particles transforms, but its derivation requires more rigorous treatment than what was possible in this lecture.
:::
<!--
Cosine simularity: 0.9247812959480968
-->
## Prioritizing Exercise Sheets for Exam Preparation

Since we have so much time in the exercises, you can stop exactly where needed. Morris wanted to proceed, but I stopped him because he will have another tweak for sheet five. We will not cover sheet five on Thursday for sure. We still have one more exercise set for sheet three and sheet four.  

::: callout-note
The course is going to end at some point, so you must decide which exercises to prioritize.
:::
If you have to choose between sheet three and sheet five, sheet five is more interesting and more important for the exam. You won’t be able to cover all exercises, so you must decide which ones to focus on.  

<!--
Cosine simularity: 0.9602122980577258
-->
## Scheduling and Discussing Exercise Sheets

I hope that this Thursday will cover sheet three and sheet four. Next exercise, sheet five and sheet six. Until we discuss sheet five, they will have time to try solving it.  

::: callout-note
Extra time for exercises doesn't help—people will do other things and forget more.
:::
If they have another two weeks, they might not prioritize the exercises. I don't mind.

<!--
Cosine simularity: 0.938574666912645
-->
## Deciding on Exercise Content and Student Preparedness

I don’t mind giving opportunities, but people will do other things and forget things. Tomorrow, we have the second exercise covering form factors and complex integrals. It’s nice because the topics are connected.  

I’m considering skipping it now and bringing it up in the next exercise class when we discuss complex structures. Some students didn’t complete the exercise—they tried, but their submissions are missing key elements. That’s why we need to discuss it in class.  

Morris tried, but others likely just heard about it. I mentioned they have the material, but engagement varies.  

<!--
Cosine simularity: 0.933734293695889
-->
## Selecting Participants for the Exercise

Usually we want Hendrik and Moritz.  
The other participants likely just heard about it. I mentioned that they have the material.  
