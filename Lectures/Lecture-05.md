<!--
Cosine simularity: 0.9804542287289655
-->
## Recap of Phase Space and Kinematics in Particle Scattering

I hope one day you receive more extensive notes from me than the bullet points I usually send, as I record myself and later use a language model to produce a PDF script, which is currently not ideal. Still, some points I discuss are mentioned, which helps me later when developing the material.  

Today we are at lecture number five, where we will discuss angle distributions and partial wave analysis. Before proceeding, I’d like to recap the last lecture. We discussed the phase space for particle reactions and the kinematics of different experiments. We reviewed a list of experiments worldwide studying hadrons, their production mechanisms, and peculiarities.  

We begin with a recap on kinematics. The first question is: **How many variables are needed to describe a $`2 \to 2`$ scattering process?**  

For scalar particles (e.g., $`0^-`$ scattering to $`0^-`$), the number of variables is given by:  

```math
2(2)(4-1) - 4 = 8 \ \text{variables from conservation laws}
```

This accounts for the degrees of freedom constrained by momentum and energy conservation.  

The second question involves spin. For example, consider $`P^+`$ scattering from $`0^-`$ to $`3^-`$ and $`1^+`$. The process is represented by a "blob" diagram, indicating the interaction region where strong interaction dynamics occur. The lines represent incoming and outgoing particles.  

> [!NOTE]  
> These are not Feynman diagrams but are sometimes called *unitarity diagrams*. We will discuss unitarity in later lectures.  

For now, this diagram serves as a visual aid for the kinematics. The task is to calculate the number of variables required to fully describe the process, focusing only on kinematics—what happens inside the blob is not considered here.  

<!--
Cosine simularity: 0.9381983842476403
-->
## Introduction to Scattering Amplitudes and Variables

We are talking only about kinematics at this point. Whatever happens in the blob does not impact the answer. The blob could represent electromagnetic, strong, or gravity interactions—anything you want. The question is how many variables are needed to describe the process. There are two possibilities: particles without spin and particles carrying spin.  

For scalar particles (no spin), the number of variables is calculated as follows:  

```math
2(2)(4-1) - 4 = 8 \ \text{variables from conservation laws}
```

This accounts for the degrees of freedom constrained by momentum and energy conservation. However, we can further reduce this by considering that there is no fixed reference frame or orientation in space. We subtract an additional six variables (three rotations and three boosts), leaving us with:  

```math
8 - 6 = 2 \ \text{variables from rotations}
```

For part (A), the answer is two variables.  

For part (B), when particles carry spin, the counting changes. The exact number depends on the spin configurations of the incoming and outgoing particles.  

> [!NOTE]  
> These calculations focus purely on kinematics—what happens inside the blob (interaction region) is not considered here.  

The example in part (C) asks for a combination of variables that fully describe the process, such as angles or invariant masses. The key takeaway is that after accounting for conservation laws and frame invariance, only two independent variables remain for scalar particles in a $`2 \to 2`$ scattering process.

<!--
Cosine simularity: 0.9439115614643421
-->
## Mandelstam Variables and Kinematic Descriptions

For part (A), you have two variables. For part (B), you have the two from the previous center and the angular distribution of the laser particles of the production. Since there is no decay information, just a $`2 \to 2`$ process, the total is 4 variables. These include the angle between the two production particles and the angle between the $`3^-`$ and $`1^+`$ particles.  

The scalar amplitude describes the amplitude as a function of $`S`$ and $`T`$, where:  

```math
S = (p_1 + p_2)^2
```
```math
T = (p_1 - p_3)^2
```

Here, $`S`$ represents the energy of the system (sum of four-vectors squared), and $`T`$ describes the transferred momentum in the vertical direction. The four-vectors $`p_1, p_2, p_3, p_4`$ include energy, three-dimensional momentum components, and helicity values ($`\lambda_3, \lambda_4`$) for particles with spin.  

For scalar particles, the amplitude is a single number. However, for particles with spin, the scattering amplitude becomes a higher-rank object. For example:  
- Spin-3 particles introduce 7 dimensions.  
- Spin-1 particles introduce 3 dimensions.  

Thus, the total scattering amplitude becomes a 21-dimensional object, representing 21 amplitudes. All these amplitudes are functions of the same two variables ($`S`$ and $`T`$).  

> [!NOTE]  
> The situation changes if decays of the final-state particles are considered. However, if restricted to the $`2 \to 2`$ process, only two variables are needed.  

For part (C), the favorite variables to describe a two-body scattering process could be the mass of particle one and two, or particle one and three. To compute the mass of two particles, you take the four-vector of the first particle, add it to the four-vector of the second, and compute the Lorentz invariant:  

```math
m^2 = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2
```

This gives the invariant mass squared of the system. Essentially, one of the variables is $`S`$ (the Mandelstam variable), and another could be constructed similarly.

<!--
Cosine simularity: 0.9264363351206988
-->
## Introduction to Mandelstam Variables and Invariants  

The Mandelstam variable $`t`$ can be defined as:  

```math
t = (p_1 - p_3)^2 = (p_2 + p_4)^2 = m_{24}^2
```  

It is common to assign particles in the final state with a minus sign and those in the initial state with a plus sign. This convention helps define the Mandelstam variables $`s`$ and $`t`$, which are invariants. These quantities characterize the entire decay or scattering process and are Lorentz invariant, meaning they do not depend on a specific reference frame.  

The term "invariants" may not be found in some dictionaries, but it is widely used in physics to describe these frame-independent variables. For example, $`s`$ and $`t`$ are such invariants.  

The scalar amplitude is a function of $`S`$ and $`T`$, where:  

```math
S = (p_1 + p_2)^2  
```  
```math
T = (p_1 - p_3)^2  
```  

Here, $`S`$ represents the total energy of the system (the squared sum of four-vectors), while $`T`$ describes the momentum transfer. For particles with spin, the scattering amplitude becomes a higher-dimensional object. For instance, spin-1 particles introduce 3 dimensions, and spin-3 particles introduce 7 dimensions, resulting in a 21-dimensional amplitude.  

> [!NOTE]  
> If only a $`2 \to 2`$ process is considered, two variables ( $`S`$ and $`T`$ ) are sufficient. Additional variables are needed if decays of final-state particles are included.  

To compute the invariant mass of two particles, you combine their four-vectors:  

```math
m^2 = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2  
```  

This gives the squared mass of the system, where $`S`$ is one of the Mandelstam variables.

<!--
Cosine simularity: 0.8878464793115682
-->
## Kinematic Variables and Their Independence in Particle Decays

We can call these variables invariants. Let's discuss examples of such sets. One example is $`S`$ and $`T`$, but we need two variables to fully describe the process. Another variable is $`U`$, defined as:

```math
U = (p_2 - p_4)^2 = (p_1 - p_3)^2
```

However, $`U`$ is not independent because it is a linear combination of $`S`$ and $`T`$. So, a valid set could be $`S`$ and $`U`$, or equivalently $`T`$ and $`U`$.  

Another useful choice is the center-of-mass energy ( $`\sqrt{S}`$ ) and the scattering angle. The angle is defined in the center-of-momentum frame, where the total momentum of all particles sums to zero. For example, if we have momenta $`p_1`$ and $`p_3`$, the angle between them characterizes the kinematics.  

> [!NOTE]  
> Any two independent variables can fully describe the kinematics, but one must ensure they are not redundant. For example, $`E_1`$ and $`E_3`$ in the lab frame also work, provided they are independent.  

The phase space mapping must be bijective—some variable choices may fold the phase space, leading to non-unique coverage. This is an advanced topic, but it’s important to avoid redundant or overlapping variables.  

For a $`2 \to 2`$ process, two variables (e.g., $`S`$ and $`T`$) are sufficient. If final-state particles decay further, additional variables are needed.  

The invariant mass of two particles is computed as:  

```math
m^2 = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2
```  

This gives the squared mass of the system, where $`S`$ is one of the Mandelstam variables.  

<!--
Cosine simularity: 0.9253771504547097
-->
## Introduction to 3-Body Decay Kinematics and Dalitz Plots  

The homework exercise involved a Dalitz plot, which is now part of our lectures. This marks a shift in the course, where we transition from overlapping topics with particle physics to material specific to hadron spectroscopy. One key subject we will explore is particle representation, particularly in three-body decays.  

The Dalitz plot is a common technique to study the dynamics of interactions in such decays. For a three-body decay, the diagram involves one incoming leg and three outgoing legs, with the "blob" representing the interaction. The number of kinematic variables remains the same as before, determined by the number of legs.  

For decays like $`3\pi`$ or $`DDK`$, two variables fully describe the process. Given these two variables—whether $`S`$ and $`T`$, angles, or others—the entire kinematics can be reconstructed. Think of it like a rigid body: if you 3D-print a blob with fixed vectors sticking out, the angles and lengths of the vectors are fixed, defining the kinematic configuration. The same applies to a three-body decay—just two variables are needed to visualize the decay in the center-of-mass frame.  

The variables $`S`$, $`T`$, and $`U`$ are examples of invariants used to describe the process. However, $`U`$ is not independent, as it is a linear combination of $`S`$ and $`T`$. A valid choice could be $`S`$ and $`U`$, or $`T`$ and $`U`$.  

Another useful set is the center-of-mass energy ( $`\sqrt{S}`$ ) and the scattering angle, defined in the frame where the total momentum is zero. The angle between momenta $`p_1`$ and $`p_3`$ characterizes the kinematics.  

> [!NOTE]  
> Any two independent variables suffice, but redundancy must be avoided. For example, $`E_1`$ and $`E_3`$ in the lab frame work if they are independent.  

The phase space mapping must be bijective—some variable choices may fold phase space, leading to non-unique coverage. This is an advanced consideration but crucial for avoiding redundancy.  

For a $`2 \to 2`$ process, two variables (e.g., $`S`$ and $`T`$) are sufficient. If final-state particles decay further, additional variables are needed.  

The invariant mass of two particles is computed as:  

```math  
m^2 = (E_1 + E_2)^2 - (\vec{p}_1 + \vec{p}_2)^2  
```  

This gives the squared mass of the system, where $`S`$ is one of the Mandelstam variables.

<!--
Cosine simularity: 0.8863660072590576
-->
## Definition and Properties of Mandelstam Variables in Kinematics  

In the center-of-mass frame, we can visualize the kinematics by drawing two vectors representing the outgoing momenta. The configuration is determined by the angles and lengths of these vectors.  

The Mandelstam variables $`S`$ and $`T`$ are defined analogously for processes with different particles in the final state. The transformation between kinematic configurations involves flipping the sign of a momentum. For example:  

```math
S = (p_1 + p_2)^2 = (p_3 + p_4)^2
```
```math
T = (p_1 - p_3)^2
```

There was a typo in the notation where $`p_1`$ should represent the decaying particle, but we will proceed with the current notation for clarity.  

The phase space integration factor for a three-body decay is given by:  

```math
\frac{dm_{12}^2}{2\pi} \frac{2P}{2p'} dm_{x}^2 m_x
```

This describes the differential phase space volume involving the invariant masses $`m_{12}`$ and $`m_x`$, along with momenta $`P`$ and $`p'`$.  

The phase space for $`3 \to DDK`$ is flat in the variables $`S`$ and $`T`$, meaning it is constant when expressed in terms of these invariants. Substituting the two-body phase spaces and applying the proper kinematic transformations yields a factor of $`\frac{1}{8\pi^2}`$. This arises from combining the phase space contributions:  

```math
\frac{1}{8\pi} \frac{2P}{\sqrt{S}}
```

for each two-body subsystem. The squared term comes from the product of two such phase space elements.  

The recursive formula discussed in the previous lecture simplifies the calculation when substituting the phase space variables. The final result includes the invariant mass terms and momentum dependencies, reflecting the kinematic constraints of the decay process.

<!--
Cosine simularity: 0.9135969654941294
-->
## Kinematic Variables and Jacobian in Three-Body Decays  

The phase space integration factor involves terms like $`\frac{2P}{\sqrt{S}}`$. Each momentum space contribution includes a factor of $`\frac{1}{2\pi} \frac{1}{8\pi^2} \frac{2P}{\sqrt{S}}`$, along with a solid angle term $`\frac{3D \Omega}{4\pi}`$. These factors simplify in the high-energy limit, where they approach unity, leaving a unit integral if no additional dependencies are present.  

For three-body decays, the cosine of the scattering angle $`\cos \theta`$ can be expressed in terms of invariant masses like $`m_{34}`$. The momentum factor $`2P`$ appears in the Jacobian when replacing $`E'`$ with $`P`$. This transformation introduces a Jacobian, though the speaker notes uncertainty about its exact form.  

The recursive formula for three-body phase space reveals that the Jacobian for transforming to paired mass variables (e.g., $`m_{23}^2`$, $`m_{24}^2`$) is constant. This means the differential width or cross section, when plotted against these variables, shows no additional density variations. The choice of Mandelstam variables (or linearly related ones) is particularly powerful because they provide an undistorted representation of the interaction dynamics.  

For example, plotting the differential width against $`m_{34}^2`$ or $`m_{23}^2`$ yields a constant density, reflecting the underlying physics without kinematic distortions. This property makes Mandelstam variables ideal for analyzing three-body processes, as they directly reveal the interaction structure.  

The phase space integration for a $`3 \to DDK`$ decay is flat in $`S`$ and $`T`$, meaning it is constant when expressed in these invariants. Combining two-body phase space elements introduces a factor of $`\frac{1}{8\pi^2}`$, derived from terms like $`\frac{1}{8\pi} \frac{2P}{\sqrt{S}}`$ for each subsystem. The recursive formula simplifies the substitution of phase space variables, leaving invariant mass terms and momentum dependencies that encode the kinematic constraints of the decay.

<!--
Cosine simularity: 0.9229546200549428
-->
## Charm Quark Decay via Weak Interaction  

The interaction blob represents the weak decay process. The example shown is the triple-G decay of the $`\Lambda_c`$ baryon into a proton, kaon, and pion.  

We measure $`\Lambda_c`$ production in proton-proton collisions or other collision types. Experiments like BES and Belle observe $`\Lambda_c`$ abundantly because charm ground-state particles are produced in large quantities and live long enough to travel a measurable distance from the primary vertex. This allows us to reconstruct them effectively.  

We have a good sample and understanding of their decay kinematics and dynamics. In this decay, a charm quark ($`c`$) is present in the initial state but absent in the final state, confirming weak interaction mediation. The charm quark transitions to a strange quark ($`s`$), which ends up in the kaon.  

This $`c \to s`$ transition occurs within the same quark generation and is not suppressed, making it an allowed process. It serves as a golden channel for detection due to its clear signature.

<!--
Cosine simularity: 0.9540905264341643
-->
## Lambda Decay Kinematics and Dalitz Plot Analysis

This decay process is the golden channel for registration because the final state contains three charged particles with no neutrals. The proton is a stable charged particle that travels well, the kaon is stable in our accelerator experiments, and the pion is also stable. These particles fly directly from the decay without distraction, leaving clear tracks through all detectors.  

We observe these tracks pointing away from the primary interaction vertex, with a shift of around 10 millimeters in LHC energies between the primary and secondary vertices. This displacement is due to the boost of the lambda particle in the laboratory frame, where it lives longer than in its rest frame. The lambda is produced with energies of a few hundred GeV in proton-proton collisions at the LHC, making this decay particularly well-suited for study.  

Here is the result of the analysis, which closely resembles experimental data. The statistics are so high that the distribution appears smooth.  

- **X-axis**: $`M_{pK}^2`$ (invariant mass squared of proton and kaon)  
- **Y-axis**: $`M_{K\pi}^2`$ (invariant mass squared of kaon and pion)  

The colored region represents all allowed kinematic values for the decay, while the white area indicates forbidden kinematics where energy and momentum conservation cannot be satisfied. If a point is selected within the colored region, we can compute the angles between particles and reconstruct the 3D configuration. However, points in the white region violate energy conservation, making them physically impossible.  

This constrained kinematic surface is called the **Dalitz plot**, and it is how we explore the decay dynamics.  

> [!NOTE]  
> The Dalitz plot is defined by the invariant mass squared of particle pairs, such as $`M_{14}^2 = (E_1 + E_4)^2 - (\vec{p}_1 + \vec{p}_4)^2`$, where $`E_i`$ and $`\vec{p}_i`$ are the energy and momentum of particle $`i`$.  

The different colors in the plot represent varying kinematic configurations, allowing us to study the decay properties in detail.

<!--
Cosine simularity: 0.8990498821783939
-->
## Probability and Kinematics in Particle Decay

Different colors on this plot indicate the varying probabilities for this reaction to occur. What we measure is the decay event, where we reconstruct the particle tracks and determine the kinematic point of decay. There is an unambiguous relationship between four-vectors and the kinematic point.  

It turns out that certain kinematic configurations are more probable than others. Particles prefer specific directions. For this decay, momentum must be fully transferred. One possibility is longer than the other, making it more likely. The rarer configuration corresponds to a different kinematic arrangement.  

To identify this pattern on the plot, consider the hint: particles align along the boundary of the kinematic surface. Inside the surface, they always have an angle between them, but on the border, they lie in a straight line.  

> [!NOTE]  
> The kinematic boundary is determined by energy and momentum conservation, defining the allowed phase space for the decay.  

To maximize the mass $`M_{pK}`$, focus on the bottom-right region of the plot. This is where the three outgoing momenta are most opposed, minimizing the total three-momentum of the system.  

```math
M_{pK}^2 = (E_p + E_K)^2 - (\vec{p}_p + \vec{p}_K)^2
```  

The Dalitz plot reveals these dynamics, showing preferred kinematic regions through color gradients. The white areas represent forbidden configurations where conservation laws are violated.  

<!--
Cosine simularity: 0.9253180407191464
-->
## Minimizing Mass in Particle Decay Kinematics

The three-momentum of the system should be as small as possible. If we add both momentum vectors, the forward momentum—like the sum of the squares—should be as large as it could possibly be. This places us on the right side of the diagram.  

When the momenta are aligned in the same direction, the mass on the y-axis should be as small as possible. Why? Because the three-momenta are in line, and we subtract them.  

> [!NOTE]  
> In the rest frame of the system (e.g., $`K\pi`$), the particles may fly alongside each other or even be at rest. Their relative momentum is minimized, and the mass reduces to the sum of their masses.  

This configuration corresponds to the minimal mass in the kinematics. To locate this point, consider the case where two particles with maximal momentum are at rest and then move in opposite directions.  

In experiments, we reconstruct such cases in the lab frame, where everything is boosted. Even if the proton is not detected, the central momentum frame is still accessible. The point where particles have maximum momentum (back-to-back) corresponds to the maximum mass, while the aligned configuration minimizes the mass.  

```math
M_{pK}^2 = (E_p + E_K)^2 - (\vec{p}_p + \vec{p}_K)^2
```  

The kinematic boundary is determined by energy and momentum conservation, defining the allowed phase space for the decay. The Dalitz plot reveals these dynamics, with forbidden configurations appearing as white regions.  

<!--
Cosine simularity: 0.913636643105262
-->
## Defining Angles and Mass Fixation in Three-Body Decay

For the three-body decay, there is a standard way to define the angle. Let me illustrate this with a setup involving a proton, kaon ($`K`$), and pion ($`\pi`$).  

First, I boost into the center-of-momentum frame for the system. In this frame, the three particles are arranged such that their momenta sum to zero. Then, I boost again into the rest frame of the $`K\pi`$ system. Here, the kaon and pion have back-to-back momenta, while the $`\Lambda_C`$ (or proton) has non-zero momentum.  

By fixing the mass of the $`K\pi`$ system, we can explore the phase space along a line where the masses of $`K`$ and $`\pi`$ are held constant. In this configuration, the lengths of their momentum vectors are fixed, and only the angle $`\theta`$ between them varies.  

```math
M_{K\pi}^2 = (E_K + E_\pi)^2 - (\vec{p}_K + \vec{p}_\pi)^2
```

The angle $`\theta`$ ranges from $`0`$ to $`\pi`$. At $`\theta = 0`$, the momenta are aligned, while at $`\theta = \pi`$, they are antiparallel. This variation allows us to scan the kinematic boundaries of the decay.  

> [!NOTE]  
> In the rest frame of the $`K\pi`$ system, their relative momentum is minimized when they are at rest or moving together. The mass then reduces to the sum of their masses.  

The kinematic constraints are determined by energy and momentum conservation, defining the allowed phase space. The Dalitz plot visualizes these dynamics, with forbidden configurations appearing as excluded regions.  

<!--
Cosine simularity: 0.9626518032978592
-->
## Kinematic Representation and Resonance Analysis in Dalitz Plots  

The corner angle is equal to $`\pi`$. The right coordinate should be zero and the left should reflect this. In this setup, the proton and the kaon ($`K`$) go in opposite directions, which corresponds to the maximum mass of the $`K`$ system. For this configuration, the lengths of all vectors are fixed, and only rotation is possible.  

The mass dependence of two particles can be expressed as a function of the angle between them: the wider the angle, the larger the mass. For the proton-kaon system, when the angle is zero, the mass is very high. When the particles move almost in the same direction, their mass is small. The same logic applies to the other half of the system.  

The most straightforward way to analyze this is to work in the rest frame of the proton-kaon system, where all momenta are fixed. By scanning along this line, we change the angle of the pair relative to the rest frame. This describes the setup where the angle is varied in one frame or another.  

There is a third variable in the $`2 \to 2`$ scattering process, called $`U`$, which introduces additional symmetry. For a three-particle system (pion, proton, kaon), the mass of the pion-proton pair is not immediately evident. If we fix the mass of this system and scan the angle, the motion along the line is determined by the relation:  

```math
U = m_{\pi p}^2 + m_{K p}^2 + m_{K \pi}^2 - \text{const.}
```

Here, $`U`$ is a linear combination of the other two mass variables, with coefficients of one. This results in a diagonal line in the Dalitz plot. Fixing the mass of the pion-proton system corresponds to moving along this diagonal, transitioning from one corner to another.  

The standard experimental representation of a Dalitz plot places the mass of one pair on the $`x`$-axis and the mass of another pair on the $`y`$-axis. However, a more symmetric representation exists, where all variables are treated equally. This uses the properties of an equilateral triangle: for any point inside, the sum of the distances to the sides is constant.  

In this symmetric representation, the masses of the particles correspond to the distances to the sides of the equilateral triangle. This allows for a fully symmetric treatment of the variables, where the masses are summed in a balanced way. The transformation between the standard and symmetric representations is not just a rotation but a skew, involving a linear transformation.  

The relation between Cartesian coordinates and the heights of the equilateral triangle involves a factor of $`\sqrt{3}/2`$ due to the 60-degree angles. This symmetric representation is elegant, but the standard representation is more practical for plotting, as it avoids the need for this transformation. Both methods fully describe the kinematics of the system.

<!--
Cosine simularity: 0.9190839220926501
-->
## Intermediate Resonances and Probability Enhancement in Particle Decays  

The kinematic representation shows points where the density increases, helping us understand the dynamics and processes guiding the interaction. In future lectures, we will see that the decay process is not just $`\Lambda_C \to 3`$ particles but proceeds via intermediate resonances. For a short moment, two particles form an intermediate state that dissociates, increasing the decay probability.  

When the energy is adjusted into a certain range, the probability for this process becomes higher because the particles interact more strongly. This is analogous to hadronic resonances in two-particle cross sections, where a "bump" appears. The physics behind this is that the quantum numbers of the two-particle system match those of an intermediate resonance. By tuning the system's energy, we observe how likely the particles are to interact at that energy.  

If an intermediate resonance exists, the system can resonate at this energy, leading to a probability increase as it passes through the resonance region. This manifests as an enhancement in the decay rate.  

The mass dependence of two particles can be expressed as a function of the angle between them: the wider the angle, the larger the mass. For example, in a proton-kaon system, when the angle is zero, the mass is very high, while particles moving in nearly the same direction have a small mass.  

The most straightforward analysis is done in the rest frame of the proton-kaon system, where all momenta are fixed. By scanning along this line, we vary the angle of the pair relative to the rest frame.  

In $`2 \to 2`$ scattering, a third variable $`U`$ introduces additional symmetry. For a three-particle system (pion, proton, kaon), the mass of the pion-proton pair is not immediately evident. Fixing this mass and scanning the angle determines the motion along the line:  

```math
U = m_{\pi p}^2 + m_{K p}^2 + m_{K \pi}^2 - \text{const.}
```  

Here, $`U`$ is a linear combination of the other two mass variables, resulting in a diagonal line in the Dalitz plot. Fixing the mass of the pion-proton system corresponds to moving along this diagonal.  

The standard experimental Dalitz plot places one pair mass on the $`x`$-axis and another on the $`y`$-axis. However, a symmetric representation treats all variables equally, using the properties of an equilateral triangle. In this form, the masses correspond to distances to the sides of the triangle, allowing a balanced treatment. The transformation between representations involves a skew, not just a rotation.  

The relation between Cartesian coordinates and the heights of the equilateral triangle includes a factor of $`\sqrt{3}/2`$ due to the 60-degree angles. While the symmetric representation is elegant, the standard form is more practical for plotting.

<!--
Cosine simularity: 0.9177523389809616
-->
## Resonance Identification in Mass Distributions

The resonance region leads to the appearance of bent structures in the telescope distribution. When projected onto one of the axes, these structures reveal a resonance-like shape, which can be identified in both projections.  

This is a particularly interesting example because resonances appear in all three particle pairs:  

1. **Horizontal lines (blue plot)**: These correspond to resonances in the $`K\pi`$ system. The fixed mass of $`K\pi`$ produces peaks, indicating $`K^*`$ resonances (particles decaying to $`K\pi`$).  
2. **Vertical lines**: These scan the energy of the $`K p`$ system. By varying the $`K\pi`$ mass, we probe resonances in the $`K p`$ system, such as the $`\Lambda`$ and $`\Sigma`$ resonances.  
3. **Diagonal lines**: These are parallel to the sides of the kinematic triangle and correspond to $`\Delta`$ resonances in the $`\pi p`$ system.  

The kinematic triangle helps visualize these resonances. For example:  
- Lines parallel to one side represent $`\Lambda`$ resonances.  
- Lines parallel to another side highlight $`\Delta`$ resonances (though these are harder to distinguish).  

> [!NOTE]  
> The symmetric representation of the Dalitz plot uses an equilateral triangle, where masses correspond to distances from the sides. This allows balanced treatment of all resonance pairs.  

The relation between the masses can be expressed as:  

```math
U = m_{\pi p}^2 + m_{K p}^2 + m_{K \pi}^2 - \text{const.}
```  

Here, $`U`$ is a linear combination of the squared invariant masses, creating diagonal lines in the plot. Fixing one mass (e.g., $`m_{\pi p}`$) corresponds to moving along such a line.  

In experimental analyses, the standard Dalitz plot places one pair mass on the $`x`$-axis and another on the $`y`$-axis. However, the symmetric representation (using the triangle) treats all variables equally, though it requires a skew transformation rather than a simple rotation.  

The enhancement in decay probability occurs when the system passes through a resonance region, similar to hadronic resonances in two-particle scattering. This happens when the quantum numbers of the intermediate state match those of a known resonance, leading to a stronger interaction and a visible "bump" in the distribution.  

<!--
Cosine simularity: 0.9202888707394199
-->
## Angular Distribution and Particle Spin  

We now discuss angular distribution for a decay within one band. Consider the phase space resonance here. As previously discussed, when traversing the Dalitz plot while keeping the mass of the combination fixed, we explore different angles. This is precisely the kinematics.  

In the rest frame of the $`K\pi`$ system, traversing the phase space by changing the angle reveals an angular dependence. Within the band, inhomogeneity can occur — one edge of the band may have a different probability than the other. Particles often prefer alignment over perpendicular configurations, making certain kinematics less probable.  

This preference arises because particles have spin. The intermediate resonance (e.g., $`K^*`$) is not a scalar particle; its spin introduces inhomogeneity in angular distributions and the Dalitz plot.  

Angular distribution is a powerful tool for understanding particle properties. It allows us to measure spin, parity, and other quantum numbers in particle interactions. Particles with higher spin produce more "bumpy" or "spiky" angular distributions, while scalar particles (spin-0) yield no asymmetries or structures in angular distributions.  

> [!NOTE]  
> The kinematic triangle helps visualize resonances, with lines corresponding to fixed masses in different particle pairs ($`K\pi`$, $`Kp`$, $`\pi p`$). The symmetric Dalitz plot representation treats all resonance pairs equally.  

The relation between masses is given by:  

```math
U = m_{\pi p}^2 + m_{K p}^2 + m_{K \pi}^2 - \text{const.}
```  

Here, $`U`$ is a linear combination of squared invariant masses, creating diagonal lines in the plot. Fixing one mass (e.g., $`m_{\pi p}`$) corresponds to moving along such a line.  

Enhancements in decay probability occur when the system passes through a resonance region, similar to hadronic resonances in two-particle scattering. This happens when the quantum numbers of the intermediate state match a known resonance, producing a visible "bump" in the distribution.

<!--
Cosine simularity: 0.9629873819596456
-->
## Nodes in Angular Distribution and Spin Determination

If there are no asymmetries at all and no structures in angular distributions, we can examine the ratio of aligned kinematics to other types of kinematics by looking at the angular distribution, especially in the rest frame of the particle decay. This allows us to infer information about the spin.  

For most particles discovered so far, the quantum numbers are not initially known. After identifying a particle as a "bump" in the spectrum, the next step is to determine its properties, including quantum numbers, by analyzing angular distributions. This is often as simple as examining the Dalitz plot and checking for minima or structures in the angular distribution.  

The presence of nodes in the angular distribution directly indicates the spin of the particle if the final state consists of scalar particles. Specifically:  
- One node corresponds to spin-1.  
- Two nodes correspond to spin-2.  
- Three nodes correspond to spin-3.  

The intensity of the distribution reflects these spin-dependent patterns.

<!--
Cosine simularity: 0.9448534393696162
-->
## Spin Projections and Quantum State Rotations

If you have three nodes, you have spin three. The intensity would vanish at certain points in the dark spot. For non-scalar particles, which are most interacting particles, the situation is more complicated. Here, scalar resonances serve as an example.  

The spin of a proton is $`\frac{1}{2}`$, and the spin of $`K^+`$ and $`\pi`$ is zero since they are scalars. The spin of $`\Lambda`$ is the same as the proton, but the presence of spin averages out the distribution. If you consider a specific spin projection of $`\Lambda_c`$ and the proton, you would observe nodes and zeros in the angular distribution. However, since we neither polarize the initial state $`\Lambda`$ nor measure the spin of the final state, everything is averaged, and the minima or nodes disappear.  

A particle with spin $`J`$ can have $`2J + 1`$ projections onto the quantization axis. Consider a particle with spin $`J`$ and a $`z`$-axis for spin quantization. The operator $`J_z`$ acting on the state $`|Jm\rangle`$ yields:  

```math
J_z |Jm\rangle = m |Jm\rangle
```

The state $`|Jm\rangle`$ can be represented as a vector with $`2J + 1`$ components. Operators in this space are matrices that act on these vectors, either returning the same state with an eigenvalue or producing a mixture of states.  

When a rotation is applied to the state, it does not simply adjust to a new projection as in classical vectors. Instead, quantum mechanics dictates that the rotated state becomes a superposition of all possible states:  

```math
R(\theta) |Jm\rangle = \sum_{m'} D^{(J)}_{m'm}(\theta) |Jm'\rangle
```

Here, $`D^{(J)}_{m'm}(\theta)`$ are the Wigner rotation matrices, which describe how the state mixes under rotation. The coefficients in this expansion determine the probability amplitudes for each projected state.

<!--
Cosine simularity: 0.9416779097559314
-->
## Wigner D Functions and Rotation Conventions

When rotating a spin state $`|Jm\rangle`$, the transformation is given by:

```math
R(\theta) |Jm\rangle = e^{-iJ_z \theta} |Jm\rangle
```

This results in a mixture of all possible states, with coefficients that are tabulated and known as Wigner D functions. These coefficients depend on the initial state, hence the $`JM`$ indices are retained in the notation.  

For example, consider a spin-1 state initially perpendicular to the $`Y`$-axis and rotated by 30 degrees. The resulting state composition can be determined by looking up these Wigner D coefficients.  

To perform a rotation about the $`Y`$-axis, we use the $`J_y`$ operator, which has zeros on the diagonal and coefficients above and below the diagonal. The transformation is applied via the matrix exponential $`e^{-iJ_y \theta}`$, but the Wigner D functions already encapsulate this result.  

A more general rotation in 3D space is described using Euler angles. In particle physics, the convention is:  
1. Rotate by $`\phi`$ about the $`Z`$-axis.  
2. Rotate by $`\theta`$ about the $`Y`$-axis.  
3. Rotate by $`\gamma`$ about the $`Z`$-axis again.  

The Wigner D function for this full rotation decomposes into three parts:  

```math
D^J_{m'm}(\gamma, \theta, \phi) = e^{-i\gamma m'} d^J_{m'm}(\theta) e^{-i\phi m}
```

The most nontrivial part is the middle rotation about $`Y`$, while the $`Z`$-rotations introduce phase factors.  

For a concrete example, take a spin-$`\frac{1}{2}`$ state $`|\frac{1}{2}, \frac{1}{2}\rangle`$ and rotate it by 30 degrees about $`Y`$. The resulting state is a superposition:  

```math
R_Y(30^\circ) \left|\frac{1}{2}, \frac{1}{2}\right\rangle = \cos(15^\circ) \left|\frac{1}{2}, \frac{1}{2}\right\rangle + \sin(15^\circ) \left|\frac{1}{2}, -\frac{1}{2}\right\rangle
```

The coefficients here are derived from the Wigner D matrix for spin-$`\frac{1}{2}`$, which takes the form:  

```math
D^{1/2}(\theta) = \begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
```

These coefficients can be found in tables alongside Clebsch-Gordan coefficients, as they are closely related to the $`SU(2)`$ group structure.  

> [!NOTE]  
> Mathematica and other software may use different sign conventions for the Wigner D functions, so caution is advised when comparing results.  

The Wigner D functions allow us to compute any rotation of a spin state, either by direct matrix exponentiation or by referencing precomputed tables. For practical calculations, tools like Python or Julia can be used to evaluate the matrix exponential of the angular momentum operators.

<!--
Cosine simularity: 0.9209568176754853
-->
## Angular Distributions and Rotational Group Properties

Be careful with Mathematica's conventions. Mathematica has an opposite sign convention to what we use—it has a plus sign here, and some indices are swapped. Wikipedia is the most reliable source for this. If you search for "Wigner D functions," it provides a table with conventions and definitions.  

The Wigner D functions are correctly implemented in Python's `sympy` library and in ROOT.  

> [!WARNING]  
> Be cautious with sign conventions when using software like Mathematica, as they may differ from standard physics conventions.  

What we have discussed so far does not involve weak or strong interactions. It is purely about rotations and the rotational group. The remarkable part is that understanding particle behavior and angular distributions requires very little input from strong interactions.  

Angular distributions are determined by general properties of how space rotates. The only input needed from strong interactions is the preference for which spin states are produced. The decay patterns and kinematic asymmetries, however, are entirely governed by the rotational group.  

This is why we can now proceed with a general recipe for analyzing angular distributions, relying primarily on rotational symmetry and minimal assumptions about the underlying interactions.  

The Wigner D functions encode these rotational properties, allowing us to predict angular distributions without detailed knowledge of the dynamics.  

> [!NOTE]  
> For accurate results, always verify conventions when using Wigner D functions in calculations or software.

<!--
Cosine simularity: 0.9443519260330505
-->
## Cascade Decay Kinematics and Spin Dimensions

We now have a general recipe to construct any particle decay chain and determine its angular distribution. Let's examine the "blob" from the previous slide and consider one possible decay kinematics and dynamics.  

I will model the process assuming three final-state particles are produced via a cascade decay: an initial particle decays first into an intermediate particle with spin $`J`$, which then decays into particles 1 and 2.  

For this system, the spin dimensions are determined by the product:  

```math
(2j_0 + 1) \times (2j_1 + 1) \times (2j_2 + 1) \times (2j_3 + 1)
```

Here, $`j_i`$ represents the spin of each particle. If a particle has spin 0, its corresponding dimension is 1.  

> [!WARNING]  
> Be cautious with sign conventions when using software like Mathematica, as they may differ from standard physics conventions.  

The Wigner D-functions correctly encode rotational properties and are properly implemented in Python's `sympy` and ROOT.  

Angular distributions are governed by rotational symmetry, requiring minimal input from strong interactions—only the preferred spin states need to be specified. The decay kinematics and asymmetries are entirely determined by the rotational group.  

This allows us to analyze angular distributions systematically, relying primarily on rotational symmetry rather than detailed dynamics.

<!--
Cosine simularity: 0.9096894937902571
-->
## General Expression for Cascade Decays and Spin Dynamics  

The rotation matrix for spin states can be expressed in terms of Euler angles as:  

```math  
R = R_z(\beta) R_y(\theta) R_z(\varphi)  
```  

If a particle has spin 0, the dimension of its corresponding spin space is 1. In the general case, the amplitude involves summing over intermediate spins and two-variable functions.  

> [!NOTE]  
> For simplicity, we align the system such that $`X_3`$ is defined in the rest frame of the initial state.  

The general expression for cascade decays consists of two components:  
1. A **model-independent part** driven by rotational symmetry (Wigner D-functions).  
2. A **dynamics-dependent part** encoded in the interaction terms $`H`$.  

The $`H`$ terms represent the physics of the interactions (weak, strong, electromagnetic, etc.). For hard interactions, $`H`$ remains unknown due to the lack of a suitable parameterization.  

> [!IMPORTANT]  
> The rotational properties of the system are fully determined by the Wigner functions, while $`H`$ encapsulates the underlying particle dynamics.  

This framework is extendable to any cascade decay process, providing a systematic way to analyze angular distributions without requiring detailed knowledge of the interaction dynamics.

<!--
Cosine simularity: 0.8843247666963694
-->
## Spin Quantization and Decay Rotation in Particle Physics

The Wigner D-function is given by:  

```math  
D_{m'm}(\theta, \theta, \varphi) = e^{-i m' \varphi} d^J_{m'm}(\theta) e^{-i m \varphi}  
```  

Here, $`H`$ refers to a particle $`\lambda_X`$ (number three), which decays into three particles: $`\lambda_X \lambda_3^0 \to 2`$. The other $`H`$ term involves $`X \to 1, 2`$ and $`G`$, where $`G`$ represents the rotation orientation of the decay.  

The first index in $`D`$ indicates which particle decays, while the second index specifies the decay products. The particles now have their spin defined in the frame where they are moving. The most natural way to quantize the spin is to align the quantization axis with the direction of motion. In this case, the $`\lambda`$ values correspond to helicity projections along the momentum $`P`$.  

For particle $`X`$, which carries spin projection $`\lambda_X`$, it decays into particles 1 and 2 at a certain angle relative to its direction of motion. To account for this angle, the quantization axis must be adjusted by rotating the spin vector of $`X`$ to align with the decay direction. This rotation is described by the decay rotation orientation $`G`$.  

> [!NOTE]  
> In aligned kinematics ($`\phi = 0`$, $`\theta = 0`$), the transformation simplifies because no rotation is needed. The Wigner $`D`$-function reduces significantly, eliminating the summation over $`\lambda_X`$.  

The rotation matrix for spin states can be expressed in terms of Euler angles as:  

```math  
R = R_z(\beta) R_y(\theta) R_z(\varphi)  
```  

If a particle has spin 0, its spin space is one-dimensional. The general amplitude involves sums over intermediate spins and functions of two variables.  

> [!IMPORTANT]  
> The rotational properties are fully determined by Wigner functions, while $`H`$ encodes the underlying dynamics (weak, strong, or electromagnetic interactions). For hard interactions, $`H`$ remains unknown due to the lack of a suitable parameterization.  

This framework systematically describes cascade decays, separating model-independent rotational symmetry effects from dynamics-dependent interaction terms.  

<!--
Cosine simularity: 0.9159372495877646
-->
## Angular Distribution and Delta Function Constraints in Particle Decays

We can significantly reduce the summation over helicity states ($`\lambda_X`$) here. Since $`X`$ is already moving along the $`Z`$-axis, no rotation is needed. The amplitude simplifies to:

```math
\sum_{\lambda_X, \lambda_3} D^{\lambda_X}_{0, \lambda_X - \lambda_3}(0) \cdot d^{\lambda_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta)
```

This introduces a delta function constraint $`\delta_{\lambda_0, \lambda_X - \lambda_3}`$, ensuring helicity conservation. The only non-rotated contribution occurs when the initial and final states match, constraining $`\lambda_X`$. The final expression becomes:

```math
H_0 \cdot D^{\lambda_X}_{\lambda_0 + \lambda_3, \lambda_3}(\theta) \cdot d^{\lambda_X}_{\lambda_0 + \lambda_3, \lambda_1 - \lambda_2}(\theta)
```

> [!NOTE]  
> The indices are determined by $`\lambda_X = \lambda_0 + \lambda_3`$ and the helicity difference $`\lambda_1 - \lambda_2`$.

To compute the angular distribution, we need input values for the helicity amplitudes $`H`$ (inside the "blobs"). These are $`(2j_1 + 1) \times (2j_2 + 1)`$ terms, which may depend on particle masses, such as $`m_X`$.  

In experimental analyses, we often approximate these amplitudes as constants initially. For example, we might assume $`H`$ is a constant $`C`$ or a particle-specific property. With this simplification, the angular distribution $`\frac{d\Gamma}{d\cos\theta}`$ becomes proportional to the squared matrix element.  

> [!IMPORTANT]  
> The cosine of the angle ($`\cos\theta`$) is preferred over $`\theta`$ itself because it avoids the Jacobian factor $`\sin\theta`$ in the differential distribution.  

The dynamics (encoded in $`H`$) are model-dependent, while the rotational properties are fully described by Wigner $`D`$-functions. For hard interactions (e.g., electromagnetic or gravitational), $`H`$ lacks a general parameterization and must be determined experimentally.  

The Wigner $`D`$-function for spin states is given by:  

```math  
D_{m'm}(\theta, \phi) = e^{-i m' \phi} d^J_{m'm}(\theta) e^{-i m \phi}  
```  

Here, $`H`$ represents the decay of particle $`X`$ (with helicity $`\lambda_X`$) into particles 1 and 2, with $`G`$ describing the decay orientation. The first index in $`D`$ specifies the decaying particle, while the second denotes the decay products.  

For spin quantization, the natural choice is to align the spin projection axis with the momentum direction ($`\vec{P}`$). If $`X`$ decays at an angle, its spin must be rotated to match the decay direction, described by $`G`$.  

> [!NOTE]  
> In aligned kinematics ($`\phi = 0`$, $`\theta = 0`$), the Wigner $`D`$-function reduces trivially, eliminating the need for summation over $`\lambda_X`$.  

The rotation matrix for spin states uses Euler angles:  

```math  
R = R_z(\beta) R_y(\theta) R_z(\phi)  
```  

For a spin-0 particle, the spin space is one-dimensional. The general amplitude involves sums over intermediate spins and depends on two variables.  

This framework separates rotational symmetry effects (model-independent) from interaction dynamics (encoded in $`H`$), providing a systematic description of cascade decays.

<!--
Cosine simularity: 0.9419263976443026
-->
## Quantum Transition Amplitudes and Spin Projections in Particle Decays

The matrix element is proportional to the matrix segment, and $`|M|^2`$ is fixed. The distribution changes from $-1$ to $1$ in $\cos\theta$, where $\theta$ is the angle. If the distribution is flat, it corresponds to one possibility. However, when dealing with particles with spin, you often observe a parabola (a second-order polynomial in $\cos\theta$) or other shapes.  

> [!NOTE]  
The amplitude $`A`$ represents the quantum transition amplitude, which is a probability amplitude. It is squared to give the observed probability. The quantity $`G`$ appears squared in experiments, as we only measure the squared value of the amplitude.  

For unpolarized decays, the distributions are averaged. You must square the amplitude and sum over the initial and final spin projections to obtain the observable distribution in experiments.  

The angular distribution $\frac{d\Gamma}{d\cos\theta}$ is proportional to the squared matrix element.  

> [!IMPORTANT]  
The cosine of the angle ($\cos\theta$) is preferred over $\theta$ itself because it avoids the Jacobian factor $\sin\theta$ in the differential distribution.  

The dynamics (encoded in $`H`$) are model-dependent, while the rotational properties are fully described by Wigner $`D`$-functions. For hard interactions (e.g., electromagnetic or gravitational), $`H`$ lacks a general parameterization and must be determined experimentally.  

The Wigner $`D`$-function for spin states is given by:  

```math  
D_{m'm}(\theta, \phi) = e^{-i m' \phi} d^J_{m'm}(\theta) e^{-i m \phi}  
```  

Here, $`H`$ represents the decay of particle $`X`$ (with helicity $\lambda_X$) into particles 1 and 2, with $`G`$ describing the decay orientation. The first index in $`D`$ specifies the decaying particle, while the second denotes the decay products.  

For spin quantization, the natural choice is to align the spin projection axis with the momentum direction ($\vec{P}$). If $`X`$ decays at an angle, its spin must be rotated to match the decay direction, described by $`G`$.  

> [!NOTE]  
In aligned kinematics ($\phi = 0$, $\theta = 0$), the Wigner $`D`$-function reduces trivially, eliminating the need for summation over $\lambda_X$.  

<!--
Cosine simularity: 0.9133527980701298
-->
## Partial Wave and Moment Analysis in Particle Decays  

In experiments, you observe angular distributions and wonder what they reveal. The first approach to analyze this is not to guess the amplitude directly, but to project these distributions onto orthogonal polynomials, which provide a convenient basis.  

The basis used here consists of Legendre polynomials, which are maximally informative for functions defined between $`-1`$ and $`1`$. Any angular distribution can be expanded in terms of these polynomials:  

```math  
f(\cos\theta) = \sum_{\ell} a_\ell P_\ell(\cos\theta)  
```  

Here, $`P_\ell(\cos\theta)`$ are the Legendre polynomials, and the coefficients $`a_\ell`$ are related to the spin of the produced particle. This method is called **partial wave analysis**. If you instead project the differential cross section onto these polynomials, it is referred to as **moment analysis**.  

> [!NOTE]  
Partial wave analysis models the cross section using amplitudes ( $`H`$ ) with free parameters, which are then adjusted to fit the data. However, the first step often involves projecting the angular distributions onto polynomials, which yields combinations of these parameters rather than their direct values.  

> [!IMPORTANT]  
This projection does not immediately reveal the underlying dynamics (encoded in $`H`$), but it provides constraints that can guide further analysis. The relationship between the polynomial coefficients and the physical amplitudes is non-trivial and requires careful interpretation.  

The Legendre polynomials are particularly useful because their coefficients reflect the spin structure of the decaying particle. For example, a flat distribution corresponds to spin-0, while a parabolic shape suggests spin-1 or higher.  

The Wigner $`D`$-functions describe the rotational properties of the decay, while the dynamics ( $`H`$ ) must be determined experimentally. For aligned kinematics ( $`\phi = 0`$, $`\theta = 0`$ ), the Wigner $`D`$-function simplifies significantly.

<!--
Cosine simularity: 0.9411182406125395
-->
## Helicity States and Particle Definitions in Martin Spearman's Book

The differences between the canonical state introduced earlier and the helicity state introduced later are not straightforward. We only briefly touched on how the state is defined in the rest frame, and we will explore this further.  

Martin Spearman's book *Elementary Particle Theory* provides the best coverage of this subject, particularly in Chapter 4. It starts from the Lorentz group, introduces vectors, and includes some group theory in a clear and accessible way without excessive detail.  

The book explains how particle definitions are constructed, offering insights into the relationship between helicity states and canonical states. The discussion is rooted in the Lorentz group framework, which is fundamental for understanding particle states in quantum field theory.  

> [!NOTE]  
Chapter 4 of *Elementary Particle Theory* by Martin Spearman is highly recommended for a deeper understanding of particle definitions and helicity states. The presentation avoids heavy mathematical formalism while maintaining rigor.  

<!--
Cosine simularity: 0.9374975962040448
-->
## Kinematics Exercise with Unlabeled Dalitz Plots

I left you an exercise involving Dalitz plots from Kleo and Babar where I removed the labels. The plots correspond to $`D`$ and $`D_s`$ decays, but the final-state particles are not specified. The axis labels remain, but the masses are hidden.  

The goal is to use kinematics to deduce the masses and identify the decays. Each group will analyze one plot and then exchange it for another.  

> [!NOTE]  
Martin Spearman's *Elementary Particle Theory* (Chapter 4) provides a clear framework for understanding particle definitions, including helicity states and canonical states, rooted in the Lorentz group. This is useful for interpreting kinematic distributions like Dalitz plots.

<!--
Cosine simularity: 0.7748775066838646
-->
## Homework and Lecture Attendance Reminders

I will give you one homework for your group, and then you can exchange it for another one, including the EP assignment. I have to leave now, but I can give you the homework from my office. Please come with me to collect it. Thanks for coming, and sorry for being slightly late.  

Your homework is due tomorrow at 8am in the same auditorium on the second floor. Be there at 8am sharp. I also need someone to handle the water supply—I usually take care of it, but if anyone else wants to volunteer, let me know.  

Mauritz, thanks for coming. For those who missed the CERN excursion, it was a lot of fun. We heard about your cheese obsession—apparently, it’s partly true. Everyone was obsessed, and we even discussed the rules for fondue. The 25th of May is the last day for fondue, so we were still within the legal limit.  

If you want to work on something before tomorrow, you still have time. However, none of you handed in the last homework. Was it too difficult, or did you just not attend the lectures?  

> [!IMPORTANT]  
> Check your emails on Moodle for homework links. Even if you don’t solve them, at least read and think about the problems.  

I was sick last week and couldn’t attend, but I hope you received my emails. It’s important to stay updated.  

Regarding the kinematics exercise with unlabeled Dalitz plots, the goal is to deduce the masses and identify the decays. Each group will analyze one plot and then exchange it for another.  

> [!NOTE]  
> Martin Spearman’s *Elementary Particle Theory* (Chapter 4) provides a framework for understanding particle definitions, including helicity and canonical states, which is useful for interpreting kinematic distributions like Dalitz plots.

<!--
Cosine simularity: 0.8512041258844096
-->
```
## Lecture Logistics and Online Resources

If you don’t handle the problems, just look and appreciate them. It’s important to attend the lectures, especially at the beginning, where we have a recap.  

These are typical problems from exercise sheet four—the last one we discussed. Today’s sheet is five, and the previous one (sheet four) included the triangle Dalitz plots.  

> [!NOTE]  
> Despite receiving exercise sheets during lectures, it’s useful to check them online for updates, as some links or corrections may be posted.  
```

<!--
Cosine simularity: 0.9151974298208496
-->
## Feasibility of Strong Interaction Studies in Lattice QCD

The examples shown so far involve weak interactions, but the question is whether similar studies can be done for strong interactions using Lattice QCD.  

Currently, Lattice QCD uses a different approach—it can handle isolated scattering of two particles but cannot yet compute densities. For instance, the decay of a $`D`$ meson or $`A_1`$ meson into three particles is not feasible on the lattice. This is because such processes involve ill-defined questions on the lattice, which primarily works with correlation functions.  

However, there is active development in this direction, particularly for three-body kinematics in Lattice QCD. This is a highly researched area, and progress is being made. For a master's thesis, exploring these topics could be valuable, though they may appear both complicated and conceptually simple at first glance.  

John Bulawa is a key researcher in this field and could provide guidance on potential thesis work. The methods and problems in Lattice QCD are evolving, making it an exciting area for new students to contribute.

<!--
Cosine simularity: 0.9268242129757556
-->
## Feasibility of Replicating Complex Probes in Experimental Physics  

Replicating complex probes appears complicated and rather simple at the same time. You probe all the points you have, but the implementation is likely very complicated.  

For a newcomer, it is feasible to make significant steps in that direction. Even at the master's level in experimental physics, a thesis could achieve this in about two months of work using experimental data. However, effort is required to ensure correctness and account for corrections due to effects.  

On the lattice, such a task would take years, but it would also be a milestone. The feasibility depends on the topic or direction chosen.  

> [!NOTE]  
> For lattice-based studies, the computational complexity is higher, but the results can serve as foundational benchmarks.  

The methods vary between experimental and lattice approaches, with the former offering faster but less rigorous results initially.

<!--
Cosine simularity: 0.9646342255719862
-->
## Scheduling and Logistics for Upcoming Meetings  

We can discuss the milestone later. A topic or direction will likely be chosen. We will speak with Professor Bilauer another time. We are meeting on Monday. The only points are if you wanted to give me a sheet or something.

<!--
Cosine simularity: 0.9277483614740625
-->
## Printing and Distribution Plans  

We are meeting on Monday. The only points are if you wanted to give me a sheet or something. I would love to print a few more and distribute them.

<!--
Cosine simularity: 0.9819736320521907
-->
## Lecture Context and Feedback  

Let's go. I would love to print a few more and distribute them. All offices are in EP1. I'm not quite sure if you got to where you wanted to get today. I think I missed the last two lectures, so I have a little lack of context. But I really enjoyed today. Nice, very nice.
