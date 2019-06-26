# Reduced-order surrogate models for scalar-tensor gravity in the strong field and applications to binary pulsars and GW170817

**Junjie Zhao<sup>1</sup>, Lijing Shao<sup>2,3</sup>, Zhoujian Cao<sup>4</sup>, Bo-Qiang Ma<sup>1,5,6</sup>**

**<sup>1</sup>School of Physics and State Key Laboratory of Nuclear Physics and Technology, Peking University, Beijing 100871, China**

**<sup>2</sup>Kavli Institute for Astronomy and Astrophysics, Peking University, Beijing 100871, China**

**<sup>3</sup>Max-Planck-Institut für Radioastronomie, Auf dem Hügel 69, D-53121 Bonn, Germany**

**<sup>4</sup>Department of Astronomy, Beijing Normal University, Beijing 100875, China**

**<sup>5</sup>Collaborative Innovation Center of Quantum Matter, Beijing, China**

**<sup>6</sup>Center for High Energy Physics, Peking University, Beijing 100871, China**

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

## License

![Creative Commons License](https://i.creativecommons.org/l/by-sa/3.0/us/88x31.png "Creative Commons License")

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).

## Introduction

This notebook is a companion to the paper posted at [arxiv:19XX.XXXXX](https://arxiv.org/abs/19XX.XXXXX). It contains three ROMs for each EOS. 

We encourage use of these data in derivative works. If you use the material provided here, please cite the paper using the reference:
```
@article{Zhao:2019xx,
XXX
XXX
XXX
}
```
and our works are based on those papers:
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
and
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
We are grateful to Bin Hu and Michael Kramer for comments.  We thank Norbert Wex
for stimulating discussions and carefully reading the manuscript.  

## Funding
This work was
supported by the Young Elite Scientists Sponsorship Program by the China
Association for Science and Technology (2018QNRC001), and was partially
supported by the National Natural Science Foundation of China (11721303,
11475006, 11690023, 11622546), the Strategic Priority Research Program of the
Chinese Academy of Sciences through the grant No. XDB23010200, the European
Research Council (ERC) for the ERC Synergy Grant BlackHoleCam under Contract No.
610058, and the High-performance Computing Platform of Peking University.  Z.C.
was supported by the ``Fundamental Research Funds for the Central
Universities''.
