from fenwick import FenwickTree

from segment_tree import SegmentTree

class BIT():
    def __init__(self, n_elements):
        self.n_elements = n_elements
        self.reset()

    def reset(self):
        self.bit = FenwickTree(self.n_elements)
        
    def get_sum_segment(self, L, R):
        prefix_sum = self.bit.prefix_sum(R+1) if L <= R else 0
        return prefix_sum
        
    def increment_segment(self, index):
        self.bit.add(index, 1)
        
    def decrement_segment(self, index):
        self.bit.add(index, -1)
        

class SegTree():
    def __init__(self, n_elements):
        self.n_elements = n_elements
        self.reset()
    
    def reset(self):
        self.count_elements = [0]*self.n_elements
        self.seg_tree = SegmentTree(self.count_elements)
        
    def get_sum_segment(self, L, R):
        prefix_sum = self.seg_tree.query(L, R, "sum") if L <= R else 0
        return prefix_sum
            
    def increment_segment(self, index):
        prefix_sum = self.count_elements[index]+1
        self.seg_tree.update(index, prefix_sum)
        
    def decrement_segment(self, index):
        prefix_sum = self.count_elements[index]-1
        self.seg_tree.update(index, prefix_sum)


class SqrtDecomp():
    def __init__(self, n_elements):
        self.n_elements = n_elements
        self.reset()

    def reset(self):
        self.n_sectors = int(self.n_elements**.5)
        self.count_elements = [0]*self.n_elements
        self.square_counts = [0] * (self.n_sectors+1)
        
        
    def get_sum_segment(self, L, R):
        prefix_sum = 0
        index = L
        while(index <= R):
            sector = int(index/self.n_sectors)
            if (index+self.n_sectors-1 <= R) and (index%self.n_sectors == 0):
                prefix_sum += self.square_counts[sector]
                index += self.n_sectors

            else:
                prefix_sum += self.count_elements[index]
                index += 1

        return prefix_sum
    
    def increment_segment(self, index):
        self.count_elements[index] += 1
        sector = int(index/self.n_sectors)
        
        if sector <= self.n_sectors:
            self.square_counts[sector] += 1
            
    def decrement_segment(self, index):
        self.count_elements[index] -= 1
        sector = int(index/self.n_sectors)
        
        if sector <= self.n_sectors:
            self.square_counts[sector] -= 1
