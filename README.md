# Shockley-Queisser Limit - Gaia Lang Formalization

> Formalization of the detailed balance limit of efficiency for p-n junction solar cells

## Overview

This project formalizes the seminal 1961 paper by Shockley and Queisser that established the theoretical efficiency limit for single-junction solar cells. The formalization is written in **Gaia Lang**, a probabilistic knowledge representation and reasoning system.

## Original Paper

**Title:** Detailed Balance Limit of Efficiency of p-n Junction Solar Cells

**Authors:** William Shockley and Hans J. Queisser

**Journal:** Journal of Applied Physics, Vol. 32, pp. 510-519

**Year:** 1961

**DOI:** 10.1063/1.1736034

## Core Contribution

The Shockley-Queisser (SQ) limit establishes the maximum theoretical efficiency of a single p-n junction solar cell under the following assumptions:

1. **Solar spectrum**: Approximated as a 6000K blackbody radiator
2. **Radiative recombination**: The only unavoidable loss mechanism
3. **Ideal p-n junction**: No non-radiative recombination
4. **Unity quantum efficiency**: Each photon with E > Eg generates one electron-hole pair
5. **Band-to-band transitions**: Only direct bandgap transitions considered

The calculated limit is approximately **30%** for a 6000K blackbody solar spectrum, and about **33.7%** under the AM1.5G standard terrestrial spectrum.

## Key Results

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Optimal bandgap** | 1.1 - 1.3 eV | Maximizes product of Voc and Jsc |
| **Maximum efficiency** | ~30% | 6000K blackbody spectrum |
| **Maximum efficiency** | ~33.7% | AM1.5G standard spectrum |
| **Open-circuit voltage** | Voc = (kT/q) × ln(Jph/J0 + 1) | Diode equation |
| **Short-circuit current** | Jsc = q × ∫[Eg,∞] Φ_sun(E) dE | Photon flux integration |

## Project Structure

```
shockley-queisser-limit-gaia/
├── gaia.toml          # Package metadata and dependencies
├── package.py         # Main formalization (15-20 knowledge nodes)
├── review.toml        # Prior probabilities for reasoning
├── README.md          # This file
└── artifacts/         # Supporting materials and references
```

## Knowledge Graph

The formalization includes **20 knowledge nodes** organized into:

### Settings (5)
- Background context and assumptions (no probability)
- Solar spectrum approximation
- Physical principles

### Claims (15)
- Scientific assertions with associated probabilities
- Core principle claims
- Solar radiation claims
- Current-voltage characteristics
- Optimization and loss mechanism claims

### Questions (3)
- Open research questions
- Extensions to the original theory

### Reasoning Strategies (10)
- **Deduction**: From detailed balance to Voc expression
- **Mathematical induction**: Jsc from photon flux
- **Case analysis**: Bandgap optimization trade-offs
- **Extrapolation**: 6000K to AM1.5 spectrum
- **Elimination**: Fundamental vs avoidable losses
- **Abduction**: High Voc implies large bandgap
- **Induction**: General bandgap principle
- **Analogy**: Multi-junction vs single-junction limits
- **Noisy-AND**: Joint requirements for efficiency
- **Composite**: Complete calculation chain

### Deterministic Operators (3)
- **Contradiction**: Radiative ≠ Non-radiative recombination
- **Equivalence**: Unity quantum efficiency
- **Conjunction**: Both thermalization and transmission losses

## Physical Loss Mechanisms

The SQ limit accounts for three fundamental, unavoidable losses:

1. **Thermalization loss**: Energy excess above bandgap is lost as heat
   - Occurs when photon energy E > Eg
   - Cannot be eliminated

2. **Transmission loss**: Photons below bandgap pass through unabsorbed
   - Occurs when photon energy E < Eg
   - Determines optimal bandgap

3. **Carnot limit**: Thermodynamic efficiency limit (~93% for 6000K/300K)
   - Based on second law of thermodynamics
   - Represents absolute upper bound

## Usage

### Prerequisites

- Python 3.8+
- Gaia Lang runtime (see https://github.com/gaia-lang/gaia)

### Running the Formalization

```bash
# Install Gaia Lang (if not already installed)
pip install gaia-lang

# Load and reason over the formalization
python package.py

# Run reasoning with review probabilities
gaia reason shockley-queisser-limit-gaia
```

### Querying the Knowledge Base

```python
from gaia import KnowledgeBase

kb = KnowledgeBase("shockley-queisser-limit-gaia")

# Query all claims
claims = kb.get_claims()

# Reason about optimal bandgap
result = kb.reason("Optimal Bandgap Existence")

# Calculate efficiency for a given bandgap
efficiency = kb.calculate_efficiency(bandgap=1.2)
```

## Extensions

This formalization can serve as a foundation for:

1. **Multi-junction cells**: Stacking multiple bandgaps
2. **Concentrated photovoltaics**: Effect of light concentration
3. **Intermediate band cells**: Sub-bandgap absorption
4. **Hot carrier cells**: Reducing thermalization loss
5. **Upconversion**: Converting low-energy photons
6. **Downconversion**: Splitting high-energy photons

## References

1. Shockley, W., & Queisser, H. J. (1961). Detailed balance limit of efficiency of p-n junction solar cells. *Journal of Applied Physics*, 32(3), 510-519. https://doi.org/10.1063/1.1736034

2. Rühle, S. (2016). Tabulated values of the Shockley–Queisser limit for single junction and tandem solar cells. *Solar Energy*, 130, 139-147. https://doi.org/10.1016/j.solener.2016.02.015

3. Green, M. A. (1982). Solar cells: operating principles, technology, and system applications. Prentice-Hall.

4. De Vos, A. (1980). Detailed balance limit of the efficiency of tandem solar cells. *Journal of Physics D: Applied Physics*, 13(5), 839. https://doi.org/10.1088/0022-3727/13/5/018

## License

MIT License - see gaia.toml for details

## Contributing

This formalization is a starting point for probabilistic reasoning about solar cell efficiency limits. Contributions welcome for:

- Additional loss mechanisms
- Multi-junction extensions
- Real material parameters
- Spectrum variations (AM0, AM1.0, AM2.0)
- Temperature effects

## Acknowledgments

This formalization is based on the foundational work of William Shockley and Hans J. Queisser, which established the fundamental limits of photovoltaic conversion.

---

*Formalization created using Gaia Lang - A probabilistic knowledge representation system*
