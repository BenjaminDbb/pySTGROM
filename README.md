# Reduced-order surrogate models for scalar-tensor gravity in the strong field and applications to binary pulsars and GW170817

**Junjie Zhao, Lijing Shao, Zhoujian Cao, Bo-Qiang Ma**


## Abstract
We investigate the scalar-tensor gravity of Damour and Esposito-Farèse (DEF),
which predicts non-trivial phenomena in the nonperturbative strong-field regime
for neutron stars (NSs). Instead of solving the modified
Tolman-Oppenheimer-Volkoff equations, we construct reduced-order surrogate
models, coded in the [pySTGROM](https://github.com/BenjaminDbb/pySTGROM#pystgrom-for-the-def-theory) package, to predict the relations of a NS
radius, mass, and effective scalar coupling to its central density. Our models
are accurate at ~1% level and speed up large-scale calculations by two
orders of magnitude. As an application, we use pySTGROM and Markov-chain
Monte Carlo techniques to constrain parameters in the DEF theory, with five
well-timed binary pulsars, the binary NS (BNS) inspiral GW170817, and a
hypothetical BNS inspiral in the Advanced LIGO and next-generation GW detectors.
In the future, as more binary pulsars and BNS mergers are detected, our
surrogate models will be helpful in constraining strong-field gravity with
essential speed and accuracy.

# pySTGROM (for the DEF theory)

## Packages required

numpy

scipy

h5py

## Usage

The ROMs in the those range:

log10Alpha0 in **[-5.3, -2.5]**

beta0 in **[-4.8, -4.0]**

For now, we have built those ROMs for 9 EOSs. 

EOSs AP3, AP4, ENG, H4, MPA1, PAL1, SLy4, WFF1, and WFF2.

The simply usage:
```python
from stgrom import LoadModel

EOS_name = 'AP4' # EOSs AP3, AP4, ENG, H4, MPA1, PAL1, SLy4, WFF1, and WFF2.

log10Alpha0 = -5.0
beta0 = -4.5

mod4EOS = LoadModel(EOS_name)
mass, radius, alphaA = mod4EOS(log10Alpha0, beta0, mod4EOS.e_cs)
```
More, refer to [Example](https://github.com/BenjaminDbb/pySTGROM/blob/master/Example.ipynb).

## Introduction

This notebook is a companion to the paper posted at [arxiv:1907.00780](https://arxiv.org/abs/1907.00780). It contains three ROMs for each EOS. 

We encourage use of these data in derivative works. If you use the material provided here, please cite the paper using the reference:
```
@article{,
      key            = "1742146",
      author         = "Zhao, Junjie and Shao, Lijing and Cao, Zhoujian and Ma,
                        Bo-Qiang",
      title          = "{Reduced-order surrogate models for scalar-tensor gravity
                        in the strong field and applications to binary pulsars and
                        GW170817}",
      year           = "2019",
      eprint         = "1907.00780",
      archivePrefix  = "arXiv",
      primaryClass   = "gr-qc",
      SLACcitation   = "%%CITATION = ARXIV:1907.00780;%%"
}
```
Our paper are based on those papers:

In order to solve the modified Tolman-Oppenheimer-Volkoff (TOV) eqautions for neutron star, we use the solver for the DEF theory from **Shao:2017gwu** and make it more efficient with parallel computing.

```
@article{Shao:2017gwu,
      author         = "Shao, Lijing and Sennett, Noah and Buonanno, Alessandra
                        and Kramer, Michael and Wex, Norbert",
      title          = "{Constraining nonperturbative strong-field effects in
                        scalar-tensor gravity by combining pulsar timing and
                        laser-interferometer gravitational-wave detectors}",
      journal        = "Phys. Rev.",
      volume         = "X7",
      year           = "2017",
      number         = "4",
      pages          = "041025",
      doi            = "10.1103/PhysRevX.7.041025",
      eprint         = "1704.07561",
      archivePrefix  = "arXiv",
      primaryClass   = "gr-qc",
      reportNumber   = "LIGO-P1700073",
      SLACcitation   = "%%CITATION = ARXIV:1704.07561;%%"
}
```
The ROMs are based on the paper **Field:2013cfa**. 

```
@article{Field:2013cfa,
      author         = "Field, Scott E. and Galley, Chad R. and Hesthaven, Jan S.
                        and Kaye, Jason and Tiglio, Manuel",
      title          = "{Fast prediction and evaluation of gravitational
                        waveforms using surrogate models}",
      journal        = "Phys. Rev.",
      volume         = "X4",
      year           = "2014",
      number         = "3",
      pages          = "031006",
      doi            = "10.1103/PhysRevX.4.031006",
      eprint         = "1308.3565",
      archivePrefix  = "arXiv",
      primaryClass   = "gr-qc",
      SLACcitation   = "%%CITATION = ARXIV:1308.3565;%%"
}
```
## Acknowledgements
We are grateful to Bin Hu, Michael Kramer, and Masaru
Shibata for comments. We thank Norbert Wex for stimulating
discussions and carefully reading the manuscript. 

## Funding
This work was supported by the Young Elite Scientists Sponsorship 
Program by the China Association for Science and Technology
(2018QNRC001), and was partially supported by the National
Natural Science Foundation of China (11721303, 11475006,
11690023, 11622546), the Strategic Priority Research Program of the 
Chinese Academy of Sciences through the grant
No. XDB23010200, the European Research Council (ERC)
for the ERC Synergy Grant BlackHoleCam under Contract
No. 610058, and the High-performance Computing Platform
of Peking University. Z.C. was supported by the "Fundamental Research 
Funds for the Central Universities".
