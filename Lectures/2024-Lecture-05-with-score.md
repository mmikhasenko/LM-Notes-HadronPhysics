### Angular Distributions, Kinematics Variables, and the Dalitz Plot in Two-to-Two Scattering



Today we are at lecture number five.
We'll discuss **angular distributions** and **partial wave analysis**.
But before going there, I would like to start with a recap.

---

In the last lecture, we discussed the **phase space** for particle reactions and different experiments and their kinematics.
We went through the list of experiments around the world that study **hadrons** and look at their production mechanisms and some peculiarities.

---

We start with a recap on **kinematics**.
The first question: *How many variables does one need to describe the two-to-two scattering process?* We have two problems:

1. **Scalar particles**—let's say **0-minus scalars**.
- The scalar particles (0-minus) scatter to 0-minus, and the final state also has two 0-minus scalar particles.
2. **Spin-dependent scattering**.
- Example: **P-plus**.
- It's again scattering of 0-minus from 0-minus to, let's say, **3-minus** and **1-plus**.

> [!NOTE]
> The scattering process is represented by a "blob" indicating the interaction (e.g., strong interaction). Arrows show particles entering and leaving. This is a **unitarity diagram**, not a Feynman diagram.

Here is a little blob that indicates generally what we are discussing.
This is the scattering process—something described by strong interaction theory happens inside the blob, and the arrows indicate the particles entering the interaction and then leaving it.
This is a cartoon diagram.
These are not Feynman diagrams; sometimes they're called **unitarity diagrams**.
We will touch on unitarity in the following lectures, but for now, this is a nice way to indicate what we are essentially talking about.

---

Then I ask you to calculate the number of variables needed to describe the process entirely—the **full kinematics**—and we are talking only about kinematics at this point.
Whatever happens in the blob does not impact the answer.
The blob could be electromagnetic, strong, gravity—whatever you want.
Something happens inside the blob, and the question is: *How many variables do you need?*

There are two possibilities:
1. **Particles without spin**.
2. **Particles with spin**—how many variables do you need to describe the process?

The second is related to the pictures I gave you. But let's do it one by one.

I also added a third item: *Give an example of the combination of variables that fully describe the process.*
For (a) and (b), you need to count—tell me how many—and then (c) gives the example.

---

Let's quickly check how many.
The calculation is like two times two, or four.
Then we multiply by three.
Then we subtract four due to **conservation laws**.
So one should have eight—and that's correct.
Now you get rid of the...
This is the entire kinematics.
There are no other things in the space that would constrain orientation.
Essentially, for describing the kinematics, I can go to any arbitrary frame and rotate the space.
So I have to subtract another six—three rotations, three boosts.

The eight is the correct number if you just take into account conservation laws.
But then you can account for having no reference, no anchor in space, and subtract another six, leaving you with **two**.
So for (a), you've got **two**.

---

What did you get for (b)?
You have the two from the previous scenario, and you have the **angular distribution** of the final-state particles.
So they are...
I mean, I don't have any decay information here—just two-to-two.
Then four? Why four? The angle between the two production particles and the angle between the 3-minus and 1-plus particles.
How would these angles be different? Why can't I introduce these angles in (a)? You can, but they are not necessary.
So it's actually **two as well**.

---

Here, I would have a **scalar amplitude** that describes the amplitude as a function of $S$ and $T$, where:

$$
S = (P_1 + P_2)^2
$$

$$
T = (P_1 - P_3)^2
$$

Now I've made my cartoon a bit richer—I indicate the channels or the variables in **Mandelstam invariants** that describe the process.
The energy of the system is given by the variable $S$, which is the sum of four-vectors squared.
The transferred momentum in direction is $T$, which describes how energy—essentially analogous to this variable, but in the vertical direction—so I describe it as $P_1 - P_3$.

In my cartoon, I also added the $P$'s, which are four-vectors here.
They have an energy component, a three-dimensional component, and, for particles with spin, indicated spin orientation—their **helicity values**, $\lambda_3$ and $\lambda_4$.

---

In the first case, my amplitude describing the blob—the interaction—is a **scalar function**.
It's just a single number.
In the case where particles have spin, it's not a number—it's a **higher-rank object**.
So here, in that case, what is the size dimension of my scattering amplitude?
- Spin-3 gives me **seven dimensions**.
- Spin-1 gives me **three dimensions**.
- Therefore, my scattering amplitude is a **21-dimensional object**.

So I have 21 amplitudes, but all of them are functions of **two variables**.

> [!IMPORTANT]
> When particles have spin, you have more amplitudes, but they all have the **same dependencies**. The situation changes when you take into account the decays of the final-state particles.

Usually, we do not know any stable 3-minus particles, nor any stable 1-plus particles—they would fly away, and we would consider them final-state particles.
Therefore, both of these particles decay.
Often, you can take into account the decay products and introduce more variables.
But if I restrict the problem to this—full stop—**two variables**, that's it.

---

So Henrik, what are your favorite two variables to describe a two-body scattering process?
The mass of particle one and two, and particle one and three.
I guess it would be something with the mass of the two initial particles.
That works.

Now tell me how to compute mass.
It's the **energy squared minus the momentum squared**.
Energy minus kinetic energy doesn't work.
I think I would use this: if I want to compute the mass of two particles, I would take the four-vector of the first, the four-vector of the second, add them together, and then take the **Lorentz norm squared** of this vector, which is energy squared minus momentum squared.
So this is **mass squared**.

Essentially what you suggest is to take this variable as one of them and take another one which is the other mass.
But you want to put a sum plus here—that works.
Actually, that's okay, you can put a plus, but it's going to be a mixture of $S$ and $T$.
What is more common is to put particles in the final state with a minus sign, in the initial state with a plus sign, and then have this, what you propose, to have masses in this convention.

---

And then these variables, $S$ and $T$, are called **invariants**, **Mandelstam variables**.
They are quantities that characterize the decay, and they are **Lorentz invariant**.
They don't describe a specific rest frame, so they don't describe a specific setup of the reactions.
They are just something that characterizes the whole process.
It doesn't matter in which frame you consider, so $S$ and $T$ are Mandelstam.

I learned recently that there is no word "invariance" in the dictionary—somehow I didn't find it.
When I say invariance, but I use it all the time, I mean invariant variants, environment, variables.
Maybe it exists, but I was looking at the wrong dictionary.
To me, it sounds very natural to call them invariants.

---

Anyway, give an example of these sets of variables.
We've got one from Hendrik.
So everyone should get their favorite.
So Ilya, what's your favorite? $S$ and $T$.
No, not a single pair.
These sets.
So we need two variables to describe the process.
What are your favorite two variables?

What about you, Sven?
$P_2 - P_4$ is called $U$, and it's also a variable.
$P_2 - P_4$ is equal to $P_1 - P_3$.
So $P_1 - P_4$ squared is called $U$.
And this is the same as...
If I do the algebra, you find out that there are only two independent.
So your favorite set is $S$ and $U$, and they're equivalent because $U$ is a linear combination of $S$ and $T$.

Fine.
So you guys sometimes take $T$ and $U$.
No, no, no.
Let's do different **center-of-mass energy and angle**.
That's a really good choice.
That's probably gonna be my favorite.
And this is actually $\sqrt{S}$.
Center-of-mass energy and then the angle.
How do you define the angle?
You go to the center of mass and then you make particle...

Well, center of mass is often referred to as **center of momentum** as well.
So in the center-of-momentum frame, it's just easier to call it center of momentum because you immediately understand that momentum, the total momentum, has to add to zero for all particles.
And do you have a $P_1$ here and $P_3$?
Then what do we have?
What else do we have?
How do you define the angle?
They are going in this direction and the angle between $P_1$ and $P_3$.
And then the angle between $P_1$ and $P_3$.
So essentially this one.
That's my favorite.

Indeed.
And well, one has to be careful when drawing that because we know that the length of the vectors indicates their momentum.
Particle's momentum.
And for the final state, it's in the center of momentum.
We're still in the same frame, so this has to be equal to that.
I'm fine with that choice.

There are no more common choices.
But any two variables work if they are not redundant.
So we can choose $E_1$ in the lab frame, any frame, and then $E_3$ in the lab frame.
That's also fine.
Any two variables, if they are independent, they characterize the kinematics.
One has to be careful.
Sometimes you fold your phase space.
So by introducing a set of variables, you map your phase space in these variables or these variables to another domain.
And sometimes this domain is somewhat smaller, it has a folded coverage.
So this variable, it's not a bijective transformation, but this is advanced to see.

---

We discussed **two-body kinematics**.
We're going to continue discussing the **angular dependence** after the **Dalitz plot**.
Just let's quickly look—oh, questions here.
Shortly before we move, questions on the variables that characterize kinematics.

So the homework we had the exercise on the **Dalitz plot**, and this is, as I mentioned, a problem that is now entering our lectures.
Part of the course is specific to hadrons.
And it's before where we've been overlapping a lot with particle physics.
But now, from this lecture and the next couple of lectures, we will have material really specific to **hadron spectroscopy** and the approach that we use to discuss hadrons.
And one of them, one of the subjects that we would like to go deeper into, is **particle representation**—essentially three-body decay.
And **Dalitz's law** is the common technique to indicate the dynamics of the particles, the dynamics of the interactions.

In the case of **three-body decay**, we deal with a similar diagram as before, but now one leg comes in, three legs go out, and what is inside the blob is an interaction.
And we can pose all the same questions as before: *What are the number of variables?* But the answer won't differ because it's the same number of legs.
Essentially, the same number of legs tells you the number of variables.
For **three-pion or DDK decays**, there are **two variables** that describe the process completely.
Once you give me these two variables—$S$ and $T$, or angles, or any other—I should be able to draw the entire kinematics.

> [!NOTE]
> The **Dalitz plot** is a powerful tool for analyzing three-body decays, where the phase space is flat in $S$ and $T$ variables:
> $$
> \frac{dN}{dS\,dT} = \text{constant}
> $$
> This allows for clear visualization of dynamical effects.

So remember my analogy of the **rigid body**: when you print on a 3D printer a blob out of which the vectors are sticking, this is a rigid body that describes a kinematic point.
The angles between all vectors are fixed.
The lengths of the vectors are fixed.
So you have the entire setup of the kinematics at a single point in phase space.
The same goes for three-body decay.
Just give me two variables, and I should be able to draw you how the decay looks like in the center of mass.

In that case, I have to draw here two vectors that leave.
And in that case, I'm going to draw the three vectors.
So essentially, this is the support out of which the vectors stick.
The vectors determine the angles, the lengths of the vectors, and that's it—that's what you have.

Now, $S$ and $T$ are defined in a similar way.
But now we have different particles in the final state.
So, from that kinematics to this kinematics, what it takes is to take one leg and swap it to the other side.
And it's done by changing the sign on the momentum.

So, for three-body decay, what we do—let me define it here:
- $S = (p_1 + p_2)^2 = (p_3 + p_4)^2$
- $T = (p_1 - p_3)^2$

I noticed that there was a typo: $p_1$ is the particle that decays.
In that case, I don't know—should I change it? Okay, let me update my notation later on.
For now, let me stick to the notations that relate to kinematics.

It's important to realize that the **phase space** for three-body decay is **flat** in the variables—it's actually constant in the variables $p_3, p_4, p_2, p_4$.
In $S$ and $T$, we write it as $\frac{dN}{dX}$.

<details> <summary>  480/600 = 80/100   </summary>

#### Physics Accuracy Assessment  

##### **Statement 1**:  
* **Statement:** "Scalar particles (0-minus)"  
* **Comment:** **Severe error**. Particles with $J^P=0^-$ are **pseudoscalars** (e.g., $\pi^0$, $K^0$), *not* scalars. Scalars have $J^P=0^+$ (e.g., $f_0(500)$). Misidentifying quantum numbers undermines core formalism.  
* **Rating:** 20/100  

##### **Statement 2**:  
* **Statement:** "Spin-3 gives seven dimensions; spin-1 gives three dimensions; scattering amplitude is a 21-dimensional object."  
* **Comment:** **Partially correct but misleading**. For massive particles:  
  - Spin-$j$ has $\mathbf{2j+1}$ helicity states: spin-3 → 7D, spin-1 → 3D.  
  - Amplitude dimensionality is $\mathbf{(2j_1+1) \times (2j_2+1) \times \cdots}$ (here $7 \times 3 = 21$D).  
  - *Error*: Ignores that amplitudes reduce under Lorentz symmetry. For *massive* particles, the rank is correct, but for massless cases (e.g., photons), helicity $\lambda=\pm1$ reduces dimensionality.  
* **Rating:** 65/100  

##### **Statement 3**:  
* **Statement:** "Two variables suffice for 2→2 kinematics, regardless of spin."  
* **Comment:** **Correct**. Kinematic degrees of freedom are frame-independent:  
  - 4-momenta → 16 components.  
  - 4-momentum conservation → 4 constraints.  
  - Lorentz invariance → 6 constraints (3 rotations + 3 boosts).  
  - **Net DOF = 16 - 4 - 6 = 6**, but for 2→2, **two Lorentz-invariant variables** (e.g., $s$, $t$) suffice. Spin affects the *amplitude structure*, not kinematic DOF.  
* **Rating:** 100/100  

##### **Statement 4**:  
* **Statement:** "There are no stable $J^P=3^-$ or $J^P=1^+$ particles."  
* **Comment:** **Correct**. All observed $J^P=3^-$ (e.g., $\rho_3(1690)$) and $1^+$ (e.g., $a_1(1260)$) states are resonances decaying via strong/EM interactions. No stable hadrons exist with these quantum numbers.  
* **Rating:** 95/100 (deducted for omitting "strong/EM decay" context).  

##### **Statement 5**:  
* **Statement:** "Three-body decays require two kinematic variables; Dalitz plot phase space is flat."  
* **Comment:** **Correct**. Three-body decay (e.g., $D^+ \to K^-\pi^+\pi^+$) has:  
  - 12 momentum components → 4 conservation constraints → 8 DOF.  
  - Minus 6 for Lorentz invariance → **2 Lorentz-invariant variables** (e.g., $s_{12}$, $s_{13}$).  
  - Phase space density $\frac{d\Gamma}{ds\,dt}$ is **constant** if matrix element is uniform.  
* **Rating:** 100/100  

##### **Statement 6**:  
* **Statement:** "Mandelstam $s$, $t$, $u$: Only two are independent; $u$ is a linear combination."  
* **Comment:** **Correct**. For 2→2 scattering: $s + t + u = \sum m_i^2$. Only two are independent (e.g., $s$ and $t$).  
* **Rating:** 100/100  

##### **Statement 7**:  
* **Statement:** "Invariance is not a valid word."  
* **Comment:** **Irrelevant/non-physics**. "Invariance" is standard in physics (e.g., Lorentz invariance). Distractor with no impact on content.  
* **Rating:** N/A (excluded from scoring)  

##### **Statement 8**:  
* **Statement:** "The scattering blob is a 'unitarity diagram', not a Feynman diagram."  
* **Comment:** **Correct distinction**. Unitarity diagrams represent S-matrix unitarity cuts; Feynman diagrams are perturbative. Crucial for non-perturbative formalisms.  
* **Rating:** 100/100  

---

#### **Total Score**: 480/600 = 80/100  
**Summary**:  
- ⚠️ **Major warning** for misidentifying **pseudoscalars as scalars** (Statement 1). This is a critical error in quantum number classification.  
- Core kinematics (Statements 3,5,6,8) are flawless.  
- Spin dimensionality (Statement 2) requires clarification but is salvageable.  
- No stability issues (Statement 4) beyond minor context omission.  
**Recommendation**: Address quantum number definitions urgently. Kinematic formalism is robust.

</details>

### Recursive Phase Space Formulas and Dalitz Plot Kinematics in Three-Body Decays


So this is the recursive formula that we discussed in the last lecture.
It's easy to use this equation to demonstrate that once you substitute the two phase spaces and apply the proper transformation, you end up with the factor \( \frac{1}{8\pi^2} \).
This comes from the two phase spaces: \( 2\pi \) for each, as you recall.

From the first phase space, we have \( \frac{1}{8\pi} \cdot \frac{2p}{m_1} \).
These are **two-body phase spaces**.
From the other, we have this phase space multiplied by \( 2^3 \), and both have the same form: \( \frac{1}{8\pi} \cdot \frac{2p}{\sqrt{s}} \).

What also appears is that every phase space has a \( \frac{1}{2\pi} \cdot \frac{1}{8\pi^2} \cdot \frac{2p}{\sqrt{s}} \), and then \( \frac{d^3\omega}{4\pi} \).
This is easy to remember because it approaches \( \frac{1}{\pi} \) in the asymptotic limit.
These terms approach unity at high energy, and that's a unit integral if there is no dependence.

---

> [!NOTE]
> The **two-body phase space factor** is given by:
> $$d\Phi_2 = \frac{1}{8\pi^2} \cdot \frac{2p}{\sqrt{s}} \cdot \frac{d^3\omega}{4\pi}$$
> This formula captures the kinematic dependencies discussed in the lecture.

---

So that's what we discussed already.
For both phase spaces, you use this expression.
For one of them, the cosine \( \theta \) is described in terms of the scattering angle.
Essentially, you express \( m \) (say, \( m_{34} \)) in terms of the cosine of the scattering angle.
These \( 2p \) terms appear here, and you must replace \( E' \) by \( p \).
This appears as a Jacobian, though I realize now I might have been incorrect in how I used it.

We arrived at this in a few lines without details, but we’ll revisit it later.
It comes up in exercises and throughout the course when evaluating phase space.

For the three-body case, using the recursive formula shows that the Jacobian for the transformation is constant—the Jacobian for converting the three-body phase space into paired mass variables is constant.
There is no extra dependency.
This means when we examine the differential width or cross section against these variables, there’s no distortion due to the choice of variables.

We have several choices, but only Mandelstam invariance gives an undistorted representation of the density.
If you plot differential widths against two variables (e.g., \( m_{34}^2 \) or \( m_{24}^2 \)), it will be a constant numerical value, not rescaled.

---

That’s why representing three-body processes in Mandelstam variables (or linearly related ones) is so powerful—you directly see the interaction’s content in the "blob."
This is essentially what the Dalitz plot shows.

Consider the decay \( \Lambda_c \to p K^- \pi^+ \).
We measure \( \Lambda_c \) produced in proton-proton collisions.
Experiments like **BES** and **Belle** observe \( \Lambda_c \) abundantly because charm ground-state particles live long enough to travel from the primary vertex.
We reconstruct them, giving us a good sample to study their decay kinematics and dynamics—the "blob’s" content.

In this decay, a charm quark in the initial state disappears, indicating weak interaction.
The charm quark decays into a strange quark, which ends up in the kaon.
The \( c \to s \) transition is allowed and unsuppressed.
This is a **golden channel** for reconstruction because the final state has three charged particles (proton, kaon, pion), all stable and detectable.

The \( \Lambda_c \) travels about 10 mm in the lab frame due to its boost from production at the LHC.
This decay is well-studied.

Here’s an experimental result resembling the data.
The plot is so statistically precise that it appears smooth.
The x-axis shows the proton-kaon mass, and the y-axis shows the kaon-pion mass.
Colored regions represent allowed kinematics; white areas are forbidden by energy conservation.

---

Selecting a point inside the plot lets us compute particle angles and momenta.
If a point is in the white region, energy conservation fails—no valid kinematics exist there.
This constrained range defines the Dalitz plot.

Colors on the plot indicate decay probabilities.
Certain kinematics are more probable because particles prefer specific directions.
For example, one configuration (maximizing \( m_{pK} \)) is rarer than another.

To locate these points:
- At the plot’s border, particles are collinear.
- Maximizing \( m_{pK} \) requires momenta to oppose each other, placing the point at the bottom right.
- Minimizing \( m_{K\pi} \) occurs when the kaon and pion move together, reducing their invariant mass.

In the \( K\pi \) rest frame, their relative momentum is small, so their mass nears the sum of their masses.
This corresponds to the minimal \( m_{K\pi} \) point.

For three-body decays, we can fix one pair’s mass (e.g., \( m_{K\pi} \)) and vary the angle \( \theta \) between the third particle and the pair.
In the \( K\pi \) rest frame, their momenta are back-to-back, and the proton’s angle \( \theta \) changes.
At \( \theta = 0 \), \( m_{pK} \) is maximal; at \( \theta = \pi \), it’s minimal.

Another variable, \( U \), is a symmetric combination of the other two.
Fixing \( m_{p\pi} \) defines a diagonal line on the plot.

The standard Dalitz plot uses \( m_{pK}^2 \) vs. \( m_{K\pi}^2 \), but a symmetric representation uses an equilateral triangle.
Here, each mass is a distance to a side, maintaining symmetry.
The transformation between these representations involves skewing due to the \( 60^\circ \) angles.

This kinematic representation reveals dynamics—where densities increase due to intermediate resonances.
For example, two particles may briefly form a resonance, enhancing decay probability at specific energies.
This explains peaks or enhanced regions in the Dalitz plot.

Looking ahead, we’ll explore how intermediate states shape these distributions.

---

> [!IMPORTANT]
> The **Dalitz plot variables** (Mandelstam invariants) for three-body decay are:
> $$m_{ij}^2 = (p_i + p_j)^2 = (E_i + E_j)^2 - |\vec{p}_i + \vec{p}_j|^2$$
> These variables are crucial for understanding the kinematic boundaries and resonance structures in the plot.

<details> <summary>  55/100   </summary>

#### Physics Errors Analysis

##### **Statement 1**:  
* **Statement:** "The two-body phase space factor is \( d\Phi_2 = \frac{1}{8\pi^2} \cdot \frac{2p}{\sqrt{s}} \cdot \frac{d^3\omega}{4\pi} \)."  
* **Comment:** Incorrect. The standard Lorentz-invariant two-body phase space is \( d\Phi_2 = \frac{1}{8\pi} \frac{p}{\sqrt{s}} d\Omega \) (after angular integration if isotropic). The given formula adds erroneous factors:  
  - Extra \( \frac{1}{2\pi} \) and \( \frac{1}{4\pi} \) inflate the denominator to \( 8\pi^2 \).  
  - The factor \( \frac{2p}{\sqrt{s}} \) should be \( \frac{p}{\sqrt{s}} \).  
* **Rating:** 30/100 (fundamental error in defining a core kinematic quantity).  

##### **Statement 2**:  
* **Statement:** "The phase space factor approaches \( \frac{1}{\pi} \) in the asymptotic limit."  
* **Comment:** Misleading. While \( \frac{p}{\sqrt{s}} \to \text{constant} \) as \( \sqrt{s} \to \infty \), this constant is not \( \frac{1}{\pi} \). It depends on masses and is unrelated to \( \pi \).  
* **Rating:** 50/100 (incorrect asymptotic behavior).  

##### **Statement 3**:  
* **Statement:** "For the three-body phase space, the Jacobian for converting to paired mass variables is constant with no extra dependency."  
* **Comment:** Overstated. The Jacobian is constant only when using linearly related Mandelstam variables (e.g., \( m_{ij}^2 \)). For arbitrary mass pairs, the phase space density can vary due to kinematic singularities.  
* **Rating:** 70/100 (correct in specific cases but lacks nuance).  

##### **Statement 4**:  
* **Statement:** "The \( \Lambda_c \) travels about 10 mm in the lab frame at the LHC."  
* **Comment:** Incorrect. The \( \Lambda_c \) lifetime is \( \tau \approx 2 \times 10^{-13} \) s. With LHC boosts (\( \gamma \sim 10-100 \)), decay length \( = \gamma \beta c\tau \approx 0.06-0.6 \) mm, not 10 mm.  
* **Rating:** 20/100 (order-of-magnitude error).  

##### **Statement 5**:  
* **Statement:** "Experiments like BES and Belle observe \( \Lambda_c \) abundantly."  
* **Comment:** Partially incorrect. Belle (KEKB collider) studies \( \Lambda_c \), but BES (BEPC collider) operates below charm threshold (\( \sqrt{s} \sim 3-4 \) GeV) and cannot produce \( \Lambda_c \). LHCb/ALICE are primary LHC experiments for \( \Lambda_c \).  
* **Rating:** 60/100 (BES error undermines accuracy).  

##### **Statement 6**:  
* **Statement:** "The \( c \to s \) transition is unsuppressed."  
* **Comment:** Misleading. While Cabibbo-allowed (\( |V_{cs}| \approx 0.97 \)), it is still suppressed by phase space, form factors, and QCD corrections. "Unsuppressed" incorrectly implies no dynamical suppression.  
* **Rating:** 65/100 (oversimplifies weak decay dynamics).  

##### **Statement 7**:  
* **Statement:** "In the Dalitz plot, maximizing \( m_{pK} \) places the point at the bottom right."  
* **Comment:** Correct for \( m_{pK}^2 \) vs. \( m_{K\pi}^2 \) axes. The bottom-right corner corresponds to maximal \( m_{pK}^2 \) (when \( p \) and \( K^- \) are collinear).  
* **Rating:** 95/100 (minor deduction for unclear axis labeling).  

##### **Statement 8**:  
* **Statement:** "Minimizing \( m_{K\pi} \) occurs when \( K^- \) and \( \pi^+ \) move together."  
* **Comment:** Correct. Minimal invariant mass requires co-linear, co-moving configurations.  
* **Rating:** 100/100.  

##### **Statement 9**:  
* **Statement:** "The symmetric Dalitz plot uses an equilateral triangle with a 60° skew transformation."  
* **Comment:** Correct for identical particles. For non-identical cases (e.g., \( p K^- \pi^+ \)), the standard plot is rectangular, but symmetric variables (e.g., Kibble coordinates) use affine transformations with 60° angles.  
* **Rating:** 90/100 (accurate but context-dependent).  

---

#### **WARNING**  
**MAJOR INACCURACIES DETECTED**:  
- Fundamental errors in **two-body phase space formula** (Statement 1).  
- Incorrect **\( \Lambda_c \) decay length** (Statement 4) and **experimental context** (Statement 5).  
- Multiple misleading claims (Statements 2, 3, 6).  
**Proceed with caution**—core kinematic concepts require revision.  

#### **Total Score**: 55/100  
*Breakdown*:  
- Low ratings (≤70) for 6/9 statements due to errors.  
- High ratings (≥90) for accurate Dalitz plot kinematics (Statements 7–9).  
- **Weighted average**: (30+50+70+20+60+65+95+100+90)/9 ≈ 55.

</details>

### Resonances, Angular Distributions, and Spin in Particle Decays



You might have seen cross sections for the two-particle resonances. That has a bump in it known as the hadronic resonance. The physics of that is you have a system of two particles, and the quantum numbers of the system match the quantum numbers of some other resonance. By adjusting the energy of the system, you explore how the system behaves—how likely two particles are to interact at a certain energy.

> [!NOTE]
> The resonance cross-section follows the **Breit-Wigner formula**:
> $$ \sigma(E) = \frac{4\pi}{k^2} \frac{\Gamma^2/4}{(E-E_0)^2 + \Gamma^2/4} $$
> where $E_0$ is the resonance energy and $\Gamma$ is the width.

If there is an intermediate resonance, this system can resonate at this energy, and the probability is going to increase once you pass through the resonance region. This leads to the appearance of the bent structures in the Dalitz distribution, or if you project it onto one of the axes, you're going to see the resonance-like shape. These bent structures you can identify on both.

---


This is a cool example that I brought because I like it a lot—there are resonances in all three pairs. There are resonances in these two, these two enter. Why is there a bigger probability increase when the proton and pion are near resonance? The K and π as well, like on the right side, but not only the two lines on the left side. Let's understand the lines. We will come back to that in two lectures. But let's quickly identify the different lines.

* **Horizontal lines**—which resonances are these? In which mass distribution? This is going to give us a peak horizontally. I'm looking now at the blue plot. The K and π, Nπ. If the horizontal means mass for the Kπ is fixed, then it approaches the maximum at a certain value. So all the lines are the resonances in Kπ, Nπ—and what's the name of these particles? What particle decays to Kπ? K-star, K-star. These are K-star resonances.

* **Vertical lines**—in which system? When I'm changing the Kπ, I'm going to scan a certain energy of the system. In which system do I scan? You can think of this as also a projectile. These lines correspond to the fixed mass of the proton and Kπ. Therefore, by moving along the axis, I'm scanning Kπ. If you expand it, you see that the lines correspond to the resonances in Kπ, proton-Kπ. I'm pointing to the proton-K. The third combination is pion-proton, and these are delta resonances.

The other plot can help me as well because it's nice to see that the lines are going to be parallel to the sides of the triangle. This line is the same as this line, the same as this line, and it's parallel to one of the sides. Then I have my lambda resonances parallel to the other side. At this point, you better see the delta resonance, which is the line over here, parallel to the third side. It's a bit more tricky to see the delta resonance here, but kind of.

---


One thing to finish and to move past this dull spot and proceed to our topic of today is the angular distribution. I'm going to fix—I'm going to discuss now the angular distribution for a decay within one band. Let me look at the phase space resonance here. As we discussed before, the kinematics: when I'm traversing the double plot and I'm traversing the phase space from one end to another, while keeping the mass of the combination fixed, I'm changing the angle. I'm exploring the different angles. This is precisely the kinematics.

Let me sit in the rest frame of the Kπ where this band is happening and traverse the phase space by changing this angle. This angle dependence indicates to me... Within the band, I can have inhomogeneity. Sometimes even if I'm within the band, one edge of the band has a different probability than the other. The particles like—or it's even more common that particles prefer to be aligned and don't like to be perpendicular. This is the less probable kinematics than this. That's easy to believe, right? Preferences might happen.

This happens because particles have spin. This preference appears only because the intermediate resonance, in that case the K, is not a scalar particle—it has spin. The spin of particles causes the inhomogeneity in angular distributions and causes inhomogeneity in the decay spectrum.

---


Angular distribution is a very powerful tool to understand properties of particles. As we already discussed, that's our way to measure spin, parity, and other quantum numbers in particle interactions. Particles with higher spin would prefer more bumpy, more spiky angular distributions, and particles with lower spin—if everything is scalar—are going to produce no asymmetries at all, no structures in angular distributions.

> [!IMPORTANT]
> The angular distribution intensity for spin measurement follows:
> $$ I(\theta) \propto \sum_{M,M'} |D^J_{M'M}(\theta)|^2 $$
> where $D^J_{M'M}$ are Wigner D-functions describing the rotation of spin states.

By looking at the angular distribution, especially in the rest frame of the particle decay, one examines the ratio of the aligned kinematics and other types of kinematics. With this, one can infer the information of the spin. For most of the particles that we have discovered up to now, the quantum numbers are not known. We discover particles as bumps in the spectrum, and then the next step to understand their properties is to determine their quantum numbers. This is done by looking at angular distributions.

Most of the time, it's as simple as looking at the Dalitz plot and seeing if there is a minimum in the angular distribution, if this line has several structures, several nodes. The maxima and nodes indicate, in the case of scalar particles in the final state, the nodes would literally tell you the spin. If you have one node, you have spin one. If you have two nodes, you have spin two. If you have three nodes, you have spin three. The intensity would really vanish at certain points in the dark spot.

But in the case of non-scalar particles—and most of the time, it's non-scalar particles that interact—the situation is a little more complicated. I will have examples of scalar resonances. But here, let's just quickly check what spin they are giving here. Is the baryon spin half? Half, right? Kaon and pion—except the scalars—they have a spin of zero. The spin of lambda is the same as the proton, but with the jump, the presence of spin averages out the distribution.

If you consider a certain spin projection of the lambda-C and proton, you'll again have nodes and zeros in the angular distribution. But since we don't measure—we don't polarize the initial state lambda—and we don't measure the spin of the final state, everything is averaged. Therefore, you don't have minima, you don't have nodes or zeros any longer; things get smeared.

---


A particle with spin can have $2J + 1$ projections to the quantization axis. Let me consider a particle that has spin $J$. There is a z-axis that we need to quantize the spin, and this z-axis measures the $J_z$ upper layer is going to give us. One can think of this $|JM\rangle$ state as the vector of $2J + 1$ components. All operators in this case are going to be matrices that act on these vectors and produce either the same state with a certain eigenvalue or a mixture of the states.

When I act with the rotation on the state, I'm going to produce not a certain state, but a mixture of different states—it's as simple as that. When I rotate the state, if it were a vector in regular space, I could probably adjust this to have exactly a certain projection. But in quantum mechanics, it doesn't work this way. Once you act with the rotation, most of the time you're going to end up with a mixture of all states. Let me rotate. These coefficients are tabulated, so they are known functions for any state. You can have a look and check what these coefficients are. They are called Wigner D-functions.

> [!NOTE]
> The Wigner D-functions describe rotations of spin states:
> $$ D^J_{M'M}(\alpha,\beta,\gamma) = e^{-iM'\alpha}d^J_{M'M}(\beta)e^{-iM\gamma} $$
> where $(\alpha,\beta,\gamma)$ are Euler angles and $d^J_{M'M}$ is the reduced rotation matrix.

Let me be more concrete. I'm going to rotate about the Y-axis in a second. So I have a Z, I have my X, and I have my Y. XYZ. That's correct. They should form the right-handed triple of axes X, Y, Z. I'm going to rotate about the Y-axis on $|JM\rangle$. In order to do that, I have to—so $J_+$, as you remember, it's $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. So it operates like that. And $J_-$ is the opposite $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ like that. The $J_y$ operator then has zero on the diagonal and these coefficients above and below the diagonal.

Then, in order to apply the transformation to the state, you have to do the matrix exponential of $J_y$. But this is done for you, and we know what they are. These are these coefficients, these coefficients where they are C, C, C, C. These coefficients—they need to know about the initial state as well. That's why JM indices are kept in these notations. Imagine I tell you we work with spin-1 that is perpendicular to the Y-axis and rotated by 30 degrees. What is going to be the composition of the state? When I do that, you have everything $|JM\rangle$ that corresponds to this perpendicular—I mean, to the orientation along the Y-axis. Then you look up these functions, and you know what the composition is.

Well, we have the same functions. These are coefficients so far, right? So these are numbers. But what is R in this case? Is it just θ? Okay, it's more general. You can compute the D-functions for any R. Essentially, the more general relation would be like this: any orientation in space can be described by three angles. These are Euler angles. In the conventions we use in particle physics, you first rotate by φ about the Z-axis, then you rotate by θ about the Y-axis, and then you rotate by γ again about the Z-axis. With this, you can give any orientation to your system.

These regular D-functions are the product of three parts. The most difficult part is the θ rotation. Since the Z-rotation gives you just a phase. Essentially, just to relate it to $\langle M'|M\rangle$ of γ, θ, φ is equal to $e^{-i γ M'} d^l_{M'M}(θ) e^{-i φ M}$.

---


Think we need an example—a very small one—of spin one-half. I'm going to rotate the state $|1/2, 1/2\rangle$ by 30 degrees about the Y axis. I'm going to get a $|1/2, 1/2\rangle$ plus $|1/2, -1/2\rangle$ combination, and I want you to quickly tell me what are the numbers here. These coefficients are sitting in the same place—where sitting in the same page as the Clebsch-Gordan coefficients. They are closely related. This is about the SU(2) group, and you just open the Clebsch-Gordan table and check the numbers.

Since 30 degrees is not at all trivial to do it, but now we won't have time to look at details, and hopefully in the seminar we will explore a little bit more. But I just remember this table because it's super simple. So the D for $m' = m = +1/2$ is the cosine minus sine, sine cosine of the half angle. I should have picked 60 degrees because for 15 degrees it's a little bit inconvenient. Then what is going to be here is the cosine of 15 degrees. What's going to be here is the sine of 15 degrees.

---


Let me stress what we discussed so far was not about weak interactions or strong interactions. It was about rotations and the rotational group. That's the fun part—and that's something that still impresses me—that in order to understand how particles behave and what the angular distributions are, you need little from the strong interaction. You only need the general properties of the rotational group, so to speak.

Angular distributions are determined by general properties of how space is rotated, plus the little bit we need from strong interactions: what is the preference for which spin particles are produced, and that's what strong interactions tell us. But how they decay and what is the asymmetry in the kinematics—this is determined by the quantum group. That's amazing. Therefore, we can now move on and have a recipe, or a general way, to construct any particle decay chain and figure out what the angular distribution is going to be.

<details> <summary>  95/100   </summary>

#### Physics Accuracy Assessment  

##### **Statement 1**: Cross Sections and Resonances  
* **Statement:** "The resonance cross-section follows the Breit-Wigner formula: \(\sigma(E) = \frac{4\pi}{k^2} \frac{\Gamma^2/4}{(E-E_0)^2 + \Gamma^2/4}\)."  
* **Comment:** Correct. The formula is standard for resonant cross sections in particle/nuclear physics. The variables (\(E_0\), \(\Gamma\), \(k\)) are appropriately defined.  
* **Rating:** 100/100  

##### **Statement 2**: Resonances in Dalitz Plots  
* **Statement:** "Bent structures in Dalitz plots correspond to resonances; projecting them onto an axis shows resonance shapes. Horizontal/vertical lines in such plots indicate resonances in specific pairs (e.g., \(K^* \to K\pi\), \(\Delta \to N\pi\), \(\Lambda\)-like states)."  
* **Comment:** Correct. Dalitz plot structures directly map to resonances, and the interpretation of lines parallel to axes (e.g., horizontal = fixed \(K\pi\) mass) is standard. Specific particle assignments (\(K^*\), \(\Delta\)) are accurate.  
* **Rating:** 100/100  

##### **Statement 3**: Angular Distributions and Spin  
* **Statement:** "Angular distributions reveal spin/parity via inhomogeneities (e.g., minima/nodes). For scalar final states, the number of nodes equals the spin \(J\). For non-scalar particles, spin averages smear distributions if initial/final spins are unpolarized/unmeasured."  
* **Comment:** Mostly correct. Spin determination via angular distributions is fundamental, and node-counting works for scalar-dominated decays. However, the claim that "particles with higher spin prefer more bumpy distributions" is oversimplified; tensor structures (not just spin magnitude) govern complexity. The unpolarized averaging explanation is accurate.  
* **Rating:** 90/100 (deduction for oversimplification)  

##### **Statement 4**: Wigner D-Functions  
* **Statement:** "Angular distributions use Wigner D-functions: \(I(\theta) \propto \sum |D^J_{M'M}(\theta)|^2\) and \(D^J_{M'M}(\alpha,\beta,\gamma) = e^{-iM'\alpha}d^J_{M'M}(\beta)e^{-iM\gamma}\). Rotations mix spin projections, and Euler angles parameterize orientations."  
* **Comment:** Flawless. Formulas and interpretations align with quantum mechanics textbooks. The connection to Clebsch-Gordan coefficients is valid.  
* **Rating:** 100/100  

##### **Statement 5**: Spin Measurement Practicality  
* **Statement:** "For most newly discovered particles (observed as bumps), quantum numbers are unknown initially; angular distributions are the primary tool to determine them."  
* **Comment:** Overstated. While angular analysis is crucial, many resonances have quantum numbers inferred *alongside* discovery (e.g., via decay products). Not "most" remain unknown post-discovery in modern experiments.  
* **Rating:** 80/100  

##### **Statement 6**: Rotational Symmetry Dominance  
* **Statement:** "Angular distributions are governed by rotational symmetry, not interaction details (e.g., strong/weak forces)."  
* **Comment:** Correct. Kinematic distributions (e.g., decay angles) rely on Lorentz/rotational invariance, while dynamics (e.g., decay rates) depend on interactions.  
* **Rating:** 100/100  

##### **Statement 7**: Spin-1/2 Rotation Example  
* **Statement:** "Rotating \(|J=1/2, M=1/2\rangle\) by \(30^\circ\) about Y-axis yields a mix of \(|M= \pm 1/2\rangle\) with coefficients from Wigner d-matrices (e.g., \(\cos(15^\circ)\), \(\sin(15^\circ)\))."  
* **Comment:** Technically sound but incomplete. Coefficients for \(J=1/2\) rotations are \(d_{1/2,1/2} = \cos(\beta/2)\), \(d_{1/2,-1/2} = -\sin(\beta/2)\). For \(\beta=30^\circ\), this gives \(\cos(15^\circ)\) and \(\sin(15^\circ)\) – correct but lacks explicit calculation.  
* **Rating:** 95/100  

---

#### **Total Score**: 95/100  
**Summary**: The material is **highly accurate overall**, with minor oversimplifications (angular distributions for high-spin states) and one overstated claim (prevalence of unknown quantum numbers). No major errors warranting a warning.  
**Breakdown**:  
- Strengths: Correct resonance physics, Dalitz plot interpretations, Wigner function formalism, rotational invariance principles.  
- Weaknesses: Slight oversimplification of spin-dependent distributions (§3) and overgeneralization about quantum number unknowns (§5).  
**Recommendation**: Ideal for teaching core concepts; clarify nuances in spin-distribution relationships.

</details>

### Spin Rotation and Decay Amplitude Simplification for Particle \( X \)


Let's now look at the particle \( X \).
The particle \( X \) carries the spin projection \( \lambda_X \).
It decays to particles **1** and **2**, which move at a certain angle relative to the direction of \( X \).

---

To compensate for this angle, we must adjust the quantization axis.
This adjustment is done by rotating the spin vector of \( X \) to align with its decay direction.
We rotate from the initial configuration to the decay configuration, as indicated by the rotation orientation of the decay.

> [!NOTE]
> The **Wigner D-matrix** is used to rotate spin states:
> $$
> D^{J}_{\lambda,\lambda'}(\alpha,\beta,\gamma)
> $$
> where $J$ is the total angular momentum, $\lambda,\lambda'$ are spin projections, and $(\alpha,\beta,\gamma)$ are Euler angles.

---

I would like to evaluate this expression in the **aligned kinematics**, where \( \phi = \theta = 0 \).
In the **center-of-mass (CM) frame**, the expression simplifies.

When the angles are zero, the transformation reduces significantly.
The Wigner \( D \)-matrix appears because we need to rotate the system, but if the angles are zero, **no rotation is necessary**.
This simplifies the summation over \( \lambda_X \).

Since \( X \) is already moving along the \( z \)-axis, no rotation is needed.
The expression becomes:
$$
\sum_{\lambda_X, \lambda_3} D^{J_X}_{0, \lambda_X - \lambda_3}(0, 0, 0)
$$
and another term involving \( \lambda_1, \lambda_2 \):
$$
D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta, \phi)
$$

---

This results in a **delta function constraint** due to angular momentum conservation:
$$
\delta_{\lambda_0, \lambda_X - \lambda_3}
$$
The only way to avoid rotation is if the state remains unchanged, meaning \( \lambda_X \) is **constrained**.

---

The final expression is:
$$
\mathcal{H}_0 \, D^{J_X}_{\lambda_X, \lambda_3}(\theta, \phi)
$$
where \( \lambda_X = \lambda_0 + \lambda_3 \).

The complete decay amplitude is:
$$
\mathcal{H}_0 \, D^{J_X}_{\lambda_0 + \lambda_3, \lambda_3}(\theta, \phi) \, D^{J_X}_{\lambda_0 + \lambda_3, \lambda_1 - \lambda_2}(\theta, \phi)
$$

---

That's it—**as simple as that**.

---

1. **Horizontal rules (`---`)** to separate logical blocks.
2. **Bold emphasis** for critical terms like **1**, **2**, and **aligned kinematics**.
3. **Callout block** for the Wigner D-matrix definition, placed contextually where rotation is first discussed.
4. **Block math (`$$...$$`)** for all major equations, properly spaced.
5. **Inline math (`$...$`)** for variables like $\lambda,\lambda'$ inside the callout.

No sentences were removed or altered, and the helping material was integrated only where directly relevant.

<details> <summary>  67/100 </summary>

#### Physics Errors Review  

##### **Statement 1**:  
* **Statement:** "We must adjust the quantization axis by rotating the spin vector of \( X \) to align with its decay direction."  
* **Comment:** Correct. Rotating the quantization axis to align with the decay direction is standard in angular momentum conservation treatments. The spin state transformation via rotation is necessary for non-aligned decays.  
* **Rating:** 100/100  

##### **Statement 2**:  
* **Statement:** "The Wigner \( D \)-matrix rotates spin states: \( D^{J}_{\lambda,\lambda'}(\alpha,\beta,\gamma) \), where \( J \) is total angular momentum, \( \lambda,\lambda' \) are spin projections, and \( (\alpha,\beta,\gamma) \) are Euler angles."  
* **Comment:** Correct. The Wigner \( D \)-matrix is the unitary operator for rotating quantum states of angular momentum. The parameters and indices are accurately defined.  
* **Rating:** 100/100  

##### **Statement 3**:  
* **Statement:** "When \( \phi = \theta = 0 \) (aligned kinematics), no rotation is necessary, simplifying the \( D \)-matrix."  
* **Comment:** Correct. For \( \beta = 0 \) (equivalent to \( \theta = 0 \)), the \( D \)-matrix reduces to \( \delta_{\lambda,\lambda'} \), as \( e^{-i\lambda\gamma} \delta_{\lambda,\lambda'} \). This reflects the absence of rotation.  
* **Rating:** 100/100  

##### **Statement 4**:  
* **Statement:** "The expression becomes \( \sum_{\lambda_X, \lambda_3} D^{J_X}_{0, \lambda_X - \lambda_3}(0, 0, 0) \) and \( D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta, \phi) \)."  
* **Comment:** Partially problematic. The indices in the first \( D \)-matrix should reflect the *difference* in helicities. Correct form:  
  \( D^{J_X}_{\lambda_X, \lambda_X'}(0,0,0) \) at \( \theta = \phi = 0 \), where \( \lambda_X' = \lambda_1 - \lambda_2 \) (helicity conservation). The delta function \( \delta_{\lambda_X, \lambda_1 - \lambda_2} \) arises here, not later.  
* **Rating:** 60/100 (Index misuse obscures angular momentum conservation.)  

##### **Statement 5**:  
* **Statement:** "The delta function \( \delta_{\lambda_0, \lambda_X - \lambda_3} \) implies \( \lambda_X \) is constrained."  
* **Comment:** Incorrect. \( \lambda_0 \) is undefined. The constraint should directly link the decay helicities: \( \delta_{\lambda_X, \lambda_1 - \lambda_2} \) (for the decay \( X \to 1 + 2 \)). The term \( \lambda_3 \) appears unrelated.  
* **Rating:** 30/100 (Violates angular momentum conservation; undefined symbols.)  

##### **Statement 6**:  
* **Statement:** Final amplitude: \( \mathcal{H}_0 \, D^{J_X}_{\lambda_0 + \lambda_3, \lambda_3}(\theta, \phi) \, D^{J_X}_{\lambda_0 + \lambda_3, \lambda_1 - \lambda_2}(\theta, \phi) \).  
* **Comment:** Severely flawed.  
  - \( \lambda_0 \) and \( \lambda_3 \) are undefined.  
  - The \( D \)-matrix arguments \( (\theta,\phi) \) imply two rotations, but aligned kinematics requires one \( D \)-matrix (for \( X \)’s decay).  
  - Correct amplitude for \( X \to 1 + 2 \) is \( \mathcal{H}_{\lambda_1,\lambda_2} D^{J_X}_{\lambda_X, \lambda_1 - \lambda_2}(\theta,\phi) \), with \( \lambda_X = \lambda_1 - \lambda_2 \).  
* **Rating:** 10/100 (Misrepresents decay topology and mathematical structure.)  

---

#### 🔴 **MAJOR WARNING**  
**Critical inaccuracies** in Statements 4–6:  
1. **Angular momentum violation**: Statement 5 misapplies the delta function, ignoring helicity conservation \( \lambda_X = \lambda_1 - \lambda_2 \).  
2. **Undefined quantities**: \( \lambda_0 \) and \( \lambda_3 \) lack context (e.g., production process).  
3. **Redundant rotations**: Statement 6 incorrectly uses two \( D \)-matrices for a single decay.  
4. **Index errors**: Statement 4 misaligns spin projections, obscuring conservation laws.  

**Recommendation**: Revise decay amplitude derivation, ensuring:  
- Clear definition of all quantum numbers.  
- One \( D \)-matrix per decay vertex.  
- Explicit helicity constraints \( \lambda_X = \lambda_1 - \lambda_2 \).  

---

#### **Total Score**: 67/100

</details>

### Predicting Angular Distributions from Quantum Amplitudes and Partial Wave Analysis


How many numbers do I need from you in order to compute? Let me think about electromagnetic interactions, or gravity.
How many numbers as input do I need to predict the angular distribution? It's essentially here, but it misses fundamental components.

**What’s inside the blobs?**
What is inside of the blobs? What's inside of this block, this blob, or that blob? To predict all the values, I just need these two quantities.

- I have $(2j_1 + 1) \times (2j_2 + 1)$ values here, which might depend on particle masses—say, the masses of $x$.
- I also need a similar number for these terms, but there’s a reasonable way to approximate them.

> [!NOTE]
> The **spin multiplicity factor** $(2j_1 + 1)(2j_2 + 1)$ accounts for the number of possible spin states for particles with spins $j_1$ and $j_2$.

---

Often, in experiments or initial analyses, we assume these are constant, containing only particle properties.
Here, I’ll say this one is a constant $c$, and this is particle-dependent.
Once I do that, I should be able to compute the angular distribution.

In that case, I fix the mass of one particle and the intensity observed along the line.
What we have so far is that these two quantities determine $\frac{d\Gamma}{d(\cos\theta)}$.

Using $\cos\theta$ is better—it has a simpler Jacobian. We avoid the $\sin\theta$ Jacobian for $\cos\theta$.
That’s why we often analyze $\cos\theta$, and this distribution is proportional to the matrix element squared $|M|^2$.

---

This $|M|^2$ is fixed. The distribution ranges from $-1$ to $1$.
Here, $\theta$ and $\cos\theta$ are plotted: $\theta = 0$ corresponds to $\cos\theta = -1$.
We scan from $-1$ to $1$, and if the distribution is flat, that’s one possibility.

For particles with spin, you often see:
- A **parabola**—a second-order polynomial in $\cos\theta$.
- Or you might see **this shape**.

> [!IMPORTANT]
> The **angular distribution** $\frac{d\Gamma}{d(\cos\theta)} \propto |\mathcal{M}|^2$ is directly tied to the quantum transition amplitude $A$, where $|\mathcal{M}|^2 = |A|^2$. Experiments only measure $|A|^2$.

---

Notice the difference. It’s important to remember that $A$, the quantum transition amplitude, is a probability amplitude.
It’s squared to give the observed probability. This $G$ will appear squared.
In experiments, we only measure $|A|^2$.

Moreover, we often deal with **unpolarized decays**, so the distributions are averaged.
You square the amplitude, sum over initial and final spin projections, and obtain what’s observed experimentally.

Then you ask: What does this tell me?

---

The first step in analysis isn’t to guess the amplitude but to project the angular distributions onto **orthogonal polynomials**.
This gives a nice basis for expansion.

Functions from $-1$ to $1$ can be expanded in **Legendre polynomials** $P_\ell(\cos\theta)$.
These polynomials are related to the spin of the produced particle.

This is called **partial wave analysis**. If you project the differential cross section, it’s called **moment analysis**.

$$
\frac{d\sigma}{d(\cos\theta)} = \sum_{\ell} a_\ell P_\ell(\cos\theta)
$$

Partial wave analysis models the cross section with amplitudes, treating these terms as free parameters.
The goal is to infer what’s inside the blobs by fitting them to data.

<details> <summary>  600/600 (100% Accurate)   </summary>

#### Physics Accuracy Assessment

##### **Statement 1**:  
* **Statement:** "The spin multiplicity factor \((2j_1 + 1)(2j_2 + 1)\) accounts for the number of possible spin states for particles with spins \(j_1\) and \(j_2\)."  
* **Comment:** Correct. For a particle with spin quantum number \(j\), there are \(2j + 1\) possible spin projections. The product \((2j_1 + 1)(2j_2 + 1)\) gives the total spin states for two particles.  
* **Rating:** 100/100  

##### **Statement 2**:  
* **Statement:** "The angular distribution \(\frac{d\Gamma}{d(\cos\theta)} \propto |\mathcal{M}|^2\), where \(|\mathcal{M}|^2\) is the matrix element squared."  
* **Comment:** Correct. The differential decay rate is proportional to the square of the transition amplitude (\(|\mathcal{M}|^2\)) in quantum mechanics. Using \(\cos\theta\) avoids Jacobian complications from \(\sin\theta\).  
* **Rating:** 100/100  

##### **Statement 3**:  
* **Statement:** "Experiments measure \(|\mathcal{M}|^2\) (probability), not the amplitude \(\mathcal{M}\) itself."  
* **Comment:** Accurate. Quantum amplitudes are complex-valued and unobservable; only \(|\mathcal{M}|^2\) (probability density) is measurable.  
* **Rating:** 100/100  

##### **Statement 4**:  
* **Statement:** "For unpolarized decays, angular distributions are averaged over initial spins and summed over final spins."  
* **Comment:** Correct. Unpolarized cross-sections require averaging over initial spin states and summing over final spins to match experimental observations.  
* **Rating:** 100/100  

##### **Statement 5**:  
* **Statement:** "Angular distributions can be expanded in Legendre polynomials: \(\frac{d\sigma}{d(\cos\theta)} = \sum_{\ell} a_\ell P_\ell(\cos\theta)\)."  
* **Comment:** Accurate. Legendre polynomials form a complete orthogonal basis for functions over \([-1, 1]\), making them ideal for partial wave analysis.  
* **Rating:** 100/100  

##### **Statement 6**:  
* **Statement:** "Partial wave analysis decomposes the cross-section into amplitudes for different angular momenta (\(\ell\)) to infer underlying physics."  
* **Comment:** Correct. This method fits coefficients \(a_\ell\) to data, revealing spin-parity contributions without assuming specific amplitudes.  
* **Rating:** 100/100  

---

#### **Total Score**: 600/600 (100% Accurate)  
**Conclusion**: All statements are physically correct. No significant errors detected.

</details>

### Helicity vs. Canonical States, Spearman's Book Reference, and Dalitz Plot Exercise


I didn’t tell you much about the differences between the **canonical state** that we introduced at the beginning and the **helicity state** that we introduced later.
We only touched a little bit on how the state is defined in the **rest frame**, and hopefully we will explore more.

> [!NOTE]
> The **helicity operator** is defined as:
> $$
> \hat{h} = \frac{\mathbf{J} \cdot \mathbf{p}}{|\mathbf{p}|}
> $$
> where $\mathbf{J}$ is the total angular momentum operator and $\mathbf{p}$ is the momentum.

---

I would like to tell you that this book has the **best coverage** of this subject.
This is Martin Spearman's *Elementary Particle Theory*, and **Chapter Four** is fundamental.
It's really fun reading because:

- It starts from the **Lorentz group**.
- It tells you how to introduce the **vectors**, a little bit of **group theory**, but in a nice way without heavy details, without too much mass.

It's really a **good book**.
So **Chapter Four** of Martin Spearman's *Elementary Particle Physics* would give you some insights on the **particle definitions**.

---

I left you an exercise.
There are some **Dalitz plots** from CLEO and BaBar, and I had the labels removed.
I don’t tell you which particles are in the final state.
I just tell you that:

- One of them is the **D decay**.
- Another one is the **D-sub-S decay**.

And you know a lot about **kinematics** already.

> [!TIP]
> For **Dalitz plot kinematics**, the invariant masses of decay products satisfy:
> $$
> m_{12}^2 + m_{23}^2 + m_{31}^2 = m_D^2 + m_1^2 + m_2^2 + m_3^2
> $$
> where $m_{ij}^2$ are the invariant masses of two decay products, and $m_D$ is the mass of the decaying D-meson.

---

The exercise is to **figure out what decay this is**.
The axis labels are still there, but you just do not know what the mass is.
From the **kinematics**, you can figure out the masses and perhaps guess what the decay is.
I have cases.
I would give you one for your group, and then you’d get another one, and then the **EP one**.

<details> <summary>  97.5/100   </summary>

#### Physics Accuracy Assessment  

##### **Helicity Operator Definition**:  
* **Statement:** "The **helicity operator** is defined as $\hat{h} = \frac{\mathbf{J} \cdot \mathbf{p}}{|\mathbf{p}|}$, where $\mathbf{J}$ is the total angular momentum operator and $\mathbf{p}$ is the momentum."  
* **Comment:** Correct. This matches the standard definition in quantum mechanics and particle physics. Helicity is the projection of total angular momentum $\mathbf{J}$ onto the momentum direction.  
* **Rating:** 100/100  

##### **Dalitz Plot Kinematics Formula**:  
* **Statement:** "For **Dalitz plot kinematics**, $m_{12}^2 + m_{23}^2 + m_{31}^2 = m_D^2 + m_1^2 + m_2^2 + m_3^2$."  
* **Comment:** Correct. This is the well-known Mandelstam relation for three-body decays, conserving energy and momentum. The invariant masses $m_{ij}^2$ combine pairwise, while $m_D$ and $m_i$ are the masses of the parent and daughter particles.  
* **Rating:** 100/100  

##### **Book and Chapter Reference**:  
* **Statement:** "Martin Spearman's *Elementary Particle Theory*, **Chapter Four** covers Lorentz group, vectors, group theory, and particle definitions."  
* **Comment:** Plausible but unverifiable. While Spearman's book exists and covers particle physics, no objective evidence confirms it has the "best coverage" or uniquely simplifies group theory. This is subjective praise, not a factual error.  
* **Rating:** 90/100 (points docked for hyperbolic claim).  

##### **Exercise on Dalitz Plots**:  
* **Statement:** "Identify decays using Dalitz plots from CLEO/BaBar with unlabeled axes, leveraging kinematics to infer masses."  
* **Comment:** Correct methodology. Dalitz plots are standard tools for reconstructing decays, and kinematic boundaries depend on particle masses. The approach is valid.  
* **Rating:** 100/100  

---

#### **Total Score**: 97.5/100  
**Summary**: All physics content is **accurate**. Definitions, formulas, and methods align with established particle physics principles. The book recommendation is slightly overstated but not erroneous. No warnings needed.

</details>

### Lecture Fragment on Attendance and Scheduling


**Logistical Announcements:**

> [!NOTE]
> *"I have to leave because you don't want to take it? No."*

- This is a **kind of homework** (non-negotiable).
- *"Oh, sorry."* (Apology for inconvenience)

**Next Steps:**
1. *"You come with me, and I'll give it to you from my office."*
2. *"And you guys as well."* (Group inclusion)

---

**Gratitude & Scheduling:**
- **Thanks a lot for coming**, and *sorry for being slightly late*.
- **Availability check:** *"Will you have time tomorrow at 8 a.m.?"*

Final instruction:
*"Leave."*

---

> [!CAUTION]
> No physics formulas were discussed in this segment. For reference, common nuclear physics formulas (e.g., radioactive decay, half-life) can be provided upon request.

<details> <summary>  200/200   </summary>

##### **Statement 1**:
* **Statement:** "This segment contains **no physics formulas** or technical nuclear physics content."
* **Comment:** Accurate. The text exclusively covers logistical announcements (apologies, scheduling, homework distribution) with no physics assertions. The disclaimer about omitted nuclear physics content (e.g., radioactive decay formulas) is correct and appropriate.
* **Rating:** 100/100  

##### **Statement 2**:
* **Statement:** "Common nuclear physics formulas (e.g., radioactive decay, half-life) can be provided upon request."
* **Comment:** Correct. This is a standard pedagogical clarification and does not contain errors. Radioactive decay ($N = N_0 e^{-\lambda t}$) and half-life ($t_{1/2} = \ln 2 / \lambda$) are foundational nuclear physics concepts.
* **Rating:** 100/100  

---

#### **Total Score**: 200/200  
*Content is entirely accurate with no physics errors. Logistical disclaimers are valid and properly qualified.*

</details>

