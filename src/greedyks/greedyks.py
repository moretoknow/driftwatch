from math import ceil

from scipy.stats import norm, kstwo, kstwobign

from .prefix_sum_structs import BIT

class GreedyKS():
    
    def __init__(self, dist=norm(0,1), m=100, min_instances=0,
                 drift_threshold=0.01, exact_prob=False, sum_struct=BIT
                ):
        self.dist = dist
        self.m = int(m)
        self.min_instances = min_instances
        self.drift_threshold = drift_threshold
        self.exact_prob = exact_prob
        self.sum_struct = sum_struct(self.m+1)
        self.reset()

    def reset(self):
        self.n = 0
        self.dp = 0
        self.dn = 0
        self.old_p = 0
        self.old_n = -1
        
        self.num = [0] * (self.m+1)
        self.most = [0] * (self.m+1)
        self.least = [1] * (self.m+1)
        
        self.sum_struct.reset()
        
    def add_element(self, x):
        self.n += 1
        f = self.dist.cdf(x)
        
        b = ceil(f*self.m)
        self.num[b] += 1
        self.sum_struct.increment_segment(b)
        
        self.most[b] = max(self.most[b], f)
        self.least[b] = min(self.least[b], f)

        prefix_sum = self.sum_struct.get_sum_segment(0, b-1)
        
        dn_alt = self.least[b] - prefix_sum/self.n
        
        prefix_sum_n = self.sum_struct.get_sum_segment(0, self.old_n-1)
        if self.old_n != -1:
            self.dn = self.least[self.old_n] - prefix_sum_n/self.n
        else:
            self.dn = 0
    
        if self.n >= self.min_instances and self.dn < dn_alt:
            self.dn = dn_alt
            self.old_n = b

        prefix_sum += self.num[b]
        
        dp_alt = prefix_sum/self.n - self.most[b]
        
        prefix_sum_p = self.sum_struct.get_sum_segment(0, self.old_p)
        self.dp = prefix_sum_p/self.n - self.most[self.old_p]
                
        if self.n >= self.min_instances and self.dp < dp_alt:
            self.dp = dp_alt
            self.old_p = b
    
    def get_D(self):
        return max(self.dn, self.dp) if self.n >= self.min_instances else 0

    def get_max_p_n_indexes(self):
        return [self.old_p, self.old_n]
    
    def detected_change(self):
        D = self.get_D()
        
        if self.exact_prob:
            prob = kstwo.sf(D, self.n)
            
        else:
            prob = kstwobign.sf(D * self.n**.5)
        
        return (prob <= self.drift_threshold)
