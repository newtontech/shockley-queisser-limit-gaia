#!/usr/bin/env python3
"""
Shockley-Queisser Limit Formalization in Gaia Lang

Based on: Shockley, W. and Queisser, H.J. (1961) "Detailed Balance Limit
of Efficiency of p-n Junction Solar Cells", Journal of Applied Physics,
Vol. 32, pp. 510-519
"""

from gaia import *

# ============================================================================
# SETTINGS - Background Context (no probability)
# ============================================================================

# Basic physical context
setting(
    content="The Sun can be approximated as a 6000K blackbody radiator"
)

setting(
    content="Solar cell performance depends on three key parameters: open-circuit voltage (Voc), short-circuit current (Jsc), and fill factor (FF)"
)

setting(
    content="Conversion efficiency η = (Voc × Jsc × FF) / P_in, where P_in is incident solar power"
)

setting(
    content="Detailed balance principle: in thermal equilibrium, absorption rate equals emission rate for each transition"
)

setting(
    content="Bandgap energy (Eg) is a fundamental material parameter determining which photons can be absorbed"
)

# ============================================================================
# CLAIMS - Scientific Assertions (with probability)
# ============================================================================

# Core principle claims
claim(
    content="Photons with energy E < Eg cannot be absorbed (transparency)",
    title="Photon Transparency Condition",
    background="Bandgap theory",
    parameters={"Eg": "bandgap energy", "E": "photon energy"},
    provenance="Shockley & Queisser 1961, Eq. 1"
)

claim(
    content="Each photon with energy E > Eg generates exactly one electron-hole pair",
    title="Quantum Efficiency Unity",
    background="Ideal p-n junction assumption",
    parameters={"quantum_efficiency": 1.0},
    provenance="Shockley & Queisser 1961, Section II"
)

claim(
    content="The only unavoidable recombination mechanism is radiative recombination",
    title="Radiative Recombination Dominance",
    background="Non-radiative losses are theoretically avoidable",
    parameters={"dominant_mechanism": "radiative"},
    provenance="Shockley & Queisser 1961, Section I"
)

claim(
    content="Radiative recombination rate equals absorption rate in thermal equilibrium",
    title="Detailed Balance Equilibrium",
    background="Principle of detailed balance",
    parameters={"equilibrium_condition": "absorption = emission"},
    provenance="Shockley & Queisser 1961, Eq. 3"
)

# Solar radiation claims
claim(
    content="Solar photon flux follows Planck blackbody distribution at 6000K",
    title="Solar Blackbody Spectrum",
    background="Sun approximation as blackbody",
    parameters={"temperature": 6000, "distribution": "Planck"},
    provenance="Shockley & Queisser 1961, Eq. 2"
)

claim(
    content="Incident solar power density at Earth is approximately 1000 W/m² (AM1.5)",
    title="Solar Irradiance",
    background="Standard test conditions",
    parameters={"irradiance": 1000, "units": "W/m²"},
    provenance="AM1.5G standard spectrum"
)

# Current-voltage characteristics claims
claim(
    content="Short-circuit current Jsc = q × ∫[Eg,∞] Φ_sun(E) dE",
    title="Short-Circuit Current",
    background="Current generation by photon absorption",
    parameters={"q": "elementary charge", "Φ": "photon flux"},
    provenance="Shockley & Queisser 1961, Eq. 5"
)

claim(
    content="Open-circuit voltage Voc = (kT/q) × ln(Jph/J0 + 1)",
    title="Open-Circuit Voltage",
    background="Diode equation at zero current",
    parameters={"k": "Boltzmann constant", "T": "temperature"},
    provenance="Shockley & Queisser 1961, Eq. 7"
)

claim(
    content="Reverse saturation current J0 depends exponentially on bandgap: J0 ∝ exp(-Eg/kT)",
    title="Reverse Saturation Current",
    background="Thermal generation of carriers",
    parameters={"exponent": "-Eg/kT"},
    provenance="Shockley & Queisser 1961, Eq. 4"
)

claim(
    content="Fill factor FF < 1 is determined by J-V curve shape",
    title="Fill Factor Limit",
    background="Non-ideal diode behavior",
    parameters={"max_value": 1.0},
    provenance="Shockley & Queisser 1961, Section III"
)

# Optimization claims
claim(
    content="There exists an optimal bandgap Eg that maximizes efficiency",
    title="Optimal Bandgap Existence",
    background="Trade-off between Voc and Jsc",
    parameters={"tradeoff": "Voc vs Jsc"},
    provenance="Shockley & Queisser 1961, Section IV"
)

claim(
    content="Optimal bandgap for 6000K solar spectrum is approximately 1.1-1.3 eV",
    title="Optimal Bandgap Value",
    background="Numerical optimization",
    parameters={"Eg_optimal": "1.1-1.3 eV"},
    provenance="Shockley & Queisser 1961, Fig. 2"
)

claim(
    content="Maximum theoretical efficiency for single-junction cell under 6000K blackbody is ~30%",
    title="Shockley-Queisser Limit",
    background="Detailed balance calculation",
    parameters={"eta_max": 0.30, "spectrum": "6000K blackbody"},
    provenance="Shockley & Queisser 1961, Table I"
)

claim(
    content="Using AM1.5G standard spectrum, the limit increases to ~33.7%",
    title="AM1.5 Efficiency Limit",
    background="Standard terrestrial spectrum",
    parameters={"eta_max_AM15": 0.337},
    provenance="Subsequent calculations, AM1.5G standard"
)

# Loss mechanisms
claim(
    content="Thermalization loss: photon energy excess above Eg is lost as heat",
    title="Thermalization Loss",
    background="Energy relaxation of carriers",
    parameters={"mechanism": "phonon emission"},
    provenance="Fundamental loss mechanism"
)

claim(
    content="Transmission loss: photons with E < Eg pass through cell unabsorbed",
    title="Transmission Loss",
    background="Bandgap transparency",
    parameters={"threshold": "Eg"},
    provenance="Fundamental loss mechanism"
)

claim(
    content="Carnot efficiency limit applies to any heat engine converting solar radiation",
    title="Thermodynamic Limit",
    background="Second law of thermodynamics",
    parameters={"Carnot_limit": "~93% for 6000K/300K"},
    provenance="Thermodynamics"
)

# Multi-junction claims
claim(
    content="Multi-junction cells can exceed the single-junction Shockley-Queisser limit",
    title="Multi-Junction Advantage",
    background="Stacking cells with different bandgaps",
    parameters={"architecture": "tandem cells"},
    provenance="Subsequent developments"
)

# ============================================================================
# QUESTIONS - Open Research Questions
# ============================================================================

question(
    content="What is the theoretical upper bound for solar cell efficiency when accounting for all physical loss mechanisms?"
)

question(
    content="How does light concentration affect the Shockley-Queisser limit?"
)

question(
    content="What bandgap combinations optimize multi-junction solar cells under realistic spectra?"
)

# ============================================================================
# DETERMINISTIC OPERATORS
# ============================================================================

# Radiative recombination cannot be the same as non-radiative recombination
contradiction(
    a="Radiative Recombination Dominance",
    b="Non-radiative recombination is the primary loss mechanism"
)

# Each photon generates one e-h pair is equivalent to unity quantum efficiency
equivalence(
    a="Quantum Efficiency Unity",
    b="Internal quantum efficiency = 1.0 for all E > Eg"
)

# Both thermalization and transmission losses are fundamental
conjunction(
    a="Thermalization Loss",
    b="Transmission Loss",
    result="Fundamental Losses Present"
)

# ============================================================================
# REASONING STRATEGIES - Probability Propagation
# ============================================================================

# Deduction: From detailed balance equilibrium to Voc expression
deduction(
    premises=["Detailed Balance Equilibrium", "Reverse Saturation Current"],
    conclusion="Open-Circuit Voltage"
)

# Mathematical induction: Derive Jsc from photon flux integration
mathematical_induction(
    base="Photon Transparency Condition",
    step="Integration over photon spectrum above bandgap",
    conclusion="Short-Circuit Current"
)

# Case analysis: Trade-off between high Jsc (small Eg) and high Voc (large Eg)
case_analysis(
    exhaustiveness="All possible bandgap energies",
    cases=[
        {"case": "Eg → 0", "result": "High Jsc, low Voc, low η"},
        {"case": "Eg → ∞", "result": "Low Jsc, high Voc, low η"},
        {"case": "Eg ≈ 1.2 eV", "result": "Balanced Jsc and Voc, maximum η"}
    ],
    conclusion="Optimal Bandgap Existence"
)

# Extrapolation: From 6000K blackbody to AM1.5 real spectrum
extrapolation(
    source="Shockley-Queisser Limit (6000K blackbody)",
    target="AM1.5 Efficiency Limit",
    continuity="Spectral shape similarity and bandgap optimization principle"
)

# Elimination: Fundamental vs avoidable losses
elimination(
    exhaustiveness="All loss mechanisms in solar cells",
    excluded=["Series resistance", "Shunt resistance", "Surface recombination"],
    survivor="Fundamental Losses Present"
)

# Abduction: High Voc implies low J0, which implies large bandgap
abduction(
    observation="High open-circuit voltage observed",
    hypothesis="Material has large bandgap energy",
    strength="inverse relationship via exponential dependence"
)

# Induction: From specific materials to general bandgap principle
induction(
    observations=[
        {"material": "Si (Eg=1.1 eV)", "efficiency": "~26%"},
        {"material": "GaAs (Eg=1.43 eV)", "efficiency": "~29%"},
        {"material": "CdTe (Eg=1.45 eV)", "efficiency": "~22%"}
    ],
    law="Optimal Bandgap Value"
)

# Analogy: Multi-junction cells analogous to multiple heat engines in series
analogy(
    source="Single-junction cell limit ~30%",
    target="Multi-junction cell theoretical limit ~68% (infinite junctions)",
    bridge="Thermodynamic cascade with decreasing temperatures"
)

# Noisy-and: Both Voc and Jsc must be high for high efficiency
noisy_and(
    premises=["Open-Circuit Voltage", "Short-Circuit Current"],
    conclusion="Shockley-Queisser Limit",
    requirement="Both must be simultaneously optimized"
)

# Composite reasoning: Complete efficiency calculation chain
composite(
    premises=["Solar Blackbody Spectrum", "Photon Transparency Condition", "Quantum Efficiency Unity"],
    conclusion="Short-Circuit Current",
    sub_strategies=[
        "Integration over photon flux",
        "Quantum efficiency assumption"
    ]
)

# General inference: Relationship between bandgap and efficiency
infer(
    premises=["Reverse Saturation Current", "Open-Circuit Voltage", "Short-Circuit Current"],
    conclusion="Optimal Bandgap Existence",
    conditional="Efficiency η(Eg) has a maximum where dη/dEg = 0"
)

print("Shockley-Queisser Limit formalization loaded successfully!")
print(f"Total knowledge nodes: {len([c for c in dir() if not c.startswith('_')])}")
