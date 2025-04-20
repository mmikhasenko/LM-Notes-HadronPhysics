# Lecture 01: Introduction to Hadron physics

## The Universe and Hadron Physics

The study of hadron physics is crucial for understanding the early universe. After the Big Bang, during the first microseconds, the universe was in a state of quark-gluon plasma (QGP) with temperatures exceeding
```math
T > 10^{12} K
```
As the universe cooled, quarks combined to form hadrons in a process called hadronization, marking a fundamental phase transition in the universe's history.

## Matter Composition

Let's consider Oxygen as an example of ordinary matter:
- Atomic structure: 8 protons, 8 neutrons (in most common isotope)
- Each nucleon (proton/neutron) consists of:
  - 3 valence quarks ($uud$ for proton, $udd$ for neutron)
  - Sea of virtual quark-antiquark pairs
  - Gluon field binding everything together

Mass composition of a proton:

```math
M_p = 938.27 \mathrm{ MeV} \gg 3 \times (m_u + m_d) \approx 15 \mathrm{ MeV}
```

This huge difference illustrates that most of the mass comes from binding energy!

## The Standard Model Lagrangian

The complete Standard Model Lagrangian can be written as:
```math
\mathcal{L}_{SM} = \mathcal{L}_{QCD} + \mathcal{L}_{EW} + \mathcal{L}_{Higgs}
```

## QCD Lagrangian in Detail

The QCD part of the Standard Model is described by:
```math
\mathcal{L}_{QCD} = -\frac{1}{4}G_{\mu\nu}^a G^{\mu\nu}_a + \sum_f \bar{\psi}_f(i\gamma^\mu D_\mu - m_f)\psi_f
```
where:
- $G_{\mu\nu}^a$ is the gluon field strength tensor
- $\psi_f$ represents quark fields of different flavors
- $D_\mu = \partial_\mu + ig_sT^aA_\mu^a$ is the covariant derivative

## Gauge Invariance in QCD

QCD exhibits SU(3) color gauge invariance. Under a local gauge transformation:
```math
\psi(x) \rightarrow U(x)\psi(x)
```
```math
A_\mu(x) \rightarrow U(x)A_\mu(x)U^\dagger(x) + \frac{i}{g_s}U(x)\partial_\mu U^\dagger(x)
```

This gauge invariance is fundamental to the theory and leads to:
- Conservation of color charge
- Self-interactions of gluons
- Asymptotic freedom
- Color confinement

