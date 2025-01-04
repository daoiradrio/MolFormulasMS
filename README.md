Project for self-teaching coding. The idea is to compute all possible and chemically reasonable molecular formulas from a given mass peak of a electron ionization mass spectrum. That includes the following steps.

- Get the mass of the mass peak, i.e. the total mass of the unknown molecule. Test cases are given in ```spectra/```

- Get the isotope pattern. From on the isotope pattern the presence of certain elements like Cl, Br, S, Si, and B can be deducted (or ruled out if there is no isotope pattern). Elements without an isotope always have to considered, that includes here C, H, O, N, P, F or I

- For each element under consideration an amount that sums up to the total mass of the mass peak is considered

- Clearly that also leads to chemically unreasonable formulas. They are ruled out by checking the double bound equivalent (https://en.wikipedia.org/wiki/Degree_of_unsaturation). For reasonable formuals this is integer-valued