### Lecture Upload Plans and Transition to Logistics

::: callout-note
**Lecture Materials & Uploads**  
The lecture content will be uploaded, including items that are already prepared. References to additional material will also be provided.
:::
---

::: callout-tip
**Logistics Reminder**  
Let’s transition to logistical discussions in the final 15 minutes of the session.
:::
---

- **Uploads:** The lecture content and references will be shared.  


- **Logistics:** Administrative details will be addressed shortly.  

---

::: callout-note
**Supporting Context**  
While this segment focuses on logistics, nuclear physics formulas like those below may appear in technical sections of the lecture:  


- Nuclear binding energy: $E_b = (Zm_p + Nm_n - m_{nuc})c^2$  


- Semi-empirical mass formula: $E_B = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(A-2Z)^2}{A} + \delta(A,Z)$  


- Radioactive decay law: $N(t) = N_0 e^{-\lambda t}$
:::
---

- **Clarity:** Separating logistical announcements from technical content improves readability.  


- **Preparation:** References and uploads ensure access to critical materials.

### The Evolution of the Universe: From Electroweak Epoch to QCD and Hadron Formation

**Right.**  
We are living in a universe made of **hardened physics**, but it was not always the case. Essentially, I like thinking of the evolution of the universe on a timescale. Here is the origin of the universe where everything started. There was a **Big Bang** first, and then several epochs followed. It started with the **Planck epoch**, then there was the **electroweak epoch**, **quarks**, and others. What has been happening during this is part of the physics that we also go through in the courses.

---

::: callout-important
**Higgs Mechanism and Symmetry Breaking**  
The Higgs potential—the field giving mass to particles and ensuring protons don’t decay so life can exist—obtains a condensate during the electroweak epoch. The potential is given by:  
$$  
V(\phi) = \mu^2 |\phi|^2 + \lambda |\phi|^4  
$$  
where $\phi$ is the Higgs field, $\mu^2 < 0$ triggers symmetry breaking, and $\lambda$ is the self-coupling constant.
:::
Essentially, let me start with the **electroweak epoch**, where the Higgs potential forms a condensate. The field that drives electroweak physics fills the entire space, creating a condensate of the Higgs field. Through this condensate, particles are slowed down, gain inertia, and obtain mass—this is the **Higgs mechanism**. The process of the potential evolving is called **spontaneous symmetry breaking**, where one of the minima is peaked. That’s how I like thinking about the electroweak stage.

---

Then, particles have masses, the universe starts evolving, and at some point, we arrive at the **quark epoch**, where the universe is filled with a **quark-gluon plasma**. Essentially, quarks and gluons make an unstructured soup of objects—quarks, gluons, and more. There is nothing about **structure formation** yet; it’s just quarks disturbing. There is no scale to discuss yet. Quarks and gluons are together, and the universe is extremely hot. From that moment, it starts cooling down. At some point, the temperature is low enough that this medium starts separating, and we arrive at the **quantum chromodynamics (QCD) epoch**.

---

::: callout-note
**Nuclear Size Scaling**  
The radius $R$ of a nucleus scales with the number of nucleons $A$ as:  
$$  
R \approx r_0 A^{1/3}  
$$  
where $r_0 \approx 1.2 \, \text{fm}$ (Fermi).
:::
This medium starts forming small volumes where quark and gluon interactions bind to a scalable level. If you think of this, you’d need two years to learn it in detail. This comes in particle physics, introductory nuclear physics, and specialized courses on **QCD** or **statistical mechanics**. You could have a special course on QCD at finite temperature, since it’s a heated medium with different laws applied to what we’ll discuss for strong interactions.

---

**Hydrogen** is what we’ll focus on now. But if you think of how quickly this happened, you’ll be slightly surprised. Essentially, this is... do you have a guess? $10^{-36}$ seconds (Planck), $10^{-12}$ (electroweak), $10^{-6}$, then $10^{-3}$, and finally **1 second**. Imagine there was nothing, and then the time it takes for sound to reach you when I clap—about 10 milliseconds—by that time, we’d already passed through all these stages and everything had formed. That’s how quickly the universe evolved.

---

The rest of the timeline to the present **13.8 billion years** has other interesting physics, but not as intense from the perspective of **hadron physics**. Hadrons are objects where strong interactions are confined to a scale of a few femtometers ($10^{-15} \, \text{m}$). There’s essentially nothing around—just small chunks of volume where quarks and gluons interact. By colliding hadrons, we study their internal structure, but there’s no natural scale smaller than this.

---

::: callout-tip
**Proton Mass Decomposition**  
The proton mass $m_p$ is dominated by QCD energy (gluon condensate):  
$$  
m_p \approx 938 \, \text{MeV}, \quad \text{with} \quad m_{\text{quarks}} \sim 9 \, \text{MeV} \quad (\text{only} \sim 1\%)  
$$  
The remainder arises from strong interaction energy.
:::
Concerning **empty space**, let’s sketch one of the most common elements on Earth. From the periodic table, what is it? **Oxygen**. Oxygen-16 (or 18) has 8 protons and 8 (or 10) neutrons. The geometry of this atom is a core of protons and neutrons, with electrons compensating the charge. The nucleus scales as the number of nucleons to the power of $1/3$ (volume scaling). Packing 16 nucleons gives a radius of about **3 fm**. Electrons, however, have wave functions **3 orders of magnitude larger** (~50 picometers). This shows how empty space is—a tiny core surrounded by vast electron space with no strong interactions.

---

Now, the **fundamental hardware**: the **Standard Model** describes most known interactions (excluding neutrinos’ open questions). The part responsible for strong interactions is **quantum chromodynamics (QCD)**. The participants are **quarks** and **gluons**, the only particles carrying **color charge**—similar to electric charge but distinct. Color charge is a quantum number; we describe it via color wave functions.

---

::: callout-important
**QCD and QED Lagrangians**  
The Lagrangian density for QCD is:  
$$  
\mathcal{L}_{\text{QCD}} = \bar{\psi}_i (i \gamma^\mu D_\mu - m) \psi_i - \frac{1}{4} G^a_{\mu\nu} G_a^{\mu\nu}  
$$  
where $D_\mu = \partial_\mu - i g_s A_\mu^a T^a$ and $G^a_{\mu\nu}$ is the gluon field strength.  
For QED:  
$$  
\mathcal{L}_{\text{QED}} = \bar{\psi} (i \gamma^\mu D_\mu - m) \psi - \frac{1}{4} F_{\mu\nu} F^{\mu\nu}  
$$  
where $D_\mu = \partial_\mu - i e A_\mu$.
:::
Other Standard Model particles (**electrons, muons, taus, photons, neutrinos**) don’t carry color charge and don’t interact strongly. Quarks come in six types: **up** (charge $+2/3$), **down** ($-1/3$), **charm**, **strange**, **top**, **bottom**. They’re grouped by generation (**light: u/d; heavier: s/c; heaviest: t/b**). Most matter is made of first-generation quarks. Strange quarks may affect neutron star equations of state. Charm and bottom are studied in high-energy collisions; the top quark’s lifetime is too short for hadronization.

---

**Hadrons** are classified as **mesons** (quark-antiquark) or **baryons** (three quarks). At the **chiral symmetry breaking scale**, gluons condense, dressing quarks and giving them effective mass. The proton’s mass is ~1 GeV, but the Higgs contributes only ~1% (3 MeV per quark); **99% comes from QCD energy** (gluon condensate).

---

::: callout-note
**Natural Units Conversion**  
In natural units ($\hbar = c = 1$):  
$$  
1 \, \text{GeV}^{-1} \approx 0.197 \, \text{fm}, \quad 1 \, \text{GeV} \approx 1.783 \times 10^{-27} \, \text{kg}  
$$  
Relating energy, mass, and length scales.
:::
Now, **quantum chromodynamics (QCD)** and **quantum electrodynamics (QED)** share a Lagrangian framework. QED’s Lagrangian is:  
$$  
\mathcal{L}_{\text{QED}} = \bar{\psi} (i \gamma^\mu D_\mu - m) \psi - \frac{1}{4} F_{\mu\nu} F^{\mu\nu},  
$$  
where $D_\mu = \partial_\mu - i e A_\mu$. Maxwell’s equations in covariant form are $\partial_\mu F^{\mu\nu} = j^\nu$. QCD’s Lagrangian adds color charge:  
$$  
\mathcal{L}_{\text{QCD}} = \bar{\psi}_i (i \gamma^\mu D_\mu - m) \psi_i - \frac{1}{4} G^a_{\mu\nu} G_a^{\mu\nu},  
$$  
with $D_\mu = \partial_\mu - i g_s A_\mu^a T^a$ and $G^a_{\mu\nu}$ as the gluon field strength.

**Natural units** ($\hbar = c = 1$) simplify conversions: $1 \, \text{GeV}^{-1} \approx 0.197 \, \text{fm}$; $1 \, \text{GeV} \approx 1.78 \times 10^{-27} \, \text{kg}$.

### Einstein Notation, Gauge Invariance, and Fermion Interactions in Field Theory

Another thing to note is that here I am explicitly using **Einstein notation** and summing over repeated indices.  


- $\mu$ here, $\mu$ there—they are repeated.  


- This means that if I were precise, I should have written here a sum from $\mu=1$ to $4$ over all components.  


- The $\nu$ is a repeated index again, so we sum.  

::: callout-note
**Summation Example**: For $F_{\mu\nu}F^{\mu\nu}$, expanding the sum yields $4 \times 4 = 16$ terms (4 components per index). If multiplied by another term with 4 components, the total becomes $16 \times 4 = 64$ terms.
:::
---

The equation of motion for this Lagrangian is obtained using the **Euler-Lagrange equation**.  


- You might remember this from classical mechanics where we had dots, and the first term was the time derivative, the second was the derivative of the field.  


- Essentially, we treat the Lagrangian as a function of the field derivatives and the fields themselves as independent objects.  


- First, we differentiate with respect to the derivatives, and then with respect to the fields.  

::: callout-important
**Key Insight**: In classical mechanics, these would be the momentum terms, but here they are **field variables**. The index $\mu$ is summed over—a simple summation.
:::
The derivative is with respect to $A_\rho$ (another index convention). If I take this Lagrangian, where everything is defined, and use the Euler-Lagrange equation, I get the equation of motion describing how the field propagates through space. We know this gives **Maxwell's equations**.  

---

Now let me introduce the second part. This was the gauge field. Let me label it 1, 2, 3, 4.  


- This is a less intuitive concept that you might not have seen before, but we will need it.  


- There are degrees of freedom that are not fixed for photons in the electromagnetic field, and there is an arbitrary **gauge choice** we can make.  

::: callout-tip
**Gauge Transformation**:  
$$  
A_\mu \rightarrow A'_\mu = A_\mu - \partial_\mu \chi  
$$  
where $\chi$ is an arbitrary scalar field. Under this, $F_{\mu\nu}$ remains invariant: $F'_{\mu\nu} = F_{\mu\nu}$.
:::
This is a **symmetry of the Lagrangian**—the gauge symmetry. If you derive Maxwell's equations from the Lagrangian, you’ll get them up to a gauge term. By fixing the gauge, you recover the standard Maxwell equations.  

---

Now we introduce **fermion fields**.  


- In electrodynamics, our leptons are described by the **Dirac field** $\psi$, a four-component spinor (not a four-vector).  


- The Lagrangian is a scalar quantity—no free indices—and is constructed from objects of different dimensionality.  

::: callout-note
**Spinor Properties**:  


- $\psi$ describes spin-$1/2$ particles with four components (particle + antiparticle).  


- The adjoint spinor is $\bar{\psi} = \psi^\dagger \gamma^0$.  


- The Dirac Lagrangian:  
$$  
\mathcal{L}_{\text{Dirac}} = \bar{\psi} (i \gamma^\mu \partial_\mu - m) \psi  
$$
:::
The equation of motion is the **Dirac equation**: $(i\not{\partial} - m)\psi = 0$ (using Feynman slash notation).  

---

To introduce **interactions**, we use **gauge invariance**.  


- For fermions, gauge invariance means changing the phase of $\psi$ locally at every space-time point.  


- The tricky part is that $\partial_\mu \psi$ introduces extra terms under a space-dependent phase transformation.  

::: callout-important
**Covariant Derivative Fix**:  
Replace $\partial_\mu$ with $D_\mu = \partial_\mu + ieA_\mu$. Under simultaneous transformations of $\psi$ and $A_\mu$, the Lagrangian remains invariant.
:::
This is the essence of **QED**: interactions arise from requiring invariance under local phase transformations.  

---

The same principle applies to other gauge theories (e.g., SU(2) for electroweak, SU(3) for QCD).  

::: callout-warning
**Key Difference in QCD**:  


- Gluons self-interact due to non-Abelian structure (terms like $f^{abc}$ in $G^a_{\mu\nu}$).  


- Coupling runs with energy: **asymptotic freedom** (weak at high energy) vs. **confinement** (strong at low energy).
:::
---

Finally, in **perturbation theory**, we compute scattering amplitudes using Feynman diagrams.  

::: callout-note
**Cross-Section and Decay Width**:  


- Cross-section:  
$$  
\sigma = \frac{1}{2E_A 2E_B |v_A - v_B|} \int |\mathcal{M}|^2 \, d\Pi_{\text{phase space}}  
$$  


- Decay width:  
$$  
\Gamma = \frac{1}{2m} \int |\mathcal{M}|^2 \, d\Pi_{\text{phase space}}  
$$
:::
These connect field theory to measurable quantities in experiments.

### Course Logistics, Exam Details, and Summer School Opportunities

::: callout-note
**Lecture & Exercise Schedule**  
It's really nice to have a watch today. We are three minutes out, but let me quickly say logistics for the course.  


- I have notes: **11 lectures and 11 exercises**.  


- *A bit fewer exercises* because we will have some breaks.  


- For **Moodle**, we put a calendar listing anticipated dates for lectures and exercises.  


- Closer to the dates, you may discuss shifting exercise sessions to other days, but for now, we keep the schedule as it is and we'll discuss later.
:::
---

::: callout-important
**Admission & Format**  
For the exam, we would like to offer during the semester that we will check the points you gain through exercise sheets, and then **50% will admit you to the examination**.  


- The exam is designed to be **easy**: you’ll receive problem sets in advance (e.g., 1–2 weeks before).  


- You’ll bring your solutions to the exam, and we’ll have a discussion.  


- **Focus**: Working on exercise sheets during the semester is *most important*.
:::
---

::: callout-tip
**How to Submit & Receive Feedback**  
Now, let me show you these beautiful exercise sheets.  


- Each sheet has a **barcode to scan** and classwork (optional for now).  


- **Homework**: 1–2 problems per assignment.  


- **Submission**: Write solutions, hand them in at the lecture, and retrieve marked sheets during Thursday exercise sessions.  


- A **box** will be provided for submissions (include your name!).
:::
---

::: callout-note
**Key Timings**  


- **Lectures**: Tuesday  


- **Exercise Sessions**: Thursday  


- **Excursion**: Fully booked, but 1–2 spots may open.  


- **Office Hours**: Thursday, 9–10 AM (Office 13B, Building B).
:::
---

::: callout-tip
**Apply Soon!**  
For our field, several **summer schools** are happening this summer:  


1. **Zurich, Switzerland**: 8 weeks  


2. **Krakow, Poland**: 4 weeks  


3. **Bochum**: 2 weeks (for advanced students)  


- Applications are open for a few more weeks.
:::
::: callout-caution
**Course Description Access**  
For the course description... Well, in order to proceed, just write an email, and I can forward you the announcement. I think I sent it to *Fast Shaft*, but I’m not sure it was propagated. These are **super exciting events** if you want to know more.
:::
---  

::: callout-note
*No physics formulas were discussed in this segment. The focus was on administrative and organizational details.*
:::
### Collaborative Problem-Solving, Resource Use, and Course Logistics

::: callout-tip
**Collaboration is encouraged!** Feel free to discuss and solve the sheets together. Use any resources you find helpful—ChatGPT, books, or other materials. The problems are **standard** and designed for learning, not assessment. How you learn is up to you.
:::
---

The lecturer follows several key texts:  


1. **Hudson Martin** (first reference)  


2. **Martin Schemer**  


3. **Thomson's Particle Physics** (general particle physics)  


4. **Martin Spearman** (dedicated to Hadron Physics)  

---

::: callout-note


- Exercise groups start this week with **three class problems**.  


- **Sheets distribution**: Two pages per sheet, 15 printed. Take one for yourself and extras for friends.  


- *"Before leaving, please take the sheets. We should stamp them together, but make sure you don’t miss one."*  


- *"Do you have a quarter of the sheet? Leave me this quarter before leaving."*
:::
---

::: callout-important
**System description**:  


- A **spark**, a **balloon**, and a **pendulum** with a sliding hanging point.  


- **Lagrangian**: Kinetic term minus potential term ($\mathcal{L} = T - V$).  
  - $\dot{X}^2$ term for the moving part.  
  - Pendulum interaction and potential energy terms.  


- **Goal**: Derive the **Dirac equation** and **Maxwell's equations**.  
*"This is a fun problem—I just dropped it on this table."*
:::
---

::: callout-note


- *"Thank everyone who came today. Hope we survive to the end of the semester!"*  


- Exercises are **not obligatory**, but *"everyone has to do the work."*  


- *"You’re gonna have troubles to get people to the board because this is not private."*
:::
---

::: callout-tip
**Upcoming focus**:  


- Reintroducing the **QED Lagrangian**:  
  $$\mathcal{L}_{QED} = \bar{\psi}(i\gamma^\mu D_\mu - m)\psi - \frac{1}{4}F_{\mu\nu}F^{\mu\nu}$$  
  Where $D_\mu = \partial_\mu + ieA_\mu$ (covariant derivative).  


- Comparing **QED** (electromagnetic interactions) and **QCD** (added complexity).  
*"Starting with a simpler case and explaining how to calculate terms is a good starting point."*
:::
---

::: callout-caution


- Only **four students** from the department are enrolled.  


- *"I don’t like the whiteboard in the office—it’s too small. You get used to it."*  


- *"No, you can stay there. That’s still not a big... I think we go right."*
:::
---

::: callout-important


- Lecturer’s reflection: *"I’ve done this exercise for QED and wonder if people grasp the complications QCD brings."*  


- **Key takeaway**: QED explains most electromagnetic interactions, while QCD introduces **non-abelian gauge symmetry** challenges.
:::
---

*"I rushed at the beginning and end, so you’ll have to explain stuff. We’ll calculate something for QED if time permits."*  
