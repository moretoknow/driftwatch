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

* **Reservoir Sampling** from Bifet *et al.*: [Machine learning for data streams: with practical examples in MOA](https://doi.org/10.7551/mitpress/10654.001.0001) (MIT Press 2018)

An algorithm that iteratively sample the input and calculate the exact value of the D statistic for the subsample. It is considered a baseline solution.

* **IKS + Reservoir Sampling** from dos Reis *et al.*: [Fast Unsupervised Online Drift Detection Using Incremental Kolmogorov-Smirnov Test](https://doi.org/10.1145/2939672.2939836) (ACM 2016)

An algorithm that uses the previously described Reservoir Sampling to interactively sample the input filtering it to IKS, an method for performing the Kolmogorov-Smirnov test which by default stores all its input, assuming the absence of memory restrictions.

* **Lall + DDSketch** from Lall *et al.*: [Data Streaming Algorithms for the Kolmogorov-Smirnov Test](https://doi.org/10.1109/BigData.2015.7363746) (IEEE Computer Society 2015) and from Masson*et al.*: [DDSketch: A Fast and Fully-Mergeable Quantile Sketch with Relative-Error Guarantees](10.14778/3352063.3352135) (Proceedings of the VLDB Endowment 2019)

A method which relies on any quantile sketch, combined with one of the state-of-the-art data structures for this purpose.


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
