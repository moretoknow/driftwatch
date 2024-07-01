# DriftWatch

This is a collection of implementations of methods for concept drift detection.

---

**Research**

If you are curious about *DriftWatch* or find it useful to your research, please refer to the paper [Online evaluation of the Kolmogorov–Smirnov test on arbitrarily large samples](https://www.sciencedirect.com/science/article/pii/S1877750323000194):

```bibtex
@article{cardoso_online_2023,
	title = {Online evaluation of the {Kolmogorov}–{Smirnov} test on arbitrarily large samples},
	volume = {67},
	issn = {1877-7503},
	url = {https://www.sciencedirect.com/science/article/pii/S1877750323000194},
	doi = {10.1016/j.jocs.2023.101959},
	urldate = {2024-07-01},
	journal = {Journal of Computational Science},
	author = {Cardoso, Douglas O. and Galeno, Thalis D.},
	month = mar,
	year = {2023},
	keywords = {Data streams, Online learning, Concept drift, Change detection},
	pages = {101959},
}
```
---

**Methods included**

In detail, the following methods can be used:

* **GreedyKS** from Cardoso and Galeno: [Online evaluation of the Kolmogorov–Smirnov test on arbitrarily large samples](https://www.sciencedirect.com/science/article/pii/S1877750323000194) (JoCS 2021)

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
