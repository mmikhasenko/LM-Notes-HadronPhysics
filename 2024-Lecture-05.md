
Today we are at lecture number five. We'll discuss **angle distributions** and **partial wave analysis**. But before going there, I would like to start with a recap.

---


In the last lecture, we discussed the **phase space** for particle reactions and different experiments in their kinematics. We went through the list of experiments around the world that study hadrons and look at their production mechanisms and peculiarities. Let's start with a recap on kinematics.

> [!NOTE]
> **Phase space** refers to the set of all possible states of a system, often described in terms of momentum and energy variables.

---


The first question: how many variables does one need to describe a two-particle scattering process? We have two problems:

1. **Scalar particles**: Let's say $0^-$ scalars. The scattering of $0^-$ scalars to $0^-$ scalars in the final state.
2. **Particles with spin**: For example, $\pi^+$ scattering. Again, scattering of $0^-$ from $0^-$ to, say, $3^-$ and $1^+$.

Here is a little blob that indicates generally what we are discussing—the scattering process. Something described by **strong interaction theory** happens inside the blob, and the arrows indicate particles entering and leaving the interaction. This is a **cartoon diagram** (not Feynman diagrams; sometimes called **unitarity diagrams**). We will touch on unitarity in following lectures. For now, this is a nice way to indicate what we're discussing.

> [!TIP]
> **Unitarity diagrams** are schematic representations of scattering processes, emphasizing conservation laws and symmetries.

---


Then I ask you to calculate the number of variables needed to describe the process entirely—the **full kinematics** (we're talking only about kinematics at this point). Whatever happens in the blob does not impact the answer—the blob could be electromagnetic, strong, gravity, whatever. So something happens inside the blob—how many variables do you need?

Two possibilities:
1. **Particles without spin**.
2. **Particles with spin**.

How many variables do you need to describe the process? The second is related to the pictures I gave you. Let's do it one by one. Take two minutes to think, then we'll discuss.

I've added item C: give an example of a combination of variables that fully describes the process. For A and B, you need to count how many variables. For C, give examples.

---


Let's check how many. Vivian, how many do you have? The calculation is like two times two or four, then multiply by three, then subtract four from conservation laws, so one should have eight—that's correct. Now we can get rid of...

This is the entire kinematics. There are no other constraints on orientation.

For describing kinematics more specifically, I can go to any arbitrary frame and rotate space, so I subtract another six (three rotations, three boosts). The eight is correct if you just consider conservation laws, but accounting for no reference frame, you subtract six more and get two. So for A you've got two.

What did you get for B? Experts in the back—how many? You have the two from before plus angular distributions of the final state particles. Why four? The angle between production particles and between the $3^-$ and $1^+$ particles. How would these angles differ? Why can't I introduce these angles in A? They're not necessary—it's actually two as well.

> [!IMPORTANT]
> The number of **independent kinematic variables** for a two-body scattering process is **two**, regardless of spin.

---


Here I would have a **scalar amplitude** describing amplitude as a function of $s$ and $t$, where:

$$
s = (p_1 + p_2)^2
$$

$$
t = (p_1 - p_3)^2
$$

Now I've made my cartoon richer by indicating channels/variables in **Mandelstam invariants** that describe the process. The energy is given by $s$ (sum of four-vectors squared), and transferred momentum is $t$ (analogous but in the vertical direction).

In my cartoon, I've added $p$'s as four-vectors (energy component, 3D component, spin orientation for particles with spin—helicity values $\lambda_3$ and $\lambda_4$). For the first case, the amplitude describing the blob is a scalar function—just a single number. With spin, it's a higher-rank object.

For spin-3 (7 dimensions) and spin-1 (3 dimensions), the scattering amplitude is a 21-dimensional object (21 amplitudes), but all are functions of two variables. This changes when considering decays of final state particles (we don't know stable $3^-$ or $1^+$ particles—they would decay). If restricted to this problem, two variables suffice.

> [!NOTE]
> **Mandelstam variables** ($s$, $t$, $u$) are Lorentz-invariant quantities that simplify the description of scattering processes.

---


Henrik, what are your favorite two variables to describe two-body scattering? Mass of particles one and two, and one and three? To compute mass: take four-vectors, add them, take Lorentz squared ($E^2 - \vec{p}^2 = m^2$). You suggest using this variable and another mass. More common to put the final state with a minus sign, initial with plus—these $s$, $t$ are Mandelstam variables (Lorentz invariants characterizing the process regardless of frame).

I learned recently "invariance" might not be in the dictionary (maybe invariant variables). Anyway, examples of variable sets: Henrik's suggestion. Ilya, what's your favorite? $s$ and $t$? What's your second favorite? Why talk about a third? Let's introduce something new. Sven? $p_2 - p_4$ is called $u$ (same as $p_1 - p_3$). $s + t + u = \sum m_i^2$. So $s$ and $u$ is equivalent ($u$ is a linear combination of $s$, $t$).

Another choice: **center-of-mass energy** and **angle**. $\sqrt{s}$ is COM energy, angle defined in COM frame between $\vec{p}_1$ and $\vec{p}_3$. Be careful—vector lengths represent momentum magnitudes. This is my favorite choice. Other choices work if independent—but beware of **phase space folding** (non-bijective transformations).

> [!TIP]
> A common choice for kinematic variables is:
> - $\sqrt{s}$: Center-of-mass energy.
> - $\theta$: Scattering angle in the COM frame.

---


We discussed two-body kinematics. Next, we'll discuss angular dependence after the Dalitz plot. Any questions on kinematic variables before moving on?

The homework exercise was on **Dalitz plots**—now entering hadron-specific material. Previous lectures overlapped with general particle physics; now we focus on hadron spectroscopy approaches. One subject is particle representation in three-body decay.

**Dalitz plots** show interaction dynamics. For three-body decay, we have one incoming, three outgoing legs. Same questions as before about variable counting, but the answer is similar (same number of legs determines variables). For $3\pi$ decay, two variables completely describe the process ($s$ and $t$ or angles).

Remember my **rigid body analogy**: 3D-printed blob with vectors sticking out—fixed angles and lengths describe kinematics. Same for three-body decay: two variables completely specify it in the COM frame (three vectors with fixed relationships).

For three-body decay:

$$
s = (p_1 - p_2)^2 = (p_3 + p_4)^2
$$
$$
t = (p_1 - p_3)^2
$$

Note there was a typo ($p_1$ should be the decaying particle)—I'll update notation later. Key point: three-body phase space is flat in these variables.

The recursive formula we discussed gives phase space as:

$$
\frac{1}{8\pi^2} \frac{2|\vec{p}|}{\sqrt{s}}
$$
for each two-body subspace. Each phase space has a $\frac{1}{2\pi}$ factor, plus 3D angular element $\frac{d\Omega}{4\pi}$. In the asymptotic limit, this approaches 1 (unit integral if no angular dependence).

For three-body decay, using the recursive formula shows the Jacobian for transformation to pair mass variables is constant—no extra dependencies. Plotting differential width vs. $m_{34}^2$ and $m_{24}^2$ gives an undistorted density representation. **Mandelstam variables** provide this clean representation where the plot directly shows interaction dynamics—this is the power of Dalitz plots.

> [!IMPORTANT]
> **Dalitz plots** are powerful tools for studying three-body decays, as they directly reflect the dynamics of the interaction through invariant mass variables.



> [!NOTE]  
> The Λc baryon decay (Λc⁺ → pK⁻π⁺) is a **golden channel** for reconstruction due to its clean final state of three charged particles.  

You can see the example of the Λc decay that I have here — Λc baryon going to the proton, K⁻, and π⁺ for that decay. We do the measurements. We measure Λc produced in proton-proton collisions or any other collisions. In the BES experiment and Belle experiment they observe Λc.  

> [!IMPORTANT]  
> **Key Properties of Λc**:  
> - Produced **abundantly** in charm ground states.  
> - Lives **sufficiently long** to fly from the primary vertex.  
> - Reconstructible due to its **decay kinematics and dynamics**.  

This is one of the particles that lives long and is produced abundantly. Particles with charm ground states are produced abundantly and they live sufficiently long to fly from the primary vertex, and we reconstruct them. That's why we have a good sample and a good understanding of their decay kinematics — well, not only kinematics but dynamics as well — the content of this blob.  

---


In that decay you see there is a charm quark in the initial state and no charm quark in the final state, indicating this happens via **weak interaction**. The charm quark disappears between initial and final states — the charm quark decays, transitioning into the strange quark that ends up in the kaon.  

> [!NOTE]  
> **Quark Transition**:  
> The **c → s transition** happens within one generation and is **not suppressed** — it's an allowed process. The amplitude is proportional to:  
> $$\mathcal{M} \propto G_F V_{cs} \langle pK^-\pi^+ | \mathcal{H}_{weak} | \Lambda_c^+ \rangle$$  
> where $G_F$ is the Fermi constant and $V_{cs}$ is the CKM matrix element.  

---


This is the golden channel for reconstruction because in the final state you have three charged particles with no neutrals. The proton is a nice charged particle that travels and is stable. The kaon is stable in our accelerator experiments, and the pion is a stable particle. Without any distraction, they fly directly from the decay and we see the tracks clearly through all detectors.  

> [!TIP]  
> **Lab Frame Observation**:  
> The Λc decay vertex is shifted by **~10 mm** from the primary vertex due to its boosted lifetime:  
> $$\tau_{lab} = \gamma \tau_0 = \frac{E_{\Lambda_c}}{m_{\Lambda_c}} \tau_0$$  
> At the LHC, Λc is produced with **hundreds of GeV**, leading to measurable displacements.  

We observe them pointing away from the primary interaction. There is about a 10 millimeter shift in Λc decay vertices between primary and secondary vertices — roughly one centimeter. This is due to the boost and the fact that Λc in the laboratory frame lives longer than in its rest frame, being produced with a few hundred GeV in proton-proton collisions at the LHC.  

---


This is a superb decay channel that we've studied extensively. Here is the experimental result of the analysis which resembles the data. If I showed you actual experimental data, you wouldn't distinguish it from this plot because the statistics are so high that the distribution is very smooth.  

> [!IMPORTANT]  
> **Dalitz Plot Axes**:  
> - **x-axis**: Invariant mass of proton and kaon ($m_{pK}^2 = (E_p + E_K)^2 - (\vec{p}_p + \vec{p}_K)^2$).  
> - **y-axis**: Invariant mass of kaon and pion ($m_{K\pi}^2 = (E_K + E_\pi)^2 - (\vec{p}_K + \vec{p}_\pi)^2$).  

On the x-axis I have the invariant mass of proton and kaon, on the y-axis the mass of kaon and pion — all allowed values for the decay. Values corresponding to physical configurations are shown in color, while the white area represents kinematically forbidden regions.  

If I select a point inside the plot, I can compute angles between particles and lengths to create a 3D kinematic configuration. But for points in the white area, I quickly find that energy conservation cannot be satisfied. The range of possible invariant mass values is limited, and this surface is called a Dalitz plot.  

---


Different colors on this plot indicate different probabilities for the decay to occur at each kinematic point. What we measure is: the decay happened, we reconstruct the particle tracks, and determine the kinematic point since there's a unique relation between four-vectors and kinematic points.  

> [!NOTE]  
> **Phase Space and Decay Width**:  
> The decay width is given by:  
> $$\Gamma = \frac{1}{2m_{\Lambda_c}} \int |\mathcal{M}|^2 d\Phi_3$$  
> where the 3-body phase space is:  
> $$d\Phi_3 = \frac{1}{(2\pi)^5} \frac{d^3p_p}{2E_p} \frac{d^3p_K}{2E_K} \frac{d^3p_\pi}{2E_\pi} \delta^4(p_{\Lambda_c} - p_p - p_K - p_\pi)$$  

It turns out certain kinematics are more probable than others — particles prefer specific directions. For this decay, everything should be transferred. This configuration is more common, while this other possibility is rarer. You should be able to identify this pattern in the plot.  

> [!TIP]  
> **Identifying Patterns**:  
> - Particles align **along one line** at the border of the plot.  
> - Inside the surface, they always have angles between them.  
> - At the border, they become **collinear**.  

Let's take two minutes to find it. Here's a hint: particles are aligned along one line at the border of the plot. Inside the surface they always have angles between them, but at the border they become collinear. Think about how you maximize the mass and where this point lies on the border.



> [!NOTE]
> **Key Insight**: In three-body decays, the **Dalitz plot** helps visualize the phase space distribution by plotting the invariant masses of two particle pairs against each other.

Okay, any thoughts? I think you should be in the bottom right because we want to maximize the mass of $p_k$. There are three momenta going out. My idea was the three momenta are in opposite directions, so the three-momentum of the sun should be as small as possible. The three-momentum of the sun? Yes, if we add both momentum vectors, the forward momentum—the sum of the squares—should be as large as possible. So we should be on the right of our diagram. Then if we add and find... because the same direction should be on the lowest. So you argue that this mass on the y-axis should be as large or as small as possible. As small as possible. Why? Because the three momenta are in line, we subtract them.

---


> [!TIP]
> **Practical Tip**: Boosting to the rest frame of a particle pair simplifies the analysis of their relative momenta.

My way of thinking is: if you go to their rest frame, if you boost at this, the $KN$ and $\pi$ fly next to each other. Their relative momentum is small. If you boost to their rest frame, they might both be at rest. Therefore, their mass would just be the sum of the masses. So it's maximum? No, minimum. Okay, so you are correct. We are looking for the minimal mass of the kinetic. Let's figure out what this point corresponds to. The kinematics are like this: two particles with maximal momentum are at rest and go in opposite directions. That corresponds to this.

---


> [!IMPORTANT]
> **Crucial Point**: In experiments, the **lab frame** and **center-of-momentum frame** are distinct, and reconstructions must account for boosts.

This plot is from experimental data, right? Yes. In experiments, how would we reconstruct this case? We won’t detect the proton. This is the lab frame, but the central momentum frame is where everything is measured. Even if the proton is at rest in the lab frame, it's already boosted. So this point is the maximum mass—they have maximum momentum and go back-to-back. This is the maximum mass, and this one minimizes the mass. Okay, good.

---


For the three-body decay, there’s a similar way to define the angle. Let me mention this quickly. I’ll boost into the frame for every setup. Apologies for using proton, $K$, and $\pi$. I’ll fix the mass of the proton-$K$ system. No, I’d like to fix the mass of the $K$-$\pi$ system. I want to explore by changing the mass of the proton.

Think of it this way: take my setup in the center-of-momentum frame and boost to the $K$-$\pi$ rest frame. In the center-of-momentum frame, three particles are emitted such that the sum of their momenta is zero. Once I boost, my $\Lambda_c$ has non-zero momentum, and $K$ and $\pi$ also have non-zero momentum. But since I’m in the rest frame of $K$ and $\pi$, these two add to zero. If I fix the mass of the system and explore phase space along the line where the mass is fixed, the length of these vectors is fixed. What’s changing? Only the angle $\theta$.

---


At this point, I have $\theta$. I’ll explore all values of the angle from $0$ to $\pi$. At one corner, the angle is $0$; at the other, it’s $\pi$. Let’s reflect a bit more. Tell me which coordinate is which. The right should be $0$, and the left... Okay, let’s see how you get that. We fixed that in this setup, the proton and $K$ go in opposite directions, which gives the maximum mass for proton-$K$. For our new setup, we can only rotate.

If you think of the dependence of the mass of two particles on the angle $\theta$, the larger the angle, the larger the mass. For $\theta = 0$, you have a very high mass. When they go almost in the same direction, the mass is small. Now you can see I can do the same with the other half.

---


> [!NOTE]
> **Key Insight**: The **symmetric Dalitz plot** uses an equilateral triangle to represent phase space symmetrically, while the standard plot is more common in experiments.

The standard representation in experimental analysis for Dalitz plots is the x-axis for the mass of one pair and the y-axis for the mass of another pair. In homework, you’ll see a more symmetric Dalitz plot where all variables enter symmetrically. This uses properties of an equilateral triangle: every point inside has distances to the sides that sum to a constant.

The variables now are the distances to the sides of the triangle. This is a symmetric representation, essentially the same as the standard plot. They’re not matching because one is skewed. To plot this, we had to find the relation between Cartesian coordinates and the heights of the triangle. It involves $\sqrt{3}/2$ due to the $60^\circ$ angles.

This symmetric representation is nice, but the standard plot is more common and easier to use. Both represent the kinematics, where density increases at certain points. The goal is to understand the dynamics and processes guiding the interaction.

---


Looking ahead, we’ll see that $\Lambda_c$ decay isn’t just to three particles but proceeds via intermediate resonances. Two particles form an intermediate state that dissociates, increasing the decay probability. If the energy matches a resonance, the probability increases.

You’ve seen cross-sections for two-particle resonances with bumps. The physics is that the system’s quantum numbers match a resonance, and at that energy, the probability peaks. This creates band structures in the Dalitz plot. Projecting onto one axis shows a resonance shape.

This example is cool because resonances appear in all three pairs. Why is there higher probability when the proton and $\pi$ are near resonance? Let’s identify the lines. Horizontal lines in the blue plot correspond to resonances in $K$-$\pi$ ($K^*$). Vertical lines scan the proton-$K$ system ($\Lambda$ resonances). The third combination is $\pi$-proton ($\Delta$ resonances).

In the symmetric plot, lines are parallel to the triangle’s sides. The $\Lambda$ resonances are parallel to one side, $\Delta$ to another. It’s trickier to see $\Delta$ here, but it’s there.

---


> [!IMPORTANT]
> **Crucial Point**: **Angular distributions** reveal spin, parity, and other quantum numbers of particles, especially in resonant states.

Now, questions about angular distributions. To finish and move to today’s topic: angular distributions. I’ll fix a resonance band and discuss angular distributions within it. Traversing the Dalitz plot while fixing the mass of a pair changes the angle. This angle dependence shows inhomogeneity—sometimes one edge of the band is more probable.

Particles often prefer alignment over perpendicular orientations. This happens because particles have spin. The intermediate resonance (e.g., $K^*$) isn’t scalar—it has spin, causing inhomogeneity in angular distributions.

Angular distributions are powerful tools to measure spin, parity, and other quantum numbers. Higher-spin particles produce spikier distributions; scalar particles produce no asymmetries. By examining angular distributions in the rest frame, we infer spin.

For most discovered particles, quantum numbers are unknown. After finding a bump, the next step is determining quantum numbers via angular distributions. Often, it’s as simple as looking for nodes—if there’s one node, spin $1$; two nodes, spin $2$; etc.

For non-scalar final states, it’s more complicated. Here, the proton has spin $1/2$, $K$ has spin $0$, $\pi$ has spin $0$. The $\Lambda_c$ spin averages out unless polarized.

---


> [!NOTE]
> **Key Insight**: The **Wigner D-matrix** describes how quantum states transform under rotations, essential for analyzing angular distributions.

A particle with spin $J$ has $2J+1$ projections onto the quantization axis. The $|JM\rangle$ state is a vector with $2J+1$ components. Operators act as matrices on these states. Rotating the state produces a mixture of states, described by Wigner D-matrices.

For example, rotating a spin-$1$ state about the $y$-axis by $30^\circ$ gives a mixture of states. The coefficients are tabulated as $d$-functions.

More generally, any orientation is described by Euler angles ($\phi$, $\theta$, $\gamma$). First rotate by $\phi$ about $z$, then $\theta$ about $y$, then $\gamma$ about $z$. The D-matrix is:

$$
D^J_{m'm}(\alpha,\beta,\gamma) = e^{-i\alpha m'} d^J_{m'm}(\beta) e^{-i\gamma m}
$$

The small $d$-matrix element for rotation about $y$ is:

$$
d^J_{m'm}(\beta) = \langle Jm'|e^{-i\beta J_y}|Jm\rangle
$$


We need an example, a very small one, of spinning on half.  
I'm going to repeat state $1/2$ by rotating it **30 degrees** about the **Y axis**.  
I'll get a $1/2$, $1/2$ plus $1/2$ minus combination, and I want you to quickly tell me what the numbers here are.  

> [!NOTE]
> These coefficients are sitting in the same place as the **Clebsch-Gordan coefficients** — they are closely related.  
> This is about the **SU(2) group**, and you can just open the Clebsch-Gordan coefficient table and check the numbers.

Since it's **30 degrees**, we won't do it all now.  
We won't have time to look at details, but hopefully in the seminar, we'll explore this more.  
Just remember this table because it's **super simple**.  

The **Wigner D-matrix** for $m' = \pm1/2$ is:

$$
D^{1/2}_{m'm}(\theta) = \begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
$$  
of the **half angle**.  

> [!TIP]  
> I should have picked **60 degrees** because for **15 degrees**, it's a little inconvenient.  
> So what's going to be here is the **cosine of 15 degrees**, and here is the **sine of 15 degrees**.

---

Questions concerning the **Wigner D functions**:  
- Would you be able to calculate any rotations of the spin projection?  
- Looks alright, right?  

> [!IMPORTANT]  
> What's **critical to note** is the **convention minus sign**.  
> If you want to do **matrix exponentiation** yourself — in previous exercises, we computed these matrices — in principle, you can do that using **Python or Julia**.  

Just put matrix exponentiation, input a matrix, and you have the **Wigner D-matrix functions**.  
But you can also look them up as they are **tabulated**.  

> [!WARNING]  
> Be careful with **Mathematica** particularly — Mathematica has an **opposite convention** to what we use.  
> It has a **plus sign here**, I think, and some indices swapped.  
> **Wikipedia** is the **most reliable source** in that respect.  

Search for **Wigner D functions**, and it gives a table with conventions and everything.  
This is my **go-to page** when I need to check Wigner functions.  

> [!NOTE]  
> They're coded correctly in **Python's sympy library** and they're coded correctly in **ROOT**.  
> There is a word beginning with Wigner.  

---

Let me stress what we discussed so far has **nothing to do** with **weak interactions** or **strong interactions**.  
It was about **rotations** and the **rotational group**.  

> [!IMPORTANT]  
> That's the **fun part**, and that's something that still impresses me — that to understand how particles behave and what the **angular distributions** are, you need **little from the strong interaction**.  

You need the **general property** of how the rotational group works.  
- **Angular distributions** are determined by **general properties** of how space is rotated.  
- Plus the little we need from **strong interactions** — what is the preference for which spin particles are produced.  

That's what **strong interactions** tell us.  
But how they **decay** and what is the **asymmetry in the kinematics** is determined by the **quantum group**.  
That's **amazing**.  

Therefore, we can now move on and have a **recipe**, a **general way** to construct any particle decay chain and figure out what the **angular distribution** will be.  

---

Let's now explore the **blob** I had in the previous slide and consider one of the possible **decay kinematics**, one of the possible **decay dynamics**.  
We're going to make up a **model** for what's inside the blob.  

> [!NOTE]  
> It's not just **kinematics** — it really involves **modeling assumptions**.  

I'm going to assume that **three particles** in the final state are produced via a **cascade process** where:  
1. The **initial particle** first goes to an **intermediate particle** with spin $J$.  
2. Then $X$ decays to **1 and 2**.  

The **three-way process** with two-variable spins gives the **dimension of the matrix discrete dimensions**.  

For this problem, since all particles have spin, I'm going to deal with dimensions which are the product of $(2j+1)$ for all particles:

$$
\text{Dimension} = \prod_{i=0}^3 (2j_i + 1)
$$  
where $j_0$ is the **initial particle spin**, and $j_1, j_2, j_3$ are the **final state particle spins**.  

> [!TIP]  
> If a particle's spin is **0**, then the dimension of the corresponding spin is **1**. That's easy.  

But in the **general case**, you have many of these **two-variable functions**, and the way to write the **amplitude** is to sum over the **intermediate spins** and to...


For simplicity, we will align the system. We consider these $X_3$ as different restaurants—specifically, the **tourism restaurant** from RTPX, where $X$reland must traverse from the initial state.  

> [!NOTE]  
> The alignment simplifies the analysis by treating $X_3$ as distinct entities, reducing complexity in tracking decay paths.  

You observe the **CM (center-of-mass) frame**, denoted as $C.M.$, $c.M.$, which is correct. This general expression is **extendable to any cascade decays**.  

---

I’d like to present a **general formula**—we’ll focus on understanding it rather than deriving it due to time constraints. The amplitude has two components:  
1. A **model-independent part** (angular dependence driven by the rotation group).  
2. **Particle interaction terms** (dynamics embedded in $H$).  

> [!IMPORTANT]  
> The amplitude structure:  
> ```math  
> A = \sum_{\lambda} H_{\lambda} \cdot D^{J*}_{\lambda,\lambda'}(\phi,\theta,0)  
> ```  
> Here, $H_{\lambda}$ encapsulates dynamics (weak/strong/EM interactions), while $D$ is the **Wigner D-matrix** for rotational transformations.  

The $H$ terms are **dark blobs** representing unresolved dynamics—weak/strong/EM interactions or other physics. This $H$ is **unknown for hard interactions** because we lack a parameterization.  

---

For a particle $\Lambda_X$ (or $X_3$), the decay sequence is:

$$\Lambda_X \rightarrow \Lambda_3^0 + \text{other products} \rightarrow H^0 + X \rightarrow \text{particles } 1, 2 \text{ and } G.$$  

- **$G$**: Describes the **rotation orientation** of the decay.  
  - The **first index** indicates the decaying particle.  
  - The **second index** specifies the decay frame.  
- **Spin quantization**: The natural choice is to align the spin projection ($\lambda$) with the **direction of motion** ($\mathbf{P}$).  

> [!TIP]  
> Helicity projections ($\lambda$) are quantized along $\mathbf{P}$. The Wigner small-$d$ matrix encodes spin transformations:  
> ```math  
> d^{J}_{\lambda,\lambda'}(\theta)  
> ```  

---

Let’s evaluate this in **aligned kinematics** ($\phi = \theta = 0$). In the $CM$ frame, the amplitude simplifies to:

$$\sum_{\lambda_X, \lambda_3} H_{\lambda_X, \lambda_3} \cdot \delta_{\lambda_0, \lambda_X - \lambda_3} \cdot d^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta)$$  

> [!NOTE]  
> At $\theta = 0$, no rotation is needed, so the Wigner $D$-matrix reduces to a **delta function** $\delta_{\lambda_0, \lambda_X - \lambda_3}$, enforcing angular momentum conservation.  

The **final constrained expression** becomes:  
```math  
A = H_0 \cdot d^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta)  
```  
where $\lambda_X = \lambda_0 + \lambda_3$ (momentum conservation).  

---

1. **$H$ contains physics**: Unresolved dynamics (e.g., couplings).  
2. **$D$-matrices handle rotations**: Essential when quantization axes change between decays.  
3. **Aligned kinematics simplify**: Delta functions enforce conservation laws.  

> [!WARNING]  
> Misalignment introduces additional rotational terms—always verify the frame definitions!



> [!IMPORTANT]  
> **Key Question**: To compute electromagnetic interactions or gravity, how many input numbers are needed to predict the angle distribution? The framework is present, but it misses fundamental components.  

What’s inside the blobs—these blocks or blobs—determines the prediction. For all values, only **this one** and **that one** are needed.  

The number of values here is given by the **spin multiplicity factor**:

$$  
(2j_1 + 1) \times (2j_2 + 1)  
$$  

These values might be functions of particle masses (e.g., masses of $x$). A similar number is required for these, but a reasonable approximation exists.  

---


> [!NOTE]  
> In experiments, initial analyses often assume these values are **constants**. Here, one constant ($c$) represents particle properties.  

By fixing the mass of one tube and the intensity along the line, the angle distribution can be computed.  

Currently, we have:

$$  
\frac{d\Gamma}{d\cos\theta}  
$$  

**Why cosine?**  
- Cosine has a better Jacobian.  
- Avoids the sine Jacobian complication.  
- Often, the cosine distribution is analyzed.  

This distribution is proportional to the **matrix element squared** ($|\mathcal{M}|^2$). Here, $M_1^3$ squared is fixed. The distribution ranges from $-1$ to $1$, with $\theta$ and $\cos\theta$ null at $-1$.  

---


> [!TIP]  
> For particles with spin, common distributions include:  
> - A **parabola** (second-order polynomial in cosine).  
> - Other distinct shapes.  

**Critical distinction**:  
- $A$ is the **quantum transition amplitude** (a probability amplitude).  
- Squaring $A$ gives the observed probability.  
- $G$ appears squared—experiments only measure the squared amplitude.  

> [!WARNING]  
> **Unpolarized decays**: Distributions are averaged. You must square the amplitude, sum over initial and final spin projections, and compare to experimental observations.  

---


> [!IMPORTANT]  
> **First-step analysis**: Instead of guessing amplitudes, project angular distributions onto **orthogonal polynomials** (e.g., Legendre polynomials).  

**Legendre polynomials**:  
- Form a basis for functions from $-1$ to $1$.  
- Related to the spin of the produced particle.  

**Two approaches**:  
1. **Partial wave analysis**: Model cross-sections with amplitudes, freeing parameters to learn what’s inside the blocks.  
2. **Moment analysis**: Project differential cross-sections onto polynomials to extract constraints.  

This process is non-trivial, and further discussion will follow.  

---


> [!NOTE]  
> Differences between **canonical states** (introduced earlier) and **helicity states** (introduced later) were briefly touched.  

**Key insight**:  
- States are defined in the rest frame.  
- Further exploration is needed.  

> [!TIP]  
> **Best resource**: Martin Spearman’s *Elementary Particle Theory* (Chapter 4).  
> - Covers Lorentz group, vectors, and group theory lightly.  
> - Fun and insightful for particle definitions.  

---


> [!CAUTION]  
> **Exercise**: Analyze Dalitz plots from CLEO and BaBar (labels removed).  
> - One plot shows $D$ decay, another $D_s$ decay.  
> - Use kinematics to deduce masses and identify the decay.  

**Task**:  
- Axis labels are present, but masses are unknown.  
- Solve for group assignments.  

> [!WARNING]  
> **Logistics**:  
> - Exercises will be distributed later (not now).  
> - Available tomorrow at 8 AM.  

---

*Thanks for attending, and apologies for the slight delay. See you tomorrow!*  
