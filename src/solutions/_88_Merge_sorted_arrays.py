from typing import List


class MergeSortedArrays:
    @staticmethod
    def merge(nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        if m == 0:
            return
        position_to_move = len(nums1) - n
        nums1[position_to_move: len(nums1)] = nums1[0:n]
        n_i, m_i = position_to_move, 0
        for i in range(0, len(nums1)):
            n_to_add = None if n_i >= len(nums1) else nums1[n_i]
            m_to_add = None if m_i >= len(nums2) else nums2[m_i]

            if n_to_add is not None and (m_to_add is None or n_to_add < m_to_add):
                nums1[i] = n_to_add
                n_i = n_i + 1
            else:
                nums1[i] = m_to_add
                m_i = m_i + 1

    @staticmethod
    def simple(nums1: List[int], n: int, nums2: List[int], m: int):
        n_i, m_i = n - 1, m - 1
        i = n + m - 1
        while i >= 0:
            if n_i >= 0 and (m_i < 0 or nums1[n_i] > nums2[m_i]):
                nums1[i] = nums1[n_i]
                n_i = n_i - 1
            else:
                nums1[i] = nums2[m_i]
                m_i = m_i - 1
            i = i - 1
