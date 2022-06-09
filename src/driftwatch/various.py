import numpy as np
import scipy.stats as st
from .IKS import IKS

import ddsketch.ddsketch as ddsketch
import ddsketch.store as ddstore
import ddsketch.mapping as ddmapping

from random import randrange

class ReservoirSampling():
    def __init__(self, size, ref_distrib, p_threshold=0.01):
        self.size = size
        self.ref_distrib = ref_distrib
        self.p_threshold = p_threshold
        self.reset()

    def reset(self):
        self.reservoir = []
        self.t = 0
        
    def add_element(self, element):
        if len(self.reservoir) < self.size:
            self.reservoir.append(element)
        else:
            r = randrange(0, self.t)
            if r < self.size:
                self.reservoir[r] = element
        self.t += 1
        
    def get_D(self):
        cdf_results = self.ref_distrib.cdf(np.sort(self.reservoir))
        n = len(self.reservoir)
        dp = (np.arange(1, n + 1) / n - cdf_results).max()
        dn = (cdf_results - np.arange(0, n) / n).max()
        return max(dp, dn)
    
    def detected_change(self):
        return st.kstwo.sf(self.get_D(), len(self.reservoir)) <= self.p_threshold

class IksReservoir():
    def __init__(self, size, ref_distrib, p_threshold=0.01):
        self.size = size
        self.ref_distrib = ref_distrib
        self.p_threshold = p_threshold
        self.reset()

    def reset(self):
        self.iks = IKS()
        self.reservoir = [[], []]
        self.t = 0

    def add_element(self, element):
        if len(self.reservoir[0]) < self.size:
            ref_element = self.ref_distrib.rvs(1)
        
            self.reservoir[0].append(ref_element)
            self.iks.Add(ref_element, 0)
            
            self.reservoir[1].append(element)
            self.iks.Add(element, 1)
        else:
            r = randrange(0, self.t)
            if r < self.size:
                ref_element = self.ref_distrib.rvs(1)
        
                self.iks.Remove(self.reservoir[0][r], 0)
                self.reservoir[0][r] = ref_element
                self.iks.Add(ref_element, 0)
                
                self.iks.Remove(self.reservoir[1][r], 1)
                self.reservoir[1][r] = element
                self.iks.Add(element, 1)
        
        self.t += 1
        
    def get_D(self):
        return self.iks.KS()
    
    def detected_change(self):
        ca = self.iks.CAForPValue(self.p_threshold)
        return self.iks.Test(ca)

class LallDDSketch():
    def __init__(self, error, ref_distrib, p_threshold=0.01):
        self.error = error
        self.p_threshold = p_threshold
        self.ref_distrib = ref_distrib
        self.reset()
        
    def reset(self):
        self.dds = ddsketch.BaseDDSketch(
            ddmapping.LogarithmicMapping(self.error),
            ddstore.DenseStore(1),
            ddstore.DenseStore(1),
            0
        )
        
        self.vec_get_quantile_value = np.vectorize(self.dds.get_quantile_value)
        self.percents = []
    
    def add_element(self, element):
        self.dds.add(element)
    
    def get_D(self):
        num_bins = len(self.dds.store.bins) + len(self.dds.negative_store.bins)
        if num_bins != len(self.percents):
            self.percents = np.linspace(0.0, 1.0, num_bins)
        quantile_values = self.vec_get_quantile_value(self.percents)
        cdf_values = self.ref_distrib.cdf(quantile_values)
        dds_D = np.abs(cdf_values - self.percents).max()
        return dds_D   
    
    def detected_change(self):
        return st.kstwo.sf(self.get_D(), self.dds.count) <= self.p_threshold
