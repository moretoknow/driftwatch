# DriftWatch

This is a collection of implementations of methods for concept drift detection.

---

**Citing**

If you find *DriftWatch* useful in your research, please cite the following paper:

```bibtex
@inproceedings{galeno_sketch_2021,
   title = {A sketch for the {KS} test for {Big} {Data}},
   doi = {10.5753/kdmile.2021.17455},
   url = {https://sol.sbc.org.br/index.php/kdmile/article/view/17455},
   urldate = {2021-11-26},
   address = {Brasil},
   booktitle = {Anais do {IX} {Symposium} on {Knowledge} {Discovery}, {Mining} and {Learning} ({KDMiLe} 2021)},
   publisher = {Sociedade Brasileira de Computação - SBC},
   author = {Galeno, Thalis D. and Gama, João and Cardoso, Douglas O.},
   month = oct,
   year = {2021},
   pages = {8--15},
}
```
---

**Methods included**

In detail, the following methods can be used:

* **GreedyKS** from Galeno *et al.*: [A sketch for the KS test for Big Data](https://sol.sbc.org.br/index.php/kdmile/article/view/17455) (KDMiLe 2021, in portuguese)

An algorithm/sketch for performing the Kolmogorov-Smirnov test interactively while using a data stream as an incremental input.

---

**Installation**

DriftWatch can be installed with the following pip command.

```sh
$ pip install git+https://github.com/moretoknow/driftwatch
```

If you notice anything unexpected, please open an [issue](https://github.com/moretoknow/driftwatch/issues) and let us know.

---

**License**

- [MIT License](https://github.com/moretoknow/driftwatch/blob/main/LICENSE)
